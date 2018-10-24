# Picture1

Before installing and rebooting the bone I toke timing measured the latency time on my current non real-time kernel. (Picture1)

# Picture2

After applying the rt patch and rebooting the system. I take a second measurement of the latency time. (Picture2)


# out.png

Out.png is a visualization of both real time and non-real time kernels. I used the togglegpio.sh 0.001 as a time intensive tasks in a separate terminal window for both plots.
As you can see the execution time of the PREEMPT_RT real-time Kernel is almost five times faster than the non-real time kernel. 

========================
Professor Yoder's Comments

Picture2.png shows a "not Found" error message.

I see only one plot.  Is must be for a load.  Where is your no load plot?

Score:  7/10