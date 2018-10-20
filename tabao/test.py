from urllib.parse import quote

import requests
requests.get().text
key = quote('女装 裙',safe='').replace('%20','+')
print(key)