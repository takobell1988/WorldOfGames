FROM python:3
ADD MainScores.py /
ADD Scores.txt /
EXPOSE 8777
RUN pip install -r "requirements.txt"
CMD [ "python", "./MainScores.py" ]