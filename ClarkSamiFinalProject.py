#Author: Sami Clark
#Date written: 2/25/2024
#Assignment: Final Project
#Short Desc: This program is a GUI alarm clock

"""We begin by importing all libraries necessary"""
from tkinter import *
import datetime
import time
import winsound
import cv2
from matplotlib import pyplot as plt
#Essentially we just imported all the information we will need to complete this program

"""This is where we define the alarm and how it gets the time"""
def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg="Current Time: "+str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
            break

def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)
#We just defined what is actually going to make the alarm work

"""This is where the window is created"""
window = Tk()
window.title("Alarm Clock")
window.geometry("400x200")
window.config(bg="#922B21")
window.resizable(width=False,height=False)
#This is how the main alarm will appear

"""This is where the labels are created"""
time_format=Label(window, text= "Remember to set time in 24 hour format!", fg="white",bg="#922B21",font=("Arial",15)).place(x=20,y=120)
addTime = Label(window,text = "Hour     Min     Sec",font=60,fg="white",bg="black").place(x = 210)
setYourAlarm = Label(window,text = "Set Time for Alarm: ",fg="white",bg="#922B21",relief = "solid",font=("Helevetica",15,"bold")).place(x=10, y=40)
#We just created all the labels for the alarm clock appearance

"""This is where the variables are defined"""
hour = StringVar()
min = StringVar()
sec = StringVar()
#Here, we are just declaring the time functions as variables

"""This is where the actual entry windows are created"""
hourTime= Entry(window,textvariable = hour,bg = "#48C9B0",width = 4,font=(20)).place(x=210,y=40)
minTime= Entry(window,textvariable = min,bg = "#48C9B0",width = 4,font=(20)).place(x=270,y=40)
secTime = Entry(window,textvariable = sec,bg = "#48C9B0",width = 4,font=(20)).place(x=330,y=40)
#We just created the windows where the user will actually enter the time

"""This is where we define the input of the hour put in"""
if hourTime == ""
    print("Please input hour in 24 format.")
#This is where the user's input is validated

"""This is where we define the input of the minute put in"""
if minTime == ""
    print("Please input minute in 24 format.")
#This is where the user's input is validated

"""This is where we define the input of the seconds put in"""
if secTime == ""
    print("Please input seconds in 24 format.")
#This is where the user's input is validated

"""This is where the submit button is defined"""
submit = Button(window,text = "Set Your Alarm",fg="Black",bg="#D4AC0D",width = 15,command = get_alarm_time,font=(20)).place(x =100,y=80)
#This is the button where you can set the actual alarm

"""This is where the exit button is defined"""
def close():
    window.destroy()
    window.quit()
#This is where the window is told to destory and close

"""This is where the thank you button window is defined"""
def openNewWindow():
    newWindow = Toplevel(window)
    newWindow.title("Thank You")
    newWindow.geometry("400x200")
    Label(newWindow, text = "Thank you for using this program!").pack()
    label = Label(window,text ="This is the main window")
    label.pack(pady = 10)
#We essentially just created the window that will appear when clicking on the thank you button

"""This is where the thank you button is defined"""
submit = Button(window,text = "Thank You",fg="Black",bg="#D4AC0D",width = 15,command = openNewWindow).place(x=270,y=80)
#This is where the button to lead to the thank you window is created

"""This is where the exit button is defined"""
submit = Button(window,text = "Exit",fg="Black",bg="#D4AC0D",width = 5,command = window.destroy).place(x=40, y=80)
submit.pack(pady=20)
#This is the button where you can exit the program

"""This is where the main function is defined"""
window.mainloop()
#This is how the entire program comes together to work
