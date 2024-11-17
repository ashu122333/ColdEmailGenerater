import pandas as pd
import os
from dotenv import load_dotenv
from llm import e_llm
import pinecone
from langchain.vectorstores import Pinecone
from pinecone import Pinecone, ServerlessSpec
import time

load_dotenv()

folder_path = 'resources'
data_frames = []

# Loop over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Read each CSV file into a DataFrame
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        data_frames.append(df)

# Concatenate all DataFrames into one
data_base = pd.concat(data_frames, ignore_index=True)

# Display the combined DataFrame
print(data_base)


embeddings=[]

for _,row in data_base.iterrows():
  embe=e_llm([row["Skills"]])[0]
  embeddings.append(embe)
print("embedding suceesful!!")


index_name = "student-portfolio"
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Wait for the index to be ready
while not pc.describe_index(index_name).status['ready']:
    time.sleep(1)

index = pc.Index(index_name)

vectors = []
id=0
for i,row in data_base.iterrows():
    vectors.append({
        "id": str(id),
        "values": embeddings[i],
        "metadata": {'skills': row["Skills"],"portfolio":row["Portfolio Website"]}
    })
    id+=1

index.upsert(
    vectors=vectors,
    namespace="ns2"
)

print("Embedding upsert to the server")