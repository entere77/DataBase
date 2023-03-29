import pymysql


def print_row(result):
    for re in result:
        print(re)
    print()


def connect():
    conn = pymysql.Connect(host="localhost", user="root", password="root", database="pt", port = 3305)
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
    exam_sql = "create table ct(" \
               "ct_id varchar(20) not null primary key, ct_name varchar(20) not null, age int, ranking varchar(10) not null, job varchar(20), point int default 0)"
    exam_sql2 = "create table pd(" \
                "pd_number char(3) not null primary key, pd_name varchar(20), quantity int, price int, company varchar(20), check(quantity >= 0 and quantity <= 10000))"
    exam_sql3 = "create table od(" \
                "od_number char(3) not null primary key, od_ct varchar(20), od_pd char(3), quantity int, destination varchar(30), dt date," \
                "foreign key (od_ct) references ct (ct_id), foreign key (od_pd) references pd (pd_number))"
    exam_sql4 = "desc od"

    insert_sql = "insert into ct values('pear','채광주',31,'silver','회사원',500)"

    delete_sql = "delete from ct where ct_id = 'pear'"

    insert_sql2 = "insert into pd values('p07','달콤비스킷',1650,1500,'한빛제과')"

    insert_sql3 = "insert into od values('o10','carrot','p03',20,'경기도 안양시','2022-05-22')"

    select_sql = "select od_pd, count(od_pd), sum(quantity) as '총주문수량' from od group by od_pd"

    select_sql = "select od_pd, if(count(case when od_ct = 'apple' or quantity >= 15 then 1 end) > 1 , 'Yes', 'No') from od"

    select_sql2 = "select pd.pd_name from pd,od where od.od_ct = 'banana' and od.od_pd = pd.pd_number"

    select_sql3 = "select pd.pd_name from pd,ct,od where ct.ct_name = '고명석' and od.od_pd = pd.pd_number and ct.ct_id = od.od_ct"

    select_sql3 = "select count(case when od_ct = 'apple' or quantity >= 15 then 1 end) from od"

    select_sql3 = "select pd.pd_name from pd,ct,od where ct.ct_name = '고명석' and ct.ct_id = od.od_ct and od.od_pd = pd.pd_number"

    select_sql4 = "desc od"

    sql1 = "select ct.ct_name, od.od_pd, od.dt from ct left outer join od on ct.ct_id = od.od_ct"

    sql2 = "select ct.ct_name, od.od_pd, od.dt from ct left outer join od on od.od_ct = ct.ct_id;"

    sql3 = "select ct.ct_name, od.od_pd, od.dt from ct right outer join od on ct.ct_id = od.od_ct"

    sql4 = "select ct.ct_name, od.od_pd, od.dt from ct right outer join od on od.od_ct = ct.ct_id"


    sql5 = "select ct.ct_name, od.od_pd, od.dt from od left outer join ct on od.od_ct = ct.ct_id"

    sql6 = "select ct.ct_name, od.od_pd, od.dt from od left outer join ct on ct.ct_id = od.od_ct"

    sql7 = "select ct.ct_name, od.od_pd, od.dt from od right outer join ct on ct.ct_id = od.od_ct"

    sql9 = "select pd_name, price from pd where company in (select company from pd where pd_name = '달콤비스킷')"

    sql12 = "select pd_name, company from pd where pd_number in (select od_pd from od where od_ct = 'banana')"

    sql13 = "select pd_name, company from pd where pd_number not in (select od_pd from od where od_ct = 'banana')"

    sql14 = "select pd_name, price, company from pd where price > all(select price from pd where company = '대한식품')"

    sql14_1 = "select ct_name from ct where ct_id in " \
              "(select od_ct from od where od_pd in " \
              "(select pd_number from pd where price > all(select price from pd where company = '대한식품')))"   #중요하니깐 다시 한번 해보기 sql14_1
    # 대한식품이 제조한 모든 제품의 단가보다 비싼 제품을 주문한 사람

    sql16_2 = "select ct_name from ct where not exists (select * from od where dt >= '2022-03-01' and dt <= '2022-03-31' and od.od_ct = ct.ct_id)"

    sql17 = "select pd_number from pd where price > all(select price from pd where company = '대한식품')"

    # create
    # view
    # good_ct(ct_id, ct_name, age, ranking) as select
    # ct_id, ct_name, age, ranking
    # from ct where
    # ranking = 'vip'
    # with check option;

    sql18 = "select ct_name from ct where not exists (select * from od where dt = '2022-03-15' and od.od_ct = ct.ct_id)"

    sql51 = "select ct.ct_name, ct.point from ct where point=(select max(point) from ct)"

    sql52 = "select pd.pd_name, pd.price, pd.company from pd where price > all(select price from pd where company = '대한식품')"

    sql53 = "select ct_name from ct where exists (select * from od where dt = '2022-03-15' and od.od_ct = ct.ct_id)"

    sql4 = "select od.od_pd, od.dt from ct inner join od on ct.ct_id = od.od_ct where ct.age >= 30"

    sql9 = "select pd.pd_name, pd.price from pd where company = (select company from pd where pd_name ='달콤비스킷')"

    sql10 = "select ct.ct_name, ct.point from ct where point = (select max(point) from ct)"

    sql12 = "select pd.pd_name, pd.company from pd where pd.pd_number in (select od_pd from od where od_ct = 'banana')"

    sql13 = "select pd.pd_name, pd.company from pd where pd.pd_number not in (select od_pd from od where od_ct = 'banana')"

    sql14 = "select pd.pd_name, pd.price, pd.company from pd where price > all(select price from pd where company = '대한식품')"

    sql15 = "select ct.ct_name from ct where ct_id in (select od_ct from od where dt = '2022-03-15')"

    sql16 = "select ct.ct_name from ct where ct_id not in (select od_ct from od where dt = '2022-03-15')"

    sql17_1 = "select pd.pd_name, pd.company from pd,od where pd.pd_number = od.od_pd and od.od_ct = 'banana'"

    sql17_2 = "select pd.pd_name, pd.company from pd where exists(select * from od where pd.pd_number = od.od_pd and od.od_ct = 'banana')"

    sql17_3 = "select pd.pd_name, pd.company from pd where pd_number in (select od_pd from od where od_ct = 'banana')"

    sql = "select pd_name from pd where pd_number in (select od_pd from od where od_ct = 'banana')"

    sql = "select ct_name from ct where ct_id in " \
          "(select od_ct from od where od_pd in " \
          "(select pd_number from pd where price > all(select price from pd where company = '대한식품')))"

    sql = "select pd.pd_name, pd.company from pd,od where od.od_ct = 'banana' and od.od_pd = pd.pd_number" # 조인 질의를 이용

    sql = "select pd.pd_name, pd.company from pd where exists(select * from od where od_ct = 'banana' and od.od_pd = pd.pd_number)" # exist 연산자를 이용

    sql = "select pd.pd_name, pd.company from pd where pd_number in (select od_pd from od where od_ct = 'banana')"

    sql = "select od.od_pd, od.dt from od inner join ct on ct.ct_id = od.od_ct where ct.age >= 30"

    select_Data(sql)

exam1()
