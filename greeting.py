import time

hour = int(time.strftime("%H"))

if hour < 12:
	print("Good morning ,how can i help you")
	
elif hour < 18:
	print("Good afternoon ,how can i help you")
	
else:
	print("it is night,how can i help you")
	
time = time.strftime("%H:%M:%S")
print(time)
