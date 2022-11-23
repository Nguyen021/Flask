from __init__ import app
from flask import render_template, request
import dao
import admin


@app.route('/', methods=['POST', 'GET'])
def index():
    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')

    prod = dao.load_prod(cate_id, kw)
    return render_template('index.html', products=prod)


@app.route('/products/<int:id>')
def details(id):
    p = dao.load_prod_id(id=id)
    return render_template('details.html', product=p)


@app.context_processor
def common():
    category = dao.load_cate()
    return {
        'categories': category
    }


# @app.route('/admin-login/')
if __name__ == '__main__':
    app.run(debug=True, port=5222)