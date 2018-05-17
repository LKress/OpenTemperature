#!/usr/bin/env python
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
from lxml import etree
from matplotlib import pyplot as plot
from matplotlib import style
import numpy as np

'''da = np.arange(24)
ListTemp = [None] * 24
ListHum = [None] * 24
ListPres = [0] *24
#style.use("ggplot")'''

###########################################################
#openXML --> open daily XML Sheet && save numbers in lists#
###########################################################

def openXML():
	et = etree.parse("XMLD.xml") 
	root = et.getroot()	
				
	for child in root:
		position = child.tag
		ListTemp[position] = (int(child.get("temp"))
		ListHum[position] = (int(child.get("hum"))
		ListPres[postion] = (int(child.get("pres"))
################		
#create figures#
################


def tempfig():
	plot.figure() #new window --> Instance
	
	#set labels/axis limits/title
	plot.xlabel('Hours')
	plot.ylabel('Degree Celsius')
	plot.xlim(0, 23)
	plot.ylim(-15,45)
	plot.title("Awesome Temperature")
	
	#create and save plot in file
	plot.plot(ListTemp,color='r',linewidth=3.0)
	plot.savefig('tempfig.png')
	
def	pressfig():
	plot.figure()
	
	#set labels/axis limits/title
	plot.figure()
	plot.xlabel('Hours')
	plot.ylabel('Press HPa')
	plot.xlim(0,23)
	plot.ylim(900,1250)
	plot.title("Awesome Press")
	
	#draw grid/create plot/save
	plot.grid()
	plot.bar(plothours,ListPres,color="g")
	plot.savefig('pressfig.png')
	
def humfig():
	plot.figure()
	
	#set labels/axis limits/title
	plot.xlabel('Hours')
	plot.ylabel('Humidity in Percent')
	plot.xlim(0, 23)
	plot.ylim(0,100)
	plot.title("Awesome Humidity")
	
	#draw grid/create plot/save
	plot.grid()
	plot.plot(ListHum,color='b',linewidth=3.0)
	plot.savefig('humfig.png')
	
		
plothours = np.arange(24)
ListTemp = [None] * 24
ListHum = [None] * 24
ListPres = [0] *24	
	
#call openXML
openXML()
#call create-functions
tempfig()
pressfig()
humfig()

