from multiprocessing import Process, Pipe

def sender(conn):
    conn.send("Hello from Sender Process")
    conn.close()

def receiver(conn):
    message = conn.recv()
    print("Receiver got:", message)
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    p1 = Process(target=sender, args=(parent_conn,))
    p2 = Process(target=receiver, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
