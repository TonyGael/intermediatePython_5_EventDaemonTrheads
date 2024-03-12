import threading

event = threading.Event()


def my_function():
    print("Waiting for event to trigger...\n")
    event.wait()
    print("Performing action because event...")


t1 = threading.Thread(target=my_function)
t1.start()

x = input("Do you want to trigger the event? (y/n): \n")

if x == 'y':
    event.set()
