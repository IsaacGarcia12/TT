import time

moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
f = open('output'+moment+'.log', 'w')