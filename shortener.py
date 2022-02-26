# 2 ячейки в бд, 1 с оригинальной ссылкой, вторая с рандомно сгенерируемой уникальной рандомной ссылкой, обращаемся к бд
import psycopg2
from psycopg2 import Error
from random import choice
from string import ascii_letters, digits
from urllib.parse import urlparse

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="worldstap2020",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="short")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    user_input_link = input('Введите ссылку: ')
   
    parsed_link = urlparse(user_input_link)
    
    #while  parsed_link.scheme != "http" or "https":
    #    user_input_link = input('Введите ссылку: ')
    #    parsed_link = urlparse(user_input_link)
    #    print('Вы ввели неправильную строку')
        
    
    random_text = ''.join(choice(ascii_letters + digits) for i in range(10))
    #print(short_link)
    short_link = parsed_link.scheme+"://" + parsed_link.netloc+"/" + random_text
    sql = "INSERT INTO link (long_link, short_link) VALUES (%s, %s)"

    cursor.execute(sql, (user_input_link, short_link)) 
    connection.commit()
    print("Короткая ссылка:",short_link) 


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
