import sqlite3
import os

# 删除现有数据库文件
if os.path.exists('certificates.db'):
    os.remove('certificates.db')

# 连接到SQLite数据库
conn = sqlite3.connect('certificates.db')

# 创建一个新的SQLite游标
cur = conn.cursor()

# 创建新的证书表，包含姓名，MOE岗位，认证项目，认证标准，认证时间，证书号
cur.execute('''
    CREATE TABLE certificates (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        moe_position TEXT NOT NULL,
        certification_program TEXT NOT NULL,
        certification_standard TEXT NOT NULL,
        certification_date TEXT NOT NULL,
        certificate_number TEXT NOT NULL
    )
''')

# 插入一些示例数据
certificates = [
    ('John Doe', 'Engineer', 'Safety Training', 'ISO 9001', '2023-06-15', '123456'),
    ('Jane Smith', 'Technician', 'First Aid', 'CPR Certified', '2023-06-20', '654321'),
    ('Alice Johnson', 'Manager', 'Project Management', 'PMP', '2023-07-10', '111222'),
    ('Bob Brown', 'Supervisor', 'Leadership Training', 'Leadership 101', '2023-08-01', '333444')
]

cur.executemany('INSERT INTO certificates (name, moe_position, certification_program, certification_standard, certification_date, certificate_number) VALUES (?, ?, ?, ?, ?, ?)', certificates)

# 提交事务
conn.commit()

# 关闭连接
conn.close()
