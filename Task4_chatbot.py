# Task 4: Basic Chatbot
# CodeAlpha Python Programming Internship
# Author: Aryan Pandey

import random
import re

def get_response(user_input):
    """
    Generate a response based on user input using predefined rules.
    """
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()
    
    # Remove punctuation except for special cases
    user_input_clean = re.sub(r'[^\w\s]', '', user_input)
    
    # Greetings
    greeting_patterns = [r'\bhello\b', r'\bhi\b', r'\bhey\b', r'\bgreetings\b', r'\bhowdy\b']
    if any(re.search(pattern, user_input_clean) for pattern in greeting_patterns):
        greetings = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Hey! Nice to chat with you!",
            "Greetings! How are you doing?",
            "Hello! I'm here to help."
        ]
        return random.choice(greetings)
    
    # How are you
    how_are_you_patterns = [r'\bhow are you\b', r'\bhow r u\b', r'\bhow\'s it going\b', r'\bwhat\'s up\b']
    if any(re.search(pattern, user_input_clean) for pattern in how_are_you_patterns):
        responses = [
            "I'm doing great, thanks for asking!",
            "I'm fine, thanks! How about you?",
            "Pretty good! Just here to help.",
            "I'm functioning perfectly! What can I do for you?"
        ]
        return random.choice(responses)
    
    # Goodbye
    goodbye_patterns = [r'\bbye\b', r'\bgoodbye\b', r'\bsee you\b', r'\bfarewell\b', r'\bquit\b', r'\bexit\b']
    if any(re.search(pattern, user_input_clean) for pattern in goodbye_patterns):
        goodbyes = [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! It was nice chatting with you!",
            "Farewell! Hope to talk to you again soon!"
        ]
        return random.choice(goodbyes)
    
    # Thank you
    thank_patterns = [r'\bthank\b', r'\bthanks\b', r'\bthx\b']
    if any(re.search(pattern, user_input_clean) for pattern in thank_patterns):
        responses = [
            "You're welcome!",
            "No problem at all!",
            "Happy to help!",
            "Anytime! That's what I'm here for."
        ]
        return random.choice(responses)
    
    # Help
    help_patterns = [r'\bhelp\b', r'\bassist\b', r'\bsupport\b']
    if any(re.search(pattern, user_input_clean) for pattern in help_patterns):
        responses = [
            "I'm here to help! You can ask me anything.",
            "Sure! What do you need help with?",
            "I'd be happy to assist you. What's your question?",
            "Let me know what you need help with!"
        ]
        return random.choice(responses)
    
    # Questions about the bot
    about_patterns = [r'\bwho are you\b', r'\bwhat are you\b', r'\babout you\b', r'\byour name\b']
    if any(re.search(pattern, user_input_clean) for pattern in about_patterns):
        responses = [
            "I'm a simple rule-based chatbot created for the CodeAlpha internship.",
            "I'm a basic chatbot designed to demonstrate Python programming concepts.",
            "I'm your friendly neighborhood chatbot! Just a simple AI assistant."
        ]
        return random.choice(responses)
    
    # Time-related questions
    time_patterns = [r'\bwhat time\b', r'\btime is it\b', r'\bcurrent time\b']
    if any(re.search(pattern, user_input_clean) for pattern in time_patterns):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    
    # Date-related questions
    date_patterns = [r'\bwhat date\b', r'\bwhat day\b', r'\btoday\'s date\b']
    if any(re.search(pattern, user_input_clean) for pattern in date_patterns):
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."
    
    # Weather (simulated)
    weather_patterns = [r'\bweather\b', r'\bforecast\b', r'\btemperature\b']
    if any(re.search(pattern, user_input_clean) for pattern in weather_patterns):
        responses = [
            "I'm just a chatbot, so I can't check the weather. But I hope it's nice where you are!",
            "I don't have weather data, but you can check your favorite weather app!",
            "Weather seems nice today! (Just kidding, I have no idea)"
        ]
        return random.choice(responses)
    
    # Default responses for unrecognized input
    default_responses = [
        "I'm not sure I understand. Can you rephrase that?",
        "Interesting! Tell me more about that.",
        "I'm still learning. Could you ask me something else?",
        "That's beyond my current knowledge. I'm a simple chatbot!",
        "I don't quite get that. Try asking something different.",
        "Hmm, I'm not sure how to respond to that. Let's talk about something else!"
    ]
    
    return random.choice(default_responses)

def chatbot():
    """
    Main chatbot function that handles the conversation loop.
    """
    print("=" * 60)
    print("WELCOME TO THE BASIC CHATBOT")
    print("=" * 60)
    print("\nI'm a simple rule-based chatbot. You can say things like:")
    print("  - 'hello' or 'hi'")
    print("  - 'how are you?'")
    print("  - 'bye' or 'goodbye'")
    print("  - 'thank you'")
    print("  - 'help'")
    print("  - 'who are you?'")
    print("  - 'what time is it?'")
    print("  - 'what's the weather?'")
    print("\nType 'exit' or 'quit' to end the conversation.")
    print("-" * 60)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("\nBot: Goodbye! Have a wonderful day!")
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        # Get and print response
        response = get_response(user_input)
        print(f"Bot: {response}")

def main():
    """Main function to run the chatbot."""
    chatbot()

if __name__ == "__main__":
    main()