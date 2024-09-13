FROM python:3.10-bullseye

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY src .

EXPOSE 8501

CMD ["streamlit", "run", "src/app.py"]

