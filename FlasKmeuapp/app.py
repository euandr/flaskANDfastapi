from flask import Flask, render_template, redirect
# 'render tamplate' para retornar uma pagina web
# precisa-se adicionar o arquivo html a uma pasta especifica.

app=Flask(__name__)

@app.route("/hello")          #criando rota com o no 'hello'    ex: http://127.0.0.1:5000/hello
def ola():
    return "hello word"

@app.route("/")
def inicio():
    # return "<h1>testando</h1>"
    return redirect("/login")
# sempre redicionara para a pagina escolhida, nesse caso 'login'.

@app.route("/login")
def login():
    return "LOGIN AQUI"

@app.route("/teste")
def teste():
    return " clique aqui para abrir o <a href='https://translate.google.com/?hl=pt-BR&tab=wT&sl=en&tl=pt&text=body%0A&op=translate'> google tradutor</a>"

@app.route("/html")
def pagina():
    return render_template("inicio.html")

@app.route("/html2")
def pagina2():
    return render_template("teste_if-for.html",nome="José", idade=25)
    



app.run()