# Cyber Security Data System

## Description

The system collects cyber-security data from different sources

## Requirements

1. Python 3.9.X
2. MongoDB - [Installation guide](https://docs.mongodb.com/manual/administration/install-community/)

## How to run

1. In the project directory, run: `./install.sh`
2. In terminal run `./run.sh`
3. Check today's logs at: `/logs`

## Routes

1. Health Check - ```GET http://127.0.0.1:5000/health-check```
2. CyberSecurityData - ```POST http://127.0.0.1:5000/cyber-security-data/<source:string>```
3. CyberSecurityData - ```GET http://127.0.0.1:5000/cyber-security-data/<source:string>```

## Examples

API examples for CURL (run in terminal)

Health Check - ```curl 'http://127.0.0.1:5000/health-check'```

CyberSecurityData - Print all cyber-security data from 'antivirus' source ```curl --location --request GET 'http://127.0.0.1:5000/cyber-security-data/antivirus'```

CyberSecurityData - Insert cyber-security data from 'antivirus' source
```
curl --location --request POST 'http://127.0.0.1:5000/cyber-security-data/antivirus' \
   --header 'Accept: application/json' \
   --header 'Content-Type: application/json' \
   --data-raw '{
       "data": {
           "id": 1234,
           "port": "81",
           "name": "ransomware",
           "datetime": 222
       }
   }'
```
CyberSecurityData - Insert cyber-security data from 'email' source
```
curl --location --request POST 'http://127.0.0.1:5000/cyber-security-data/email' \
   --header 'Accept: application/json' \
   --header 'Content-Type: application/json' \
   --data-raw '{
    "data": {
        "events": [
            {
                "key": "port",
                "value": 11,
                "ext_name": "phishing",
                "id": 1235
            },
            {
                "key": "noise",
                "value": "love",
                "timestamp": 111,
                "ext_name": "phishing",
                "id": 1236
            }
        ]
    }
   }'
```