# 🏦 Banking Application Experience Analysis

This project focuses on developing a **sentiment analysis system** for banking applications of three major Ethiopian banks: **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank**.

The goal is to collect and analyze customer feedback to gain insights into user sentiments about their digital banking experiences. The results will provide actionable intelligence for improving customer service, identifying issues, and enhancing the competitive positioning of the respective banking applications.

---

## 🎯 Objectives

The main objectives of this project are to:

- Collect customer feedback data from various sources.
- Apply advanced sentiment analysis techniques to assess customer opinions.
- Store the analysis results in an **Oracle** database for further reporting and insights.

---

## 📁 Project Structure

```
banking-application-sentiment-analysis/
│
├── data/                  # Raw and processed datasets
├── notebooks/   
     ├── Data_Cleaning.ipynb           
├── scripts/
│   ├── Data_Cleaning.py   # Text preprocessing and cleaning
│   ├── Loading.py  
│   └──        
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
```

---

## 🔧 Prerequisites

Ensure the following are installed on your machine:

- Python **3.8** or newer  
- `pip` (Python package manager)  
- Oracle Database (or access credentials to an existing instance)  

📌 You also need to configure the Oracle connection settings in `loading.py`.

---

## 🧰 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/samrizee/banking-application-sentiment-analysis.git
   cd banking-application-sentiment-analysis
   ```

2. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database settings:**  
   Edit the `loading.py` file to include your Oracle DB credentials and connection string.
