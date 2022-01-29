FROM python:3.7

WORKDIR /app
COPY requirements.txt /app
RUN pip install  --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 5001
#CMD sleep 20s && flask db init && flask db migrate -m "inital" && flask db upgrade && python3 entrypoint.py
#CMD python3 wait_for.py && python3 entrypoint.py