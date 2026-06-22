# Task Manager - Trade Finance Toolkit
# A command-line task tracker for the team

tasks = []


def add_task(description):
    """Add a new task to the list."""
    task = {"description": description, "done": False}
    tasks.append(task)
    print(f"Added task: {description}")
def list_tasks():
    """Show all tasks in the list."""
    if len(tasks) == 0:
        print("Task list is empty.")
        return
    for index, task in enumerate(tasks):
        mark = "DONE" if task["done"] else "TODO"
        print(f"[{index}] ({mark}) {task['description']}")

def main():
    print("=== Task Manager ===")
    while True:
        print("\nOptions: add, list, quit")
        choice = input("Choose an option: ").strip()

        if choice == "add":
            desc = input("Task description: ").strip()
            add_task(desc)
        elif choice == "list":
            list_tasks()    
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown option")


if __name__ == "__main__":
    main()
