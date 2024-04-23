class Task:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                break

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def display_tasks(self):
        for task in self.tasks:
            status = 'Completed' if task.completed else 'Not Completed'
            print(f"{task.task_id}: {task.description} ({status})")



def main():
    todo_list = TodoList()
    
    while True:
        print("\nTodo List Options:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            task_id = len(todo_list.tasks) + 1
            task = Task(task_id, description)
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.mark_task_completed(task_id)
            print("Task marked as completed!")
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
            print("Task deleted successfully!")
        elif choice == '4':
            print("\nTasks:")
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
