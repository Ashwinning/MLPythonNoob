#Numerical stability
# https://classroom.udacity.com/courses/ud730/lessons/6370362152/concepts/71235296110923

a = 1000000000;

for x in range(0, 1000000):
    a += 0.000001

print(a-1000000000)
