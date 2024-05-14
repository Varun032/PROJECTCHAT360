from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for searching logs
@app.route('/search_logs', methods=['GET'])
def search_logs():
    level = request.args.get('level')
    log_string = request.args.get('log_string')
    timestamp = request.args.get('timestamp')
    source = request.args.get('source')

    # Perform search based on filters
    # Here you would search through the log files and return matching logs
    # This is just a dummy response for demonstration
    logs = [
        {"level": "error", "log_string": "Failed to connect", "timestamp": "2023-09-15T08:00:00Z", "source": "log1.log"},
        {"level": "info", "log_string": "Connection established", "timestamp": "2023-09-16T08:00:00Z", "source": "log2.log"}
    ]

    filtered_logs = []
    for log in logs:
        if (not level or log['level'] == level) and \
           (not log_string or log['log_string'] == log_string) and \
           (not timestamp or log['timestamp'] == timestamp) and \
           (not source or log['source'] == source):
            filtered_logs.append(log)

    return jsonify(filtered_logs)

if __name__ == '__main__':
    app.run(debug=True)
