from flask import Flask

application = Flask(__name__)

@application.route('/')
def greet():
    return 'Hello, world!'

if __name__ == '__main__':
    application.run()

