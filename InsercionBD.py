import pymysql as pymysql


connection = pymysql.connect(host='90.164.253.234', port=3304, user='administrador', password='password',
                             db='bd_relacional')
cursor = connection.cursor()


def insertarRestaurante(restaurante1, restaurante2, distancia):
    try:
        sql = "INSERT INTO `similitudrestaurantes` (`restaurante1`, `restaurante2`, `similitud`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (restaurante1, restaurante2, distancia))
        connection.commit()

    except Exception as exc:
        print(exc)


def cerrarConexion():
    connection.close()