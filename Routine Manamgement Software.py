#Create a Fun Routine Management Software for individulas to help them with their routine
#This Software currently takes 7 routines and 7 alarms where the alarms are meme sound effects for each consecutively
#The User input their routine and time period and each alarm rings on that time peroid until User input Enter to stop it
#The Modules used are datetime,time,schedule,pygame
import datetime
import time
import schedule
import pygame
pygame.init()
pygame.mixer.init()
name=str(input("Enter Your Name:-"))
print(f"                                Welcome To The Routine Management Software,{name.capitalize()}                                           ")
def user_time():#Function to take user time in format(Hour:Minute AM/PM)
    parse_time=datetime.datetime.strptime(user2,"%I:%M %p").time()
    return parse_time
def convert_time(user_time):#Function to convert time given by user to (24 hr clock)
    return datetime.datetime.strptime(user_time,"%I:%M %p").strftime("%H:%M")
def WakeUp():#Function of 1st alarm
    pygame.mixer.music.load("brahma-rooster-89888.mp3")
    pygame.mixer.music.play(-1)#Plays the music forever

    input("Press Enter To Stop The Alarm(1)")
    if input:
        pygame.mixer.music.stop()#Stops the music after entering Input
def Exercises():#Function of 2nd alarm
    pygame.mixer.music.load("exercise_time.wav")
    pygame.mixer.music.play(-1)

    input("Press Enter To Stop The Alarm(2)")
    if input:
        pygame.mixer.music.stop()
def Breakfast():#Function of 3rd alarm
    pygame.mixer.music.load("Breakfast.mp3")
    pygame.mixer.music.play(-1)

    input("Press Enter To Stop The Alarm(3)")
    if input:
        pygame.mixer.music.stop()
def water():#Function of 4th alarm
    pygame.mixer.music.load("it's-time-to-drink-water-made-with-Voicemod.mp3")
    pygame.mixer.music.play(-1)

    input("Press Enter To Stop  The Alarm(4)")
    if input:
        pygame.mixer.music.stop()
def lunch():#Function of 5th alarm
    pygame.mixer.music.load("time-for-lunch-64-kbps.mp3")
    pygame.mixer.music.play(-1)

    input("Press Enter To Stop The Alarm(5)")
    if input:
        pygame.mixer.music.stop()
def dinner():#Function of 6th alarm
    pygame.mixer.music.load("dinner.mp3")
    pygame.mixer.music.play(-1)

    input("Press Enter To Stop The Alarm(6)")
    if input:
        pygame.mixer.music.stop()
def sleep():#Function of 7th alarm
    pygame.mixer.music.load("its-time-to-go-to-bed_wUZtynX.mp3")
    pygame.mixer.music.play(-1)

    input("Press Enter To Stop The Alarm(7)")
    if input:
        pygame.mixer.music.stop()

print(f"                                     Our Program Supports 7 Routines,{name.capitalize()}                                                              ")
print("The Seven Routines are:-")
print("1. Wake-Up/Good-Morning.")
print("2. Do Exercises.")
print("3. Time For Breakfast.")
print("4. Drink Water.")
print("5. Time For Lunch.")
print("6. Time For Dinner.")
print("7. Sleep/Good-Night.")
print("                                    Enter The Number Given Beside Each Routine To Assign "                                )
print("                          Time Should Be Entered Between (1-12) In The Format:-(Hour:Minute AM/PM)")
count=0
while(count<7):
    try:
        user1 = int(input("Select Which Routine To Assign:-"))
        user2 = input("Enter The Time At Which The Task Should Be Done(Format:-Hour:Minute AM/PM):-")#input variable to take user time period
        t=convert_time(user2)#Convert_time function is stored in t
        user_time()
        if(user1==1):
            print(f"{name.capitalize()} has Choosen [Wake-Up] at {user2} (Routine 1 Saved Successfully)")
            schedule.every().day.at(t).do(WakeUp)#This function helps in play the music everyday at specified time given by user
            count=count + 1
        elif (user1 == 2):
            print(f"{name.capitalize()} has Choosen [Do Exercises] at {user2} (Routine 2 Saved Successfully)")
            schedule.every().day.at(t).do(Exercises)
            count = count + 1
        elif (user1 == 3):
            print(f"{name.capitalize()} has Choosen [Time For Breakfast] at {user2} (Routine 3 Saved Successfully)")
            schedule.every().day.at(t).do(Breakfast)
            count = count + 1
        elif (user1 == 4):
            print(f"{name.capitalize()} has Choosen [Drink-Water] at {user2} (Routine 4 Saved Successfully)")
            schedule.every().day.at(t).do(water)
            count = count + 1
        elif (user1 == 5):
            print(f"{name.capitalize()} has Choosen [Time For Lunch] at {user2} (Routine 5 Saved Successfully)")
            schedule.every().day.at(t).do(lunch)
            count = count + 1
        elif (user1 == 6):
            print(f"{name.capitalize()} has Choosen [Time For Dinner] at {user2} (Routine 6 Saved Successfully)")
            schedule.every().day.at(t).do(dinner)
            count = count + 1
        elif (user1 == 7):
            print(f"{name.capitalize()} has Choosen [Sleep/Good-Night] at {user2} (Routine 7 Saved Successfully)")
            schedule.every().day.at(t).do(sleep)
            count = count + 1
        elif(user1>7):
            print("Please Enter Routine From (1-7)")
    except Exception as e:
        print("Enter Time From (1-12) And In The Format (Hour:Minute AM/PM)")
print("                                     ⏰ Routine Time Running                                                      ")

while True:
    schedule.run_pending()#Checks the Users System Clock to play the music

    time.sleep(1)
