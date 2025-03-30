import heapq

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority):
        heapq.heappush(self.tasks, (priority, task))

    def get_next_task(self):
        if self.tasks:
            return heapq.heappop(self.tasks)[1]
        return None

scheduler = TaskScheduler()
scheduler.add_task("Tarefa 1", 3)
scheduler.add_task("Tarefa 2", 1)
scheduler.add_task("Tarefa 3", 2)

print(scheduler.get_next_task())  
print(scheduler.get_next_task())  
print(scheduler.get_next_task())  

