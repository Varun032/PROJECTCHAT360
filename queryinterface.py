from flask import Flask, request, jsonify

app = Flask(__name__)

# API integration
from logingestor import API1, API2

api1 = API1()
api2 = API2()

# Define a route for logging messages via API1
@app.route('/log_api1', methods=['POST'])
def log_api1():
    data = request.json
    level = data['level']
    message = data['message']
    api1.log_message(level, message)
    return jsonify({'status': 'success'})

# Define a route for logging messages via API2
@app.route('/log_api2', methods=['POST'])
def log_api2():
    data = request.json
    level = data['level']
    message = data['message']
    api2.log_message(level, message)
    return jsonify({'status': 'success'})

# Define a route for searching logs
@app.route('/search_logs', methods=['GET'])
def search_logs():
    level = request.args.get('level')
    log_string = request.args.get('log_string')
    timestamp = request.args.get('timestamp')
    source = request.args.get('source')

    # Perform search based on filters
    # Dummy response for demonstration
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
