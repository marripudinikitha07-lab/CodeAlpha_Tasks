🤖 AI FAQ Chatbot using NLP



Overview



AI FAQ Chatbot is a beginner-friendly Python project developed using Streamlit.  

The application answers user questions by matching them with the most relevant FAQ using Natural Language Processing (NLP) techniques.



The chatbot uses TF-IDF vectorization and Cosine Similarity to find the best matching response from a predefined dataset.





Features



\- FAQ-based intelligent chatbot system

\- NLP preprocessing (cleaning, tokenization, stopwords removal)

\- TF-IDF vectorization for text conversion

\- Cosine similarity for best match detection

\- Interactive chat UI using Streamlit

\- Chat history stored using session state

\- Clear chat functionality

\- Beginner-friendly implementation

\- No backend required





Technologies Used



\- Python

\- Streamlit

\- Pandas

\- NLTK

\- Scikit-learn





Installation



Install the required libraries using:



```bash

pip install streamlit pandas nltk scikit-learn





Running the Project



Run the application using:



```bash

python -m streamlit run app.py





Project Structure



CodeAlpha\_AI-FAQ-Chatbot/

│

├── app.py

├── README.md

└── requirements.txt







How It Works



1\. User enters a question in the chat box  

2\. Text is cleaned and preprocessed  

3\. TF-IDF converts text into numerical vectors  

4\. Cosine similarity compares input with FAQ dataset  

5\. The most similar question is selected  

6\. The corresponding answer is displayed  





Future Scope



\- Add AI/LLM integration for smarter responses  

\- Expand FAQ dataset for better accuracy  

\- Add voice input feature  

\- Add multilingual support  

\- Improve UI with better chat design  





Conclusion



This project demonstrates how NLP and machine learning techniques can be used to build a simple intelligent chatbot using Python and Streamlit.





Author



Nikitha Marripudi

