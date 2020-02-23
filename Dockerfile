FROM python:3-alpine
WORKDIR /app

COPY . /app

EXPOSE 8777

RUN touch /app/Scores.txt
RUN pip install --requirement requirements.txt
CMD ["python","/app/MainScores.py"]