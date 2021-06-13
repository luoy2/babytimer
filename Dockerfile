# 建立 python3.6 环境
FROM python:3.6
# 镜像作
# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1
# 创建 babyTimer 文件夹
RUN mkdir /babyTimer
# 将 babyTimer 文件夹为工作目录
WORKDIR /babyTimer

# 将当前目录加入到工作目录中（. 表示当前目录）
ADD backend/requirements.txt /tmp/requirements.txt
# 利用 pip 安装依赖（- i 表示指定清华源，默认源下载过慢）
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

