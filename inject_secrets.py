from decouple import config
import base64
from pathlib import Path

base64_content= config('SECRET_JSON_BASE64')

if not base64_content:
    raise ValueError('SECRET_JSON_BASE64 is missing')

json_content= base64.b64decode(base64_content).decode('utf-8')

file_path= Path(__file__).parent / 'keys.json'
with open(file_path, 'w') as f:
    f.write(json_content)

print(f'File written to {file_path} successfully!')