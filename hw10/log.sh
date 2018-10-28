
#!/bin/bash

for i in {1..30}
do
	# Read temp sensor on i2c bus 2
	tempC=`i2cget -y 2 0x49`
	tempF=$((($tempC * 9/5) + 32))
	./demo.py $tempF 0 

	sleep 1
done

