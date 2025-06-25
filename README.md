🛠️ AWS Log Analysis Pipeline (S3 → Lambda → DynamoDB)
A basic serverless log processing pipeline that ingests raw log files from S3, parses them using AWS Lambda (Python), and stores structured entries in DynamoDB.

📌 Features
Upload log files to Amazon S3

Trigger AWS Lambda function on file upload

Parse log lines (e.g., Apache access logs)

Save structured data to DynamoDB

Fully serverless, scalable, and cost-effective

🧱 Architecture
scss
Copy
Edit
S3 (log file)
   ↓ (trigger)
AWS Lambda (Python parser)
   ↓
DynamoDB (structured logs)

📁 Example Log Format
swift
Copy
Edit
23.30.147.145 - - [20/May/2015:16:05:50 +0000] "GET /index.html HTTP/1.1" 200 22956 "-" "Mozilla/5.0 Chrome/32.0"
📜 Lambda Python Code (snippet)
python
Copy
Edit
match = log_pattern.match(line)
if match:
    table.put_item(Item={
        'log_id': str(uuid.uuid4()),
        'ip': match.group('ip'),
        'timestamp': match.group('timestamp'),
        'method': match.group('method'),
        'path': match.group('path'),
        'status': match.group('status'),
        'user_agent': match.group('user_agent')
    })

    
🔧 AWS Services Used
Amazon S3 – stores raw logs

AWS Lambda – processes logs using Python

Amazon DynamoDB – stores structured data

IAM – manages access securely

📈 What I Learned
Event-driven pipelines using S3 triggers

Python-based log parsing with regular expressions

DynamoDB schema design for fast querying

Hands-on experience with serverless AWS services

