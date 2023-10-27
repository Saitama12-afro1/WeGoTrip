
FROM python:3.8


WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000
WORKDIR /app/project
RUN python manage.py migrate


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]