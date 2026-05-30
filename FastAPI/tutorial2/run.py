import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "tutorial2.src.main.server.server:app", 
        host="0.0.0.0",
        port=3001,
        reload=True.as_integer_ratio
        )
    

#  pasta tutorial2 não tem um __init__.py, então não é um pacote. Se der erro, conserte isso.