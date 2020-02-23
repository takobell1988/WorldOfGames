FROM python:3
WORKDIR /app

COPY . /app

EXPOSE 8777
RUN touch /app/Scores.txt
RUN pip install -r /app/requirements.txt
CMD ["python","/app/MainScores.py"]