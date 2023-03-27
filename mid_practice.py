import pymysql


def print_row(result):
    for re in result:
        print(re)
    print()


def connect():
    conn = pymysql.Connect(host="localhost", user="root", password="root", database="mid_practice", port=3305)
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
    exam_sql = "create table customer(ct_id varchar(20) not null primary key, ct_name varchar(20) not null, age int, ranking varchar(20) not null," \
               " job varchar(20), point int default 0)"
    exam_sql2 = "create table product(pd_number char(3) not null primary key, pd_name varchar(20), quantity int, price int, company varchar(20)," \
                "check (quantity >=0 and quantity <= 10000))"
    exam_sql3 = "create table my_order(order_number char(3) not null primary key, order_ct varchar(20), " \
                " order_pd char(3), quantity int, destination varchar(20)," \
                " order_dt date, foreign key (order_ct) references customer (ct_id),foreign key (order_pd) references product (pd_number))"
    exam_sql4 = "drop table my_order"
    exam_sql5 = "insert into my_order values('o10', 'carrot', 'p03', 20, '경기도 안양시','2022-05-22')"
    exam_sql6 = "delete from product where pd_number= 'p01'"
    exam_sql7 = "select * from my_order"
    exam_sql8 = "drop table my_order"


    exam_sql9 = "select count(CASE WHEN order_ct = 'apple' or quantity >=15 then 1 end) from my_order"

    exam_sql10 = "select ct_id, ct_name, ranking from customer where Length(ct_id) >= 5"
    exam_sql11 = "select ct_id, ct_name, ranking from customer where ct_id like '_____%'"
    exam_sql12 = "select ct_name from customer where age is not null"
    exam_sql13 = "select ct_name, ranking, age from customer order by  age desc"
    exam_sql14 = "select company, count(*) as '제품수', max(price) as '최고가' from product group by company"
    exam_sql15 = "update product set company = '민국푸드' where pd_name = '매운쫄면'"
    exam_sql16 = "select order_pd, order_ct, sum(quantity) as '총주문수량' from my_order group by order_pd, order_ct"
    exam_sql17 = "select product.pd_name from product, my_order where my_order.order_ct = 'banana' and product.pd_number = my_order.order_pd"
    exam_sql18 = "select product.pd_name from product, customer, my_order where ct_name = '고명석' and customer.ct_id = my_order.order_ct and product.pd_number = my_order.order_pd"

    exam_sql19 = "select product.pd_name from product, my_order where my_order.order_ct = 'banana' and product.pd_number = my_order.order_pd"

    exam_sql20 = "select product.pd_name from product, customer, my_order where ct_name = '고명석' and customer.ct_id = my_order.order_ct and my_order.order_pd = product.pd_number"

    exam_sql21 = "select product.pd_name from product, customer, my_order where ct_id = '고명석' and customer.ct_id = my_order.order_ct and product.pd_number = my_order.order_pd"

    exam_sql22 = "select product.pd_name from product, customer, my_order where customer.ct_id = my_order.order_ct = 'banana' and my_order.order_pd = product.pd_number"

    exam_sql23 = "select product.pd_name from product,customer, my_order where customer.ct_name = '고명석' and customer.ct_id = my_order.order_ct and" \
                 "my_order.order_pd = product.pd_number "

    exam_sql24 = "create table my_order(" \
                 "order_number char(3) not null primary key," \
                 "order_ct varchar(20)," \
                 "order_pd char(3)," \
                 "quantity int," \
                 "destination varchar(20)," \
                 "order_dt date," \
                 "foreign key(order_ct) references customer (ct_id)," \
                 "foreign key(order_pd) references product (pd_number))"




    create_Table(exam_sql24)

exam1()
