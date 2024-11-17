# Cold Email Generator

## Overview
The **Cold Email Generator** is a tool designed to automate the process of creating professional and targeted cold emails for job providers. It uses advanced AI and web scraping technologies to extract job information, match candidates, and craft personalized emails.

---

## Features
1. **Job Portal Scraping**: Extracts job details from a given job portal link using **LangChain**.
2. **AI-Powered Job Analysis**:
   - Extracts key information such as Role, Experience, Skills, and Job Description using the **Groq API** with the `Llama-3.2-90B-text-preview` model.
3. **Candidate Matching**:
   - Generates **384-dimensional embeddings** for candidates using **Hugging Face Inference API**.
   - Searches for suitable candidates in a **Pinecone vector database** and retrieves their portfolios.
4. **Cold Email Creation**:
   - Combines job details and matching candidates' information to generate personalized cold emails.
   - Emails include links to candidates' portfolios for better employer engagement.

---

## Tools Used
- **LangChain**: For web scraping job information from job portals.
- **Groq API**: 
  - To extract job information and generate emails using `Llama-3.2-90B-text-preview`.
- **Hugging Face Inference**: To generate embeddings for candidate profiles.
- **Pinecone**: To store and query embeddings for matching candidates.
- **Streamlit**: To create an interactive and user-friendly interface.

---

## How to Use
1. Input the job portal link in the application.
2. The tool scrapes the job details and analyzes the job description.
3. Suitable candidates are matched from the database, and their portfolio links are included.
4. A professionally crafted cold email is generated for the job provider.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cold-email-generator.git
   cd cold-email-generator
