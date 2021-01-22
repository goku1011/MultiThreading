import time
import multiprocessing

store_result = []

def square_data(arr):
    global store_result
    for i in arr:
        store_result.append(i*i)
        print('square ' + str(i*i))
    print('within a process result: '+ str(store_result))

if __name__ == '__main__':
    arr=[2,3,4,5]
    p1 = multiprocessing.Process(target=square_data, args=(arr,))
    p1.start()
    p1.join()
    print('result' + str(store_result))
    print("Done!")

# When you create a new process, it will create a new copy of the store_result
# Every process has its own address space (virtual memory)
# Thus program variables are not shared between two processes
