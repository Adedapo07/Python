largestN = int(input("Enter the largest number:"))
smallestN= int(input("Enter the smallest number:"))

while(smallestN):
    nstore=smallestN
    smallestN= largestN % smallestN
    largestN=nstore
print("HCF/GSF is:", largestN)