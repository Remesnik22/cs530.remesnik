import socket
import time

HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 65432        # Port used by the server

times = []
for _ in range(20):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        start = time.time()
        data = s.recv(1024)
        end = time.time()
        times.append(end - start)

avg_time = sum(times) / len(times)
print(f"Average round-trip time: {avg_time:.6f} seconds")
