import os
	from RPi import GPIO 
	from time import sleep
	GPIO.setmode(GPIO.BOARD)
	GPIO.cleanup()
	GPIO.setup(8, GPIO.OUT)
	GPIO.output(8, GPIO.LOW)
	GPIO.setup(26, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	GPIO.output(26, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	stri = "leer"
	data = 0
	def strke():
	    for i in range(100):
	        b = "level="+str(i)+"/100"
	        if(stri.find(b)!=-1):
	            if data<i:
	                data=i
	    data=data/33
	    if data<=1:
	            GPIO.output(24, GPIO.HIGH)
	    if data<=2:
	            GPIO.output(26, GPIO.HIGH)
	    if data<=3:
	            GPIO.output(24, GPIO.HIGH)
	            GPIO.output(26, GPIO.HIGH)
	
	while True:
		try:
			stri = os.system("iwlist wlan0 scan")
			try:
				stri.find("key:off")
				var = 1
			except:
				var = 0
			if(var==0):
				print("Passwort-freies WiFI verfuegbar")
				GPIO.output(8, GPIO.HIGH)
				strke()
				print("Sendeleistung: ", data,"/100")
			else:
				print("Nur Passwort-geschützte WiFi's verfuegbar")
				GPIO.output(8, GPIO.LOW)
	
		except KeyboardInterrupt:
			GPIO.cleanup()
			exit()
