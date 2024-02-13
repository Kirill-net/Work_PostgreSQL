import psycopg2

conn = psycopg2.connect(database='netology_db', user='postgres', password='admin')
cur = conn.cursor()
def get_create_table(cursor):                       # создаем таблицы
    cur.execute("""
        DROP TABLE clients, phone_number
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clients ( 
        id SERIAL PRIMARY KEY,
        fist_name VARCHAR(40) NOT NULL, 
        last_name VARCHAR(40) NOT NULL, 
        email VARCHAR(40) UNIQUE NOT NULL 
        );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phone_number (
        id SERIAL PRIMARY KEY,
        number VARCHAR(10) UNIQUE NULL,
        client_id integer NOT NULL REFERENCES clients(id)
        );
    """)
    conn.commit()
def search(cursor, cl_name):                  # вспомогательная функция, возвращает id по Имени и Фамилии клиента
    cur.execute("""
        SELECT id FROM clients
        WHERE fist_name = %s AND last_name = %s;
    """, (cl_name[0], cl_name[1]))
    return cur.fetchone()
def search_cl(cursor, cl_data):               # поиск клиента по имени, фамилии, адресу или телефону
    cur.execute("""
        SELECT * FROM clients c
        JOIN phone_number p ON c.id = p.client_id
        WHERE fist_name=%s OR last_name=%s OR email=%s OR number=%s;
    """, (cl_data, cl_data, cl_data, cl_data)
    )
    cl = cur.fetchall()
    print(cl)
def add_new_client(cursor, client):           # добавляет нового клиента
    cur.execute("""
        INSERT INTO clients (fist_name, last_name, email)
        VALUES (%s,%s,%s);
        """, client
        )
    conn.commit()
def add_new_number_ph(cursor, cl_phone):      # добавляет телфон по клиенту
    cur.execute("""
        INSERT INTO phone_number (number, client_id)
        VALUES (%s,%s);
        """,(cl_phone[2], search(cursor, cl_phone))
        )
    conn.commit()
def update_client(cursor, cl_name, change):    # вносит изменения в данные клиента
    cur.execute("""
         UPDATE clients SET fist_name=%s, last_name=%s, email=%s
         WHERE fist_name=%s AND last_name=%s;
         """, (change[0], change[1], change[2], cl_name[0], cl_name[1])
    )
    conn.commit()
def delete_phone(cursor, client):        # удаляет телефон
    cur.execute("""
        DELETE FROM phone_number WHERE client_id=%s
        """,(search(cursor, client))
        )
    conn.commit()
def delete_client(cursor, client):      # удаляет клиента
    delete_phone(cursor, client)
    cur.execute("""
        DELETE FROM clients WHERE id=%s
        """,(search(cursor, client))
        )
    conn.commit()
                                                   # данные для передачи в функции
client1 = ('Ivan', 'Nicolaev', 'Ivan123@mail.ru')
client2 = ('Konstantin', 'Sidorov', 'ks@mail.ru')
client3 = ('Roman', 'Kochalov', 'ks@mail.ru')
cl_phone = ('Ivan', 'Nicolaev', '1234567')
cl_phone2 = ('Konstantin', 'Sidorov', '2345434')
cl_phone3 = ('Konstantin', 'Sidorov', '2345777')
change = ('Konstantin', 'Sidorov', 'k88787@mail.ru')

                                                # пробуем работу функций
get_create_table(cur)

add_new_client(cur, client1)
add_new_number_ph(cur, cl_phone)

add_new_client(cur, client2)
add_new_number_ph(cur, cl_phone2)
add_new_number_ph(cur, cl_phone3)

update_client(cur, client2, change)

search_cl(cur, '1234567')

delete_phone(cur, client1)
delete_client(cur, client1)



cur.close()
conn.close()
