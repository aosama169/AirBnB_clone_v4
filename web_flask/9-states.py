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

    @app.route('/cities_by_states', strict_slashes=False)
    def cities_by_states():
        """
        fetch data from storage engine and display rendered HTML page
        """
        states = storage.all("State")
        result = states.values()
        states_result = sorted(result, key=attrgetter('name'))
        return render_template('8-cities_by_states.html',
                               states_result=states_result)

    @app.route('/states', strict_slashes=False)
    @app.route('/states/<id>', strict_slashes=False)
    def states_id(id=None):
        """
        fetch data from storage engine and display rendered HTML page
        """
        states = storage.all("State")
        result = states.values()
        if (id is None):
            states_result = sorted(result, key=attrgetter('name'))
            return render_template('9-states.html',
                                   states_result=states_result, id=id)
        for state in result:
            if state.id == id:
                return render_template('9-states.html',
                                       states_result=state, id=id)
        return render_template('9-states.html',
                               states_result=None, id=id)

    @app.teardown_appcontext
    def teardown(self):
        """
        remove current SQL Alchemy Session after each request
        """
        storage.close()

    app.run(host='0.0.0.0', port='5000')
