import tkinter as tk
from threading import Thread
from assistant import main
import queue

# Queue to collect assistant logs
log_queue = queue.Queue()

# Attach the log queue to speak and listen modules
from utils import speak, listen
speak.log_queue = log_queue
listen.log_queue = log_queue


def start_jarvis():
    Thread(target=main, daemon=True).start()

def update_logs():
    try:
        while True:
            log = log_queue.get_nowait()
            log_display.insert(tk.END, log + "\n")
            log_display.see(tk.END)
    except queue.Empty:
        pass
    root.after(200, update_logs)

# UI Setup
root = tk.Tk()
root.title("JARVIS SYSTEM")
root.geometry("600x500")
root.configure(bg="#121212")

# Title
title = tk.Label(root, text=" JARVIS ASSISTANT", font=("Orbitron", 20), fg="#00FFFF", bg="#121212")
title.pack(pady=10)

# Start Button
start_btn = tk.Button(root, text="Start", font=("Orbitron", 12), bg="#00aaff", fg="white", command=start_jarvis)
start_btn.pack(pady=10)

# Log Display
log_display = tk.Text(root, width=70, height=20, bg="#1f1f1f", fg="#00ffcc", font=("Consolas", 10))
log_display.pack(pady=10)

# Start log updater loop
update_logs()

root.mainloop()
