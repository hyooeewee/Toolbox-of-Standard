# coding=utf-8
from flask import Flask, jsonify, render_template
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://123.60.58.210:7687", auth=("neo4j", "12345678")) #认证连接数据库
app = Flask(__name__) #flask框架必备

def buildNodes(nodeRecord): #构建web显示节点
    data = {"id": nodeRecord._id, "label": list(nodeRecord._labels)[0]} #将集合元素变为list，然后取出值
    data.update(dict(nodeRecord._properties))
    return {"data": data}
def buildEdges(relationRecord): #构建web显示边
    data = {"source": relationRecord.start_node._id,
            "target":relationRecord.end_node._id,
            "relationship": relationRecord.type}
    return {"data": data}

@app.route('/')#建立路由，指向网页
def index():
    return render_template('index.html')

@app.route('/graph/')#两个路由指向同一个网页，返回图的节点和边的结构体
def get_graph():
    with open(r'.\WEB\templates\temp.txt','r', encoding='utf-8') as file:
        file_contents = file.read()
    # key = key.decode('utf-8')
    print("----------------------------------")
    print(file_contents)
    print("------------------------------------------")
    with driver.session() as session:
        words = 'MATCH  (p:STANDARD{name:"' + file_contents + '"})-[r]->(n) RETURN p, r, n'
        # print(words)8
        results=session.run(words).values()
        nodeList=[]
        edgeList=[]
        for result in results:
            # 检查结果的内容，然后进行相应的操作,此处有多少个if取决于特征有多少种
            if result and len(result) >= 1:
                nodeList.append(result[0])
                nodeList.append(result[2])
                nodeList = list(set(nodeList))
                edgeList.append(result[1])


        nodes = list(map(buildNodes, nodeList))
        edges= list(map(buildEdges,edgeList))

    return jsonify(elements = {"nodes": nodes, "edges": edges})

if __name__ == '__main__':
    app.run(debug = True) #flask框架必备