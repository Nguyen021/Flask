from flask import render_template

from saleappv1 import app, dao


@app.route("/")
def index():
    data = dao.load_data()
    product = dao.load_product()
    return render_template('index.html', cate=data, products=product)


if __name__ == '__main__':
    app.run(debug=True)
