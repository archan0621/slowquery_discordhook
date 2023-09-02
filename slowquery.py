import os
import requests
import time

log_file_path = '/var/log/slowlog/mysql-slow.log'
last_position = 0

while True:
    try:
        with open(log_file_path, 'r') as file:
            file.seek(last_position)
            new_data = file.read()

            if new_data:
                url = ''
                data = {
                    "embeds": [{
                        "title": "🚨경고🚨 슬로우 쿼리 발생",
                        "description": new_data
                    }]
                }

                try:
                    response = requests.post(url, json=data)
                    print(f'Sent HTTP request: {response.status_code}')
                except Exception as e:
                    print(f'Failed to send HTTP request: {e}')

            last_position = file.tell()

        time.sleep(1)  
    except Exception as e:
        print(f'Error reading the log file: {e}')