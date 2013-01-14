import serial

port = '/dev/ttyUSB0'
speed = 2400 

ser = serial.Serial(port ,speed)

while True:
	data = ser.readline()
	if data != None:	
		print 'Output: ' + ser.readline().rstrip()
		
ser.close()
