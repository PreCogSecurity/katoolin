FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

RUN pip install --no-cache-dir .

CMD ["python3", "katoolin.py"]
