import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todo.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description, due_date=None, priority="medium"):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'due_date': due_date,
            'priority': priority.lower(),
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added with ID {task['id']}")

    def list_tasks(self, show_completed=False):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return

        print("\nTo-Do List:")
        print("-" * 50)
        for task in self.tasks:
            if not show_completed and task['completed']:
                continue
                
            status = "✓" if task['completed'] else " "
            priority = task['priority'].upper()
            due_date = f" | Due: {task['due_date']}" if task['due_date'] else ""
            print(f"{task['id']:3}. [{status}] {task['description']} (Priority: {priority}{due_date})")
        print("-" * 50)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task ID {task_id} not found.")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                del self.tasks[i]
                self.save_tasks()
                print(f"Task {task_id} deleted.")
                return
        print(f"Task ID {task_id} not found.")

    def clear_completed(self):
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task['completed']]
        if len(self.tasks) < initial_count:
            self.save_tasks()
            print(f"Cleared {initial_count - len(self.tasks)} completed tasks.")
        else:
            print("No completed tasks to clear.")

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. List All Tasks (including completed)")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Clear Completed Tasks")
    print("7. Exit")

def main():
    todo = TodoList()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD, optional): ")
            priority = input("Enter priority (low/medium/high, default medium): ") or "medium"
            todo.add_task(description, due_date if due_date else None, priority)
            
        elif choice == '2':
            todo.list_tasks()
            
        elif choice == '3':
            todo.list_tasks(show_completed=True)
            
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as completed: "))
            todo.complete_task(task_id)
            
        elif choice == '5':
            task_id = int(input("Enter task ID to delete: "))
            todo.delete_task(task_id)
            
        elif choice == '6':
            todo.clear_completed()
            
        elif choice == '7':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
