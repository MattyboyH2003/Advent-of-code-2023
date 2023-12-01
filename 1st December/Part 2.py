d = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9", "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}

with open("input.txt") as f:
    ls = f.readlines()

vs = []

for l in ls:
    n = ""
    for i in range(len(l)):
        for k in d.keys():
            if len(l) - i >= len(k) and l[i:i+len(k)] == k:
                n += d[k]

    vs.append(int(n[0] + n[-1]))

print(sum(vs))
