import psycopg2 
def table():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")

    cursor=conn.cursor()
    cursor.execute('''create table employee(Name Text,Id Int,Age Int);''')
    print('Table created successfully')
    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")

    cursor=conn.cursor()
    name=input('Enter name:')
    id=input('Enter id:')
    age=input('Enter age:')
    query='''insert into employee(Name,Id,Age) values(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    # cursor.execute('''insert into employee(Name,Id,Age) values('Ravi',01,25);''')
    print('Data added successfully')
    conn.commit()
    conn.close()
data()