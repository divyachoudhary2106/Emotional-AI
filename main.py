import os
import google.generativeai as genai

# Gemini API Key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY not found.")
    exit()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

message = input("How are you feeling today? ").lower()

sad_words = ["sad", "upset", "lonely", "depressed", "stressed"]
happy_words = ["happy", "good", "great", "excited", "awesome"]
angry_words = ["angry", "mad", "frustrated"]

emotion = "neutral"

for word in sad_words:
    if word in message:
        emotion = "sad"

for word in happy_words:
    if word in message:
        emotion = "happy"

for word in angry_words:
    if word in message:
        emotion = "angry"

print("\nDetected Emotion:", emotion)

if emotion == "sad":

    print("\nHey, that sounds rough.")
    print("Need a joke, story, or motivation boost?")

    choice = input(
        "\nChoose:\n"
        "1. Joke\n"
        "2. Story\n"
        "3. Motivation\n"
        "Enter choice: "
    )

    if choice == "1":

        prompt = f"""
        The user is feeling sad.

        User message: {message}

        Tell a funny and cheerful joke.
        """

    elif choice == "2":

        prompt = f"""
        User message: {message}

        Tell a short inspiring story.
        """

    else:

        prompt = f"""
        User message: {message}

        Give a powerful motivational message.
        """

    response = model.generate_content(prompt)
    print("\n" + response.text)

elif emotion == "happy":

    prompt = f"""
    User message: {message}

    The user is feeling happy.

    Respond in a fun, energetic and positive way.
    Celebrate their happiness.
    """

    response = model.generate_content(prompt)
    print("\n" + response.text)

elif emotion == "angry":

    prompt = f"""
    User message: {message}

    The user is feeling angry.

    Give a calm and supportive response.
    Help the user relax.
    """

    response = model.generate_content(prompt)
    print("\n" + response.text)

else:

    prompt = f"""
    User message: {message}

    The user's emotion is unclear.

    Respond naturally and ask a thoughtful follow-up question.
    """

    response = model.generate_content(prompt)
    print("\n" + response.text)
  
