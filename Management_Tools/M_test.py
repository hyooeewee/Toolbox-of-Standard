from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Neo4j图形界面的URL
neo4j_url = 'http://localhost:7474'  # 替换为你的Neo4j图形界面地址

@app.route('/')
def index():
    # 使用代理将请求转发到Neo4j图形界面
    response = requests.get(neo4j_url)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
