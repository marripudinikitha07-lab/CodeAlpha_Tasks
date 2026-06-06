import streamlit as st
import pandas as pd
import nltk
import re

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('stopwords')

# ---------------------------
# FAQ DATASET
# ---------------------------

faq_data = {
    "Question": [
        "What is Artificial Intelligence?",
        "What is Machine Learning?",
        "What is Deep Learning?",
        "What is Python?",
        "What is Streamlit?",
        "How does AI work?",
        "What are the applications of AI?",
        "Is Python easy to learn?",
        "Can I build AI projects with Python?",
        "What is NLP?",

        "What is Data Science?",
        "What is a chatbot?",
        "What is TensorFlow?",
        "What is Scikit-learn?",
        "What is a neural network?",
        "What is supervised learning?",
        "What is unsupervised learning?",
        "What is reinforcement learning?",
        "What is computer vision?",
        "What is generative AI?",

        "What is GitHub?",
        "What is Git?",
        "Why should I learn Python?",
        "What is a programming language?",
        "What is a database?",
        "What is SQL?",
        "What is cloud computing?",
        "What is an API?",
        "What is cybersecurity?",
        "What is data analysis?",
        "What is an algorithm?",
        "What is a data structure?",
        "What is a variable in Python?",
        "What is a function in Python?",
        "What is object oriented programming?",
        "What is a loop?",
        "What is an if statement?",
        "What is debugging?",
        "What is software development?",
        "What is web development?",
        "What is front end development?",
        "What is back end development?",
        "What is full stack development?",
        "What is HTML?",
        "What is CSS?",
        "What is JavaScript?",
        "What is a Python library?",
        "What is NumPy?",
        "What is Pandas?",
        "What is data visualization?",
        "What is Matplotlib?",
        "What is automation?",
        "What is an operating system?",
        "What is Linux?",
        "What is Windows?",
        "What is a software engineer?",
        "What is an internship?",
        "How can I improve my coding skills?",
        "How do I start learning programming?",
        "What are coding projects?"
    ],
    "Answer": [
        "Artificial Intelligence is the simulation of human intelligence by machines.",
        "Machine Learning is a subset of AI that enables systems to learn from data.",
        "Deep Learning is a subset of Machine Learning that uses neural networks.",
        "Python is a popular programming language used for AI, web development, and data science.",
        "Streamlit is a Python framework used to create interactive web applications.",
        "AI works by processing data, learning patterns, and making decisions.",
        "AI is used in healthcare, education, finance, robotics, and many other fields.",
        "Yes, Python is considered one of the easiest programming languages for beginners.",
        "Yes, Python provides libraries like TensorFlow, PyTorch, and Scikit-learn for AI development.",
        "NLP stands for Natural Language Processing, which enables computers to understand human language.",

        "Data Science is the field of extracting insights and knowledge from data.",
        "A chatbot is a software application that simulates conversations with users.",
        "TensorFlow is an open-source machine learning framework developed by Google.",
        "Scikit-learn is a Python library used for machine learning and data analysis.",
        "A neural network is a computational model inspired by the human brain.",
        "Supervised learning is a machine learning technique that uses labeled data for training.",
        "Unsupervised learning finds hidden patterns in data without labeled outputs.",
        "Reinforcement learning teaches an agent to make decisions through rewards and penalties.",
        "Computer vision enables computers to interpret and understand images and videos.",
        "Generative AI creates new content such as text, images, music, or code.",

        "GitHub is a platform used for version control and collaborative software development.",
        "Git is a version control system that helps track changes in source code.",
        "Python is easy to learn, versatile, and widely used in many industries.",
        "A programming language is a set of instructions used to communicate with computers.",
        "A database is an organized collection of data stored electronically.",
        "SQL is a language used to manage and query databases.",
        "Cloud computing provides computing services over the internet.",
        "An API allows different software applications to communicate with each other.",
        "Cybersecurity involves protecting systems, networks, and data from attacks.",
        "Data analysis is the process of examining data to draw conclusions and support decision-making.",
        "An algorithm is a step-by-step procedure used to solve a problem or perform a task.",
        "A data structure is a method of organizing and storing data efficiently.",
        "A variable is a container used to store data values in Python.",
        "A function is a reusable block of code designed to perform a specific task.",
        "Object Oriented Programming is a programming paradigm based on objects and classes.",
        "A loop is used to execute a block of code repeatedly.",
        "An if statement is used to make decisions based on conditions.",
        "Debugging is the process of finding and fixing errors in a program.",
        "Software development is the process of designing, creating, testing, and maintaining software.",
        "Web development involves building and maintaining websites and web applications.",
        "Front end development focuses on the visual and interactive parts of a website.",
        "Back end development focuses on server-side logic, databases, and application functionality.",
        "Full stack development combines both front end and back end development skills.",
        "HTML is the standard markup language used to create web pages.",
        "CSS is used to style and format web pages.",
        "JavaScript is a programming language used to create interactive web pages.",
        "A Python library is a collection of pre-written code that helps perform specific tasks.",
        "NumPy is a Python library used for numerical and scientific computing.",
        "Pandas is a Python library used for data manipulation and analysis.",
        "Data visualization is the graphical representation of information and data.",
        "Matplotlib is a Python library used to create charts and graphs.",
        "Automation is the use of technology to perform tasks with minimal human intervention.",
        "An operating system manages computer hardware and software resources.",
        "Linux is an open-source operating system widely used in servers and development environments.",
        "Windows is a popular operating system developed by Microsoft.",
        "A software engineer designs, develops, tests, and maintains software applications.",
        "An internship provides practical work experience in a professional environment.",
        "You can improve coding skills through regular practice, projects, and problem solving.",
        "You can start learning programming by choosing a language like Python and practicing consistently.",
        "Coding projects are practical applications built to solve problems and demonstrate programming skills."
    ]
}

faq_df = pd.DataFrame(faq_data)

# ---------------------------
# NLP PREPROCESSING
# ---------------------------

stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = text.split()

    words = [
        word for word in words
        if word not in stop_words
    ]

    return " ".join(words)

faq_df["Processed"] = faq_df["Question"].apply(preprocess)

# ---------------------------
# TF-IDF + COSINE SIMILARITY
# ---------------------------

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    faq_df["Processed"]
)

def get_response(user_question):

    processed_question = preprocess(user_question)

    user_vector = vectorizer.transform(
        [processed_question]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match_index = similarity_scores.argmax()

    best_score = similarity_scores[0][best_match_index]

    if best_score < 0.2:
        return "Sorry, I couldn't find a relevant answer."

    return faq_df.iloc[best_match_index]["Answer"]

# ---------------------------
# STREAMLIT UI
# ---------------------------

st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI FAQ Chatbot")

st.write(
    "Ask a question related to AI, Python, Machine Learning, NLP, or Streamlit."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_question = st.chat_input("Type your question here...")

if user_question:

    answer = get_response(user_question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()

# Clear Chat Button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()