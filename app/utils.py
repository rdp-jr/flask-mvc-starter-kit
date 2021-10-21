from flask import render_template
import os

def register_error_handlers(app):

    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('/errors/404.html'), 404
        # return "404"
        

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('errors/405.html'), 405

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        return render_template('errors/500.html'), 500

def register_blueprints(app):
    """
    Automatically register routes (blueprints) using the route variable in each route file
    """

    import pkgutil 
    import app.routes as routes
    import importlib

    pkgpath = os.path.dirname(routes.__file__)
    blueprints = [name for _, name, _ in pkgutil.iter_modules([pkgpath])]
    for blueprint in blueprints:
        bp = importlib.import_module('app.routes.' + blueprint)
        app.register_blueprint(bp.route)