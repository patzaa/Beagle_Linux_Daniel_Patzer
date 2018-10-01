
# Make file
The make file compiles app.c in app.arm. When getting executed it will print “Hello World” on the screen. <br />

# Cross Compiling 
a.out got cross-compiled on the host and copied to the bone <br />

# Kernal
directory Kernel/hello you will find a hello.c file, after executing Make, you can execute the Kernel model by sudo insmode hello.ko  <br /> 
In a different terminal you can open the terminal log to read the messages <br /> 

•	enter: bone$ sudo bash <br />
•	bone$ cd /var/log/ <br />
•	bone$ tail -f kern.log <br />

In directory Kernel/gpio_test you will find gpio_test.c. This file uses the kernel to read imput from a button and switches an LED accordingly. (LED: P9_15 Button: P9_16) <br />


Directory Kernel/ebbchar is a LKM to communicate with the Kernel. It is part of the second tutorial provided by Derek Molloy) <br />
