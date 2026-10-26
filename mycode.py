import sys
from collections import Counter

logs = sys.argv[1]
index = int(sys.argv[2])

with open(logs) as f:
  lines = f.readlines()

print("Total lines:", len(lines))
dict = Counter()
for i in lines:
  fields = i.split()

  if len(fields) > index:
    key = fields[index]
    dict[key] += 1
    print(dict)

print("Top 1:")
for i , n in dict.most_common(3):
  print(i, n)