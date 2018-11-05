import time

i = 0
while True:
    print("Hello")
    time.sleep(i)
    if i == 3:
        print("End of Loop")
        break
    i += 1
