#!/usr/bin/python3

import sys

from usb_switch import USBSwitch
#from classes.GPIO_PINS import *

USB_POWER_SWITCH_GPIO        = 14

def usage():
   print(str(sys.argv[0]) + " on|off|1|0")


#########################################################################################
#
# Main
#
#########################################################################################
def main(argv):

   state = False
   if len(sys.argv) < 2:
      return usage()

   state_str = sys.argv[1]

   if str(state_str) in ["on", "ON", "On", "1", "True"]:
      state = True
   elif str(state_str) in ["off", "OFF", "Off", "0", "False"]:
      state = False
   else:
      return usage()

   print("Desired State:" + str(state))

#   usb_ctl = USBPowerSwitch(state)
   switch = USBSwitch(USB_POWER_SWITCH_GPIO, state)

if __name__ == "__main__":
   main(sys.argv[1:])
