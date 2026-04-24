import requests

API_KEY = "your_api_key_here"  # replace later

def ask_ai(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error connecting to AI"

def main():
    print("🤖 AI Productivity Assistant")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter your task/question: ")
        
        if user_input.lower() == "exit":
            break

        reply = ask_ai(user_input)
        print("\nAI Response:\n", reply)
        print("-" * 50)

if __name__ == "__main__":
    main()
