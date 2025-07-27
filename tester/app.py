import base64
import json
import os
import time
import re
from io import BytesIO

import requests
from PIL import Image

from levenshtein_distance import levenshtein_distance

url = 'http://127.0.0.1:8000'
res = []

attempts_count = 0
while res != 200:
    res = None
    try:
        response = requests.get(url + '/ping', headers={'Content-Type': 'application/json'})
        res = response.status_code
    except:
        pass
    attempts_count += 1
    time.sleep(0.5)
    if attempts_count > 30:
        print('cant ping :(')
        exit(1)

encoder_url = url
decoder_url = url

folder_path = 'tests'
tests_count = 0
pattern = re.compile(r'^test\d+\.txt$') 
if os.path.exists(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if pattern.match(file_name):
                tests_count += 1
    
for i in range(1, tests_count + 1):
    print(f'test: {i}')
    text = open(f'tests/test{i}.txt', encoding='utf-8').read()
    module = __import__(f'tests.test{i}', fromlist=['f'])
    f = module.f

    try:
        data = requests.post(encoder_url + '/encode', data=json.dumps(dict(text=text)), headers={'Content-Type': 'application/json'})    
        image_bytes = base64.b64decode(data.json()['data'])
        image = Image.open(BytesIO(image_bytes))
        file_size = len(image_bytes)
    
        image = f(image)
        buffer = BytesIO()
        image.save(buffer, format='PNG')
        buffer.seek(0)
    
        new_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    
        data = requests.post(decoder_url + '/decode', data=json.dumps(dict(data=new_base64)), headers={'Content-Type': 'application/json'})    
        encoded_text = data.json()['text']
        print(f'dif: {levenshtein_distance(text, encoded_text)}, file_size: {file_size}')
    except Exception as e:
        print(f'error: {e}')
        print(f'dif: inf, file_size: inf')
