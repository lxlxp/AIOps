import numpy as np
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import pandas as pd
import csv
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary


num_topics = 8 #datadog and elastic stack
#num_topics = 9 #splunk
lda = LdaModel.load('lda/datadog_8.model') #datadog
#lda = LdaModel.load('lda/elastic_8.model') #elastic stack
#lda = LdaModel.load('lda/splunk_9.model') #splunk
topic_list = lda.print_topics(num_topics=num_topics, num_words=15)
dictionary = Dictionary.load('lda/datadog.dict')#change the name of the platform
corpus = np.load('lda/datadog_corpus.npy', allow_pickle=True).tolist()#change the name of the platform
docs = np.load('lda/datadog_docs.npy', allow_pickle=True).tolist()#change the name of the platform
topics = lda.get_document_topics(corpus)
file_name = "dataset/datadog-aiops.csv"#
with open(file_name, 'r', encoding='utf-8', errors='surrogatepass') as all:
    df = pd.read_csv(all)
    x = list()
    y = list()
    cnt = 0
    filter_cnt = 0
    f = 0
    corpus_header = ["time","0","1","2","3"]
    fpath2 = "datadog_lda.csv" #change the name of the platform
    with open(fpath2, 'w') as out:
        wr = csv.writer(out)
        wr.writerow(corpus_header)
        for idx, row in df.iterrows():
            try:
                time = row['creation_date']
                bucket = [0]*num_topics
                for top in topics[cnt]:
                    bucket[top[0]] = top[1]
                try:
                    wr.writerow([time,bucket[4],(bucket[5]+bucket[3]+bucket[1]+bucket[7]),bucket[0],(bucket[2]+bucket[6])]) #datadog
                    #wr.writerow([time,bucket[4],(bucket[5]+bucket[7]),(bucket[0]+bucket[1]+bucket[2]+bucket[3]),bucket[6]]) #elastic stack
                    #wr.writerow([time,(bucket[2]+bucket[4]),(bucket[0]+bucket[6]),(bucket[3]+bucket[5]+bucket[7]+bucket[8]),bucket[1]]) #splunk
                    # title, desc, code, creation_date, tags])
                    cnt += 1
                except Exception as e:
                    print("Error msg: %s" % e)
                if cnt % 1000 == 0:
                    print("Processing %s row..." % cnt)


            except Exception as e:

                filter_cnt += 1

