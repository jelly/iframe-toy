from multiprocessing import Process

from flask import Flask, render_template

app1 = Flask(__name__)
app2 = Flask(__name__)


@app1.route('/')
def index():
    return render_template('example.html')


@app1.route('/frame1')
def frame1():
    return render_template('frame1.html')


@app2.route('/frame2')
def frame2():
    return render_template('frame2.html')


@app2.route('/snoop')
def snoop():
    return render_template('snoop.html')


def server1():
    app1.run()


def server2():
    app2.run(port=5001)


if __name__ == '__main__':
    p1 = Process(target=server1)
    p2 = Process(target=server2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
