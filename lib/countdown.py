# your code goes here!

def countdown(seconds):
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        seconds -= 1
    print("HAPPY NEW YEAR!")


def countdown_with_sleep(seconds):
    import time
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        time.sleep(1)
        seconds -= 1
    print("HAPPY NEW YEAR!")