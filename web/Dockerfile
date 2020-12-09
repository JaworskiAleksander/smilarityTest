FROM      python:3.9.1-buster
WORKDIR   /usr/src/app
COPY      requirements.txt ./
RUN       pip install --no-cache -r requirements.txt
COPY      . .
RUN       pip install ./en_core_web_sm-1.2.0.tar.gz
CMD       [ "python", "app.py" ]