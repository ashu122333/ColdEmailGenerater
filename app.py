import streamlit as st
from scrape import scrape_web
from llm import to_json, gen_email
from query import query

st.title("Cold Email Generator")

suggestions = ["https://internshala.com/internship/details/work-from-home-backend-development-internship-at-aadi-foundation1731837745"]
url_input=st.text_input("Enter the Job portail website's LINK.")

st.text(f"eg: {suggestions[0]}")

scan_button=st.button("Scan the Page")

st.write(
    """
    <style>
    .fixed-height-code {
        overflow-y: hidden; /* Hide vertical scrollbar */
        white-space: pre-wrap; /* Enable line wrapping */
        word-wrap: break-word; /* Break long words */
        background-color: #343231; /* Optional: code background color */
        padding: 10px;
        border-radius: 5px;
        font-family: monospace;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
def get_portfolios():
    st.text("Sutable portfolios!!!")
    portfolios=query(json_info['skills'])
    links=[]
    skills=[]
    if not portfolios:
        st.text("Did not find any sutable candidate...")
        return None
    for section in portfolios:
        meta=section["matches"][0]["metadata"]
        link=meta['portfolio']
        links.append(link)
        skill=meta["skills"]
        skills.append(skill)
        st.markdown(f'<div class="fixed-height-code"><pre>{f"Skill: {skill}  Portfoilio: {link}"}</pre></div>', unsafe_allow_html=True)
    email=gen_email(json_info,links)
    st.text("Generated Email!!!")
    st.markdown(f'<div class="fixed-height-code"><pre>{email}</pre></div>', unsafe_allow_html=True)


if scan_button:
    info=scrape_web(url_input)
    st.text("Scraped website's contents!!!")
    json_info=to_json(info)
    role_info=f"Role: {json_info['role']}"
    exp_info=f"Experience: {json_info['experience']}"
    skills_info=f"Skills: {json_info['skills']}"
    des_info=f"Description: {json_info['description']}"
    st.markdown(f'<div class="fixed-height-code"><pre>{role_info}</pre></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="fixed-height-code"><pre>{exp_info}</pre></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="fixed-height-code"><pre>{skills_info}</pre></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="fixed-height-code"><pre>{des_info}</pre></div>', unsafe_allow_html=True)

    get_portfolios()
else:
    st.text("Please Enter the URL!!!")



st.markdown("---")  # Adds a horizontal line
st.markdown("---")  # Adds a horizontal line


st.image("resources\Screenshot 2024-11-17 144308.png", caption="Project Flow Chart", width=700)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("resources\groqcloud.webp", caption="groq cloud", use_column_width=True)

with col2:
    st.image("resources\langchian.png", caption="lang chain", use_column_width=True)

with col3:
    st.image("resources\pinecone.png", caption="pinecone", use_column_width=True)




st.header("About the Project")
st.write("""
This project is a **Cold Email Generator** that automates the process of creating professional and targeted emails for job providers. It leverages cutting-edge technologies like **LangChain**, **Groq Cloud**, and **Pinecone** to achieve the following workflow:

### Workflow:
1. **Job Information Extraction**:
   - The user inputs a job portal website link.
   - The job details are scraped using LangChain and passed to a large language model (LLM) hosted on Groq Cloud.

2. **Job Details Analysis**:
   - The LLM extracts key information from the job post, including:
     - **Role**
     - **Experience Required**
     - **Skills Needed**
     - **Job Description**

3. **Candidate Matching**:
   - The extracted skills are used to query a **vector database** hosted on Pinecone.
   - The database contains candidate profiles and portfolios, which are matched based on relevance.

4. **Cold Email Generation**:
   - The job information and the most suitable candidates' portfolios are passed to the LLM.
   - A professional cold email is generated, tailored to the job provider, and includes links to the candidates' portfolios.

---

### Tools Used:
- **LangChain**: For web scraping job information from job portal websites.
- **Groq API**:
  - Uses the **LLama-3.2-90B-text-preview** model for:
    - Extracting job information (Role, Experience, Skills, Description).
    - Generating personalized cold emails.
- **Hugging Face Inference**:
  - Creates **384-dimensional embeddings**  using model (e5-small-v2) of candidate profiles for efficient similarity searches.
- **Pinecone**: A powerful vector database used to store and query embeddings for finding the most relevant candidates.

---

### Key Features:
- **Automated Job Analysis**: Simplifies understanding job requirements.
- **Smart Candidate Matching**: Uses advanced vector search for precise recommendations.
- **Customizable Cold Emails**: Professional emails designed to maximize impact.
- **End-to-End Automation**: Streamlines the entire process of job-candidate communication.

This tool is designed for **recruiters** and **job placement agencies** to enhance efficiency in identifying and reaching out to potential employers with the most suitable candidates.
""")







