import sqlite3 

# def get_all(query):
#     conn = sqlite3.connect('C:/Users/Admin/OneDrive/Máy tính/Full-stack/flask/data/newsdb.db')
#     data=conn.execute(query).fetchall()
#     conn.close()
#     return data
    
def get_all(query):
    conn = sqlite3.connect('C:/Users/Admin/OneDrive/Máy tính/Full-stack/flask/data/newsdb.db')
    c = conn.cursor() 
    data=c.execute(query)
    s=data.fetchall()
    conn.commit() 
    conn.close()
    return s

def get_news_by_id():
    conn=sqlite3.connect('data/newsdb.db')

    conn.close()


if __name__ == '__main__':
    # sql_query="select * from category"
    print(get_all("SELECT * FROM category"))