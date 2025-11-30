import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

st.markdown("""
    <style>
        /* Disable horizontal scroll everywhere */
        .block-container, .main, html, body {
            overflow-x: hidden !important;
        }

        /* Force text to wrap inside output */
        pre, code, div {
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
        }
    </style>
""", unsafe_allow_html=True)

def create_streamlit_app(llm, portfolio, clean_text):
    st.markdown(
        """
        <style>
            .header-title {
                display: flex;
                align-items: center;
                gap: 4px;                /* spacing between icon and text */
                margin-bottom: 5px !important;
            }
            .header-title h1 {
                font-size: 2.0rem;
                font-weight: 700;
                margin: 0 !important;    /* remove top/bottom margin */
                padding: 0 !important;
            }
        </style>

        <div class="header-title">
            <img src="https://www.gstatic.com/images/branding/product/1x/gmail_48dp.png"
                width="28" style="margin:0; padding:0;">
            <h1>Mail Generator</h1>
        </div>
        """,
        unsafe_allow_html=True
    )





    url_input = st.text_input("Enter a URL:", value="https://careers.nike.com/lead-data-engineer/job/R-74098")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    


    create_streamlit_app(chain, portfolio, clean_text)


