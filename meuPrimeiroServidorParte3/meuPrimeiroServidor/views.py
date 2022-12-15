import os
import sqlite3

import flask


def set_views(app):
    @app.route('/', methods=['GET'])
    def main_page():
        seletor = []
        with sqlite3.connect(os.path.join('static', 'database', 'test.db')) as con:
            cur = con.cursor()

            lista_jogadores = cur.execute('SELECT valor, nome FROM jogadores').fetchall()
            for item in lista_jogadores:
                seletor.append('<option value=\"{0}\">{1}</option>'.format(item[0], item[1]))

            seletor = '\n'.join(seletor)

        return flask.render_template(
            'index.html',
            meu_novo_paragrafo='<p>Parágrafo gerado por servidor</p>',
            seletor_jogadores=seletor
        )

    @app.route('/copa', methods=['GET'])
    def pagina_da_copa():
        return flask.render_template(
            'neymar.html'
        )

    @app.errorhandler(404)
    def page_not_found(page):
        return flask.render_template('404.html'), 404

    app.register_error_handler(404, page_not_found)

    return app
