from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Questa funzione dice a Python di caricare la tua pagina HTML
    return render_template('index.html')

if __name__ == '__main__':
    # Avvia il server in modalità debug per vedere le modifiche in tempo reale
    app.run(debug=True)
