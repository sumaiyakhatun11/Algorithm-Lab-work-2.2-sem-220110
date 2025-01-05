def KnapsackGreedy(obj,knapsackCapacity,weights,profit):
    items=[]

    for i in range(obj):
        ratio=profit[i]/weights[i]
        items.append((ratio,profit[i],weights[i]))

    items.sort(reverse=True)

    totalProfit=0
    totalWeight=0

    for ratio,profit,weight in items:
        if totalWeight+weight<=knapsackCapacity:
            totalProfit+=profit
            totalWeight+=weight

        else:
            remainingCapacity=knapsackCapacity-totalWeight
            totalProfit+=profit*(remainingCapacity/weight)
            totalWeight+=remainingCapacity
            break

    return totalProfit


knapsackCapacity=int(input('Enter Knapsack Capacity: '))
obj=int(input('Enter number of objects: '))
weights=list(map(int,input('Enter Weight: ').split()))
profit=list(map(int,input('Enter profit: ').split()))

maxProfit= KnapsackGreedy(obj,knapsackCapacity,weights,profit)
print(f'The Maximum profit that can be obtained is {maxProfit}')
