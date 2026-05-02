import psycopg2
from config import load_config

def get_con():
    return psycopg2.connect(**load_config())



# import sys
# import os

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from config import load_config

# import psycopg2
# from config import load_config

# def get_con(config):
#     try:
#         with psycopg2.connect(**config) as conn:
#             print('Connected to the PostgreSQL server.')
#             return conn
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == '__main__':
#     config = load_config()
#     get_con(config)

