#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  OpenTemp.py
#
#  Copyright 2018 Luis Kress <luis.kress@stud.th-bingen.de> Jo Hausmann <johannes.hausmann@stud.th-bingen.de>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from flask import Flask, render_template
import Sensor_Data
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    temp = Sensor_Data.getTemperatur()
    hum = Sensor_Data.getHumidity()
    press = Sensor_Data.getPressure()
    return render_template("homePictures.html", temperature=temp, humidity=hum, pressure=press)

@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template("About.html")

@app.route('/config', methods=["GET", "POST"])
def config():
    return render_template("Configuration.html")

@app.route('/temperature', methods=["GET", "POST"])
def temp():
    return render_template("graphs/Temp.html")

@app.route('/humidity', methods=["GET", "POST"])
def hum():
    return render_template("graphs/Hum.html")

@app.route('/pressure', methods=["GET", "POST"])
def press():
    return render_template("graphs/Press.html")

if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port=5005)
