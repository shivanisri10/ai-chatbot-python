# 🤖 AI Chatbot using Python

A beginner AI chatbot built using **Python** and **Natural Language Processing (NLP)**. It reads intents from a JSON file, matches user input using word stemming and tokenization, and replies with an appropriate response.

---

## ✨ Features

- Responds to user greetings
- Answers basic questions
- Simple intent recognition using NLP
- Easy to extend - just add new entries to `intents.json`

---

## 📁 Project Structure

```
ai-chatbot-python/
├── chatbot.py        # Main chatbot code
├── intents.json      # Patterns and responses
├── requirements.txt  # Dependencies
└── README.md         # Project info
```

---

## 🛠️ Technologies Used

- **Python** - core language
- **NLTK** - tokenization and stemming
- **NumPy** - listed as a dependency for NLP support

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/shivanisri10/ai-chatbot-python.git
cd ai-chatbot-python
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the chatbot**
```bash
python chatbot.py
```

---

## 🧠 How It Works

1. The user types a message
2. The message is **tokenized** (split into words) and **stemmed** (words reduced to root form) using NLTK
3. Each word is compared against patterns stored in `intents.json`
4. The intent with the most word matches is selected
5. A random response from that intent is printed

---

## ➕ How to Add New Topics

Open `intents.json` and add a new block:

```json
{
  "tag": "weather",
  "patterns": ["what is the weather", "is it raining", "weather today"],
  "responses": [
    "I can't check live weather, but try Google or weather.com!",
    "No weather API yet — but that's a great next feature to add!"
  ]
}
```

Save the file and re-run `chatbot.py`. No other changes needed!

---

## 🎯 Goal

This project was built while learning **AI/ML fundamentals** and **Natural Language Processing** as a first-year CSE student.

---

## 📄 License

Open source under the [MIT License](LICENSE).
