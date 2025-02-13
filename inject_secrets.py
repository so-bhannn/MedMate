from dotenv import load_dotenv
import os
import base64
from pathlib import Path
import sys

def inject_secrets():
    try:
        load_dotenv()

        base64_content = os.getenv('SECRET_JSON_BASE64')
        if not base64_content:
            raise ValueError('SECRET_JSON_BASE64 environment variable is not set')

        json_content = base64.b64decode(base64_content).decode('utf-8')

        file_path = Path(__file__).parent / 'keys.json'
        with open(file_path, 'w') as f:
            f.write(json_content)

        print(f'Firebase credentials written to {file_path} successfully!')
        return True

    except Exception as e:
        print(f'Error injecting secrets: {str(e)}', file=sys.stderr)
        return False

if __name__ == '__main__':
    success = inject_secrets()
    if not success:
        sys.exit(1)