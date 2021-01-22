from multiprocessing import Pool
import time

def f(x):
    sum=0
    for i in range(10000):
        sum += i*i
    return sum

if __name__ == '__main__':

    t1 = time.time()
    result=[]
    for i in range(100000):
        result.append(f(i))

    print("Serial Processing Time: ", time.time()-t1)

    t2 = time.time()
    p = Pool()
    result = p.map(f, range(100000))
    p.close()
    p.join()
    print("Parallel Processing Time: ", time.time()-t2)

# Serial Processing Time:  87.06237530708313
# Parallel Processing Time:  24.24444603919983
