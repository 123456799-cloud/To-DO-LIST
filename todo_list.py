#Task 1
# ToDo list using python

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "pending"})

    def update_task(self, task_id, status):
        if task_id < len(self.tasks):
            self.tasks[task_id]["status"] = status
        else:
            print("Invalid task ID")

    def delete_task(self, task_id):
        if task_id < len(self.tasks):
            del self.tasks[task_id]
        else:
            print("Invalid task ID")

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task['task']} - {task['status']}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_id = int(input("Enter the task ID to update: "))
            status = input("Enter the new status (pending/done): ")
            todo_list.update_task(task_id - 1, status)
        elif choice == "3":
            task_id = int(input("Enter the task ID to delete: "))
            todo_list.delete_task(task_id - 1)
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
