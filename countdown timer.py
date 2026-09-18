import time

set_timer= int(input("Enter the time in seconds: "))

for x in range(1, set_timer +1):
    print(x)
    time.sleep(1)
print("Time's up!")
