import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)
bpm = []
time1 = []

def search():
    message_label.config(text="")
    patient_id = patient_id_entry.get()
    data_str = r.get(patient_id)
    if data_str is not None:  # Check if the key exists in Redis
        data = json.loads(data_str)
        # Convert the strings back to arrays
        bpm[:] = json.loads(data['bpm'])
        time1[:] = json.loads(data['time1'])
        message_label.config(text=f"This patient {patient_id} was found.")
    else:
        message_label.config(text=f"No data found for {patient_id}.")

def play():
    # Clear the previous plot
    ax.clear()
    # Example: Plot a simple line
    ax.plot(time1,bpm)
    ax.set_title('Heart Rate Over Time')
    plot_placeholder.draw()

root = tk.Tk()

# Create a placeholder for the plot
figure = Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(111)
plot_placeholder = FigureCanvasTkAgg(figure, root)
plot_placeholder.get_tk_widget().pack()

# Create a search bar
search_frame = tk.Frame(root)
search_frame.pack()

patient_id_entry = tk.Entry(search_frame)
patient_id_entry.pack(side=tk.LEFT)

# Create a search button
search_button = tk.Button(search_frame, text="Search Patient", command=search)
search_button.pack(side=tk.LEFT)

message_label = tk.Label(root, text="")
message_label.pack()

# Create a play button
play_button = tk.Button(root, text="Show Heart Rate Graph", command=play)
play_button.pack()

root.mainloop()
