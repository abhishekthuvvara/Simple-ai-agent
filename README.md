# 🤖 Rule-Based Order Chatbot

A simple rule-based chatbot developed using **Python** and **Pandas**. The chatbot reads data from an Excel file and responds to predefined user queries using `if-elif-else` statements.

## 📌 Project Overview

This project demonstrates the fundamentals of a rule-based AI chatbot. Instead of using machine learning or NLP, the chatbot uses predefined conditions to answer questions related to an order dataset stored in an Excel file.

## ✨ Features

- Greets the user.
- Runs continuously until the user types `exit`.
- Uses `if-elif-else` decision-making logic.
- Reads order data from an Excel dataset.
- Answers predefined questions such as:
  - Total Orders
  - Total Sales
  - Available Payment Methods
  - Pending Orders
  - Product List

## 🛠 Technologies Used

- Python 3
- Pandas
- OpenPyXL
- Visual Studio Code

## 📂 Project Structure

```
Simple-ai-agent/
│── simple ai agent.py
│── Dataset for Data Analytics.xlsx
│── requirements.txt
│── README.md
```

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Simple-ai-agent.git
```

### Move into the project folder

```bash
cd Simple-ai-agent
```

### Install the required libraries

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python "simple ai agent.py"
```

## 💬 Supported Commands

| User Input | Bot Response |
|------------|--------------|
| hi | Greets the user |
| hello | Greets the user |
| hey | Greets the user |
| total orders | Displays the total number of orders |
| total sales | Displays total sales amount |
| payment methods | Shows available payment methods |
| pending orders | Displays the number of pending orders |
| products | Lists all available products |
| exit | Closes the chatbot |

## 📊 Dataset

The chatbot uses the Excel dataset:

```
Dataset for Data Analytics.xlsx
```

The dataset includes information such as:

- Order ID
- Date
- Customer ID
- Product
- Quantity
- Unit Price
- Payment Method
- Order Status
- Coupon Code
- Referral Source
- Total Price

## 🎯 Learning Objectives

This project demonstrates:

- Rule-Based Artificial Intelligence
- Control Flow
- Decision Making
- Python Loops
- Conditional Statements
- Reading Excel files using Pandas

## 🚀 Future Improvements

- Natural Language Processing (NLP)
- Voice-based interaction
- GUI using Tkinter
- Database integration
- Machine Learning chatbot
- Flask or Streamlit web application

## 👨‍💻 Author

**Abhishek Thuvvara**

B.Tech Artificial Intelligence Student

GitHub: https://github.com/abhishekthuvvara
