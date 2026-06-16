from workflows.order_workflow import build_workflow

graph = build_workflow()

sample_order = {
    "order_id": "ORD-1001",
    "customer": "Tesla",
    "items": [
        {
            "product": "Laptop",
            "quantity": 3
        },
        {
            "product": "Mouse",
            "quantity": 2
        }
    ],
    "inventory_status": "",
    "invoice_total": 0,
    "approval_required": False,
    "approved": False,
    "retry_count": 0,
    "status": "",
    "audit_logs": [],
    "error": "",
    "approval_required": False,
    "approved": False,
    "retry_count": 0,

    "inventory_reasoning": "",
    "invoice_reasoning": "",
    "approval_reasoning": "",
    "supervisor_reasoning": "",
}

result = graph.invoke(sample_order)

print(result)