# CODSOFT
🔐 Password Generation Process
1️⃣ Character Selection
🔤 Lowercase Letters → a-z

🔠 Uppercase Letters → A-Z (if enabled)

🔢 Digits → 0-9 (if enabled)

❗ Special Symbols → !@#$%^&*() (if enabled)

2️⃣ Password Construction
⚡ Mandatory Inclusion → At least 1 character from each selected set.

🎲 Random Fill → Remaining characters picked randomly.

🔀 Shuffling → Final shuffle to prevent predictable patterns.

3️⃣ User Customization
📏 Length → Choose between 8-128 characters.
Delete README.md

🛠 Character Types → Toggle uppercase, digits, symbols on/off.

4️⃣ Output
🔑 Secure Password → Generated & displayed


TO DO LIST:
1. Initializing the To-Do List 🚀
When you start the application, the TodoList class is initialized.

It tries to load existing tasks from todo.json.
If the file doesn't exist or is empty/corrupted, it starts with an empty list of tasks.
It also determines the next_id for new tasks to ensure unique IDs.
2. Adding a New Task ➕
You'll be prompted to enter a description for your task.
You can optionally add a due date (in YYYY-MM-DD format), set a priority (low, medium, or high), and assign a category.
A new task dictionary is created with a unique ID, the details you provided, a completed status of False, and a created_at timestamp.
The new task is added to your list, and the entire list is saved back to todo.json.
You'll see a ✅ Task added with ID [ID] confirmation.
3. Listing Tasks 📋
You have two main options:
List Pending Tasks: This shows only tasks that are not yet completed.
List All Tasks: This displays both pending and completed tasks.
Each task is displayed with its ID, completion status (✓ for completed, for pending), description, priority, due date (if provided), and category (if provided).
If no tasks match your criteria (e.g., no tasks in a specific category), you'll see a 📭 No tasks found matching your criteria. message.
You can also sort tasks by priority or due_date when listing.
4. Marking a Task as Completed ✅
You'll be asked to enter the ID of the task you want to mark as complete.
The application finds the task by its ID and updates its completed status to True and sets a completed_at timestamp.
The updated task list is saved.
A ✅ Task [ID] marked as completed. message confirms the action.
If the task is already completed, it will let you know with an ℹ️ emoji.
5. Deleting a Task 🗑️
You'll be asked for the ID of the task to delete.
The task is removed from the list.
The updated list is saved to todo.json.
You'll see a 🗑️ Task [ID] deleted. confirmation.
6. Clearing Completed Tasks 🧹
This function goes through your task list and removes all tasks that are marked as completed.
The remaining tasks are saved.
A message indicates how many tasks were cleared (e.g., 🧹 Cleared X completed tasks.).
If there are no completed tasks, it will show an ℹ️ emoji with a message.
7. Showing Statistics 📊
This provides a summary of your tasks.
It tells you how many tasks are ✅ Completed and how many are 🔄 Pending.
It also lists the number of tasks under each 🏷️ Category you've used.
8. Filtering and Sorting Tasks 🔍
This option allows you to refine your task view:
By Category: Enter a category name, and it will list all tasks belonging to that category.
By Priority: Enter a priority level (low, medium, or high), and it will display tasks with that priority.
Sort by Due Date: This will list all tasks, sorted by their due dates.



