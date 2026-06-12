import mysql.connector

def get_database_connector():
    
    connection=mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="3TP5MK8AXT6joQv.root",
        password="nEoUZdeVKjona0T7",
        database="student_task_manager",
        port=4000
    )
    return connection
