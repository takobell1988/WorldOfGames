FROM python:3
ADD MainScores.py /
ADD Scores.txt /
CMD [ "python", "./MainScores.py" ]