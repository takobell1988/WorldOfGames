from flask import Flask
app = Flask(__name__)


def score_server():
    file = open('Scores.txt', 'r')
    score = file.read()
    print(score)
    return score


@app.route('/')
def run_page():
    return '<html>' \
               '<head>' \
               '<title>Scores Game</title>' \
               '</head>' \
               '<body>' \
                    '<h1>The score is <div id="score">' + score_server() + '</div></h1>' \
               '</body>' \
           '</html>'



if __name__ == '__main__':
    app.run()