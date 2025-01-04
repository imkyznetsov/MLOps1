FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl build-essential wget

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN pip install jupyter nbformat quarto-cli black black[jupyter] flake8

CMD ["jupyter", "notebook", "EDA_HW1_MLOps.ipynb", "--no-browser", "--allow-root", "--ip=0.0.0.0"]