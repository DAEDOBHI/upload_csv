from flask import Flask
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():
    with open('test.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print(', '.join(row))
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
