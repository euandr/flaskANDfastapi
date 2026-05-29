#python
necessario aprender alguns requisitos importantes para entender isso.
[[RequisitosForFastAPi]]

## tutoriais

- [ ] tuttorial 1 [ # Python FastAPI Tutorial: Build a REST API in 15 Minutes ](https://youtu.be/iWS9ogMPOI0?si=NWUbM6UQF5TetlsG)
- [ ] tutorial 2 [ # FastAPI: do zero à arquitetura profissional (sem caos) ](https://youtu.be/HAz1eJsRB4M?si=Hj7ai7ZVJrcubOcB)

## lendo documentação

[documentação](https://fastapi.tiangolo.com/#recap)
Comece pela documentação - muito boa

## informações

@app.get()

- esse @ se chama **decorato**

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
