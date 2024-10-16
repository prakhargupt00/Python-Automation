import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pygame
import datetime
import time
#pip install pygame

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        # Initialize pygame for playing sound
        pygame.mixer.init()

        self.time_label = tk.Label(root, text="Set Alarm (HH:MM:SS)", font=("Arial", 14))
        self.time_label.pack(pady=10)

        self.time_entry = tk.Entry(root, font=("Arial", 14))
        self.time_entry.pack(pady=10)

        self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=10)

        self.file_button = tk.Button(root, text="Select MP3 File", command=self.load_mp3)
        self.file_button.pack(pady=10)

        self.alarm_time = None
        self.mp3_file = None

        # Start checking for the alarm
        self.check_alarm()

    def load_mp3(self):
        self.mp3_file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.mp3_file:
            messagebox.showinfo("Selected File", f"Loaded: {self.mp3_file}")

    def set_alarm(self):
        alarm_input = self.time_entry.get()
        try:
            self.alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M:%S").time()
            messagebox.showinfo("Alarm Set", f"Alarm set for {self.alarm_time}")
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS format.")

    def check_alarm(self):
        if self.alarm_time:
            current_time = datetime.datetime.now().time()
            if current_time >= self.alarm_time:
                if self.mp3_file:
                    self.play_sound()
                self.alarm_time = None  # Reset alarm after it goes off
        self.root.after(1000, self.check_alarm)

    def play_sound(self):
        pygame.mixer.music.load(self.mp3_file)
        pygame.mixer.music.play()
        messagebox.showinfo("Alarm", "Alarm is ringing!")

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
