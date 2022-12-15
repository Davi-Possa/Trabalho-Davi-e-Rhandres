import flask

from views import set_views
from models import set_models


def main():
    app = flask.Flask(
        'meu servidor',
        template_folder='templates',
        static_folder='static'
    )

    app = set_views(app)
    app = set_models(app)

    app.run(debug=True)


if __name__ == '__main__':
    main()
