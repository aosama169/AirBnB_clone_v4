#!/usr/bin/python3
"""
 start Flash web Application listens on 0.0.0.0, port 5000
"""
if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """
        display "Hello HBNB!"
        """
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """
        display "HBNB"
        """
        return "HBNB"

    @app.route('/c/<path:text>', strict_slashes=False)
    def c(text):
        """
        display "C" follow by variable list text
        """
        for i in range(len(text)):
            if text[i] == '_':
                text = text[:i] + ' ' + text[i+1:]
        c_text = "C " + text
        return c_text

    app.run(host='0.0.0.0', port='5000')
