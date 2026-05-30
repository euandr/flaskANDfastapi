# aprendendo sobre fastAPI

python

necessario aprender alguns requisitos importantes para entender isso.
[[RequisitosForFastAPi]]

## tutoriais

- [X]  tuttorial 1 [ # Python FastAPI Tutorial: Build a REST API in 15 Minutes ](https://youtu.be/iWS9ogMPOI0?si=NWUbM6UQF5TetlsG)
- [X]  tutorial 2 [ # FastAPI: do zero à arquitetura profissional (sem caos) ](https://youtu.be/HAz1eJsRB4M?si=Hj7ai7ZVJrcubOcB)
- [ ]  aplicar conhecimento em sistema de tasks ( so com fastAPi, use sqlite(CRUD))

## lendo documentação

[documentação](https://fastapi.tiangolo.com/#recap)
Comece pela documentação - muito boa

- [X]  tutorial user guide/RequestBody

## informações

@app.get()

- esse @ se chama **decorato**
-

documentação da API que esta desenvolvendo

- You can see it directly at: http://127.0.0.1:8000/openapi.json.
  - abaixo do nome FASTAPI de docs é tem o link.

endpoint

- é onde é possivel enviar ou receber dados
- get task/

### type hints

✔ deixar código mais legível

✔ ajudar IDEs

✔ melhorar autocomplete

✔ detectar erros antes de executar

✔ facilitar manutenção

- tipos: srt, int, float
- quando nao souber o tipo user ******any******

```
from typing import Any

def some_function(data: Any):
print(data)
```

```def
 def process_items(items: list[str]):
    for item in items:
        print(item)

```

- isso significa que items é uma lista e cada item dentro dela é do tipo str
- funciona de forma semelhante para tuplas
- para **dict**s seria:

  ```
  def process_items(prices: dict[str, float]):

  ```

  - princes é do tipo dict, e a chave é str e o valor é float.
    ```
    def process_item(item: int | str):
        print(item)
    ``

    ```
  - isso diz que ITEM pode ser INT ou STR.

### pydantics

doc: [documentação](https://pydantic.dev/docs/)

## async e await

await só funciona detro de uma função async.
um afuncao async retorna: <coroutine object ...>

- para chamar uma funcao async é necessario usar o await para ver os dados. Mas, como await so funciona em funcao await entao, só é possível chamr uma função async dentro de outra função async

```

async def ola():
    return "oi"

async def main():
    await ola()
``
```

sincrono == sequencial

- because the computer / program follows all the steps in sequence before switching to a different task, even if those steps involve waiting.

## query string

**Query string** é a parte da URL usada para passar **informações extras** para um site ou sistema.

Ela segue um padrão bem simples:

``?chave=valor&chave2=valor2&chave3=valor3``

### Componentes:

* `?` → inicia a query
* `chave` → nome do parâmetro
* `=` → separa nome e valor
* `valor` → o que você quer passar
* `&` → separa vários parâmetros

Não há palavras reservadas. É definido pelo servidor como o FASTAPI.
