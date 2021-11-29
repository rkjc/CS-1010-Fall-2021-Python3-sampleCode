import time


for a in range(10):
    for x in range(50):
        print()
    print("hey there " + str(a) + " " + ('*' * a))
    for x in range(5):
        print()
    time.sleep(0.5)


print("did the screen clear?")