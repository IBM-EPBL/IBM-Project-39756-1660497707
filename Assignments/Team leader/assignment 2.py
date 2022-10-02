import os
import random
for i in range (30,80):

	h= random.randint(65,75)
	t= random.randint(35,40)
	temp = t
	humidity = h 
	print (t)
	print (h)

	if (humidity >=75 or temp >=40):
		print ("! ! HIGH ALERT ! !")
	else:
		print("LOW")     
