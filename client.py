import socket
import json
import redis

SERVER_ADDRESS = "127.0.0.1"
PORT = 3000

# Connect to your Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

bpm = []
time1 = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as front_socket:
    front_socket.connect((SERVER_ADDRESS, PORT))

    while True:
        data = front_socket.recv(1024)
        if not data:
            break

        # Decode the received data as JSON
        response = data.decode()
        data = json.loads(response)
        print(data)

        # Extract data and append to lists
        id = data['id']
        x = data['BPM']
        y = data['time1']
        bpm.append(x)
        time1.append(y)

    # Close the connection
    front_socket.close()

# Convert lists to JSON strings
bpm_str = json.dumps(bpm)
time1_str = json.dumps(time1)

# Store the arrays in Redis
r.set(id, json.dumps({'bpm': bpm_str, 'time1': time1_str}))
