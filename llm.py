import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import chromadb.utils.embedding_functions as embedding_functions


load_dotenv()

e_llm=embedding_functions.HuggingFaceEmbeddingFunction(
    api_key=os.getenv("HF_API_KEY"),
    model_name="ggrn/e5-small-v2")

llm=ChatGroq(
    model="llama-3.2-90b-text-preview",
    # model="llama-3.1-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0)

to_json_prompt=PromptTemplate.from_template(
    """
      ### SCRAPED TEXT FROM WEBSITE:
      {page_data}
      ###INSTRUCTIONs:
      the scrapped text is from the careers apge of a website.
      Your job is to extract the job postings and return them in json format containing following keys: `role`,`experience`,`skills` and `description`.
      only return the valid JSON
      ### VALID JSON (NO PREAMBLE)

  """
)

def to_json(page_data):
    chain_extract=to_json_prompt | llm
    json_responce=chain_extract.invoke(input={"page_data":page_data})
    print(json_responce.content)
    json_parser=JsonOutputParser()
    json_responce=json_parser.parse(json_responce.content)
    return json_responce[0]


prompt_email=PromptTemplate.from_template(
    """
    ### JOB DESCRIPTION:
    {job_description}

    ###INSTRUCTIONS:
    you are anshu gupta, a business development executive at softCon . softCon is an AI & Softerware contarcter company which takes contractes from 
    other company by proviedeing our empolyes to them.
    your job is to write a cold email to the client regarding the job mentioned above and fulfilling their needs.
    Also add the most relevent ones from the following links to showcase softCon : {portfolio_links}.
    add all the unique portfolio links in the email.
    Remember you are anshu gupta , BDE at softCon.
    DO NOT PROVIDE PREAMBLE.

    ### (EMAIL (NO PREAMBLE))
    """
)


def gen_email(job_info,portfolios_links):
    email_chain=prompt_email | llm
    email=email_chain.invoke(input={"job_description":job_info,"portfolio_links":portfolios_links})
    print(email.content)
    return email.content