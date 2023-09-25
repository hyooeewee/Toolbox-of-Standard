# Toolbox-of-Standard

# TODO
## 界面
- [ ] 登录界面容器优化，阴影优化
- [ ] 主界面整体风格优化
- [ ] 查询结果显示框自适应，宽度应设置为不可调，防止横向滚轮出现
- [ ] 首页没什么功能，不如去掉
## 逻辑
- [ ] 登陆界面逻辑优化，元素整理
- [ ] 主界面逻辑补充
- [ ] 完成账户逻辑
## 数据
- [ ] 已有数据的整理
- [ ] 添加剩余省市的地方标准
- [ ] 添加团体协会标准
## 下载功能
- [ ] 不同省市下载方式有所不同，大部分省市通过可直接re下载
- [ ] 当前发现部分
## 登录验证
- [ ] 离线验证考虑通过机器码进行验证？
- [ ] 服务器搭建完成后进行服务器端验证？
## 服务器搭建
- [ ] 搭建SQLite服务器，账户数据与规范标准情况均存放于服务器
- [ ] 本地数据库同时保留，初始状况设置为空，历次查询结果在本地服务器也保存一份，每次查询按钮点击时，匹配服务器端数据
- [ ] 服务器数据定期更新，尽量挑选各省市服务器压力较低的时段
- [ ] 账户注册采用机器码作为唯一识别信息
## 新增功能
- [ ] 根据给定关键词，自动生成规范表
- [ ] 爬取各省市的公告，如有新发布的公告，获取关键词和原文链接，作为新闻推送

# 更新
## 2023-9-14
- [ ] 补充部分注释
- [ ] 调整登陆页面风格，主页按钮布局，补充新增功能标签页
- [ ] 天津的实施状态和实施日期可显示
- [ ] 四川的数据清洗调整
- [ ] 整理代码，把奇奇怪怪的print删除，统一代码调试风格
## 2023-9-19
- [ ] 搭建云数据库，部署MySQL
- [ ] 重构数据，数据库格式更换为{代码，区域，标准名，开始时间，截止时间，当前状态，下载链接，headers，更新时间}
- [ ] 当前完成天津、北京、河北、四川、上海的数据库重构
- [ ] 格式化规范号显示方式，去除空格
- [ ] 日期统一为“yyyy年mm月dd日”的格式
## 2023-9-21
- [ ] 国标爬取代码重构
## 2023-9-22
- [ ] IP代理池部署
- [ ] 完成国标爬取

## 2023-9-25
- [ ] 数据上云！


> 目前已经完成软件的打包发布，可以从此处[<img src="https://www.emojiall.com/images/60/openmoji/1.0/1f4e5.png" width="25px" height="25px">](https://github.com/hyooeewee/Toolbox-of-Standard/tags)下载需要的版本
