def towerOfHanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towerOfHanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towerOfHanoi(n - 1, auxiliary, target, source)

numDisks = int(input("Enter the number of disks: "))
if numDisks <= 0:
    print("Number of disks must be greater than 0.")
else:
    print(f"\nSteps to solve Tower of Hanoi for {numDisks} disks:")
    towerOfHanoi(numDisks, 'A', 'C', 'B')
