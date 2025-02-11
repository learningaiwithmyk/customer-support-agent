import mysql.connector
from app.db.config import Config

class PolicyInfoService:
    def __init__(self):
        self.db_config = Config.DB_CONFIG

    def fetch_details(self,policy_type:str,policy_product:str):

        try:
            connection=mysql.connector.connect(**self.db_config)
            cursor=connection.cursor(dictionary=True)

            if not policy_product:
                query="""select * from policy_details where type_of_policy=%s"""
                cursor.execute(query,(policy_type,))
                result=cursor.fetchall()
            else:
                query="""select * from policy_details where type_of_policy=%s and policy_product=%s """
                cursor.execute(query,(policy_type,policy_product))
                result=cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise Exception(f"Database Connection error: {str(e)}")
        finally:
            cursor.close()
            connection.close()