import psutil
import math

# print CPU count => in my case it is 20
print('----------')
print('CPU Count')
print('----------')
print(psutil.cpu_count())
print('')

# when 1 cpu is detected, return the usage percentage
# while (1):
#     print(psutil.cpu_percent(1))

# psutil.virtual_memory is returned as params
# Ex) svmem(total=68635951104, available=59620298752, percent=13.1, used=9015652352, free=59620298752)
# Convert Bytes to GB (KB -> MB -> GB)
sysmem = round(psutil.virtual_memory()[0] / 1024.0/1024.0/1024.0)
avamem = round(psutil.virtual_memory()[1] / 1024.0/1024.0/1024.0)
percentmem = psutil.virtual_memory()[2]
usedmem = round(psutil.virtual_memory()[3] / 1024.0/1024.0/1024.0)
freemem = round(psutil.virtual_memory()[4] / 1024.0/1024.0/1024.0)

print('----------------------')
print('Memory Data => in GB')
print('----------------------')


print('Total system memory is: ' + str(math.floor(sysmem)) + 'GB')
print('Available memory is: ' + str(math.floor(avamem)) + 'GB')
print('Percent memory used is: ' + str(math.floor(percentmem)) + '%')
print('Used memory is: ' + str(math.floor(usedmem)) + 'GB')
print('Free memory is: ' + str(math.floor(freemem)) + 'GB')