from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/projetos')
def projetos():
   return render_template('projeto.html')

@app.route('/voluntariado')
def voluntariado():
   return render_template('voluntariado.html')


if __name__ == "__main__":
   app.run(degub=True)