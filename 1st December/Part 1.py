
with open("input.txt") as inFile:
    lines = inFile.readlines()

numbers = [str(i) for i in range(0, 10)]
values = []

for line in lines:
    nums = "".join([c for c in line if c in numbers])
    values.append(int(nums[0] + nums[-1]))

print(sum(values))