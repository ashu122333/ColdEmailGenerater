# from langchain.vectorstores import Pinecone
from pinecone import Pinecone,ServerlessSpec
from llm import e_llm
import os

index_name = "student-portfolio"
# pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
# index = pc.Index(host="https://student-portfolio-yzw815b.svc.aped-4627-b74a.pinecone.io")

api_key=os.getenv("PINECONE_API_KEY")
pc=Pinecone(api_key)
index = pc.Index(index_name)


def query(skills):
    q_embe=e_llm(skills)
    results=[]
    for i in range(len(skills)):
        try:
            res = index.query(
                namespace="ns2",
                vector=q_embe[i],
                top_k=1,
                include_metadata=True
            )
            results.append(res)
        except Exception as e:
            print(f"Error querying Pinecone: {e}")
            return None

    print(results)
    return results

# query(['Adobe After Effects', 'Adobe Illustrator', 'Adobe Photoshop', 'Adobe Premiere Pro', 'Video Editing'])