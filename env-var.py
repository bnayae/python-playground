# https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
# https://www.programiz.com/python-programming/string-interpolation

import os

env = os.getenv('OPEN_AI_API')
print(f'OPEN.AI API = {env}')