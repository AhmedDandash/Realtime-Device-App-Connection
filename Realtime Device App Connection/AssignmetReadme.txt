# Heart Rate Monitoring System

## Overview
This project consists of three components: a server, a client, and a graphical user interface (GUI). The server emulates a medical device by generating simulated heart rate data and sending it to the client over a TCP socket connection. The client receives this data and stores it using Redis. The GUI provides a user-friendly interface to search for and visualize heart rate data stored in Redis.

## Server (server.py)
### Purpose
- Emulate a medical device by generating simulated heart rate data for a patient.
- Send the generated data to a client over a TCP socket connection.

### Key Components
- **Socket Setup:** Creates a TCP socket and binds it to a specified host and port (0.0.0.0:6002).
- **Data Generation:** Continuously generates random heart rate readings for a patient.
- **JSON Serialization:** Formats the heart rate data into a JSON object and sends it to the client via the socket.

## Client (client.py)
### Purpose
- Connect to the backend server to receive simulated heart rate data.
- Store the received heart rate data using Redis for later retrieval and analysis.

### Key Components
- **Socket Connection:** Establishes a TCP socket connection with the backend server (192.168.1.22:6002).
- **Data Reception:** Receives JSON-formatted heart rate data from the server, decodes it, and extracts heart rate values.
- **Redis Storage:** Stores the extracted heart rate data in Redis using a patient ID as the key.

## GUI (GUI.py)
### Purpose
- Provide a user-friendly interface to search for heart rate data based on patient IDs.
- Display heart rate values graphically using Matplotlib within the GUI.

### Key Components
- **Search Functionality:** Allows users to enter a patient ID and search for corresponding heart rate data stored in Redis.
- **Plotting:** Utilizes Matplotlib to plot heart rate values over time.
- **Error Handling:** Displays appropriate error messages (e.g., invalid patient ID, missing data) using Tkinter's messagebox module.
