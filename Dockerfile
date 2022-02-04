FROM python:3.7

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install numpy

CMD ["python", "convertor.py"]