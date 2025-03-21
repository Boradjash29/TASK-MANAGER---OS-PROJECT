import psutil

def list_processes(sorted_key=None):
    """Returns a list of running processes with relevant info."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except psutil.NoSuchProcess:
            pass
    if sorted_key:
        processes = sorted(processes, key=lambda x: x.get(sorted_key, 0), reverse=True)
    return processes

def kill_process(pid):
    """Kills the process with the given PID."""
    try:
        proc = psutil.Process(pid)
        proc.terminate()  # Sends SIGTERM to gracefully terminate
        proc.wait(timeout=3)  # Wait for process to terminate
        return f"Process {pid} killed successfully."
    except psutil.NoSuchProcess:
        return f"No process found with PID {pid}."
    except psutil.AccessDenied:
        return f"Access denied to kill process {pid}."
    except Exception as e:
        return f"Error killing process {pid}: {str(e)}"
