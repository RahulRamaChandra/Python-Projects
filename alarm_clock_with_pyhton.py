"""An alarm clock is a clock with a function that can be activated to ring at a time set in advance, used to wake someone up.
For this task, I will be using the DateTime module in Python to create an alarm clock and the sound library in Python to play the alarm sound.
The DateTime module comes preinstalled in the Python programming language so you can easily import it in your program.
The playsound library can be easily installed by using a pip command; pip install playsound."""


from datetime  import datetime
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
"""now = datetime.now()
current_period = now.strftime("%p")
print(current_period)
current_hour =now.strftime("%I")
current_minute = now.strftime("%M")
current_seconds = now.strftime("%S")
print(current_hour)
print(current_minute)
print(current_seconds)"""
while True:
    now = datetime.now()
    print(now)
    current_hour =now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period == current_period :
        if alarm_hour == current_hour :
            if alarm_minute == current_minute :
                if alarm_seconds == current_seconds :
                    print("Wake Up!")
                    playsound("audio.mp3")
                    break
