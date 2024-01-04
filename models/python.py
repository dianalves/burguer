import pymysql

# vamos conectar com o banco / servidor com as credenciais

conn = pymysql.connect (
    host= '192.168.0.201',
    user= 'diana',
    database= 'diana',
    password= 'Diana1234',
    cursorclass=pymysql.cursors.DictCursor
)


def execute(sql):
    # vamos abrir a conexão com o servidor
    with conn:
        # aqui a gente abre um cursor que irá executar os comandos SQL
        with conn.cursor() as cursor:
            cursor.execute(sql)
            # vamos ler os resultados
            result = cursor.fetchall()
            return result
        
if __name__ == '__main__':
    print(execute("""select burguer.name, group_concat(ingredient.name) 
from burguer 
join BurguerIngredients on burguer.id = BurguerIngredients.burguer_id
join ingredient on BurguerIngredients.ingredient_id = ingredient.id
group by burguer.name;"""))