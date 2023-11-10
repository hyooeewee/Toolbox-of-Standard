from datetime import datetime
import pymysql

def Pattarn(type,keywords):
    if type == "不限":
        type_pattarn = ""
        if keywords == "":
            return "SELECT * FROM standard_db.NEWS "
    elif type == "住房城乡建设部" :
        type_pattarn = "住建部"
    elif type == "北京市住建厅" :
        type_pattarn = "北京市"
    if keywords == None or len(keywords.split()) == 0 :
        keywords_pattarn = ""
    else:
        keywords_list = keywords.split()
        if len(keywords_list) == 1:
            keywords_pattarn = f"AND TITLE LIKE '%{keywords_list[0]}%'"
        else:
            keywords_pattarn = f"AND TITLE LIKE '%{keywords_list[0]}%'"
            for i in range(len(keywords_list)-1):
                keywords_pattarn = keywords_pattarn + f" AND TITLE LIKE '%{keywords_list[i+1]}%' "
    total_pattarn ="SELECT * FROM standard_db.NEWS " + f"WHERE TYPE LIKE '%{type_pattarn}%' " + keywords_pattarn
    return total_pattarn

def data_filter(total_list,start_d,end_d):
    start = datetime.strptime(start_d, "%Y-%m-%d")
    end = datetime.strptime(end_d, "%Y-%m-%d")
    result_list = []
    for i in range(len(total_list)):
        News_time = datetime.strptime(total_list[i][2], "%Y-%m-%d")
        if News_time>=start and News_time<=end:
            result_list.append(total_list[i])
    return result_list


def get_News(database_config,type,keywords,start_d,end_d):
    pattarn = Pattarn(type,keywords)
    connection = pymysql.connect(**database_config)
    try:
        # 创建一个数据库游标对象
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            sql_query = pattarn
            cursor.execute(sql_query)
            # 获取所有行的结果
            rows = cursor.fetchall()
            # 将结果转换为列表
            result_list = list(rows)
    finally:
        # 关闭数据库连接
        connection.close()
    if result_list:
        result = data_filter(result_list,start_d,end_d)
    return result

