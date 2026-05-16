import time

print("POMODORO TIMER")

work = int(input("Enter work time in minutes: "))
break_time = int(input("Enter break time in minutes: "))
rounds = int(input("Enter number of rounds: "))

for i in range(rounds):

    print(f"\nRound {i+1} Study Time Started!")

    seconds = work * 60

    while seconds > 0:

        mins = seconds // 60
        secs = seconds % 60

        print(f"Study Time Left: {mins:02d}:{secs:02d}", end="\r")

        time.sleep(1)

        seconds -= 1

    print("\nStudy Time Over!")

    if i != rounds - 1:

        print("\nBreak Time Started!")

        seconds = break_time * 60

        while seconds > 0:

            mins = seconds // 60
            secs = seconds % 60

            print(f"Break Time Left: {mins:02d}:{secs:02d}", end="\r")

            time.sleep(1)

            seconds -= 1

        print("\nBreak Time Over!")

print("\nAll Sessions Completed!")
