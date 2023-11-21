#Asynchronous  database operation

#bt this is synchronous database operation understand this first as a beginner then asynchronous database operation/connections become easy to understand 


# import psycopg2 this library is use for syncronous programming not for async

import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'shivam'
username = 'postgres'
pswrd = '' ##yaha apka pswrd daliyeeeeeeeeeeeeeeeeeeeeeeeeeeeee
port_id = '5432'
con = None
cur = None
try:
    con = psycopg2.connect(

        host = hostname,
        dbname = database,
        user = username,
        password = pswrd,
        port = port_id
    )

    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor) #with the help of this it will gic=ve the data in the type of dict

    cur.execute('drop table  if exists employee')


    create_table = '''CREATE TABLE if not exists employee(
                    id    int primary key,
                    name  varchar(50) not null,
                    salary int,
                    phone_no varchar (15) not null 
    )'''
    
    cur.execute(create_table)

    insert = 'insert into employee(id , name ,salary , phone_no) values(%s , %s , %s ,%s)'
    insert_values = [(1, 'shivam', 50000, '123456789'),
                     (2, 'rohit', 50000, '123456789'), 
                     (3, 'harsh', 50000, '123456789'), 
                     (4, 'kiran', 50000, '123456789')]
    

    for values in insert_values:
        cur.execute(insert, values)

    update_table = 'update employee set salary = salary +(salary * 0.5)'
    cur.execute(update_table)

#     shivam 75000  this is the output
# rohit 75000
# harsh 75000
# kiran 75000


    delete_query = "DELETE FROM employee WHERE name = %s"
    delete_value = ('kiran',)

    cur.execute(delete_query, delete_value)
# shivam 75000
# rohit 75000
# harsh 75000

    cur.execute('select * from employee')
    for values in cur.fetchall():
        print(values['name'],values['salary'])





    










    con.commit()


except Exception as error:
    print(error)
finally: 
    if cur is not None:
      cur.close()
    if con is not None:
       con.close()