import json
import random
import nltk
from nltk.stem import PorterStemmer

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

with open("intents.json") as f:
    intents = json.load(f)

stemmer = PorterStemmer()


def clean_input(text):
    """
    Tokenize and stem the user's input.
    Tokenize = split a sentence into individual words
    Stem     = reduce each word to its root form
    """
    words = nltk.word_tokenize(text.lower())
    return [stemmer.stem(word) for word in words]


def get_response(user_input):
    """
    Compare the user's input against every pattern in intents.json.
    Count how many words match, then return a response from the
    best-matching intent.
    """
    user_words = clean_input(user_input)

    best_match_tag = None
    best_match_score = 0

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = clean_input(pattern)

            matches = sum(1 for word in user_words if word in pattern_words)

            if matches > best_match_score:
                best_match_score = matches
                best_match_tag = intent["tag"]

    if best_match_score > 0:
        for intent in intents["intents"]:
            if intent["tag"] == best_match_tag:
                return random.choice(intent["responses"])

    return "I'm not sure I understand. Could you rephrase that?"


def main():
    """Main function — runs the chat loop."""
    print("=" * 45)
    print("   AI Chatbot — Python & NLP Project")
    print("   Type 'quit' to exit")
    print("=" * 45)
    print()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "bye"):
            print("Bot: Goodbye! Have a great day!")
            break

        response = get_response(user_input)
        print(f"Bot: {response}")
        print()


if __name__ == "__main__":
    main()
