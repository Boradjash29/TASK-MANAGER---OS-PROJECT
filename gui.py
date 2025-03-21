import tkinter as tk
from tkinter import ttk, messagebox
from resource_monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage  
from process_manager import list_processes, kill_process
class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("800x600")
        self.configure(bg='black')

        # Labels for CPU, Memory, Disk, and Network Usage
        self.cpu_label = ttk.Label(self, text="CPU Usage: --%", background='black', foreground='white')
        self.cpu_label.pack(pady=5)

        self.memory_label = ttk.Label(self, text="Memory Usage: --%", background='black', foreground='white')
        self.memory_label.pack(pady=5)

        self.disk_label = ttk.Label(self, text="Disk Usage: --%", background='black', foreground='white')
        self.disk_label.pack(pady=5)

        self.network_label = ttk.Label(self, text="Network Usage: -- KB/s", background='black', foreground='white')
        self.network_label.pack(pady=5)

        # Listbox for processes
        self.process_listbox = tk.Listbox(self, height=20, width=80)
        self.process_listbox.pack(pady=10)

        self.kill_button = ttk.Button(self, text="Kill Process", command=self.kill_selected_process)
        self.kill_button.pack(pady=5)

        self.sort_cpu_button = ttk.Button(self, text="Sort by CPU", command=lambda: self.update_process_list("cpu_percent"))
        self.sort_cpu_button.pack(pady=5)

        self.sort_memory_button = ttk.Button(self, text="Sort by Memory", command=lambda: self.update_process_list("memory_percent"))
        self.sort_memory_button.pack(pady=5)

        self.sort_name_button = ttk.Button(self, text="Sort by Name", command=lambda: self.update_process_list("name"))
        self.sort_name_button.pack(pady=5)

        self.search_label = ttk.Label(self, text="Search Process:", background='black', foreground='white')
        self.search_label.pack(pady=5)

        self.search_entry = ttk.Entry(self)
        self.search_entry.pack(pady=5)
        self.search_entry.bind("<KeyRelease>", self.filter_processes)

    
        self.update_system_info()
        self.update_process_list()
        self.after(5000, self.check_for_alerts)

    def update_system_info(self):
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()
        network_usage = get_network_usage()

        # Update labels
        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.config(text=f"Memory Usage: {memory_usage}%")
        self.disk_label.config(text=f"Disk Usage: {disk_usage}%")
        self.network_label.config(text=f"Network Usage: {network_usage} KB/s")

        self.after(1000, self.update_system_info)  # Update every 1 seconds

    def update_process_list(self, sorted_key=None, filtered_processes=None):
        self.process_listbox.delete(0, tk.END)
        processes = filtered_processes if filtered_processes else list_processes()
        
        if sorted_key:
            processes.sort(key=lambda x: x.get(sorted_key, 0), reverse=True)
        
        if not processes:
            self.process_listbox.insert(tk.END, "No processes found.")
        else:
            for proc in processes:
                self.process_listbox.insert(tk.END, f"PID: {proc['pid']} | {proc['name']} | CPU: {proc['cpu_percent']}% | Memory: {proc['memory_percent']}% ")

    def kill_selected_process(self):
        selected = self.process_listbox.get(tk.ACTIVE)
        if selected:
            try:
                pid = int(selected.split('|')[0].strip().split(': ')[1])
                result = kill_process(pid)
                messagebox.showinfo("Info", result)
            except ValueError:
                messagebox.showerror("Error", "Invalid process selection.")

    def filter_processes(self, event=None):
        search_term = self.search_entry.get().lower()
        processes = list_processes()
        filtered_processes = [proc for proc in processes if search_term in proc['name'].lower()]
        self.update_process_list(filtered_processes=filtered_processes)

    def check_for_alerts(self):
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        if cpu_usage > 80:
            messagebox.showwarning("High CPU Usage", f"CPU usage is high: {cpu_usage}%")
        if memory_usage > 80:
            messagebox.showwarning("High Memory Usage", f"Memory usage is high: {memory_usage}%")
        self.after(5000, self.check_for_alerts)

if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()