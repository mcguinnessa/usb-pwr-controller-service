# usb-pwr-controller-service
An RPi flask REST API for the USB Power Switch 

#Install
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt 

#Create Service
create link to service file in /etc/systemd/system/usb-switch.service

sudo systemctl daemon-reload
sudo systemctl start usb-switch
sudo systemctl enable usb-switch
sudo systemctl status usb-switch

Currently listens on port 5003, can be changed in the service file

Supported Endpoints
/usb-switch/<state>
{"state":state}

