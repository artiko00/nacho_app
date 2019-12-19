from flask import Blueprint,render_template,request

# El Objeto

tabla = {'titulo':[]
        ,'subtitulo':[]}

bp = Blueprint('principal',__name__,url_prefix='/')

@bp.route('/')
def principal():
    return render_template('prototipo.html',tabla=tabla)

@bp.route('/',methods=['POST'])
def principal_post():
    titulo = request.form['titulo'].strip()
    subtitulo = request.form['subtitulo'].strip()
    tabla['titulo'].append(titulo)
    tabla['subtitulo'].append(subtitulo)
    return render_template('prototipo.html',tabla=tabla)
