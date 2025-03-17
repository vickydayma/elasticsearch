#!/usr/bin/env python
# coding: utf-8

# import all required libraries
import openai
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex, Settings
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader

# OpenAI API KEY (without api key query engine will not work)
#openai.api_key = "SDgsdgSDgsGd53Ssdg53578GsdggsdhsdhwetQWt"

#Set Default model setting same as you inserted data into index
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Step 1: Configure Elasticsearch store connection
es=ElasticsearchStore(
               index_name="blog_data_index",
               es_api_key="es api key",
               es_cloud_id="es cloud id"
               )



#Step 2: Want to use an vector store data of loading from documents
index=VectorStoreIndex.from_vector_store(vector_store=es)

#Step 3: Create the query engine
qe=index.as_query_engine()
#Step 4: Create query
response=qe.query("What is the summary of this blog?")
#Step 5: Print Response
print(response)


#Step:6 Close Elasticsearch connection
es.close()




