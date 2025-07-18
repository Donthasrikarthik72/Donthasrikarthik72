
print("🤖 Smart Response Bot")
mood = input("How are you feeling today? ").lower()
if "good" in mood or "great" in mood:
    print("That's awesome! Keep smiling 😊")
elif "bad" in mood or "sad" in mood:
    print("Sorry to hear that. Hope things get better ❤️")
else:
    print("Thanks for sharing. Stay positive!")
