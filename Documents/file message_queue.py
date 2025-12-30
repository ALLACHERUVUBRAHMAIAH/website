from multiprocessing import Process, Queue

def producer(queue):
    queue.put("Message 1")
    queue.put("Message 2")
    queue.put("Message 3")

def consumer(queue):
    while not queue.empty():
        msg = queue.get()
        print("Consumed:", msg)

if __name__ == "__main__":
    queue = Queue()

    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
