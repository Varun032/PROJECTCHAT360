This project implements a Log Management System consisting of a Log Ingestor and a Query Interface. The Log Ingestor integrates multiple APIs to capture logs at different stages, while the Query Interface offers a user-friendly interface for searching logs based on various filters.

Setup Instructions
Clone the repository to your local machine:
Install the required dependencies:
pip install flask

Run the Flask application:
python queryinterface.py

Access the Query Interface at http://localhost:5000 in your web browser.

System Design
The Log Management System consists of two main components:

Log Ingestor:

Integrates multiple APIs to capture logs at different stages.
Each API is represented by a class with methods to log messages at different levels.
Logs are formatted and written to designated log files.
Query Interface:

Provides a user interface (Web UI) for searching logs.
Offers filters based on log level, log string, timestamp, and metadata source.
Utilizes Flask framework for routing and handling HTTP requests.
Features Implemented
Log Ingestor:
API Integration:

Integrates multiple APIs to capture logs at different stages.
Provides classes for each API with methods to log messages.
Log Formatting:

Standardizes the format for logging across all APIs.
Includes fields like timestamp, log level, source, and log message.
Error Handling:

Implements robust error handling to ensure logging failures do not disrupt functionality.
Handles network errors, file I/O errors, etc.
Query Interface:
User Interface:

Provides a user-friendly interface for searching logs.
Offers a web-based interface accessible via a browser.
Search Functionality:

Implements full-text search across logs.
Offers filters based on log level, log string, timestamp, and metadata source.
Potential Improvements
Scalability:

Implement distributed logging for handling high volumes of logs efficiently.
Utilize scalable storage solutions like Elasticsearch for log storage and retrieval.
Advanced Features:

Add support for additional features like search within specific date ranges, regular expression search, combining multiple filters, etc.
Implement real-time log ingestion and searching capabilities.
Security:

Implement authentication and authorization mechanisms to control access to the query interface.
Ensure secure handling of sensitive log data.
Performance Optimization:

Optimize search algorithms and indexing mechanisms for faster search results.
Implement caching mechanisms to improve performance.
Conclusion
The Log Management System provides a robust solution for capturing, storing, and searching logs efficiently. By following the setup instructions and exploring the system design, users can effectively manage logs and troubleshoot issues with ease.