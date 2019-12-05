"""
python 3.7

script to create SQL database and deploy
John Armitage 3/12/2019
"""
import os

postgres_user = os.environ['POST_USER'].rstrip()
postgres_pass = os.environ['POST_PASSWORD'].rstrip()
uri = os.environ['URI_POSTGRES'].rstrip()
port = os.environ['POST_PORT'].rstrip()
dbase = os.environ['DBASE'].rstrip()

#DATABASE_URI = 'postgres+psycopg2://postgres:WRMNSXGol1@a8f213870167411ea9df302af6eaa18b-1639397014.eu-west-1.elb.amazonaws.com:5432/John-axel'
DATABASE_URI = 'postgres+psycopg2://{}:{}@{}:{}/{}'.format(postgres_user, postgres_pass, uri, port, dbase)