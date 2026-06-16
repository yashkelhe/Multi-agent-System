from database.db import SessionLocal
from database.models import Inventory


def seed_inventory():

    db = SessionLocal()

    try:

        if db.query(Inventory).count() == 0:

            items = [

                Inventory(
                    product="Laptop",
                    stock=10
                ),

                Inventory(
                    product="Mouse",
                    stock=50
                ),

                Inventory(
                    product="Keyboard",
                    stock=20
                )
            ]

            db.add_all(items)

            db.commit()

            print("Inventory seeded")

    finally:

        db.close()