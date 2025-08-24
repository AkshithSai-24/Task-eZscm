# Task-eZscm

A multi-level Python project demonstrating chatbot, calculator, and translation tools using LangChain and Gemini AI.

---

## Project Structure

```
Task-eZscm/
│
├── Level 1/
│   ├── chatbot.py
│   └── logs.txt
│
├── Level 2/
│   ├── calculator_tools.py
│   ├── chat_bot_tools.py
│   └── logs.txt
│
├── Level 3/
│   ├── calculator_tools.py
│   ├── chat_bot_cal_trans.py
│   ├── translator_tools.py
│   └── logs.txt
│
├── requirements.txt
└── README.md
```

---

## Levels Overview

### Level 1: Basic Chatbot

- **File:** `chatbot.py`
- **Description:** Simple chatbot using LangChain and Gemini AI.
- **Log:** Interactions saved in `logs.txt`.

### Level 2: Chatbot with Calculator Tools

- **Files:** `chat_bot_tools.py`, `calculator_tools.py`
- **Description:** Chatbot can answer math questions using calculator tools (add, subtract, multiply, divide, etc.).
- **Log:** Interactions saved in `logs.txt`.

### Level 3: Chatbot with Calculator & Translator Tools

- **Files:** `chat_bot_cal_trans.py`, `calculator_tools.py`, `translator_tools.py`
- **Description:** Chatbot supports both calculator and translation functionalities.
- **Log:** Interactions saved in `logs.txt`.

---

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/AkshithSai-24/Task-eZscm.git
   cd Task-eZscm
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_google_gemini_api_key
     ```

---

## Usage

- **Level 1:**  
  Run the basic chatbot:
  ```sh
  python Level\ 1\chatbot.py
  ```

- **Level 2:**  
  Run the chatbot with calculator tools:
  ```sh
  python Level\ 2\chat_bot_tools.py
  ```

- **Level 3:**  
  Run the chatbot with calculator and translator tools:
  ```sh
  python Level\ 3\chat_bot_cal_trans.py
  ```

---

## Main Branch

- The main branch contains all levels and the shared `requirements.txt`.
- Each level is self-contained and can be run independently.

---
