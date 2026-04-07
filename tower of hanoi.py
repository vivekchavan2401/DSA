def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)


num_of_disks = int(input("Enter number of disks: "))

if num_of_disks <= 0:
    print("Please enter a number greater than 0")
else:
    print("Steps to solve Tower of Hanoi:")
    tower_of_hanoi(num_of_disks, "A", "B", "C")
