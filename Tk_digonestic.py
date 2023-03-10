import tkinter as tk
from std_msgs.msg import String
import subprocess
import threading
import subprocess as sub
import signal
from sys import exit
import time
import rospy
import ros
import pc7
from subprocess import Popen, PIPE
from pc7 import*
from tkinter import* 
from pc7.srv import*
import sys
#from __future__ import print_function
#from pc7.srv import *


parent = tk.Tk()
var = tk.StringVar()
var2 = tk.StringVar()
parent.geometry("800x500")

global n
velocity = tk.Label(parent, text = "Velocity Motor", font=('Times', 24)).place(x = 20, y = 50)
position = tk.Label(parent, text = "Position Motor", font=('Times', 24)).place(x = 20, y = 90)
rotation =  tk.Label(parent, text = "Rotation Motor", font=('Times', 24)).place(x = 20, y = 130)
#rotation =  tk.Label(parent, textvariable=var, font=('Times', 24)).place(x = 500, y = 45)
#rotation =  tk.Label(parent, textvariable=var2, font=('Times', 24)).place(x = 500, y = 120)
############################################################################################################################################################################################################
#------------------------------------------------------------------START VELOCITY MOTOR--------------------------------------------------------------------------------------------------------------
###########################################################################################################################################################################################################

def call_rstart():
   pop = subprocess.Popen(['rosrun', 'pc7', 'rotation_server']).communicate(pop)

#############################################################################################################################################################################################################
#-------------------------------------------------------------------START VELOCITY MOTOR-----------------------------------------------------------------						
#############################################################################################################################################################################################################
def call_vstart():
   pub = rospy.Publisher('vstart', String, queue_size=10)
   rospy.init_node('velocity', anonymous=True)
   pop = 1 #subprocess.Popen(['rosrun', 'pc7', 'velocity_server']).communicate(pop)
   rospy.loginfo(pop)
   pub.publish(pop)
   
#############################################################################################################################################################################################################
#--------------------------------------------------------------------STOP VELOCITY MOTOR---------------------------------------------------------------------------------------------------------
#############################################################################################################################################################################################################
def call_vstop():
   pop.kill(pop)
   print("finish_velocity")  
#############################################################################################################################################################################################################
#---------------------------------------------------------------------START POSITION MOTOR-------------------------------------------------------------------------------------------------------------
#############################################################################################################################################################################################################
def call_pstart():
   pop = subprocess.Popen(['rosrun', 'pc7', 'position_server']).communicate(pop)
    
############################################################################################################################################################################################################
#--------------------------------------------------------------------STOP POSITION MOTOR------------------------------------------------------------------------------------------------------------
############################################################################################################################################################################################################ 
def call_pstop():
  
#############################################################################################################################################################################################################
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###########################################################################################################################################################################################################




#############################################################################################################################################################################################################
#-------------------------------------------------------------------ROS VELOCITY CLIENT---------------------------------------------------------------------------------------------------------------
#############################################################################################################################################################################################################
 def velocity_controller(x):
    rospy.wait_for_service('applyVelocity')
    try:
        velocity_control = rospy.ServiceProxy('applyVelocity', Velocity)
        resp1 = velocity_control(x)
        return resp1.velocity_old
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

############################################################################################################################################################################################################
#-------------------------------------------------------------PUBLISH VELOCITY VALUE TO A BUTTON-----------------------------------------------------------------------------------------------------------
############################################################################################################################################################################################################

def velocity_controller(x):
    rospy.wait_for_service('applyVelocity')
    try:
        velocity_control = rospy.ServiceProxy('applyVelocity', Velocity)
        resp1 = velocity_control(x)
        return resp1.velocity_old
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def call_vok(*args):
  
   username = 500
   velocity_controller(int(username))
   #entry1.delete(0, "end")

#############################################################################################################################################################################################################
#--------------------------------------------------------------------------ROS POSITION CLIENT---------------------------------------------------------------------------------------------------------
#############################################################################################################################################################################################################
def position_controller(x):
    rospy.wait_for_service('applyPosition')
    try:
        position_control = rospy.ServiceProxy('applyPosition', Position)
        resp1 = position_control(x)
        return resp1.position_old
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

#############################################################################################################################################################################################################
#-------------------------------------------------------------PUBLISH POSITION VALUE TO A BUTTON----------------------------------------------------------------------------------------------------------
#############################################################################################################################################################################################################
def call_pok(*args):
    
    username2 = 50000
    position_controller(int(username2))
    #entry2.delete(0, "end")
   
#############################################################################################################################################################################################################
#------------------------------------------------------------------------PUBLISH ROTATION VALUE TO A BUTTON----------------------------------------------------------------------------------------
#############################################################################################################################################################################################################
def call_rotok(*args):
   username3 = 500
   velocity_controller(int(username3))
   #entry3.delete(0, "end")
############################################################################################################################################################################################################
#-------------------------------------------------------------------------------FOR ENTRY-BOX---------------------------------------------------------------------------------------------------------------
############################################################################################################################################################################################################  
#entry1 = tk.Entry(parent)
#entry1.bind("<Return>", call_vok)
#entry1.place(x = 185, y = 60)
#entry2 = tk.Entry(parent)
#entry2.bind("<Return>", call_pok)
#entry2.place(x = 185, y = 100)
#entry3 = tk.Entry(parent)
#entry3.bind("<Return>", call_rotok)
#entry3.place(x = 190, y = 140)
############################################################################################################################################################################################################
#------------------------------------------------------------------------------INSTRUCTION GIVEN-&-BUTTON CREATION-------------------------------------------------------------------------------------------
############################################################################################################################################################################################################
#var.set("Hey! How are you doing?" '\n'  "PUT THE VALUE AS PER BELOW INSTRUCTION" '\n')
#var2.set('\n' "V_Frwd = (+)Value & V_Bkwd = (-)Value" '\n' "P_Frwd = (+)Value & P_Bkwrd = (-)Value" '\n' '\n' "Position_Movement                 Velocity_Movement" '\n' "20Degree = 11110                   Velocity Run" '\n' "45Degree = 25000                    Min To Max" '\n' "90Degree = 50000                  (+)/(-)200 To 300" '\n' "180Degree = 90000                     .....For" '\n' "360Degree = 180000                   Velocity Only" '\n') 
   
sbmitbtn1 = tk.Button(parent, text = "Check v", activebackground = "green", activeforeground = "blue", command = call_vok, state= "normal")
sbmitbtn1.place(x = 370, y = 60)

sbmitbtn2 = tk.Button(parent, text = "Check p", activebackground = "green", activeforeground = "blue", command = call_pok, state= "normal")
sbmitbtn2.place(x = 370, y = 100)

sbmitbtn3 = tk.Button(parent, text = "Check r", activebackground = "green", activeforeground = "blue", command = call_rotok, state= "normal")
sbmitbtn3.place(x = 370, y = 140)

sbmitbtn4 = tk.Button(parent, text = "Close", activebackground = "green", activeforeground = "blue", command=parent.destroy, state= "normal")
sbmitbtn4.place(x = 1500, y = 550)

sbmitbtn5 = tk.Button(parent, text = "On P", activebackground = "green", activeforeground = "blue", command = call_pstart, state= "normal")
sbmitbtn5.place(x = 200, y = 180)

sbmitbtn6 = tk.Button(parent, text = "On V", activebackground = "green", activeforeground = "blue", command = call_vstart, state= "normal")
sbmitbtn6.place(x = 80, y = 180)

sbmitbtn6 = tk.Button(parent, text = "On R", activebackground = "green", activeforeground = "blue", command = call_rstart, state= "normal")
sbmitbtn6.place(x = 320, y = 180)

#sbmitbtn7 = tk.Button(parent, text = "Stop Velocity", activebackground = "green", activeforeground = "blue", command = call_vstop, state= "normal")
#sbmitbtn7.place(x = 80, y = 220)

#sbmitbtn8 = tk.Button(parent, text = "Stop Position", activebackground = "green", activeforeground = "blue", command = call_pstop, state= "normal")
#sbmitbtn8.place(x = 200, y = 220)

#sbmitbtn8 = tk.Button(parent, text = "Stop Rotation", activebackground = "green", activeforeground = "blue", command = call_rstop, state= "normal")
#sbmitbtn8.place(x = 320, y = 220)

######################################################################################################################################################################################################### #-------------------------------------------------------------------------------MAIN FUNCTION--------------------------------------------------------------------------------------------------------------
#############################################################################################################################################################################################################
if __name__ == "__main__":

        	
 		parent.mainloop()
	
