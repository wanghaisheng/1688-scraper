# 使用Python作为基础镜像, slim-buster是一个轻量级的镜像, 适合生产环境使用
FROM python:3.9-slim-buster
# 设置工作目录
WORKDIR /app
# 复制应用代码到容器中
COPY . .
# 安装js运行环境
RUN apt-get update && apt-get install -y nodejs npm
# 安装依赖项
RUN pip install --no-cache-dir --upgrade -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 设置启动命令
#CMD ["python", "app.py"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
