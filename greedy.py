from RandomNumberGenerator import RandomNumberGenerator

def greedy(tasks):

    tasks_sorted = sorted(tasks, key=lambda x: (-x[3], -x[2], x[2]/x[1]), reverse=True)
    schedule = []
    print(tasks_sorted)

    current_time = 0
    for task in tasks_sorted:
      if current_time + task[1] <= task[3]:
        schedule.append(task)
        current_time += task[1]
            
    # Zwróć harmonogram
    return schedule

rng = RandomNumberGenerator(1)

n = 6
tasks = [[i, rng.nextInt(1, 29), rng.nextInt(1, 9), rng.nextInt(1, 29)] for i in range(n)]

# tasks = [(1, 3, 3, 3), (2, 4, 2, 10), (3, 2, 1, 6), (4, 2, 2, 15), (5, 3, 4, 21), (6, 4, 2, 16)]
schedule = greedy(tasks)
print(schedule)