import mysql.connector

# MySQL 서버에 연결
mydb = mysql.connector.connect(
    host="192.168.148.4",  # MySQL 호스트 이름
    user="seohanbit",    # MySQL 사용자명
    password="gksqlc0627!",  # MySQL 비밀번호
    database="madang",  # 사용할 데이터베이스 이름
    port=4567  # MySQL 포트 번호 (기본값)
)

# MySQL 커서 생성
cursor = mydb.cursor()

# 데이터 검색
sql_select = "SELECT * FROM Book"
cursor.execute(sql_select)
result = cursor.fetchall()

for row in result:
    print(row)
print("\n")

# 데이터 삽입
sql_insert = "INSERT INTO Book(bookid, bookname, publisher, price) VALUES (11, '스포츠 의학', '한솔의학서적', 90000)"
cursor.execute(sql_insert)
mydb.commit()

# 데이터 검색
sql_select = "SELECT * FROM Book"
cursor.execute(sql_select)
result = cursor.fetchall()

for row in result:
    print(row)
print("\n")

# 데이터 삭제
sql_delete = "DELETE FROM Book WHERE bookid = '11'"
cursor.execute(sql_delete)
mydb.commit()

# 데이터 검색
sql_select = "SELECT * FROM Book"
cursor.execute(sql_select)
result = cursor.fetchall()

for row in result:
    print(row)
print("\n")

# 연결 종료
mydb.close()
