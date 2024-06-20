def TowerOfHanoi(N, S, E, D):
    if N == 1:
        print("Move", N, "From", S, "To", D)
        return 
    TowerOfHanoi(N-1, S, D, E)
    print("Move", N, "From", S, "To", D)
    TowerOfHanoi(N-1, E, S, D)
N = int(input("Enter the number of disks: "))
TowerOfHanoi(N, "Source", "Extra", "Destination")
print("All disks have been successfully moved to the Destination!")
