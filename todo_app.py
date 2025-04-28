class TodoApp:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\n--- Todo App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            index = 1
            for task in self.tasks:
                print(str(index) + ". " + task)
                index += 1

    def update_task(self):
        self.view_tasks()
        try:
            task_no = int(input("Enter task number to update: "))
            if 1 <= task_no <= len(self.tasks):
                new_task = input("Enter new task: ")
                self.tasks[task_no - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    def delete_task(self):
        self.view_tasks()
        try:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(self.tasks):
                deleted = self.tasks.pop(task_no - 1)
                print(f"Task '{deleted}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

app = TodoApp()
while True:
            app.show_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                app.add_task()
            elif choice == '2':
                app.view_tasks()
            elif choice == '3':
                app.update_task()
            elif choice == '4':
                app.delete_task()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-5.")

# Create an object of the TodoApp class

