#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DXML.py
#  
#  Copyright 2018 Jo Hausmann <johannes.hausmann@stud.th-bingen.de>
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
import time
import os
import sys
day = time.strftime("%d")
hour = time.strftime("%H")

def create():
	root = etree.Element("day"+day)
	my_tree= etree.ElementTree(root)
	write(my_tree)
	

def addhour(temp, hum, pres):
	try:
		tree= etree.parse("XMLD.xml")   #Parse an existing XML Sheet
		root = tree.getroot()   
		child = etree.SubElement(root, "hour" + hour, temp=str(temp), #Create a new Child
		hum=str(hum), pres=str(pres))
		my_tree = etree.ElementTree(root)  #Add Child to tree
		write(my_tree)					   #Call write function
	except etree.XMLSyntaxError:
		print ("File doesn't have root node")
	except IOError:
		print("File doesn't exist in the directory")	
			
		
		
def write(my_tree):
	if isinstance(my_tree,etree._ElementTree):
		f = open("XMLD.xml", "w")
		f.write(etree.tostring(my_tree, pretty_print=True))
		f.close()
	else:
		os.error("Given argument is not object of class etree")		

