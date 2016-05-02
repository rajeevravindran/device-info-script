_deviceID=$(cat /proc/cpuinfo | grep Serial | cut -d ':' -f 2)
_macEth=$(ifconfig eth0 | awk '/HWaddr/ {print $5}')
_macWlan=$(ifconfig wlan0 | awk '/HWaddr/ {print $5}')
#echo $_deviceID
#echo $_macEth
#echo $_macWlan
echo  \{\"id\":\"$_deviceID\"\,\"etho\":\"$_macEth\"\,\"wlan0\":\"$_macWlan\"\}
