FROM      python:3.9.1-buster
WORKDIR   /usr/src/app
COPY      requirements.txt ./
RUN       pip install --no-cache-dir -r requirements.txt
COPY      . .
RUN       python3 -m spacy download en_core_web_sm
CMD       [ "python", "app.py" ]