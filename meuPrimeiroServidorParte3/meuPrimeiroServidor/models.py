import flask


def set_models(app):
    @app.route('/jogadores', methods=['POST'])
    def hexa():
        jogador = flask.request.form.get('selecionado')
        print('o jogador selecionado foi', jogador)

        response = flask.jsonify({'jogador': jogador})
        response.headers.add('Access-Control-Allow-Origin', '*')  # Essa linha é necessária. Requisição dos navegadores
        return response  # retorna resposta para a página Web

    return app