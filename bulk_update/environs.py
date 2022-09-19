import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Environ:
    DATA_DB_HOST = os.environ.get('DATA_DB_HOST')
    DATA_DB_USER = os.environ.get('DATA_DB_USER')
    DATA_DB_PW = os.environ.get('DATA_DB_PASS')
    DATA_DB_NAME = os.environ.get('DATA_DB_NAME')

    T3_DB_HOST = os.environ.get('T3_DB_HOST')
    T3_DB_USER = os.environ.get('T3_DB_USER')
    T3_DB_PW = os.environ.get('T3_DB_PASS')
    T3_DB_NAME = os.environ.get('T3_DB_NAME')



if __name__ == '__main__':
    env = os.environ
    for k,v in env.items():
        print(f"{k} : {v}")