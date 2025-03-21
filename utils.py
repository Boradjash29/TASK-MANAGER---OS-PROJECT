import matplotlib.pyplot as plt
import psutil
import time

cpu_usage = []
memory_usage = []

def monitor_performance():
    while True:
        cpu_usage.append(psutil.cpu_percent())
        memory_usage.append(psutil.virtual_memory().percent)

        if len(cpu_usage) > 50:
            cpu_usage.pop(0)
            memory_usage.pop(0)

        plt.clf()
        plt.subplot(2, 1, 1)
        plt.plot(cpu_usage, label='CPU Usage (%)')
        plt.title('CPU Usage')
        plt.xlabel('Time (s)')
        plt.ylabel('CPU Usage (%)')

        plt.subplot(2, 1, 2)
        plt.plot(memory_usage, label='Memory Usage (%)')
        plt.title('Memory Usage')
        plt.xlabel('Time (s)')
        plt.ylabel('Memory Usage (%)')

        plt.tight_layout()
        plt.pause(1)
