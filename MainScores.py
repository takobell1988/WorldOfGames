from flask import Flask
app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        file = open('Scores1.txt', 'r')
        score = file.read()
        return '<html>' \
               '<head>' \
               '<title>Scores Game</title>' \
               '</head>' \
               '<body>' \
               '<h1>The score is <div id="score">' + score + '</div></h1>' \
            '</body>' \
            '</html>'

    except BaseException as e:
        return '<html>' \
               '<head>' \
               '<title>Scores Game</title>' \
               '</head>' \
               '<body>' \
               '<h1>The score is <div id="score" style="color:red">{ERROR}</div></h1>' \
                '</body>' \
                '</html>'


if __name__ == '__main__':
    app.run()