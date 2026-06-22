# Task Manager - Trade Finance Toolkit
# A command-line task tracker for the team

tasks = []


def add_task(description):
    """Add a new task to the list."""
    task = {"description": description, "done": False}
    tasks.append(task)
    print(f"Added task: {description}")


def main():
    print("=== Task Manager ===")
    while True:
        print("\nOptions: add, quit")
        choice = input("Choose an option: ").strip()

        if choice == "add":
            desc = input("Task description: ").strip()
            add_task(desc)
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown option")


if __name__ == "__main__":
    main()
