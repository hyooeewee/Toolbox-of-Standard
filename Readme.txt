# *.ui和*.qrc文件转换为*.py
# cmd命令行输入（Login,res是源文件名，新文件可以再定义，但无必要）：
pyuic5 Login.ui -o LoginUi.py
pyuic5 Main.ui -o MainUi.py
pyrcc5 res.qrc -o res_rc.py