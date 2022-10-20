import json
from saleappv1 import app


def load_data():
    with open("%s/data/categories.json" % app.root_path, encoding="utf8") as f:
        categories = json.load(f)
        return categories


def load_product():
    with open(f"{app.root_path}/data/product.json", encoding="utf8") as f:
        return json.load(f)