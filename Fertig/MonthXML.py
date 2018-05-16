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
		et = etree.parse("XMLD.xml") #baum datei holen
		day = etree.SubElement(et.getroot(),"day"+time.strftime("%d")) #unterknoten mit aktuellem datum uebergeben
		write(etree.ElementTree(et.getroot())) #baum schreiben
	except etree.XMLSyntaxError:
		sys.stderr.write("Error: File is empty")
	except OSError: #fuer pi noch anpassen je nach fehlermeldung
		sys.stderr.write("Error: File could not be found")



def initialize():
	month = etree.Element("month"+ time.strftime("%m")) #root Knoten erstellen
	write(etree.ElementTree(month))


def write(mytree):
	if isinstance(mytree, etree._ElementTree):
		f = open("XMLTest.xml","wb")
		f.write(etree.tostring(mytree, pretty_print=True))
		f.close()
	else:
		sys.stderr.write("Error!\n")
