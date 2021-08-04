FROM registry.cn-hangzhou.aliyuncs.com/li_jixiang/jixiang:ubuntu-python

MAINTAINER li_jixiang723@163.com

WORKDIR /root

COPY . /root

RUN pip3 install -r requirements.txt

EXPOSE 10103

CMD ["python3", "main.py"]
