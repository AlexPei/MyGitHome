
#基于python:3.6.4官网镜像
FROM python:3.6.4
 
# 设置工作目录
WORKDIR /myapp2
 
# 复制当前目录下的文件到工作目录
COPY . /myapp2
 
# 安装pip库
RUN pip install --trusted-host pypi.python.org -r requirements.txt
 
# 暴露82端口
EXPOSE 82
 
# 定义环境变量
ENV NAME World
 
# 容器启动后执行命令, 运行app
CMD ["python", "myapp2.py"]
