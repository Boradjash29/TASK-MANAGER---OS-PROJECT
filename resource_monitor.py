import psutil

# Function to get CPU usage percentage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get memory usage percentage
def get_memory_usage():
    return psutil.virtual_memory().percent

# Function to get disk usage percentage
def get_disk_usage():
    return psutil.disk_usage('/').percent

# Function to get network usage (bytes sent and received per second)
def get_network_usage():
    net_io1 = psutil.net_io_counters()
    bytes_sent1 = net_io1.bytes_sent
    bytes_recv1 = net_io1.bytes_recv
    
    psutil.time.sleep(1)  # Wait for 1 second
    
    net_io2 = psutil.net_io_counters()
    bytes_sent2 = net_io2.bytes_sent
    bytes_recv2 = net_io2.bytes_recv
    
    sent_speed = (bytes_sent2 - bytes_sent1) / 1024  # Convert to KB/s
    recv_speed = (bytes_recv2 - bytes_recv1) / 1024  # Convert to KB/s
    
    return f"Sent: {sent_speed:.2f} KB/s | Received: {recv_speed:.2f} KB/s"