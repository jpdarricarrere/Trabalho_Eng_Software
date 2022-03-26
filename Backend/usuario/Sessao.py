from collections import defaultdict
import random

from .ServicoUsuario import ServicoUsuario

_TOKEN_SIZE = 12
_ELEMENTOS = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

class Sessao:

    def __init__(self):
        self._todas_sessoes = defaultdict(list)

    def gera_token(self):
        token = ''
        for _ in range(_TOKEN_SIZE):
            token = token + random.choice(_ELEMENTOS)
        return token

    def login(self, email: str, senha: str) -> dict:
        dto = dict()
        usuarios = ServicoUsuario.listar_todos()     # TODO: adicionar um 'find_by_email' em RepositorioUsuario para evitar isso
        for usuario in usuarios:
            if usuario.get_email() == email and usuario.get_senha() == senha:
                dto = usuario.dto()
                token = self.gera_token()
                dto['token'] = token 
                sessoes_desse = self._todas_sessoes[email]
                sessoes_desse.append(token)
                self._todas_sessoes[email] = sessoes_desse
        return dto

    def logout(self, email: str, token: str):
        self._todas_sessoes[email].remove(token)

    def invalidar_todas_para_usuario(self, email) -> None:
        if email in self._todas_sessoes:
            del self._todas_sessoes[email]

    def todas(self):  # Apenas para debug e desenvolvimento, deletar depois
        return self._todas_sessoes