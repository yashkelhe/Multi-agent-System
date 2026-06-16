from fastapi import APIRouter

from models.order import OrderRequest

from workflows.order_workflow import build_workflow

router = APIRouter()

graph = build_workflow()


@router.get("/")
def health():

    return {
        "status": "healthy"
    }


@router.post("/orders")
def create_order(order: OrderRequest):

    state = {

        "order_id": order.order_id,

        "customer": order.customer,

        "items": [
            item.model_dump()
            for item in order.items
        ],

        "inventory_status": "",

        "invoice_total": 0,

        "approval_required": False,

        "approved": False,

        "retry_count": 0,

        "status": "",

        "inventory_reasoning": "",

        "invoice_reasoning": "",

        "approval_reasoning": "",

        "supervisor_reasoning": "",

        "audit_logs": [],

        "error": ""
    }

    result = graph.invoke(state)

    return result


@router.post(
    "/approve/{order_id}"
)
def approve_order(order_id: str):

    return {
        "order_id": order_id,
        "approved": True
    }