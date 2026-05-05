FROM python:3.13.2
LABEL maintainer="Holger Meister"

COPY . /app
WORKDIR /app

RUN pip install -e .

CMD ["python", "main.py"]