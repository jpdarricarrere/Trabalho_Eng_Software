# Bike Manager Backend

Esse é o backend para o "Sistema para locação de bicicletas".

Ele é implementado em Python, tendo como base o framework FastAPI.

# Como rodar

## Setup inicial

Esses são os passos iniciais, que devem ser feitos apenas na primeira vez que estiver configurando o ambiente para o desenvolvimento em uma nova máquina.

Primeiramente, certifique-se de que possui a versão 3 do Python instalada.

Após, instale o framework FastAPI e suas dependências, seguindo esses passos (caso encontre algum erro, tente a forma alternativa abaixo):

Instale o FastAPI rodando o comando `pip install fastapi` no seu terminal/prompt

Instale o servidor Uvicorn rodando o comando `pip install "uvicorn[standard]"` no seu terminal/prompt

Alternativamente, siga os passos no próprio site do framework: https://fastapi.tiangolo.com/#installation 

Tendo feito esse setup inicial, nas próximas vezes que quiser rodar o programa pode começar direto do passo abaixo:

## Rodando

Com as dependências instaladas, abra um terminal/prompt na pasta "bike-manager-be" e rode o comando `uvicorn main:app --reload`

Você deve perceber várias linhas de log aparecendo. Se tudo correu bem, verá algo semelhante a "INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)" em uma delas.

Para testar que o sistema foi inicializado corretamente, abra o seu browser e acesse http://localhost:8000/ (ou equivalente). Você deverá receber na página um JSON como esse: `{"Status":"It lives!"}`. Se chegou nesse ponto, sucesso! Caso tenha encontrado algum problema, verifique se seguiu todos os passos e não obteve nenhum erro neles.

A parte `--reload` do comando utilizado faz com que qualquer alteração que seja feita no código do backend seja dinamicamente recarregado, portanto não é necessário reiniciar o servidor ao fazer alguma alteração.

## Encerrando

Uma vez que deseje encerrar o servidor, aperte Ctrl+C na janela do terminal onde inicializou ele para encerrá-lo.


# API

## Documentação

Para checar os endpoints fornecidos, acesse http://localhost:8000/docs no seu browser. Lá, encontrará uma lista com os endpoints e métodos disponíveis para eles, incluindo quais parâmetros podem receber.

Essa página é gerada dinamicamente de acordo com o que está definido no código, portanto estará sempre atualizada de acordo com a versão que você possui localmente.



