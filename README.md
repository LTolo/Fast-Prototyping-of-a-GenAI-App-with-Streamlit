# Fast Prototyping of GenAI Apps with Streamlit

This repository contains the projects developed during the **DeepLearning.AI** course: *"Fast Prototyping of GenAI Apps with Streamlit"*. The goal of this project is to demonstrate the evolution from a basic data processing tool to a fully integrated AI-powered data assistant.

## 🚀 Project Overview

The project is divided into two main stages of development, showcasing how to build, scale, and integrate LLMs into data applications.

### 📁 [GenAi-data-ingestion-and-cleaning]
This module focuses on the fundamentals of Streamlit and local data handling.
* **Key Features:** CSV data ingestion, automated text cleaning using Regex, and interactive data visualization (Bar Charts).
* **Tech Stack:** Streamlit, Pandas, Python (Regex).
* **Learning Goal:** Understanding state management (`st.session_state`) and building a responsive UI layout.

### 📁 [GenAi-data-assistant](./GenAi-data-assistant)
The final stage of the application, transforming the prototype into a cloud-native AI assistant.
* **Key Features:** * **Snowflake Integration:** Direct connection to cloud data warehouses.
    * **Cortex AI:** Leveraging the `claude-3-5-sonnet` model directly within Snowflake for high-performance inference.
    * **Natural Language Querying:** A chatbot interface that allows users to ask questions about their data in plain English.
* **Tech Stack:** Streamlit, Snowflake (Snowpark & Cortex), Matplotlib, Claude 3.5 Sonnet.
* **Learning Goal:** Implementing RAG (Retrieval-Augmented Generation) patterns and deploying enterprise-grade GenAI apps.

---

## 🛠️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/DEIN-USER-NAME/Fast-Prototyping-of-a-GenAI-App-with-Streamlit.git](https://github.com/DEIN-USER-NAME/Fast-Prototyping-of-a-GenAI-App-with-Streamlit.git)
    ```

2.  **Install Dependencies:**
    Each folder contains its specific logic. Ensure you have the necessary libraries installed:
    ```bash
    pip install streamlit pandas snowflake-snowpark-python matplotlib
    ```

3.  **Snowflake Configuration:**
    For the Data Assistant (Module 3), ensure your `.streamlit/secrets.toml` is configured with your Snowflake credentials (do not commit this file to GitHub!).

---
*Disclaimer: This project was built as part of the DeepLearning.AI course curriculum.*
