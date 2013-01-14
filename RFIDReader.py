import serial

def IDCheck(data):
	if data== '4E009C33FA':
		print 'Shys wallet'
	elif data == '5900285E23':
		print 'Keychain'

port = '/dev/ttyUSB0'
speed = 2400

ser = serial.Serial(port, speed)

while True:
	data = ser.readline()
	if data != None:
		data = data.rstrip()
		print 'Output: ' + data
		IDCheck(data)
		ser.flushInput()
ser.close()
