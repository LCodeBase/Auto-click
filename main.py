import pyautogui
import time
import threading
import keyboard
import tkinter as tk
from tkinter import ttk, messagebox
import json

# Set pyautogui to maximum speed
pyautogui.PAUSE = 0

# Global variables
automation_active = False
key_or_button = None
speed = 10
click_counter = 0
click_position = None

# Function to repeatedly click a key or mouse button
def click_action():
    global automation_active, key_or_button, speed, click_counter, click_position
    while automation_active:
        if click_position:
            pyautogui.click(click_position)
        elif key_or_button == "mouse1":
            pyautogui.click(button='left')
        elif key_or_button == "mouse2":
            pyautogui.click(button='right')
        else:
            pyautogui.press(key_or_button)
        click_counter += 1
        click_counter_label.config(text=f"Total Clicks: {click_counter}")
        time.sleep(0.001)

# Function to start the automation
def start_automation():
    global automation_active
    if not key_or_button and not click_position:
        messagebox.showerror("Error", "Please configure a valid key/button or position.")
        return
    automation_active = True
    threading.Thread(target=click_action, daemon=True).start()

# Function to stop the automation
def stop_automation():
    global automation_active
    automation_active = False

# Function triggered when F1 is pressed
def toggle_activity():
    global automation_active
    if automation_active:
        stop_automation()
        status_label.config(text="Automation Disabled", foreground="red")
    else:
        start_automation()
        status_label.config(text="Automation Enabled", foreground="green")

# Function to configure the key and speed
def configure():
    global key_or_button, speed, click_position
    key_or_button = key_entry.get()
    try:
        speed = float(speed_entry.get())
        if speed <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Speed must be a number greater than 0.")
        return
    if key_or_button.lower() == "position":
        click_position = pyautogui.position()
        key_or_button = None
        messagebox.showinfo("Position Captured", f"Coordinates: {click_position}")
    else:
        click_position = None
    status_label.config(text="Settings saved. Press F1 to start.", foreground="blue")
    toggle_button.config(state=tk.NORMAL)

# Function to save configurations to a JSON file
def save_configurations():
    configurations = {
        "key_or_button": key_or_button,
        "speed": speed,
        "click_position": click_position
    }
    with open("configurations.json", "w") as file:
        json.dump(configurations, file)
    messagebox.showinfo("Saved", "Configurations saved successfully!")

# Function to load configurations from a JSON file
def load_configurations():
    global key_or_button, speed, click_position
    try:
        with open("configurations.json", "r") as file:
            configurations = json.load(file)
            key_or_button = configurations.get("key_or_button")
            speed = configurations.get("speed", 10)
            click_position = tuple(configurations.get("click_position", []))
            status_label.config(text="Configurations loaded. Press F1 to start.", foreground="blue")
            toggle_button.config(state=tk.NORMAL)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No configuration file found.")

# GUI with Tkinter
root = tk.Tk()
root.title("Key and Mouse Automation")
root.geometry("400x400")

# Labels and inputs for configuration
config_frame = ttk.LabelFrame(root, text="Configurations")
config_frame.pack(padx=10, pady=10, fill="both", expand=True)

key_label = ttk.Label(config_frame, text="Enter key or 'mouse1'/'mouse2' or 'position':")
key_label.pack(pady=5)

key_entry = ttk.Entry(config_frame)
key_entry.pack(pady=5)

speed_label = ttk.Label(config_frame, text="Enter speed (ignored if optimized):")
speed_label.pack(pady=5)

speed_entry = ttk.Entry(config_frame)
speed_entry.pack(pady=5)

config_button = ttk.Button(config_frame, text="Save Configurations", command=configure)
config_button.pack(pady=5)

save_button = ttk.Button(config_frame, text="Save Configurations to File", command=save_configurations)
save_button.pack(pady=5)

load_button = ttk.Button(config_frame, text="Load Configurations from File", command=load_configurations)
load_button.pack(pady=5)

# Program status label
status_label = ttk.Label(root, text="Waiting for configurations...", foreground="blue")
status_label.pack(pady=10)

click_counter_label = ttk.Label(root, text="Total Clicks: 0", foreground="black")
click_counter_label.pack(pady=5)

toggle_button = ttk.Button(root, text="Activate/Deactivate Automation (F1)", state=tk.DISABLED, command=toggle_activity)
toggle_button.pack(pady=10)

# Function to detect hotkeys
def start_hotkey_listener():
    keyboard.add_hotkey('F1', toggle_activity)

# Start the hotkey listener in a separate thread
threading.Thread(target=start_hotkey_listener, daemon=True).start()

# Start the GUI
root.mainloop()
