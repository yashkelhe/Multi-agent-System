from database.db import SessionLocal
from database.models import Inventory


def get_stock(product):

    db = SessionLocal()

    try:

        item = (
            db.query(Inventory)
            .filter(
                Inventory.product == product
            )
            .first()
        )

        if not item:
            return 0

        return item.stock

    finally:

        db.close()


def reduce_stock(product, qty):

    db = SessionLocal()

    try:

        item = (
            db.query(Inventory)
            .filter(
                Inventory.product == product
            )
            .first()
        )

        item.stock -= qty

        db.commit()

    finally:

        db.close()