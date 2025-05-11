from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular():
    resultado = None
    if request.method == 'POST':
        valor_inicial = float(request.form['valor_inicial'])
        taxa_juros = float(request.form['taxa_juros']) / 100
        tempo = int(request.form['tempo'])

        # Fórmula de juros compostos: VF = VI * (1 + i) ** t
        resultado = valor_inicial * (1 + taxa_juros) ** tempo

    return render_template('page.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
