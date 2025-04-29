import json
import os

class TodoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.tasks = json.load(file)
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def show_menu(self):
        print("\n--- Todo App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

    def add_task(self):
        task = input("Enter the task: ").strip()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            print("Task added successfully!")
        else:
            print("Task cannot be empty!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            while True:
                ch = input("Do you want to add a task? (Y/N): ").strip().lower()
                if ch == 'y':
                    self.add_task()
                    break
                elif ch == 'n':
                    print("OK, Goodbye!")
                    break
                else:
                    print("Please enter Y or N.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def update_task(self):
        if not self.tasks:
            print("No tasks to update!")
            return

        self.view_tasks()
        while True:
            task_no = input("Enter task number to update: ").strip()
            if task_no.isdigit():
                task_no = int(task_no)
                if 1 <= task_no <= len(self.tasks):
                    new_task = input("Enter new task: ").strip()
                    if new_task:
                        self.tasks[task_no - 1] = new_task
                        self.save_tasks()
                        print("Task updated successfully!")
                        break
                    else:
                        print("Task cannot be empty!")
                else:
                    print("Invalid task number!")
            else:
                print("Please enter a valid number!")

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete!")
            return

        self.view_tasks()
        while True:
            task_no = input("Enter task number to delete: ").strip()
            if task_no.isdigit():
                task_no = int(task_no)
                if 1 <= task_no <= len(self.tasks):
                    deleted = self.tasks.pop(task_no - 1)
                    self.save_tasks()
                    print(f"Task '{deleted}' deleted successfully!")
                    break
                else:
                    print("Invalid task number!")
            else:
                print("Please enter a valid number!")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-5): ").strip()
            if choice not in {'1', '2', '3', '4', '5'}:
                print("Invalid choice! Please enter a number between 1-5.")
                continue

            match choice:
                case '1': self.add_task()
                case '2': self.view_tasks()
                case '3': self.update_task()
                case '4': self.delete_task()
                case '5':
                    print("Goodbye!")
                    break

if __name__ == "__main__":
    app = TodoApp()
    app.run()
