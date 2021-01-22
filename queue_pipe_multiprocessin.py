import multiprocessing

def calc_square(arr, result, v):
    v.value = 5.67
    for idx,n in enumerate(arr):
        result[idx] = n*n

def qcalc_square(arr, q):
    for n in arr:
        q.put(n*n)


if __name__ == "__main__":
    numbers=[2,3,4]

    result = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d',0.0)
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=calc_square, args=(numbers, result, v))
    p2 = multiprocessing.Process(target=qcalc_square, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("\nUsing Queue: ")
    while q.empty() is False:
        print(q.get())

    print("\nUsing Array: ")
    print(result[:])
