from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    risultato = None
    if request.method == 'POST':
        # Il trucco è qui: ignora tutto e restituisce sempre 24
        risultato = 24
        
    return render_template('index.html', risultato=risultato)

if __name__ == '__main__':
    app.run(debug=False)
