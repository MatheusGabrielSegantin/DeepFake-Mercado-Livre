from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)


app.config['SECRET_KEY'] = 'Aqui_e_a_chave_do_grupo'

host = 'localhost'
database = r'C:\Users\Aluno\Downloads\BANCO.FDB'
user = 'SYSDBA'
password = 'sysdba'



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/endereco')
def novo_usu():
    return render_template('endereco.html')

@app.route('/adicionar_endereco', methods=['POST'])
def adicionar_endereco():
    cep = request.form['cep']
    email = request.form['email']
    senha = request.form['senha']

    cursor = con.cursor()

    try:
        cursor.execute("""SELECT 1 FROM usuario u WHERE nome = ?""", (nome,))
        if cursor.fetchone():
            flash('Erro: Usuário já cadastrado')
            return redirect(url_for('novo_usu'))

        cursor.execute( """ INSERT INTO usuario (nome,email,senha)
                            VALUES (?, ? ,?)""", (nome, email, senha))

        con.commit()
        flash("Usuário cadastrado com sucesso")
        return redirect(url_for('lista_usu'))

    except Exception as e:
        flash(f"Ocorreu um error -> {e}")
        con.rollback()
        return redirect(url_for('novo_usu'))

    finally:
        cursor.close()


if __name__ == '__main__':
    app.run(debug=True)