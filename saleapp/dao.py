from models import *


def load_cate():
    return Categories.query.all()


def load_prod(cate_id = None, kw = None):
    query = Products.query.filter(Products.active.__eq__(True))

    if cate_id:
        query = query.filter(Products.category_id.__eq__(cate_id))

    if kw:
        query = query.filter(Products.name.contains(kw))

    return query.all()

def load_prod_id(id):
    return Products.query.get(id)