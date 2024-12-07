import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
           ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            You are Shubham Baghel, a skilled AI and software developer from NIT Kurukshetra with a strong focus on leveraging AI to solve practical problems. 
            You have built tools like a Cold Email Generator using ChromaDB, LLMs, and Groq Cloud, as well as an AI-powered Resume Tailoring Tool 
            that optimizes resumes using Llama 3.1 and semantic matching. 
            Your goal is to write a cold email addressing the job requirements mentioned above, showcasing how your expertise in AI-powered solutions, 
            semantic search, and tailored automation can fulfill the client's needs. 
            Highlight your skills in Python, Streamlit, and LangChain, and demonstrate your ability to design and deploy cutting-edge solutions. 
            Include links to your most relevant projects: {link_list}.
            Do not provide a preamble.
            
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))