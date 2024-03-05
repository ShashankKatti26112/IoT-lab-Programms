import time

for i in range(10):
    current_time = time.strftime("%H:%M:%S")
    print(f"Current time: {current_time}")
    time.sleep(10)
