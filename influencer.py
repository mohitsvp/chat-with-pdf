import streamlit as st
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import json


def main():

    load_dotenv()

    st.set_page_config(page_title="Chat with PDF", page_icon=":books:")

    st.header("Hi, I am Chitti the Robot :robot_face:")

    with open("data.json", "rb") as json_file:
        data = json.load(json_file)
        
        # Create Embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(data, embeddings)

        user_question = st.text_input("Ask a question about your documents:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)

            # docs = str(docs[0])

            st.write(docs)

            # st.write(docs.split("URL")[-1])



            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain({"input_documents": docs, "question": user_question},return_only_outputs=True)
            
            st.write(response['output_text'])



if __name__ == '__main__':
    main()