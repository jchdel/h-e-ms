My focus while not waiting for new gadgets to add in my setup, is to design a (graceful) way of identifing patterns in MQTT streams (or in timeserie DB) as soon as possible.

For instance, to discover that the dish machine just started a cycle, and a bit later on that this cycle is an heavy eco one.
With that information the system could infer needed energy for following time frame allowing/forbidding other workloads to start according to wheather forecast or other inputs.

My goal is total off-grid for myself and partial off-grid for my customers (if they are afraid of being totaly off-grid).

For now, I still have absolutely no clue about machine learning.
But I have experience reading graphs as a scientist in a lab...
And a lot more as GNU/Linux sysadmin and developer...

I guess my first iteration will be to record a couple of runs of live data I want to profile and try to find some mean+error envoloppe. Then to try to filter a bit raw inputs and compare time frames against related part of indentified patterns to see if one is just probably starting...
