def roundRobin(processess, arrivalTime, burstTime, priorities):
    #  Realizes round robin algorithm
    timeQuantum = int(input("Podaj kwant czasu:"))
    prioritySetting = int(input("Czy piorytet 1 jest mniejszy od 2? (1 - nie, 0 - tak):"))
    baseBurtTime = burstTime.copy()
    n = len(processess)
    time = 0
    readyProcesses = []
    privilegedProcesses = []
    if prioritySetting:
        priority = -1
    else:
        priority = 99999999
    lastDone = -1
    waitTime = []
    completionTime = [0, 0, 0, 0, 0]
    while True:
        for x in range(n):
            # Check which processes have already arrived
            if arrivalTime[x] <= time and burstTime[x] != 0:
                readyProcesses.append(x)
        for x in readyProcesses:
            # Check priorities of current processes
            if prioritySetting:
                if priorities[x] > priority:
                    priority = priorities[x]
                    privilegedProcesses.clear()
                    privilegedProcesses.append(x)
                elif priorities[x] == priority:
                    privilegedProcesses.append(x)
                else:
                    continue
            else:
                if priorities[x] < priority:
                    priority = priorities[x]
                    privilegedProcesses.clear()
                    privilegedProcesses.append(x)
                elif priorities[x] == priority:
                    privilegedProcesses.append(x)
                else:
                    continue
        for x in privilegedProcesses:
            # Provide one process with CPU time
            count = len(privilegedProcesses)
            last = privilegedProcesses[-1]
            if count == 1:
                lastDone = -1
            if x <= lastDone and x != last:
                continue
            else:
                if x == last and x <= lastDone:
                    x = privilegedProcesses[0]
                lastDone = x
                if baseBurtTime[x] == burstTime[x]:
                    waitTime.append(time)
                print(processess[x], end=' ')
                if burstTime[x] <= timeQuantum:
                    print(time, end='-')
                    time += burstTime[x]
                    burstTime[x] = 0
                    completionTime[x] = time
                    print(time)
                else:
                    print(time, end='-')
                    time += timeQuantum
                    burstTime[x] -= timeQuantum
                    print(time)
                privilegedProcesses.clear()
                readyProcesses.clear()
                if prioritySetting:
                    priority = -1
                else:
                    priority = 99999999
                break
        for x in burstTime:
            if x != 0:
                end = 0
                break
            else:
                end = 1
        if end:
            break

    sum = 0
    for x in range(n):
        sum += (waitTime[x] - arrivalTime[x])
    print("\nTo = ", sum/n)
    sum = 0
    for x in range(n):
        sum += (completionTime[x] - arrivalTime[x])
    print("Tcp = ", sum/n)




