from flask import Flask
import datetime
#��ʼ��һ��flask����
#flask()
#��Ҫ����һ������__name__
#1����flask���ȥѰ����Դ
#2����flask��� ���� Fask_Sqlalchemy���ִ����ʱ�򣬺�ȥѰ���������ڵ�λ��
myapp2 = Flask(__name__)

##app.route�Ǹ�װ����
##@��ͷ�������ں��������棬˵����װ����
##���װ���������ã�����һ��URL����ͼ������ӳ��
##127.0.0.1:5000/  --->ȥ����ִ�� hell_world������������ؽ���������


@myapp2.route('/')
def index():
    return'<h1>���ǵ�һ��flask����Ŷ~~t/Hello World</h1>'

@myapp2.route('/time',methods=['post','get'])
def get_time():
    now=str(datetime.datetime.now())#�ѵ�ǰʱ��ת�����ַ���
    return '��ǰ��ʱ����:%s'%now
    
##��������ļ�����Ϊ��ڳ������У���ô��ִ��app.run()
if __name__ == '__main__':
    #����һ��Ӧ�÷��������������û�������
    #while True:
    #  listen()
    #myapp2.run(debug=True)
    myapp2.run(host='0.0.0.0', port=82)
#http://0.0.0.1:8888/time