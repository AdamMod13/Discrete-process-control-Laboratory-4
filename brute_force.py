import itertools
from RandomNumberGenerator import RandomNumberGenerator

def brute_force(tasks):
    schedules = list(itertools.permutations(tasks))
    best_schedule = None
    min_delay = float('inf')
    
    for schedule in schedules:
        current_time = 0
        current_delay = 0
        for task in schedule:
            current_time += task[1] 
            current_delay += max(0, current_time - task[3]) * task[2]
        if current_delay < min_delay:
            min_delay = current_delay
            best_schedule = schedule
            

    return best_schedule

rng = RandomNumberGenerator(1)

n = 4
tasks = [[i, rng.nextInt(1, 29), rng.nextInt(1, 9), rng.nextInt(1, 29)] for i in range(n)]

# tasks = [(1, 3, 3, 3), (2, 4, 2, 10), (3, 2, 1, 6), (4, 2, 2, 15), (5, 3, 4, 21), (6, 4, 2, 16)]
schedule = brute_force(tasks)
print(schedule)