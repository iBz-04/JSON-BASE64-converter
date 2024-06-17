import base64
import json

json_content = {#JSON goes here}

json_str = json.dumps(json_content)

base64_encoded = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

print(base64_encoded)