import datetime
import time


print("---scratch-2---\n")

print(time.time())
print(time.localtime()[0])
print('month',time.localtime()[1])
print(datetime.datetime.now())
print (datetime.datetime.now().strftime("%y"))
print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print (datetime.datetime.now().strftime("%Y-%B-%A %H:%M:%S %p"))

print("\n-------end-------")



# https://www.programiz.com/python-programming/datetime/strftime

