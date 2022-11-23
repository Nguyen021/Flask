from sqlalchemy import Column, Integer, String, Text, Float, Boolean, orm, ForeignKey
from __init__ import db, app


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)


class Categories(Base):
    __tablename__ = 'Categories'

    name = Column(String(100), nullable=False)
    products = orm.relationship('Products', backref='category', lazy = True)

    def __repr__(self):
        return '<Categories %r>' %self.name

class Products(Base):
    __tablename__ = 'Products'


    name = Column(String(200), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Categories.id), nullable=False)

    def __repr__(self):
        return '<Products %r>' % self.name


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Categories(name="Điện Thoại")
        # c2 = Categories(name="Máy Tính Bảng")
        # c3 = Categories(name="Tablet")
        # c4 = Categories(name="Phụ Kiện")

        # c1 = Categories.query.get(5)
        # c2 = Categories.query.get(6)
        # c3 = Categories.query.get(7)
        # c4 = Categories.query.get(8)


        # db.session.delete_all([c1,c2,c3,c4])
        # db.session.commit()

        Categories.query.filter(Categories.id > 4).delete()
        db.session.commit()
        p1 = Products(name='Galaxy S22 Pro 1', description='Samsung, 128GB', price=25000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=1)
        p2 = Products(name='Galaxy Fold 4S', description='Samsung, 128GB', price=38000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',
                     category_id=4)
        p3 = Products(name='Apple Watch S5S', description='Apple, 32GB', price=18000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=3)
        p4 = Products(name='Galaxy Tab S8S', description='Samsung, 128GB', price=22000000,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=2)

        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()