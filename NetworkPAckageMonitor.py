import tkinter as tk
from tkinter import scrolledtext
from scapy.all import sniff
import threading

class TrafficAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Traffic Analyzer")
        self.capturing = False
        self.thread = None

        # GUI Elements
        self.start_button = tk.Button(root, text="Start Capture", command=self.start_capture)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Capture", command=self.stop_capture)
        self.stop_button.pack(pady=10)

        self.log_area = scrolledtext.ScrolledText(root, height=20, width=70)
        self.log_area.pack(pady=10)

    def start_capture(self):
        if not self.capturing:
            self.capturing = True
            self.log_area.delete(1.0, tk.END)  # Clear previous log
            self.thread = threading.Thread(target=self.capture_packets)
            self.thread.start()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_capture(self):
        self.capturing = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def capture_packets(self):
        sniff(prn=self.packet_callback, store=0)

    def packet_callback(self, packet):
        if not self.capturing:
            return
        self.log_area.insert(tk.END, f"{packet.summary()}\n")
        self.log_area.see(tk.END)  # Scroll to the end

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficAnalyzerApp(root)
    root.mainloop()
