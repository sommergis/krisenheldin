from os import environ

# these envs are not set in Google Cloud Run but only local
try:
    host                = environ["POSTGRES_HOST"]
    port                = environ["POSTGRES_PORT"]
except:
    pass

database                = environ["POSTGRES_DB"]
user                    = environ["POSTGRES_USER"]
password                = environ["POSTGRES_PASSWORD"]

try:
    cloud_sql_instance_name = environ["CLOUD_SQL_CONNECTION_NAME"]
    # cloud sql
    DATABASE_CONNECTION_URI = f"postgres+pg8000://{user}:{password}@/{database}?unix_sock=/cloudsql/{cloud_sql_instance_name}/.s.PGSQL.5432"
except:
    # local
    DATABASE_CONNECTION_URI = f"postgresql://{user}:{password}@{host}:{port}/{database}"