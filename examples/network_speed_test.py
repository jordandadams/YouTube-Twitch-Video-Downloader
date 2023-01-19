import speedtest
import math

# getting network speed
# Instantiate Speedtest
st = speedtest.Speedtest()

# Convert Bytes to MB (KB -> MB)
download = round(st.download() / 1024.0/1024.0)
upload = round(st.upload() / 1024.0/1024.0)
ping = st.results.ping

print('----------------------')
print('Memory Data => in MB')
print('----------------------')

print('Download Speed is: ' + str(math.floor(download)) + 'MB')
print('Upload Speed is: ' + str(math.floor(upload)) + 'MB')
print('Ping is: ', ping)