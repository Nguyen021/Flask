from flask import render_template, request

from saleapp import app
from saleapp import dao


@app.route("/")
def home():
    cate = dao.load_categories()

    produ = dao.load_products(cate_id=request.args.get("category_id"))
    return render_template('index.html', categories=cate, products=produ)


if __name__ == '__main__':
    app.run(debug=True)
