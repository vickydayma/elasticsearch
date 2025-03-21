#!/usr/bin/env python
# coding: utf-8
# import all required libraries
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex, Settings
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader



# Step 1: Load documents
loader = SimpleDirectoryReader(input_files=["Users/sample_data.txt"])
docs = loader.load_data()

# Step 2: Set the embedding model to HuggingFaceEmbedding
# Default model setting
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Step 3: Configure Elasticsearch store
es=ElasticsearchStore(
               index_name="blog_data_index",
               es_api_key="es api key",
               es_cloud_id="es cloud id"
               )

# Step 4: Create StorageContext and VectorStoreIndex
sc=StorageContext.from_defaults(vector_store=es)
index=VectorStoreIndex.from_documents(docs,storage_context=sc)

print(isinstance(index, VectorStoreIndex))  # Expected output: True

# Close Elasticsearch connection
es.close()
