<<<<<<< HEAD
FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn",,"main:app","--host","0.0.0.0","--port","8000"]
=======
FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn",,"main:app","--host","0.0.0.0","--port","8000"]
>>>>>>> dfc895b24a537a3ae1f9ba3ef172b9a2ee2817f9
