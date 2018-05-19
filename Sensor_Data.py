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
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time
import bme680
import RPi.GPIO as GPIO
import sys


sensor = bme680.BME680()  #Instance/Object of BME680

########################################
#Please check BME680 instructions first#
#Balance samples for accuracy          #
########################################
sensor.set_humidity_oversample(bme680.OS_2X) 
sensor.set_pressure_oversample(bme680.OS_4X) 
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_0)

##########################################################
#.get_sensor_data() --> boolean (i2c kernel module running?)#
#.data.temperature/humidity/pressure --> retrieve data   #
##########################################################
def getTemperatur():
	if sensor.get_sensor_data():
		return temperature = sensor.data.temperature
	else:
		sys.stderr.write("Error! Couldn't retrieve temperature data from BME680 Sensor")
		#return 0

def getPressure():
	if sensor.get_sensor_data():
		return pressure = sensor.data.pressure
	else:
		sys.stderr.write("Error! Couldn't retrieve pressure data from BME680 Sensor")
		#return 0

def getHumidity():
	if sensor.get_sensor_data():
		return humidity = sensor.data.humidity
	else:
		sys.stderr.write("Error! Couldn't retrieve humidity data from BME680 Sensor")
		#return 0

def getOversamples():
	s =" "
	return (s = "{0:} Temp, {1:} Hum, {2:} Press".format(sensor.get_temperature_oversmaple(), sensor.get_humidity_oversample(), sensor.get_pressure_oversample())
	
