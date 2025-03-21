import tkinter as tk
from tkinter import ttk, messagebox
from process_manager import list_processes, kill_process
from resource_monitor import get_cpu_usage, get_memory_usage, get_disk_usage
from gui import TaskManagerApp

def main():
    # Set up the main application window and start the Tkinter event loop
    app = TaskManagerApp()
    app.mainloop()

if __name__ == "__main__":
    main()
