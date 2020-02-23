FROM python:3
ADD MainScores.py /
ADD Scores.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./MainScores.py" ]