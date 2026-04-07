
study_data = {}


def add_subject():
    subject = input("Enter subject name: ").strip()

    if subject == "":
        print("Subject name cannot be empty.")
        return

    if subject in study_data:
        print("Subject already exists.")
    else:
        study_data[subject] = 0
        print(f"{subject} added successfully.")


def add_study_hours():
    subject = input("Enter subject name: ").strip()

    if subject not in study_data:
        print("Subject not found. Add it first.")
        return

    try:
        hours = float(input("Enter study hours: "))
        if hours < 0:
            print("Hours cannot be negative.")
            return
        study_data[subject] += hours
        print(f"Added {hours} hours to {subject}.")
    except ValueError:
        print("Please enter a valid number.")


def view_records():
    if not study_data:
        print("No study records found.")
        return

    print("\nStudy Records:")
    for subject, hours in study_data.items():
        print(f"{subject}: {hours} hours")


def show_total_hours():
    total = sum(study_data.values())
    print(f"Total study hours: {total}")


def show_menu():
    print("\n--- Student Study Tracker ---")
    print("1. Add subject")
    print("2. Add study hours")
    print("3. View records")
    print("4. Show total study hours")
    print("5. Exit")
