import time,random
n=random.randint(1,10)*100

start = time.time()

print("Sleep for {} ms".format(n))
time.sleep(n/1000)

print(time.time()-start)

