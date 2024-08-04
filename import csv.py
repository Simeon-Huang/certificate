import sqlite3
import csv

# 连接到SQLite数据库
conn = sqlite3.connect('certificates.db')

# 创建一个新的SQLite游标
cur = conn.cursor()

# 打开CSV文件并读取数据
with open('certificates.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute('INSERT INTO certificates (name, moe_position, certification_program, certification_standard, certification_date, certificate_number) VALUES (?, ?, ?, ?, ?, ?)',
                    (row['name'], row['moe_position'], row['certification_program'], row['certification_standard'], row['certification_date'], row['certificate_number']))

# 提交事务
conn.commit()

# 关闭连接
conn.close()
