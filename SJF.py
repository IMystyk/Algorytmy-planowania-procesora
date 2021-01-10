def sjf(processess, arrivalTime, burstTime, priorities):
    # Realizes sjf algorithm
    n = len(processess)
    time = 0
    prioritySetting = int(input("Czy piorytet 1 jest mniejszy od 2? (1 - tak, 0 - nie):"))
    readyProcesses = []
    privilegedProcesses = []
    waitTime = []
    if prioritySetting:
        priority = -1
    else:
        priority = 99999999
    waitTime = []
    for x in range(n):
        waitTime.append(0)
    completionTime = []
    for x in range(n):
        completionTime.append(0)

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
        nextProcess = privilegedProcesses[0]
        for x in privilegedProcesses:
            # Check which process arrived first
            if burstTime[nextProcess] > burstTime[x]:
                nextProcess = x
        waitTime[nextProcess] = time
        print(processess[nextProcess], end=' ')
        print(time, end='-')
        time += burstTime[nextProcess]
        completionTime[nextProcess] = time
        print(time)
        burstTime[nextProcess] = 0
        if prioritySetting:
            priority = -1
        else:
            priority = 99999999
        readyProcesses.clear()
        privilegedProcesses.clear()

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
    print("\nTo = ", sum / n)
    sum = 0
    for x in range(n):
        sum += (completionTime[x] - arrivalTime[x])
    print("Tcp = ", sum / n)
