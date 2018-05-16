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

import re
import time
import bme680
import RPi.GPIO as GPIO

sensor = bme680.BME680()  #Instance/Object of BME680

sensor.set_humidity_oversample(bme680.OS_2X) #Please check BME680 instructions first                           
sensor.set_pressure_oversample(bme680.OS_4X) #Balance samples for accuracy
sensor.set_temperature_oversample(bme680.OS_8X)

def gettemperatur():
	if sensor.get_sensor_data():
		return temperature = sensor.data.temperature
	else:
		print ("Error! Couldn't retrieve temperature data from BME680 Sensor")
		return 0	
		
def getpressure():
	if sensor.get_sensor_data():
		return pressure = sensor.data.pressure
	else:
		print ("Error! Couldn't retrieve pressure data from BME680 Sensor")
		return 0			
		
def gethumidity():
	if sensor.get_sensor_data():
		return humidity = sensor.data.humidity
	else:
		print ("Error! Couldn't retrieve humidity data from BME680 Sensor")
		return 0			
