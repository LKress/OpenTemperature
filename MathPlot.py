#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  MathPlotXML.py
#
#  Copyright 2018 Jo Hausmann <dracula@localhost.localdomain>
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
import matplotlib
matplotlib.use('agg')
from lxml import etree
from matplotlib import pyplot as plot
from matplotlib import style
#import numpy as np
import sys
import calendar
import datetime
import os

###########################################################
#openXML --> open daily XML Sheet && save numbers in lists#
#try & except --> XML Syntax or file not accessible       #
###########################################################

def XMLD(et):
	root = et.getroot()
	for child in root:
			position = int(child.get("hour"))
			ListTemp[position]=(float(child.get("temp")))
			ListHum[position]=(float(child.get("hum")))
			ListPres[position]=(float(child.get("pres")))
def XMLM(et):
	root = et.getroot()
	for child in root:
			position = int(child.get("day"))
			ListTempM[position-1]=(float(child.get("temp")))
			ListHumM[position-1]=(float(child.get("hum")))
			ListPresM[position-1]=(float(child.get("pres")))

def openXML(dayormonth):
	try:
		if (dayormonth == 0):
			et = etree.parse("XMLD.xml")
			XMLD(et)
			return([min(x for x in ListTemp if x is not None),max(x for x in ListTemp if x is not None),
				min(x for x in ListTemp if x is not None),max(x for x in ListHum if x is not None),
				min(x for x in ListPres if x is not 0),max(x for x in ListPres if x is not 0)])

		else:
			et= etree.parse("XMLM.xml")
			XMLM(et)
			return([min(x for x in ListTempM if x is not None),max(x for x in ListTempM if x is not None),
				min(x for x in ListTempM if x is not None),max(x for x in ListHumM if x is not None),
				min(x for x in ListPresM if x is not 0),max(x for x in ListPresM if x is not 0)])


	except etree.XMLSyntaxError:
		sys.stderr.write("Error: File is empty\n")
		sys.exit(1)
	except OSError:
		sys.stderr.write("Error: File could not be found\n")
		sys.exit(1)

################
#create figures#
################


def tempfig(maxmin, dayormonth, name):
#create ylimits list
	ylimits=maxmin
	plot.figure() #new window --> Instance

	#set labels/axis limits/title
	plot.xlabel('Hours')
	plot.ylabel('Degree Celsius')
	plot.title("Awesome Temperature")

	#sets limits for axis
	x = object if( dayormonth==1) else 23
	if isinstance(ylimits,list):
		plot.ylim(ylimits[0]-5, ylimits[1]+5)
		plot.xlim(0, x)
	else:
		plot.ylim(-15,45)
		plot.xlim(0, x)

	#create and save plot in file
	plot.grid()
	plot.plot(ListTemp,color='r',linewidth=3.0)
	plot.savefig('./static/temperature.png')

def	pressfig(maxmin, dayormonth, name):
	ylimits=maxmin
	plothours = []
	for i in range(24):
		plothours.append(i)
	#plot.figure()

	#set labels/axis limits/title
	plot.figure()
	plot.xlabel('Hours')
	plot.ylabel('Press HPa')
	plot.title("Awesome Press")

	if isinstance(ylimits,list):
		plot.ylim(ylimits[4]-5, ylimits[5]+5)
	else:
		plot.xlim(0,23) #needs to be set manually
		plot.ylim(900,1250)#-------""------------

	#draw grid/create plot/save
	plot.grid()
	plot.bar(plothours,ListPres,color="g")
	plot.savefig('./static/pressure.png')



def humfig(maxmin,dayormonth,name):
	ylimits=maxmin
	plot.figure()

	#set labels/axis limits/title
	plot.xlabel('Hours')
	plot.ylabel('Humidity in Percent')

	if isinstance(ylimits,list):
		plot.ylim(ylimits[2]-5, ylimits[3]+5)
		plot.xlim(0,23)
	else:
		plot.xlim(0, 23)
		plot.ylim(0,100)

	#draw grid/create plot/save
	plot.grid()
	plot.plot(ListHum,color='b',linewidth=3.0)
	plot.savefig('./static/humidity.png')


now = datetime.datetime.now()
ListTemp = [None] * 24
ListHum = [None] * 24
ListPres = [0] *24
#call openXML
maxmin=[]
maxmin= openXML()
#call create-functions
tempfig(maxmin)
pressfig(maxmin)
humfig(maxmin)

now = datetime.datetime.now()
timestamp = datetime.datetime.fromtimestamp(os.path.getmtime("./XMLM.xml"))

a = calendar.monthrange(now.year, now.month)
ListTempM =[None] *a[1]
ListHumM = [None] * a[1]
ListPresM = [0] *  a[1]

if (now.hour == 23):
	name = "now.year-now.month-now.day"
	maxmin = openXML(1)
	tempfig(maxmin,1,name,a)
	pressfig(maxmin,1,name,a)
	humfig(maxmin,1,name,a)
	
	




