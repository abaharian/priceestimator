import mysql.connector

print('Enter database connection attribs: (for using default just press Enter)')
username = input('username: ')
if len(username) < 2:
    username = 'default'
password = input('password: ')
if len(password ) < 2:
    password = '123456'
hostip = input('host name or IP: ')
if len(hostip) < 2:
    hostip = '127.0.0.1'
db = input("database name: ")
if len(db) < 2:
    db = 'accomodation'

query = "create table sitedata(id integer, type varchar(20), \
    person_no integer, bath_no integer, location varchar(50), \
        city_name varchar(20), monthly_price integer, \
            auth_plugin='mysql_native_password');"
try:
    con = mysql.connector.connect(user=username, password=password, host=hostip, database=db)
    cursor = con.cursor
    cursor.execute(query)
    print('Database created successfuly')
except Exception as ex:
    print("Problem in creating database: ")
    print('\t', ex)
