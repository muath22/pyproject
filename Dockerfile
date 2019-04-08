FROM python:3.4-alpine
ADD . /code
WORKDIR /code
#RUN pip install flask
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000

#ROM python:3
#LABEL maintainer="raljohani@sa.ibm.com"
#COPY . /app
#WORKDIR /app
#RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["auth.py"]