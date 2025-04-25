from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/calculomedia", methods=['POST'])
def calcularmedia():
    situacao = ""
    nota1 = float(request.form['nota1'])
    nota2 = float(request.form['nota2'])
    nota3 = float(request.form['nota3'])

    media = round(((nota1+nota2+nota3)/3),2)


    if media >= 7:
        situacao = "Aprovado"

    else:
        situacao = "Reprovado"

    resultado = f"{media} e {situacao}"

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)