# DXML.py

## How DXML works
DXML gets called by your Main.py function every hour. 
It contains three functions with different purposes. 1.Creating a new sheet 2.Adding a new child node to your existing sheet and 3. A simple write function.

### Create function
```
def create():
	root = etree.Element("day"+day)
	my_tree= etree.ElementTree(root)
	write(my_tree)
```
That's fairly simple. 
1. Create root node with the present day
2. Add root node to object
### Addhour function
```
def addhour(temp, hum, pres):
	try:
		tree= etree.parse("XMLD.xml")   
		root = tree.getroot()   
		child = etree.SubElement(root, "hour" + hour, temp=str(temp), 
		hum=str(hum), pres=str(pres))
		my_tree = etree.ElementTree(root)  
		write(my_tree)					   
```
1. Parse existing XML sheet
2. Get root node
3. Create subelement with weather data --> add to object
### Write function
```
def write(my_tree):
	if isinstance(my_tree,etree._ElementTree):
		f = open("XMLD.xml", "wb")
		f.write(etree.tostring(my_tree, pretty_print=True))
		f.close()
	else:
		os.error("Given argument is not object of class etree")		
```
1. Check if tree is an instance of ElementTree
2. Write object as string to XML Sheet

