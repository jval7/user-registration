FROM python:3.7

WORKDIR /app
COPY requirements.txt /app
#COPY app /app
RUN pip install  --no-cache-dir -r requirements.txt
EXPOSE 5001
#CMD sleep 20s && flask db init && flask db migrate -m "inital" && flask db upgrade && python3 entrypoint.py
CMD ["tail", "-f", "/dev/null" ]