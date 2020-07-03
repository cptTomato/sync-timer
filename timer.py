import time

class Time():
    def countdown(myinput):
        while myinput > 0:
            print(myinput)
            myinput = myinput-1
            time.sleep(60)

myinput = int(input("How many minutes you need to wait for the sync? /n "))
zeit = Time
zeit.countdown(myinput)
print("Timer is done")
