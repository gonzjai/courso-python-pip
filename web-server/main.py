import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    A = [1,2,3,4]

@app.get(/contact, response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola, Esta es mi pagina</h1>
    <p>Y estoy aprendiendo con ella</p>
    """
def run():
    store.get_categories()


if __name__ == '__main__':
    run()