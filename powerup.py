import pymysql


def print_row(result):
    for re in result:
        print(re)
    print()


def connect():
    conn = pymysql.Connect(host="localhost", user="root", password="root", database="powerup", port = 3305)
    return conn.cursor(), conn


cursor, conn = connect()


def create_Table(sql):
    global cursor
    cursor.execute(sql)


def insert_Data(sql):
    global conn, cursor
    cursor.execute(sql)
    print("Insert Data Complete.")
    conn.commit()


def select_Data(sql):
    global conn, cursor
    cursor.execute(sql)
    result_data = cursor.fetchall()
    print_row(result_data)


def describe_Table(sql):
    global conn, cursor
    cursor.execute(sql)
    result = cursor.fetchall()
    print_row(result)


def delete_Data(sql):
    global conn, cursor
    cursor.execute(sql)
    print("Delete Data Complete.")
    conn.commit()


def exam1():

    create_sql = "create table customer(ct_id varchar(20) not null primary key, ct_name varchar(10) not null, age int, ranking varchar(10) not null, job varchar(20), point int default 0)"

    create_sql = "create table product(pd_number char(30) not null primary key, pd_name varchar(20), quantity int, price int, company varchar(20), check(quantity >= 0 and quantity <= 10000))"

    create_sql = "create table my_order(od_number char(3) not null primary key, od_customer varchar(20)," \
                 "od_product char(3), quantity int, destination varchar(30), od_date date," \
                 "foreign key (od_customer) references customer (ct_id), foreign key (od_product) references product (pd_number))"

    insert_sql = "insert into product values('p04','맛난초콜릿',1250,2500,'한빛제과')"

    delete_sql = "delete from product where pd_number = '쿵떡파이'"

    insert_Data(insert_sql)


exam1()