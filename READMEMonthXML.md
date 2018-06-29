# MonthXML
## How MonthXML works
MonthXML has one important method:  
addDay() calculates the median of the daily collected data and adds it to the MXML xml-Sheet.
```
def addDay():
	try:
		et = etree.parse("XMLM.xml")
		weatherArr = getDayData()
		day = etree.SubElement(et.getroot(),"day"+time.strftime("%d"), temp=str(weatherArr[0]), hum=str(weatherArr[1]), pres=str(weatherArr[2]))
		write(etree.ElementTree(et.getroot())) 
	except etree.XMLSyntaxError:
		sys.stderr.write("Error: File is empty\n")
	except OSError:
		sys.stderr.write("Error: File could not be found\n")
```
