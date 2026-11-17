# ============================================================
# ABSCONDITUS — BACKEND DA FICHA DE JOGADOR
# Python + Flask (leve, roda local no seu PC)
# ============================================================

import os
import json
import uuid
import random
from datetime import datetime
from flask import Flask, request, jsonify, Response

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'personagens')
os.makedirs(DATA_DIR, exist_ok=True)

app = Flask(__name__, static_folder=BASE_DIR, static_url_path='')


# ============================================================
# ROTAS ESTÁTICAS — serve o frontend HTML/CSS/JS
# ============================================================

@app.route('/')
def index():
    caminho = os.path.join(BASE_DIR, 'Ficha-Jogador.html')
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    return Response(conteudo, mimetype='text/html')

@app.route('/<path:path>')
def static_files(path):
    caminho = os.path.join(BASE_DIR, path)
    if not os.path.exists(caminho):
        return jsonify({'erro': 'Arquivo não encontrado'}), 404
    if caminho.lower().endswith('.css'):
        with open(caminho, 'r', encoding='utf-8') as f:
            return Response(f.read(), mimetype='text/css')
    if caminho.lower().endswith('.js'):
        with open(caminho, 'r', encoding='utf-8') as f:
            return Response(f.read(), mimetype='application/javascript')
    with open(caminho, 'rb') as f:
        return Response(f.read())


# ============================================================
# API — PERSONAGENS
# ============================================================

@app.route('/api/personagens', methods=['GET'])
def listar_personagens():
    """Lista todos os personagens salvos."""
    personagens = []
    for nome_arquivo in os.listdir(DATA_DIR):
        if nome_arquivo.endswith('.json'):
            caminho = os.path.join(DATA_DIR, nome_arquivo)
            try:
                with open(caminho, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                personagens.append({
                    'id': dados.get('id'),
                    'nome': dados.get('nome'),
                    'rank': dados.get('rank'),
                    'atualizado_em': dados.get('atualizado_em')
                })
            except Exception as e:
                app.logger.warning('Falha ao ler %s: %s', nome_arquivo, e)
    return jsonify(personagens)


@app.route('/api/personagens/<personagem_id>', methods=['GET'])
def obter_personagem(personagem_id):
    """Retorna um personagem pelo ID."""
    caminho = os.path.join(DATA_DIR, f'{personagem_id}.json')
    if not os.path.exists(caminho):
        return jsonify({'erro': 'Personagem não encontrado'}), 404
    with open(caminho, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    return jsonify(dados)


@app.route('/api/personagens', methods=['POST'])
def salvar_personagem():
    """Cria ou atualiza um personagem."""
    dados = request.get_json(force=True) or {}

    personagem_id = dados.get('id') or str(uuid.uuid4())
    agora = datetime.now().isoformat()

    personagem = {
        'id': personagem_id,
        'nome': dados.get('nome', 'Sem nome'),
        'rank': dados.get('rank', ''),
        'classe': dados.get('classe', ''),
        'raca': dados.get('raca', ''),
        'idade': dados.get('idade', ''),
        'organizacao': dados.get('organizacao', ''),
        'descricao': dados.get('descricao', ''),
        'atributos': dados.get('atributos', {}),
        'pericias': dados.get('pericias', {}),
        'recursos': dados.get('recursos', {}),
        'combate': dados.get('combate', {}),
        'magia': dados.get('magia', {}),
        'inventario': dados.get('inventario', ''),
        'caso': dados.get('caso', ''),
        'criado_em': dados.get('criado_em', agora),
        'atualizado_em': agora
    }

    caminho = os.path.join(DATA_DIR, f'{personagem_id}.json')
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(personagem, f, ensure_ascii=False, indent=2)

    return jsonify({'id': personagem_id, 'status': 'salvo'})


@app.route('/api/personagens/<personagem_id>', methods=['DELETE'])
def deletar_personagem(personagem_id):
    """Remove um personagem salvo."""
    caminho = os.path.join(DATA_DIR, f'{personagem_id}.json')
    if not os.path.exists(caminho):
        return jsonify({'erro': 'Personagem não encontrado'}), 404
    os.remove(caminho)
    return jsonify({'status': 'deletado'})


# ============================================================
# API — ROLAGEM DE DADOS
# ============================================================

@app.route('/api/dados/rolar', methods=['POST'])
def rolar_dados():
    """Rola dados no formato NdM (ex: 2d6, 1d20)."""
    dados = request.get_json(force=True) or {}
    expressao = dados.get('expressao', '1d20')

    try:
        quantidade, faces = expressao.lower().split('d')
        quantidade = int(quantidade)
        faces = int(faces)
    except Exception:
        return jsonify({'erro': 'Expressão inválida. Use o formato NdM (ex: 2d6).'}), 400

    if quantidade < 1 or quantidade > 100 or faces < 1 or faces > 1000:
        return jsonify({'erro': 'Valores fora do intervalo permitido.'}), 400

    rolagens = [random.randint(1, faces) for _ in range(quantidade)]

    return jsonify({
        'expressao': expressao,
        'rolagens': rolagens,
        'total': sum(rolagens)
    })
# ============================================================
# INICIALIZAÇÃO
# ============================================================

if __name__ == '__main__':
    print('ABSCONDITUS BACKEND rodando em http://127.0.0.1:5000')
    print('Personagens salvos em:', DATA_DIR)
    app.run(host='127.0.0.1', port=5000, debug=True)
