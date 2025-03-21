from flask import Flask, jsonify
from resource_monitor import get_cpu_usage, get_memory_usage, get_disk_usage

app = Flask(__name__)

@app.route('/cpu')
def cpu():
    return jsonify(cpu=get_cpu_usage())

@app.route('/memory')
def memory():
    return jsonify(memory=get_memory_usage())

@app.route('/disk')
def disk():
    return jsonify(disk=get_disk_usage())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
