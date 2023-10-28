# 서비스를 빨리 구현을 해야하는 상황 -> flask
# AI Engineer -> Developer
from flask import Flask, request, render_template
import sqlite3 # 파일 형태의 로컬 데이터 베이스

# flask 가동
app = Flask(__name__)

# SQlite와 연결
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# 데이터베이스 테이블 생성
def create_table():
    print("DB가 생성됩니다.")
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = f"CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def add_book(title, author):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = f"INSERT INTO books (title, author) VALUES ('{title}', '{author}')"
    print(sql)
    cursor.execute(sql) # 실행해
    conn.commit() # 반영해
    conn.close()

# 요청이 많아서 자주 끊었다 연결하면 무리가 가지 않나요? -> 나중에..
# 초당 천건 이상은 되야 그때부터 고민해도 늦지않습니다.

# 업데이트할 값이 뭐야? id
@app.route('/update/<int:id>', methods=['PUT'])
def update_book(id):
    new_title = request.form['title']
    new_author = request.form['author']

    print("Update book...", new_title, new_author)

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = f"UPDATE books SET title='{new_title}', author='{new_author}' WHERE id={id}"
    cursor.execute(sql)
    conn.commit()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def main():
    create_table()

    if request.method == 'POST':
        print("유저로부터 POST 요청이 들어왔습니다.")
        title = request.form['title']
        author = request.form['author']
        add_book(title, author)

    conn = get_db_connection()

    sql = f"SELECT * FROM books"
    cursor = conn.execute(sql)
    results = cursor.fetchall()
    conn.close()

    return render_template('index.html', books=results)

if __name__ == "__main__":
    app.run()


# flask -> SQLITE 연동 및 데이터 생성

 # DB connection SQlite와 연결