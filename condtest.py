import time

x, y, z = time.strftime("%H:%M:%S").split(":")
x, y, z = int(x), int(y), int(z)

if x >= 18 or x < 6 :
    # Either method works:
    print("Good Night")                 # With commas
    # or:
    # print("Good Night")

print("Hour:", x)
print("Min:", y)
print("Sec:", z)