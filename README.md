# **Cold Email Generator for Job Applications**

## **Overview**
The **Cold Email Generator for Job Applications** is an AI-powered tool designed to streamline the job application process. It uses cutting-edge natural language processing to create personalized and compelling cold emails tailored to specific job postings. By leveraging AI, web scraping, and semantic search, the generator ensures your emails are professional, relevant, and engaging.

---

## **Features**
1. **Web Scraping**:
   - Automatically extracts job details from job posting URLs using **WebBaseLoader**.

2. **AI-Powered Analysis**:
   - Utilizes **LLaMA 3.1 70B**, an open-source large language model, to process job data and convert it into structured JSON format.

3. **Semantic Search**:
   - Leverages **ChromaDB** for efficient and contextually relevant information retrieval.

4. **Personalized Email Generation**:
   - Creates tailored cold emails based on the specifics of the job posting, ensuring high relevance and professionalism.

5. **User-Friendly Interface**:
   - Built with **Streamlit**, providing a simple and interactive web interface for users.

6. **Cloud-Based Processing**:
   - Powered by **Groq Cloud** for high-speed AI inference and seamless scalability.

---

## **Technologies Used**
- **Python**: Core programming language for the project.
- **LangChain**: Framework for managing and chaining AI-powered tasks.
- **LLaMA 3.1 70B**: Open-source large language model for natural language processing and email generation.
- **Groq Cloud**: Cloud platform for efficient and rapid AI inference.
- **Streamlit**: Framework for building an intuitive web application.
- **ChromaDB**: Database for semantic search and information retrieval.
- **WebBaseLoader**: Library for extracting job details from posting URLs.

---

## **Installation**

### **Prerequisites**
- Python 3.9 or higher
- Virtual environment (recommended)
- Required libraries (listed in `requirements.txt`)

### **Setup Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/cold-email-generator.git
   cd cold-email-generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser (default: [http://localhost:8501](http://localhost:8501)).

---

## **Usage**

1. **Input Job Posting URL**:
   - Paste the job posting URL in the provided field.

2. **AI Analysis**:
   - The AI extracts job details and converts them into structured JSON format.

3. **Generate Email**:
   - Click the "Generate Email" button to create a personalized cold email tailored to the job posting.

4. **Edit and Export**:
   - Review and edit the generated email, then export it for use.

---

## **Folder Structure**
```
cold-email-generator/
│
├── app.py                # Main Streamlit app script
├── modules/              # Custom Python modules
│   ├── scraping.py       # Web scraping logic
│   ├── ai_analysis.py    # LLaMA 3.1 AI-powered analysis
│   ├── email_generator.py # Cold email generation logic
│   ├── semantic_search.py # Semantic search integration
│
├── templates/            # Streamlit UI templates
│
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # License information
└── .gitignore            # Git ignore file
```

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature description"`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**
- **Meta AI** for the open-source LLaMA 3.1 70B model.
- **Groq Cloud** for providing high-performance AI inference.
- **ChromaDB** for powerful semantic search capabilities.
- **Streamlit** for enabling an intuitive user interface.

---

### **Contact**
For questions or feedback, reach out at **shubhambaghel307@gmail.com**.
