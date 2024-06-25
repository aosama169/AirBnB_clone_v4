#!/usr/bin/python3
"""
 start Flash web application listens on 0.0.0.0, port 5000
"""
if __name__ == '__main__':
    from flask import Flask
    from flask import render_template
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
        display "C" followed by variable list text
        """
        for i in range(len(text)):
            if text[i] == '_':
                text = text[:i] + ' ' + text[i+1:]
        c_message = "C " + text
        return c_message

    @app.route('/python', strict_slashes=False)
    @app.route('/python/<path:text>', strict_slashes=False)
    def python(text=None):
        """
        displays "Python" followed by variable list text
        """
        if text is None:
            text = "is cool"
        else:
            for i in range(len(text)):
                if text[i] == '_':
                    text = text[:i] + ' ' + text[i+1:]
        python_text = "Python " + text
        return python_text

    @app.route('/number/<int:n>', strict_slashes=False)
    def number(n):
        """
        display "n is a number" where n is int argument
        """
        if type(n) is int:
            n_text = str(n) + " is a number"
            return n_text

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        """
        display HTML page with H1 tag: "Number: n"
        """
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_odd_or_even(n):
        """
        display HTML page with H1 tag: "Number: n is even|odd"
        """
        if n % 2 is 0:
            value = "even"
        else:
            value = "odd"
        return render_template('6-number_odd_or_even.html', n=n, value=value)

    app.run(host='0.0.0.0', port='5000')
