FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE 5000:5000

CMD [ "flask" , "run" ]