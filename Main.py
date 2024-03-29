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

#import sys
import time
import DXML #adjust name
import MonthXML #adjust name
import Sensor_Data
import os

start_time = time.time()
current_time = time.time()
ten_minutes = 600

while current_time - start_time <= ten_minutes:
	current_time = time.time()
	tmp = Sensor_Data.getTemperatur()
	hum = Sensor_Data.getHumidity()
	press = Sensor_Data.getPressure()

if time.strftime("%H") == 0:
	DXML.create()
	DXML.addhour(Sensor_Data.getTemperatur(), Sensor_Data.getHumidity(), Sensor_Data.getPressure())
else:
	DXML.addhour(Sensor_Data.getTemperatur(), Sensor_Data.getHumidity(), Sensor_Data.getPressure())


if time.strftime("%H") == 23:
	MonthXML.addDay()
os.system("python3 MathPlot.py")
