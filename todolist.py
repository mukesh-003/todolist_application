class Task:
    def __init__(self, id, description, due_date, status="Incomplete"):
        self.id = id
        self.description = description
        self.due_date = due_date
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task_id = len(self.tasks) + 1
        task = Task(task_id, description, due_date)
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(f"ID: {task.id}, Description: {task.description}, Due Date: {task.due_date}, Status: {task.status}")

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.id == task_id:
                task.status = new_status

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            todo_list.add_task(description, due_date)

        elif choice == "2":
            todo_list.list_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to update status: "))
            new_status = input("Enter new status (Incomplete/Complete): ")
            todo_list.update_task_status(task_id, new_status)

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please choose a valid option.")
