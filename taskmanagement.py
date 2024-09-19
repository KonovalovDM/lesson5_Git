# Создаем класс 'Task'

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

        def mark_complete(self):
            self.completed = True

        def __str__(self):
            status = "Выполнено" if self.copleted else "Не выполнено"
            return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_copleted(self, task, index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
        else:
            print("некорректный индекс задачи. Такой задачи нет")

    def get_pending_tasks(self):
        pending_tasks = self.get_pending_tasks()
        if not pending_tasks:
            print("Все задачи выполнены!")
        else:
            for task in pending_tasks:
                print(task)

# Создаем экземпляр класса 'TaskManager'
task_manager = TaskManager()

# Добавляем задачи с помощью метода 'add_task'
task_manager.add_task("Сделать домашку", "2024-10-15")
task_manager.add_task("Помыть посуду", "2024-10-15")
task_manager.add_task("Купить продукты", "2024-10-16")

# Выводим текущий список задач
print("Список невыполненных задач:")
task_manager.show_pending_tasks()

# Отмечаем задачу как выполненную с указанным индексом
task_manager.mark_task_copleted(0)

# Выводим текущий список - список невыполненных задач
print("\nПосле выполнения задачи:")
task_manager.show_pending_tasks()
