# Homework 3
 This hw03 folder contains the i2c_temp_sens.py, temp.sh and the etch_encoder.py <br />
 
 
# i2c_temp_sens.py <br />
using the TMP101 sensors to read temperature through i2c bus <br />

# temp.sh <br />
shell script to read the values of two TMP101 sensors connected to the i2c bus, output in Fahrenheit. <br />

# etch_encoder.py <br />
This is a simple etch-a-sketch program running on the 8x8 Matrix controlled by two rotational encoders. The two buttons are used for reset and quitting the game. <br />
execute the setup.sh in ~/exercises/sensors/eQEP otherwise the second encoder will not work. <br />
Pinning from the encoder are: <br />
P8_33, P8_35 for eQEP1<br />
P8_41, P8_42 for eQEP2<br />


