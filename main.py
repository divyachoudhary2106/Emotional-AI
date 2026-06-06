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

print("Detected Emotion:", emotion)

if emotion == "sad":
    print("Hey, that sounds rough.")
    print("Life is being a little dramatic today, huh?")
    print("But don't worry, I'm here with you. 💙")
    print("Need a joke, a story, or a motivation boost?")

    choice = input(
        "\nChoose:\n"
        "1. Joke 😆\n"
        "2. Story 📖\n"
        "3. Motivation 💪\n"
    )

  if choice == "1":
        print(f"\nI see. You mentioned: {situation}")
        print("Let me cheer you up with a joke!")
        print(get_joke())

    elif choice == "2":
        print(get_story())

    elif choice == "3":
        print(get_motivation())

elif emotion == "happy":
    print("Ayy, let's gooo! 🎉")
    print("Love that energy.")
    print("Whatever happened today, keep it up! 😎")

elif emotion == "angry":
    print("Okay... somebody clearly tested your patience today. 😅")
    print("Before we start a villain arc, let's calm down a bit.")
    print("Want to talk about it?")

else:
    print("Hmm... I'm not fully sure how you're feeling yet. 🤔")
    print("Tell me more, I'm listening. 👀") 
  
