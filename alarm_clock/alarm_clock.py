from playsound import playsound
import time

CLEAR="\033[23]"
CLEAR_ALL="\033[H"


def alarm(seconds):
    time_elapsed=0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{CLEAR_ALL}Time left: {minutes_left:02d} minutes and {seconds_left:02d} seconds", end='\r')

    playsound("love_alarm.mp3")


minutes = int(input("Enter the number of minutes for the alarm: "))
seconds=int(input("Enter the number of seconds for the alarm: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)

# alarm(10)