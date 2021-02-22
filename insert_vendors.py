import psycopg2
from config import config



def insert_cliente(nome_cliente):
    """ Insere um cliente na tabela cliente """
    sql = """INSERT INTO cliente(
                            nome_cliente, cpf, endereco_cliente, telefone
                                )
             VALUES(%s, %s, %s, %s) RETURNING id_cliente;"""
    conn = None
    id_cliente = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (nome_cliente))
        # get the generated id back
        id_cliente = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id_cliente


if __name__ == '__main__':
    # insert one cliente
    insert_cliente(["Danilo", "297987465412", "dasldhaaslk", "5656887354"])