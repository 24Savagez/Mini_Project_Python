with open("file1.txt") as file_1:
    nums_1 = file_1.readlines()

with open("file2.txt") as file_2:
    nums_2 = file_2.readlines()

result = [int(num) for num in nums_1 if num in nums_2]
# Write your code above 👆

print(result)
