import os

def print_log(message):
    print(os.environ.get('MY_VAR'))
    print(f'The log added after github  {message}')
