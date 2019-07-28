
#基于python2.7官网镜像
FROM python:2.7-slim
 
# 设置工作目录
WORKDIR /app
 
# 复制当前目录下的文件到工作目录
COPY . /app
 
# 安装pip库
RUN pip install --trusted-host pypi.python.org -r requirements.txt
 
# 暴露80端口
EXPOSE 80
 
# 定义环境变量
ENV NAME World
 
# 容器启动后执行命令, 运行app
CMD ["python", "app.py"]
