from flask import Flask
from Score import read_score

app = Flask(__name__)

# score_server - This function will serve the score. It will read the score from the scores 
# file and will return an HTML

@app.route('/')
def score_server():
    msg = f'<html>\n<head>\n\t<title>Scores Game</title>\n</head>\n<body>\n\t<h1>The score is <div id="score">{read_score()}</div></h1>\n</body>\n</html>'
    return msg

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8777)