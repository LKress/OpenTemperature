#FlaskOpenTemp
##How Flask for Opentemp works
The Flask Webserver is running as long as the Raspberry Pi is running. It gets started after the installscript is finished or when the Raspberry Pi gets rebooted.

Via the methods @app.route Flask leads between the different pages.
As example the method for the homepage:
```
@app.route('/', methods=["GET", "POST"])
def index():
    temp = Sensor_Data.getTemperatur()
    hum = Sensor_Data.getHumidity()
    press = Sensor_Data.getPressure()
    return render_template("homePictures.html", temperature=temp, humidity=hum, pressure=press)
```
The last line of code sets the port, where the user can reach the OpenTemperature homepage to 5005. The address for the website is the local IP of the Raspberry Pi.
###Enter this to reach the webpage:
```
http://local_IP_RaspberryPi:5005/
```
