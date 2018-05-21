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

from lxml import etree
import sys
import time

def addDay():
	try:
		et = etree.parse("XMLM.xml") #baum datei holen
		weatherArr = getDayData()
		day = etree.SubElement(et.getroot(),"day"+time.strftime("%d"), temp=str(weatherArr[0]), hum=str(weatherArr[1]), pres=str(weatherArr[2])) #unterknoten mit aktuellem datum uebergeben
		write(etree.ElementTree(et.getroot())) #baum schreiben
	except etree.XMLSyntaxError:
		sys.stderr.write("Error: File is empty\n")
	except OSError: #fuer pi noch anpassen je nach fehlermeldung
		sys.stderr.write("Error: File could not be found\n")



def initialize():
	month = etree.Element("month"+ time.strftime("%m")) #root Knoten erstellen
	write(etree.ElementTree(month))


def write(mytree):
	if isinstance(mytree, etree._ElementTree):
		f = open("XMLM.xml","wb")
		f.write(etree.tostring(mytree, pretty_print=True))
		f.close()
	else:
		sys.stderr.write("Error!\n")

def getDayData():
	et = etree.parse("XMLD.xml")
	root = et.getroot()
	avTemp = avHum = avPress = counter = 0
	for child in root:
		avTemp += float(child.get("temp"))
		avHum += float(child.get("hum"))
		avPress += float(child.get("pres"))
		counter += 1
	avTemp /= counter
	avHum /= counter
	avPress /= counter
	return [avTemp,avHum,avPress]
