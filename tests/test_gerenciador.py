from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK

from gerenciador_tarefas.gerenciador import app, TAREFAS


def test_quando_listar_tarefas_devo_retornar_codigo_de_status_ok():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == HTTP_200_OK


def test_quando_listar_tarefas_formato_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.headers["Content-Type"] == "application/json"

def test_quando_listar_tarefas_retorno_deve_ser_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert isinstance(resposta.json(), list)


def test_deve_listar_tarefas():
    tarefa = {
        "id": 1,
        "titulo": "titulo",
        "descricao": "descrição",
        "estado": "finalizado",
    }
    TAREFAS.append(tarefa)
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.json() == [tarefa]
    TAREFAS.clear()