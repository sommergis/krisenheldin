from os import environ

host        = environ["POSTGRES_HOST"]
database    = environ["POSTGRES_DB"]
user        = environ["POSTGRES_USER"]
password    = environ["POSTGRES_PASSWORD"]
port        = environ["POSTGRES_PORT"]

DATABASE_CONNECTION_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'