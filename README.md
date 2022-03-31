# AIOps

## File description ##
```
│ preprocess.py:code to preprocess the data
│ 
├─dataset：the data without preprocess
│      datadog-aiops.csv
│      elastic-aiops.csv
│      splunk-aiops.csv
│      
├─impact：the process code and result of topic impact
│      datadog_impact.csv
│      datadog_impact.pdf:topic impact result
│      datadog_lda.csv
│      elastic_impact.csv
│      elastic_impact.pdf:topic impact result
│      elastic_lda.csv
│      impact.py:calculate topic impact and draw the graph
│      lda_phase.py:calculate phase probability by lda
│      splunk_impact.csv
│      splunk_impact.pdf:topic impact result
│      splunk_lda.csv
│      
└─lda：the process code and result of lda , the result of diffculty and popularity
        datadog-difficulty.csv:difficulty result
        datadog-popularity.csv:popularity result
        datadog.dict
        datadog.py:lda analysis of datadog
        datadog_8.model
        datadog_8.model.expElogbeta.npy
        datadog_8.model.id2word
        datadog_8.model.state
        datadog_corpus.npy
        datadog_docs.npy
        datadog_topic.png:lda topic result
        elastic-difficulty.csv:difficulty result
        elastic-popularity.csv:popularity result
        elastic.dict
        elastic.py:lda analysis of elastic stack
        elastic_8.model
        elastic_8.model.expElogbeta.npy
        elastic_8.model.id2word
        elastic_8.model.state
        elastic_corpus.npy
        elastic_docs.npy
        elastic_topic.png:lda topic result
        lda.ipynb:calculate popularity and difficulty
        splunk-difficulty.csv:difficulty result
        splunk-popularity.csv:popularity result
        splunk.dict
        splunk.py:lda analysis of splunk
        splunk_9.model
        splunk_9.model.expElogbeta.npy
        splunk_9.model.id2word
        splunk_9.model.state
        splunk_corpus.npy
        splunk_docs.npy
        splunk_topic.png:lda topic result
```        
