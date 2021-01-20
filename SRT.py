def srt(processess, arrivalTime, burstTime, priorities):
    # Realizes srt algorithm, it's a bit rough, but it works
    n = len(processess)
    times = arrivalTime.copy()
    times.append(9999999)
    times.sort()
    timeCounter = 0
    baseBurstTime = burstTime.copy()
    time = 0
    prioritySetting = int(input("Czy piorytet 1 jest mniejszy od 2? (1 - tak, 0 - nie):"))
    readyProcesses = []
    privilegedProcesses = []
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
            if arrivalTime[x] <= time:
                timeCounter += 1
            if arrivalTime[x] <= time and burstTime[x] != 0:
                readyProcesses.append(x)
        # for x in readyProcesses:
        #     # Check priorities of current processes
        #     if prioritySetting:
        #         if priorities[x] > priority:
        #             priority = priorities[x]
        #             privilegedProcesses.clear()
        #             privilegedProcesses.append(x)
        #         elif priorities[x] == priority:
        #             privilegedProcesses.append(x)
        #         else:
        #             continue
        #     else:
        #         if priorities[x] < priority:
        #             priority = priorities[x]
        #             privilegedProcesses.clear()
        #             privilegedProcesses.append(x)
        #         elif priorities[x] == priority:
        #             privilegedProcesses.append(x)
        #         else:
        #             continue
        nextProcess = readyProcesses[0]
        for x in readyProcesses:
            # Check which process has shortest remaining burst time
            if burstTime[nextProcess] > burstTime[x]:
                nextProcess = x
            elif burstTime[nextProcess] == burstTime[x]:
                if prioritySetting:
                    if priorities[nextProcess] < priorities[x]:
                        nextProcess = x
                else:
                    if priorities[nextProcess] > priorities[x]:
                        nextProcess = x

        if baseBurstTime[nextProcess] == burstTime[nextProcess]:
            waitTime[nextProcess] = time
        print(processess[nextProcess], end=' ')
        print(time, end='-')
        if burstTime[nextProcess] <= (times[timeCounter] - time):
            time += burstTime[nextProcess]
            burstTime[nextProcess] = 0
            completionTime[nextProcess] = time
            print(time)
        else:
            burstTime[nextProcess] -= (times[timeCounter] - time)
            time += (times[timeCounter] - time)
            print(time)
        if prioritySetting:
            priority = -1
        else:
            priority = 99999999
        readyProcesses.clear()
        privilegedProcesses.clear()
        timeCounter = 0

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
