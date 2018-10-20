Before installing and rebooting the bone I toke timing measured the latency time on my current non real-time kernel. (Picture1)
After applying the rt patch and rebooting the system. I take a second measurement of the latency time. (Picture2)
Out.png is a visualization of both real time and non-real time kernels. I used the togglegpio.sh 0.001 as a time intensive tasks in a separate terminal window for both plots.
 As you can see the execution time of the PREEMPT_RT real-time Kernel is almost five times faster than the non-real time kernel. 
