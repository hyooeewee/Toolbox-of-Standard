from time import sleep

import openpyxl

# 打开Excel文件
excel_file = openpyxl.load_workbook('C:\\Users\\MASON_S\\Desktop\\1.xlsx')

# 选择要读取的工作表
sheet = excel_file['1']  # 替换为你的工作表名称

# 创建一个空的列表，用于存储每行的内容
data = []

# 遍历工作表的每一行
for row in sheet.iter_rows(values_only=True):
    row_data = list(row)  # 将行数据转换为列表
    data.append(row_data)

# 关闭Excel文件
excel_file.close()

# 打印或处理读取的数据
for row in data:
    print("CREATE (n1:STANDARD {" + "\n" +\
        'S_ID:"'+ str(row[0]) + ')", '+ "\n" +\
        'name:"'+ str(row[1]) + '",' + "\n" +\
        'start_time:"' + str(row[2]) + '",' + "\n" +\
        'url:"' + str(row[3]) + '"})' + "\n" +\
        'WITH n1 '+ "\n" +\
        'MATCH (n2:FENBU {name:"' + str(row[5]) + '"})'  + "\n" +\
        'MATCH (n3:ZIFENBU {name:"'+ str(row[6]) + '"})' + "\n" +\
        'MATCH (n4:STATUS {name:"' + str(row[7]) + '"})' + "\n" +\
        'MATCH (n5:TYPE {name:"' + str(row[4]) + '"})' + "\n" +\
        "CREATE (n1)-[:分部工程]->(n2)" + "\n" +"CREATE (n1)-[:子分部工程]->(n3)" + "\n" +"CREATE (n1)-[:状态]->(n4)" + "\n" + "CREATE (n1)-[:属地]->(n5)"+ "\n" + "\n" + "\n")
