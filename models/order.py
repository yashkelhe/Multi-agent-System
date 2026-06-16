from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):

    product: str

    quantity: int


class OrderRequest(BaseModel):

    order_id: str

    customer: str

    items: List[OrderItem]