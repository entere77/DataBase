import pymysql


def print_row(result):
    for re in result:
        print(re)
    print()


def connect():
    conn = pymysql.Connect(host="localhost", user="root", password="root", database="kjh", port=3305)
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
    # exam_sql = "create table student(st_id varchar(20) primary key, st_name varchar(20), st_age int);"
    # exam_sql = "drop table stuedent;"
    # exam_sql = "create table sugang(sugang_no int primary key, sugang_st varchar(20), foreign key(sugang_st) references student(st_id));"
    # exam_sql = "select sum(pd_quantity) as '재고량 합계' from product where pd_com = '한빛제과';"
    # exam_sql = "select ct_id, ct_name, ranking from customer;"
    # exam_sql = "select distinct pd_com from product;"
    # exam_sql = "select pd_name, price As '가격' from product;"
    # exam_sql = "select pd_name, price+500 As '조정 단가' from product;"
    # exam_sql = "select pd_name, pd_quantity, price from product where pd_com = '한빛제과';"
    # exam_sql = "select order_product, quantity_product, order_date from my_order where order_customer='apple' && quantity_product >=15;"
    # exam_sql = "select order_product, quantity_product, order_date, order_customer from my_order where order_customer = 'apple' or quantity_product >= 15;"
    # exam_sql = "select pd_name, price, pd_com from product where 2000 <= price && price <= 3000;"
    # exam_sql = "select ct_id, ct_name, ranking from customer where ct_id like '_____';"
    # exam_sql = "select ct_name from customer where age is not null;"
    # exam_sql = "select ct_name, ranking, age from customer order by age asc;"
    # exam_sql = "select avg(price) from product "
    # exam_sql = "select sum(pd_quantity) As '재고량 합계' from product where pd_com = '한빛제과';"
    # exam_sql = "select count(ct_id) from customer;"
    # exam_sql = "select count(age) from customer;"
    # exam_sql = "select count(*) As '고객수' from customer;"
    # exam_sql = "select order_product, sum(quantity_product) from my_order group by(order_product);"
    # exam_sql = "select pd_com, count(*) As '제품수', max(price) As '최고가' from product group by(pd_com);"
    # exam_sql = "select order_product, order_customer, sum(quantity_product) As '총주문수량' from my_order group by order_product, order_customer;"
    # exam_sql = "select order_product, order_customer, sum(quantity_product) As '총주문수량' from my_order group by order_product, order_customer"
    # exam_sql = "select order_product, pd_name from my_order, product where my_order.order_customer='banana' && product.pd_number = my_order.order_product;"
    exam_sql1 = "select product.pd_name from my_order, product where my_order.order_customer = 'banana' && my_order.order_product = product.pd_number;"
    exam_sql = "select pd_name, order_product from product, my_order, customer where customer.ct_name = '고명석' && " \
               "customer.ct_id = my_order.order_customer && my_order.order_product = product.pd_number;"


# 쿼리 집합들 두번째 실습
#     select
#     my_order.order_product, my_order.order_date
#     from customer inner
#     join
#     my_order
#     on
#     my_order.order_customer = customer.ct_id
#     where
#     customer.age;



    select_Data(exam_sql1)


exam1()
