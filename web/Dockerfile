FROM      python:3.9.1-buster
WORKDIR   /usr/src/app
COPY      requirements.txt ./
RUN       pip install --no-cache -r requirements.txt
COPY      . .
CMD       [ "python", "app.py" ]