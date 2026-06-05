from datetime import datetime, timedelta

subjects = {}

def add_subject():
    name = input("Subject: ")
    chapters = int(input("Number of chapters: "))
    exam_date = input("Exam Date (YYYY-MM-DD): ")

    subjects[name] = {
        "chapters": chapters,
        "completed": 0,
        "exam": exam_date
    }

def show_plan():
    today = datetime.today()

    for sub, data in subjects.items():
        exam = datetime.strptime(data["exam"], "%Y-%m-%d")

        days_left = (exam - today).days

        remaining = data["chapters"] - data["completed"]

        if days_left > 0:
            per_day = round(remaining / days_left, 2)
        else:
            per_day = remaining

        print(f"\n{sub}")
        print(f"Days Left: {days_left}")
        print(f"Remaining Chapters: {remaining}")
        print(f"Study {per_day} chapters/day")

while True:
    print("\n1 Add Subject")
    print("2 Show Plan")
    print("3 Exit")

    choice = input("> ")

    if choice == "1":
        add_subject()

    elif choice == "2":
        show_plan()

    elif choice == "3":
        break
