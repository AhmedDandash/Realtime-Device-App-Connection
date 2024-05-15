import socket
import random
import json
import time

HOST = '0.0.0.0'
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as app_socket:
    app_socket.bind((HOST, PORT))
    app_socket.listen()

    print((HOST, PORT))

    conn, addr = app_socket.accept()
    with conn:
        print('Connection from:', addr)
        id = random.randint(1, 100)
        for timestamp in range(100):
            time.sleep(0.25)  

            bpm = random.randint(60, 90)
            time1 = timestamp

            response = {'BPM': bpm, 'time1': time1, 'id': id}
            json_response = json.dumps(response)
            conn.sendall(json_response.encode())

        conn.close()
