import mysql.connector
from app.db.config import Config

class PackageService:
    def __init__(self):
        self.db_config=Config.DB_CONFIG

    def fetch_details(self,order_id:str):
        try:
            connection=mysql.connector.connect(**self.db_config)
            cursor=connection.cursor(dictionary=True)

            query="""select * from package_service where order_id=%s"""
            cursor.execute(query,(order_id,))
            result=cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise Exception(f"Dabase Connection error : {str(e)}")
        finally:
            cursor.close()
            connection.close()