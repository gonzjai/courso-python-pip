import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola, Esta es mi pagina</h1>
    <p>Y estoy aprendiendo con ella</p>
    <p>Lo estoy probando con FastAPI</p>
    <p>Me parece genial que se recargue automaticamente al usar uvicorn main:app --reload</p>
    """
@app.get('/page', response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola a todos. Sean bienvenidos al blog de pr&aacute;ctica</h1>
    <p>En este blog podr&aacute;n encontrar algunos de los conten&iacute;dos con los que me he familiarizado en la programaci&oacute;n</p>
    <h2>Python</h2>
    <p>Este es el lenguage con el que he iniciado mi camino en la programaci&oacute;n</p>
    <p>Una de sus caracteristicas es que su sintaxis es comoda para trabajar y puede procesa grandes catidades de datos sin mucho esfuerzo</p> 
    <h3>❤️</h3>
    """

def run():
    store.get_categories()


if __name__ == '__main__':
    run()