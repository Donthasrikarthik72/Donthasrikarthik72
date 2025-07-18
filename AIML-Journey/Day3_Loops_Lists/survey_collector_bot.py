
print("🧠 Survey Collector Bot")
survey_data = []
n = int(input("How many users do you want to survey? "))
for i in range(n):
    print(f"\n🧾 Survey #{i+1}")
    name = input("Enter name: ")
    age = input("Enter age: ")
    subject = input("Favorite subject: ")
    entry = f"{name}, Age: {age}, Subject: {subject}"
    survey_data.append(entry)
print("\n✅ Survey Complete. Collected Data:")
for data in survey_data:
    print("📄", data)
