command = ""
started = False
stopped = False
while True:
    command = input(">  ").lower()
    if command == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started...")
    elif command == "stop":
        if stopped:
            print("Car is already stopped!")
        else:
            stopped = True
            print("Car stopped....")
    elif command  == "help":
        print(""" 
Press start to start the car
press stop to stop the car
press quit to exit the game

        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")


