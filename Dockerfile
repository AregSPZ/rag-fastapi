# define python version
FROM python:3.12-slim

# define app dir
WORKDIR /app

# extract requirements and install them into empty container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# fill the container (which now only has installed dependencies) with the code itself
COPY ./app ./app

# application launch command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]