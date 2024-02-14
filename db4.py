import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
                  DROP TABLE clients, phone_number
              """)
        cur.execute("""
                  CREATE TABLE IF NOT EXISTS clients ( 
                  id SERIAL PRIMARY KEY,
                  first_name VARCHAR(40) NOT NULL, 
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
def search(conn, first_name, last_name):     # вспомогательная функция, возвращает id по Имени и Фамилии клиента
    with conn.cursor() as cur:
        cur.execute("""
                  SELECT id FROM clients
                  WHERE first_name = %s AND last_name = %s;
                  """, (first_name, last_name))
        return cur.fetchone()
def add_phone(conn, client_id, phones):                         # добавляет телфон по клиенту
    with conn.cursor() as cur:
        cur.execute("""
                  INSERT INTO phone_number (client_id, number)
                  VALUES (%s,%s);
                  """, (client_id, phones))
def add_client(conn, first_name, last_name, email, phones=None):    # добавляет нового клиента
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO clients (first_name, last_name, email)
            VALUES (%s,%s,%s);
            """, (first_name, last_name, email))
        if phones !=None:
            client_id = search(conn, first_name, last_name)
            add_phone(conn, client_id, phones)
def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):  # меняем данные
    data = {'first_name': first_name, 'last_name': last_name, 'email': email}
    with conn.cursor() as cur:
        for key, arg in data.items():
            if arg != None:
                cur.execute("""
                    UPDATE clients SET {}=%s WHERE id=%s""".format(key), (arg, client_id))
        if phones != None:
            cur.execute("""
                    UPDATE phone_number SET number=%s
                    WHERE client_id=%s;
                    """, (phones, client_id))

def delete_phone(conn, client_id, phones):           # удаляет телефон (конкретный)
    with conn.cursor() as cur:
        cur.execute("""
                DELETE FROM phone_number WHERE client_id=%s AND number=%s
                """, (client_id, str(phones)))
        conn.commit()
def delete_client(conn, client_id):              # удаляет клиента (вместе с телефоном)
    with conn.cursor() as cur:
        cur.execute("""
                DELETE FROM phone_number WHERE client_id=%s
                """, (str(client_id)))
        conn.commit()
        cur.execute("""
                DELETE FROM clients WHERE id=%s
                """,(str(client_id)))
        conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phones=None):                # поиск клиента
    data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phones}
    with conn.cursor() as cur:
        cur.execute(f"""
                SELECT * FROM clients c
                JOIN phone_number p ON c.id = p.client_id
                WHERE (first_name=%(first_name)s IS NULL OR first_name=%(first_name)s) 
                AND (last_name=%(last_name)s IS NULL OR last_name=%(last_name)s)
                """, data)
        print(cur.fetchone())


client1 = ('Ivan', 'Nicolaev', 'Ivan123@mail.ru')
client2 = ('Konstantin', 'Sidorov', 'ks@mail.ru')
client3 = ('Roman', 'Kochalov', 'ksfff@mail.ru')

with psycopg2.connect(database='netology_db', user='postgres', password='admin') as conn:
     create_db(conn)
     add_client(conn,'Ivan', 'Nicolaev', 'Ivan123@mail.ru', 456456)
     add_client(conn, 'Konstantin', 'Sidorov', 'ks@mail.ru', 988776)
     change_client(conn, 1,None, None, 'ivan@mail.ru', 77777)
#     delete_phone(conn, 1, 77777)
#     delete_client(conn, 1)
     find_client(conn, 'Ivan', None)

     change_client(conn, 1, None, 'Nic')
     find_client(conn, 'Ivan', None)

conn.close()
