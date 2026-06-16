from database.models import Base
from database.db import engine

from services.inventory_seed import seed_inventory

Base.metadata.create_all(bind=engine)

seed_inventory()