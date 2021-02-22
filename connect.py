import psycopg2
from config import config

def connect():
    """ Conecta ao banco de dados PostgreSQL"""
    conn = None
    try:
        #leia os parametros de conexão
        params = config()
        #conecta ao servidor PostgreSQL
        print("Conectando ao banco de dados PostgreSQL...")
        conn = psycopg2.connect(**params)
        #cria um cursor
        cur = conn.cursor()
        #executa uma sentença SQL
        print("Versão do banco de dados do PostgreSQL:")
        cur.execute('Select version()')
        #Mostra a versão do PostgreSQL
        db_version = cur.fetchone()
        print(db_version)
        #fecha a comunicação com o PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()