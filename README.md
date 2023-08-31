
# PDF Text Analysis with Streamlit and Langchain

This is a simple Streamlit app that allows you to upload PDF files and ask questions related to the content of those PDFs. The app uses various natural language processing techniques to process and analyze the text in the uploaded PDFs and provide answers to user questions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/chitti-the-robot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd chitti-the-robot
   ```

3. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

4. You'll also need to set up your environment variables. Create a `.env` file in the project directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

## Usage

1. Open the Streamlit app in your web browser by visiting `http://localhost:8501` (or the URL provided by Streamlit).

2. You will see a header introducing Chitti the Robot and a file upload widget.

3. Upload your PDF file using the file upload widget.

4. Click on the "Process" button to start analyzing the uploaded PDF.

5. Chitti the Robot will extract text from the PDF and split it into chunks. It will then create embeddings and a knowledge base to answer your questions.

6. Enter a question in the text input field and click "Ask" to get an answer related to the content of the uploaded PDF.

7. The answer will be displayed on the screen.

## Dependencies

Chitti the Robot relies on the following libraries and frameworks:

- [Streamlit](https://streamlit.io/): For building interactive web applications with Python.
- [dotenv](https://pypi.org/project/python-dotenv/): For loading environment variables from a `.env` file.
- [PyPDF2](https://pythonhosted.org/PyPDF2/): For extracting text from PDF files.
- [langchain](https://github.com/langchain/langchain): A library for various natural language processing tasks.
- [OpenAI](https://openai.com/): For utilizing language models and embeddings.

Make sure to install these dependencies using the provided `requirements.txt` file.

## License

This project is licensed under the [MIT License](LICENSE).

---
