from flask import Flask, jsonify

app = Flask(__name__)

from usb_switch import USBSwitch

ON = "on"
OFF = "off"


USB_SWITCH=14
usb_switch = USBSwitch(USB_SWITCH, False)

######################################################################
#
# Get temperature in Celcius
#
######################################################################
@app.route("/usb-switch/<state>")
def set_switch(state):
   state = state.lower()
   print("Input:" + str(state))

   if state in [ON, 1]:
      state_b = True
   elif state in [OFF, 0]:
      state_b = False
   else:
      abort(403)

   if(usb_switch.set_switch_state(state_b)):
      return jsonify({"state": state})
   else:
      abort(500)
   
######################################################################
#
# Get temperature in Farenheit
#
######################################################################
#@app.route("/DS18B20/f")
#def farenheit():
#   return get_temperature(F_INDEX)
#    celcius,farenheit = ds18b20_helper.read_temp()
#    rc = {"value": farenheit}
#    print("C:" + str(rc))
#    return jsonify(rc)
    
