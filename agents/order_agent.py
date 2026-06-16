from services.audit_service import add_audit_log


def order_agent(state):

    try:

        if not state["order_id"]:
            raise ValueError("Missing Order ID")

        if not state["customer"]:
            raise ValueError("Missing Customer")

        if not state["items"]:
            raise ValueError("Order contains no items")

        for item in state["items"]:

            if item["quantity"] <= 0:
                raise ValueError(
                    f"Invalid quantity for {item['product']}"
                )

        state["status"] = "ORDER_VALIDATED"

        add_audit_log(
            state,
            "Order Agent validated order"
        )

        return state

    except Exception as e:

        state["status"] = "FAILED"

        state["error"] = str(e)

        add_audit_log(
            state,
            f"Order validation failed: {e}"
        )

        return state