import time
import threading

def square_nums(arr):
    for i in arr:
        time.sleep(0.2)
        print(i*i)

def cube_nums(arr):
    for i in arr:
        time.sleep(0.2)
        print(i*i*i)

if __name__ == "__main__":
    t = time.time()
    arr = [2,3,4,5]
    t1 = threading.Thread(target=square_nums, args=(arr,))
    t2 = threading.Thread(target=cube_nums, args=(arr,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Time: ", time.time()-t)
