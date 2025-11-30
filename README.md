# Gen-AI-Project-Mail-Generator
This project is an AI-powered  Email generator designed for IT and service-based companies. It automates outreach by extracting job listings from a company’s careers page and generating personalized emails tailored to each job description.

Using Groq, LangChain, ChromaDB, and Streamlit, the tool analyzes job postings, retrieves relevant portfolio links from a vector database, and composes high-quality outreach emails for business development teams.

-> Features

Scrapes job listings from any careers page URL

Analyzes job descriptions using Groq LLMs

Uses LangChain for chaining, prompt templates, and retrieval

Stores portfolio content in a vector database (ChromaDB)

Matches relevant portfolio links based on job requirements

Generates personalized cold emails automatically

Clean user interface built using Streamlit

-> How It Works

User enters a company’s careers page URL.

The system fetches job listings from that page.

Groq-powered LLaMA models analyze the job descriptions.

ChromaDB retrieves portfolio items relevant to the job requirements.

LangChain composes a customized cold email for each role.

The final email includes matched portfolio links for stronger outreach impact.

-> Real-World Scenario: TCS → Godrej

Consider this scenario:

Godrej is hiring for multiple tech roles and is investing heavily in recruitment, onboarding, and training.
TCS, a major IT services company, wants to offer Godrej a dedicated engineering team to reduce hiring time and costs.

Instead of manually checking the Godrej careers page and writing emails, the business development executive at TCS can use this tool.

The system will:

Scrape Godrej’s open roles

Analyze a job such as “Senior Data Engineer – Godrej”

Retrieve matching TCS portfolio projects (e.g., cloud migration, data engineering pipelines)

Generate a personalized cold email where the TCS executive introduces solutions directly aligned with Godrej’s job requirements

This saves hours of manual work and creates highly relevant outreach emails with minimal effort.

-> Architecture Overview

Groq Cloud powers high-speed LLM inference

LangChain handles prompt templates, retrieval, and chain logic

ChromaDB stores embeddings for portfolio assets

Streamlit provides the front-end UI

Python manages scraping, job extraction, and orchestration

