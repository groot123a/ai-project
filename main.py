import random

def ai_response(user_input):
    responses = [
        f"AI Suggestion: You can break '{user_input}' into smaller steps.",
        f"Tip: Start working on '{user_input}' for 25 minutes (Pomodoro).",
        f"Insight: Prioritize '{user_input}' based on urgency and importance.",
        f"Automation Idea: Try automating parts of '{user_input}' using scripts."
    ]
    return random.choice(responses)

def main():
    print("🤖 AI Task Assistant (CLI)")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter your task: ")
        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break
        
        response = ai_response(user_input)
        print(response)
        print("-" * 40)

if __name__ == "__main__":
    main()
