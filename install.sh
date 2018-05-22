#!/bin/bash
#
#  Copyright 2018 Luis Kress <luis.kress@stud.th-bingen.de Jo Hausmann <johannes.hausmann@stud.th-bingen.de>
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
echo "###################################################
#OpenTemp install & Downloading BME 680 from link #
#Pip installs lxml, MathPlot                      #
###################################################" 

sleep 3

#####################################
#All I2C functions are located here.#
#####################################
 
function checkI2cBus(){
lsmod | grep i2c_dev
if [ $? -eq 1]
    then 
		echo "Not enabled... Next step enable I2C"
		enableI2cBus
	else
		echo "Already loaded by Kernel $(uname -r)"
fi
}

function enableI2cBus(){
	echo "Enabling kernel module"
    echo "i2c-dev" >> /etc/modules
    echo "i2c-bcm2708" >> /etc/modules
    echo "dtparam=i2c1=on" >> /boot/config.txt
    echo "dtparam=i2c_arm=on" >> /boot/config.txt
    sed -i -e 's/blacklist i2c-bcm2708/#blacklist i2c-bcm2708/' /etc/modprobe.d/raspi-blacklist.config
}
function checkI2CDevice(){
i2cdetect -y 0
case $? in
	  1)
	  echo "Not connected on bus 0"
	  ;;
	  0)
	  echo "Connected"
esac	  
i2cdetect -y 1
case $? in
	 1)
	 "Not connected on bus 0"
	 return 0
	 ;;
	 0)
	 echo "Connected"
esac	 
		
}	
function autocronjob(){
#System wide? User specific?
#crontab -l > ./.opemtempcron
#Setting system wide cron job for OpenTemp main
read -p "Enter your OpenTemp directory" : dir
read -p "Set user for OpenTemp (root|pi|foo|...)" :user
echo "50 */1 * * * $user $dir" >> /etc/crontab
#Setting system wide cron job for Flask Server
read -p "Enter your WebServer directory (full path):" dir2
read -p "Set user for WebServer (root|pi|foo|...)" :user
echo "@reboot         $user $dir" >> /etc/crontab
}

echo "Checking for sudo permissions"
     if [ "$(whoami)" != "root" ] 
        then
         exec sudo su
        
     fi
echo "Installing BME 680 libraries"
     python -c "import bme680"
     if [ $? -eq 0 ]
        then
			echo "Already installed. Continue"
		else
		    pip3 install bme680
		    
	 fi	    	
        
echo "Installing LXML libraries"
     python -c "import lxml"
     if [ $? -eq 0 ]
        then
			echo "Already installed. Continue"
		else
		    pip3 install lxml
		    
	 fi	    	
        
echo "Installing MatPlot Py libraries"
     python -c "import matplotlib"
     if [ $? -eq 0 ]
        then
			echo "Already installed. Continue"
		else
		    pip3 install matplotlib
		    
	 fi	   

#Enable I2C Bus on Raspberry PI

read -p "Is your I2C bus already enabled? * for not sure:) (Y|y|N|n|*):" answer
case $answer in
     "Y"|"y")
      echo "We will continue with checking connectivity"
      checkI2CDevice();;
     "N"|"n")
      enableI2cBus()
      ;;
    "*")
     echo "Checking Kernel module"
     checkI2cBus()
esac 

echo"########################################
#All done. Your I2C BME 680 is connected# 
#Flask & OpenTemp are loaded by cron    #
#Web Interface running IP Device:5005   #
#########################################"

