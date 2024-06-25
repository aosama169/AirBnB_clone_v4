#!/usr/bin/python3
"""
 start Flash web application listens on 0.0.0.0, port 5000
"""
if __name__ == '__main__':
    from flask import Flask
    from flask import render_template
    from models import storage
    from operator import attrgetter
    app = Flask(__name__)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """
        fetch data from storage engine and display rendered HTML page
        """
        states = storage.all("State")
        result = states.values()
        states_result = sorted(result, key=attrgetter('name'))
        return render_template('7-states_list.html',
                               states_result=states_result)

    @app.teardown_appcontext
    def teardown(self):
        """
        remove current SQL Alchemy Session after each request
        """
        storage.close()

    app.run(host='0.0.0.0', port='5000')
