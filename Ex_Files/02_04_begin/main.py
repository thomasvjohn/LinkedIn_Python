NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

print("While Loop")
i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

print("For Loop")
for name in NAMES:
    print(name)

print("For Loop with Zip")
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

print("For Loop with Reversed")
for name in reversed(NAMES):
    print(name)

print("For Loop with Index")
for i in range(5):
    print(i)

# enumerate
print("For Loop with Enumerate")
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
