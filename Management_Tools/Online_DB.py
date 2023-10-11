#数据清洗
##去除所有空格
##年月日格式化
##新数据格式为{代码，区域，标准名，开始时间，截止时间，当前状态，下载链接，headers，更新时间}

# 定义数据库连接参数
import pymysql
import sqlite3
# 定义云端数据库连接参数
online_db_config = {
    'host': '123.60.58.210',  # 远程MySQL数据库的主机地址（IP地址或域名）
    'user': 'root',        # 远程MySQL数据库的用户名
    'password': '123456',    # 远程MySQL数据库的密码
    'database': 'standard_db',  # 要连接的数据库名称
    'port': 3306                    # MySQL默认端口号
}
Local_db_PATH = r'.\Database\users.db'
# 定义本地数据库位置

def online_db_test():
    try:
        connection = pymysql.connect(**online_db_config)
        print('成功连接到MySQL数据库')

    except pymysql.Error as e:
        print(f'连接错误: {e}')
    finally:
        # 最后记得关闭数据库连接
        if 'connection' in locals():
            connection.close()
    input("按回车键继续...")

def local_db_test():
    try:
        conn = sqlite3.connect(Local_db_PATH)
        cur = conn.cursor()
        print('成功连接到SQLite数据库')
    except pymysql.Error as e:
        print(f'连接错误: {e}')
    finally:
        # 最后记得关闭数据库连接
        if 'connection' in locals():
            conn.commit()
            conn.close()
    input("按回车键继续...")

def data_transmit():
    # 连接本地SQLite数据库
    sqlite_connection = sqlite3.connect(Local_db_PATH)
    sqlite_cursor = sqlite_connection.cursor()
    # 连接云端mysql数据库
    mysql_connection = pymysql.connect(**online_db_config)
    mysql_cursor = mysql_connection.cursor()
    # 选中所有数据
    sqlite_cursor.execute('SELECT * FROM standards')
    data_to_insert = sqlite_cursor.fetchall()
    i = 1
    for row in data_to_insert:
        mysql_cursor.execute('INSERT INTO STANDARD (SN, TYPE, NAME, START_DATE, END_DATE , STATUS, LINK, RE_HEADERS, UPDATE_TIME) '
                             'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', row)
        i = i + 1
        print("共计" + str(len(data_to_insert)) + "条数据，当前已插入完成" + str(i) + "条！")
    mysql_connection.commit()
    mysql_connection.close()
    sqlite_connection.close()
# 将数据插入到MySQL数据库

def main():
    online_db_test()
    local_db_test()
    data_transmit()

if __name__ == "__main__":
    main()
