import pymysql


def execute(sql):
    # vamos conectar com o banco / servidor com as credenciais
    conn = pymysql.connect(
        host= '192.168.0.201',
        database= 'diana',
        user= 'diana',
        password= 'Diana1234',
        cursorclass=pymysql.cursors.DictCursor
    )

    # vamos abrir a conexão com o servidor
    with conn.cursor() as cursor:

        # aqui a gente abre um cursor que irá executar os comandos SQL
        cursor.execute(sql)
        # vamos ler os resultados
        result = cursor.fetchall()
        return result

if __name__ == '__main__':
    print(execute("""select * from burguer"""))
