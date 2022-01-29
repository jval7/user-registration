from time import sleep
import sqlalchemy as sal

if __name__ == "__main__":
    for _ in range(5):
        try:
            engine = sal.create_engine('mysql+pymysql://coink:coink@db:3306/coinktable')
            conn = engine.connect()
            conn.close()
            print('Db tested successfully')
            break
        except:
            print("Mysql is not available. Sleep for 5 sec")
            sleep(5)
