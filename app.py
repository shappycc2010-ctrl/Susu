from flask import Flask, render_template, request, jsonify
from semantic_memory import load_memory, save_memory
from flyer_generator import generate_flyer
from news_fetcher import get_news

app = Flask(__name__)

memory = load_memory()

# Core AI loop
def reason(user_input):
    response = ""
    action = None
    user_input_lower = user_input.lower()

    # Chat greetings
    if "hello" in user_input_lower or "hi" in user_input_lower:
        response = "Hi Shappy! How can I help you today?"

    # News request
    elif "news" in user_input_lower:
        country = "us"
        category = None
        if "tech" in user_input_lower or "technology" in user_input_lower:
            category = "technology"
        elif "sports" in user_input_lower:
            category = "sports"
        elif "nigeria" in user_input_lower:
            country = "ng"
        news_list = get_news(country=country, category=category)
        response = "Here are the latest headlines:\n" + "\n".join(news_list)

    # Flyer request
    elif "flyer" in user_input_lower:
        colors = memory.get("preferences", {}).get("colors", ["black", "green"])
        filename = generate_flyer(colors)
        response = f"Flyer generated: {filename}"

    # Memory request
    elif "my colors" in user_input_lower:
        colors = memory.get("preferences", {}).get("colors", [])
        response = f"Your favorite colors: {', '.join(colors)}" if colors else "No colors saved."

    # Save preferences
    elif "set colors" in user_input_lower:
        words = user_input_lower.split()
        # Simple parser for colors
        color_list = [word for word in words if word in ["black","green","blue","red","yellow","white","purple"]]
        if "preferences" not in memory:
            memory["preferences"] = {}
        memory["preferences"]["colors"] = color_list
        save_memory(memory)
        response = f"Saved your colors: {', '.join(color_list)}"

    else:
        response = "I remember everything and can suggest next steps!"

    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    response = reason(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
