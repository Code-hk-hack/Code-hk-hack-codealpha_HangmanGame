# 🤖 Mahiru - Rule-Based Chatbot

A simple, friendly rule-based chatbot built in Python. Mahiru greets the user, asks for their name, checks in on how they're feeling, and responds using predefined keyword matching — all through a console-based conversation loop.

## Features
- Greets the user and waits for a valid "hello" before starting
- Personalized responses based on the name entered (with special easter-egg replies)
- Detects positive vs. negative mood keywords and responds empathetically
- Graceful conversation exit only after the user says "bye"
- Option to restart the chat or end the session completely

## Concepts Demonstrated
- `while` loops for input validation
- `if / elif / else` conditional logic
- String methods (`.lower()`, `.strip()`)
- Lists for keyword matching
- f-strings for dynamic output

## How to Run
```bash
python chatbot.py
```

## Example Interaction
```
Mahiru: Say 'hello' to start our chat! 👋
You: hello
Mahiru: Yay! Hello there! Great, let's chat! 🎉
Mahiru: What's your name?
You: Alex
Mahiru: Nice to meet you, Alex! What a lovely name! ✨
```

## Possible Improvements
- Expand keyword lists to catch more variations of mood/greetings
- Add more topics the bot can respond to (weather, jokes, etc.)
- Refactor repeated input-validation loops into a reusable function
