from RandomNumberGenerator import RandomNumberGenerator

def schedule_tasks(tasks):
    # sort tasks by deadline in increasing order
    tasks = sorted(tasks, key=lambda x: x[3])
    n = len(tasks)
    d = tasks[-1][3]
    # initialize a 2D list with zeros
    w = [[0]*(d+1) for _ in range(n+1)]
    # fill the first row with zeros
    for j in range(d+1):
      w[0][j] = 0
    # fill the rest of the table
    for i in range(1, n+1):
      for j in range(d+1):
        if j >= tasks[i-1][2]:
          w[i][j] = max(w[i-1][j], w[i-1][j-tasks[i-1][2]] + tasks[i-1][1])
        else:
          w[i][j] = w[i-1][j]
    # find the optimal value
    O = w[n][d]
    # construct the schedule
    H = []
    j = d
    for i in range(n, 0, -1):
      if w[i][j] != w[i-1][j]:
        H.append(tasks[i-1][0])
        j -= tasks[i-1][2]
    # reverse the schedule and return it with the optimal value
    H.reverse()
    return O, H


tasks = [(1, 3, 3, 3), (2, 4, 2, 10), (3, 2, 1, 6), (4, 2, 2, 15), (5, 3, 4, 21), (6, 4, 2, 16)]

result = schedule_tasks(tasks)
print("Maksymalny zysk:", result[0])
print("Harmonogram wykonywania zadań:", result[1])
