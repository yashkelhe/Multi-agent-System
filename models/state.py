
from typing import TypedDict, List, Dict, Any



class OrderState(TypedDict):

    order_id: str

    customer: str

    items: List[Dict[str, Any]]

    inventory_status: str

    invoice_total: float

    approval_required: bool

    approved: bool

    retry_count: int

    status: str

    inventory_reasoning: str

    invoice_reasoning: str

    approval_reasoning: str

    supervisor_reasoning: str

    audit_logs: list

    error: str