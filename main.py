from tracker import add_subject, add_study_hours, view_records, show_total_hours, show_menu


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_subject()
        elif choice == "2":
            add_study_hours()
        elif choice == "3":
            view_records()
        elif choice == "4":
            show_total_hours()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
