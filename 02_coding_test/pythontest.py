import boto3
import time
import datetime
import os


date = time.strftime('%Y%m%d-%H%M%S')
backuppath = "./dbbackup" + date + "/"
bucket ="bucketname" 

try:
    backupfolder = os.mkdir(backuppath)
except: print("folder exists")

host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
db = os.getenv('MYSQL_DATABASE')

backup = backuppath + db

arg1 = """mysqldump -h 34.89.77.57 -u %s -p  %s > %s.sql""" % (user, db, backup)

os.system(arg1)

arg2 = """zip -r %s.zip %s.sql""" % (backup, backup)  

os.system(arg2)

filename = backup + ".zip"

object_name = db + ".zip"
s3 = boto3.resource('s3')

response = s3.meta.client.upload_file(filename, bucket, object_name)

cleanup = """ rm -r %s """ % (backuppath)

os.system(cleanup)
