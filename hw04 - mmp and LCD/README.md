# The directory /pictures include the Memory map and the two pictures for the display 



The GPIO_button_mmap.c is a c script making use of the mmap functionality. This script maps to two GPIO registers, GPIO1 and GPIO3. It uses two buttons connected to the GPIO P9_25 and GPIO P9_23 to control two of the internal LEDs on the beagleboard(execute ./GPIO_button.mmap) <br />

The gpio_toggle.c file toggles the internal LED USRA3 <br />


# All files according to the LCD display are stored in the directory display including:

•	boris.sh will display boris full screen on the LCD (See pictures/boris_fullscreen.jpg ) execute it via sudo <br />
•	text_name.sh uses Imagemagick to print my name and a message on a white screen (see pictures/text_name.jpg) <br />
•	I edited the rotate command in 'reset.sh' and 'on.sh' so that the display would rotate an image or video 90 degrees. <br />
•	movie.sh shows a movie on the Display, by changing the rotate= 1 you can rotate the video. <br />
•	off.sh can be executed to shut off the LCD. <br />
•	install.sh is install file to install all necessary packages for the display <br />

