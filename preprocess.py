import re
from nltk.corpus import stopwords
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

#去除text中的所有非字母内容，包括标点符号、空格、换行、下划线等
def replace_all_blank(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    res = " ".join(text.split())  # 删除多余的空格
    return res

#过滤代码片段
def codefilter(htmlstr):
    s = re.sub(r'(<code>)(\n|.)*?(</code>)', ' ', htmlstr, re.S)
    return s

#过滤html中的标签
def htmlfilter(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    re_url = re.compile(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%|-|_)*\b', re.MULTILINE)

    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    # s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_br.sub(' ', s)
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    s = re_url.sub('', s)
    # 去掉多余的空行
    # blank_line = re.compile('\n+')
    s = re.sub(r'\\n(\B|\b)', ' ',s)
    return s
##替换常用HTML字符实体.
# 使用正常的字符替换HTML中特殊的字符实体.
# 你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
# @param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"', '34': '"', }

    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称，如&gt;
        key = sz.group('name')  # 去除&;后entity,如&gt;为gt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr
# 获取单词的词性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

#去除停用词,小写,词形还原
def preprocess(str):
    str = re.sub(r"won't", "will not", str)
    str = re.sub(r"can't", "can not", str)
    str = re.sub(r"n't", " not", str)
    str = re.sub(r"'ve", " have", str)
    str = re.sub(r"'ll", " will", str)
    str = re.sub(r"'re", " are", str)
    #小写
    str = str.lower()
    #去除数字，标点符号和非字母符号
    str = replace_all_blank(str)
    #分词
    tokens = word_tokenize(str)

    tagged_sent = pos_tag(tokens)  # 获取单词词性

    wnl = WordNetLemmatizer()
    lemmas_sent = []
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))  # 词形还原

    #英语停用词和常用词
    english_stopwords = stopwords.words("english")
    words_stopwordsremoved = []
    for word in lemmas_sent:
        if word not in english_stopwords:
            words_stopwordsremoved.append(word)
    result = ''
    for word in words_stopwordsremoved:
        result += ' ' + word
    return result.strip()


#处理post的body部分
def processbody(str):
    str = replaceCharEntity(str)
    str = codefilter(str)
    str = htmlfilter(str)
    str = preprocess(str)
    return str


if __name__ == '__main__':
    df = pd.read_csv('questions_used.csv')
    # df.at[0, 'title'] = processbody(str(df.at[0, 'title']))
    # print(df.at[0, 'title'])
    for index, row in df.iterrows():
        title = str(row['title'])
        body = str(row['body'])
        df.at[index, 'title'] = processbody(title)
        df.at[index, 'body'] = processbody(body)
        print(df.at[index, 'title'])
    df.to_csv("processed_questions1.csv")
