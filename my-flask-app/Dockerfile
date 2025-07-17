FROM python:3.11 AS builder
WORKDIR /app
COPY ./app/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir --prefix=/install/packages -r requirements.txt

FROM python:3.11-slim 
WORKDIR /app
ENV PYTHONPATH=/app/packages/lib/python3.11/site-packages
COPY --from=builder install/packages /app/packages
COPY ./app/ .
EXPOSE 5000
CMD [ "python","app.py" ]