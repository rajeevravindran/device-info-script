
n=1

echo 'Enter number of devices'
read n

echo Generating $n device info

function hexPrinter(){
randomInteger=$[ ($RANDOM % 100 ) + 16]
randomHex=$(printf '%x\n' $randomInteger)
echo $randomHex;
}

for ((i=1;i<=$n;i++))
do
_deviceID=$i;
_macEth=$(hexPrinter):$(hexPrinter):$(hexPrinter):$(hexPrinter):$(hexPrinter):$(hexPrinter)
_macWlan=$(hexPrinter):$(hexPrinter):$(hexPrinter):$(hexPrinter):$(hexPrinter):$(hexPrinter)
#echo $_deviceID
#echo $_macEth
#echo $_macWlan
echo  \{\"id\":\"$_deviceID\"\,\"etho\":\"$_macEth\"\,\"wlan0\":\"$_macWlan\"\}
done
