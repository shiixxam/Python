 #Asynchronous  database operation


import asyncio
import asyncpg

async def connect_to_database():
    connection = await asyncpg.connect(
        host='localhost',
        database='shivam',
        user='postgres',
        password='',    #yaha apka pswrd daliyeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        port=5432
    )
    return connection

async def create_table(connection):
    # Example query to create a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    )
    """
    await connection.execute(create_table_query)

async def insert_data(connection):
    insert_data_query = """
    INSERT INTO users (username, email) VALUES ($1, $2)
    """
    await connection.execute(insert_data_query, 'shivam', 'shivam@gmail.com')

async def fetch_data(connection):
    fetch_data_query = """
    SELECT * FROM users
    """
    result = await connection.fetch(fetch_data_query)
    print("Fetched data from the database:")
    for row in result:
        print(row)

async def main():
    try:
        connection = await connect_to_database()

        await create_table(connection)

        await insert_data(connection)

        await fetch_data(connection)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        await connection.close()

asyncio.run(main())
