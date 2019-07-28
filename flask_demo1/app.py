from flask import Flask

#初始化一个flask对象
#flask()
#需要传递一个参数__name__
#1方便flask框架去寻找资源
#2方便flask插件 比如 Fask_Sqlalchemy出现错误的时候，好去寻找问题所在的位置
app = Flask(__name__)

##app.route是个装饰器
##@开头，并且在函数的上面，说明是装饰器
##这个装饰器的作用，是做一个URL与视图函数的映射
##127.0.0.1:5000/  --->去请求执行 hell_world这个函数并返回结果给浏览器


@app.route('/')
def index():
    return'<h1>我是第一个flask程序哦~~t/Hello World</h1>'


##如果当着文件是作为入口程序运行，那么就执行app.run()
if __name__ == '__main__':
    #启动一个应用服务器，来接受用户的请求
    #while True:
    #  listen()
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=81)
