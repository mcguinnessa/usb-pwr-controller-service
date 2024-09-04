
import os
import glob
import time

#from classes.GPIO_PINS import *
import RPi.GPIO as GPIO

class USBSwitch:

   class DeviceException(Exception):
      pass

   def __init__(self, control_pin, state=False):
      self.GPIO_ID = control_pin

      self.set_switch_state(state)

   ###############################################################
   # 
   #  
   # 
   ###############################################################
   def set_switch_state(self, state):

      rc = False
      try:
         #BCM means GPIO number, BOARD means physical port number
         GPIO.setmode(GPIO.BCM)   # The physical number on the board
         #GPIO.setmode(GPIO.BOARD)  # The GPIO number
         GPIO.setup(self.GPIO_ID, GPIO.OUT)

         if state:
            GPIO.output(self.GPIO_ID, GPIO.HIGH)
         else:
            GPIO.output(self.GPIO_ID, GPIO.LOW) 

         self.state = state
         rc = True

      except Exception as e:
         import traceback
         traceback.print_exc()
         print("Exception Thrown:" + str(e))
      #   raise USBSwitch.DeviceException

      print("GPIO set:" + str(rc))
      return rc
 
