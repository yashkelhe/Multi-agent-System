from services.audit_service import add_audit_log
from services.llm_service import ask_llm

from services.inventory_service import (
    get_stock,
    reduce_stock
)


def inventory_agent(state):

    try:

        inventory_snapshot = []

        for item in state["items"]:

            inventory_snapshot.append(
                {
                    "product": item["product"],
                    "stock": get_stock(
                        item["product"]
                    )
                }
            )

        prompt = f"""
You are an enterprise inventory agent.

Inventory:

{inventory_snapshot}

Customer Order:

{state['items']}

Tasks:

1. Check inventory availability
2. Explain your reasoning
3. Mention any stock risks

Keep answer under 100 words.
"""

        reasoning = ask_llm(prompt)

        state["inventory_reasoning"] = reasoning

        available = True

        for item in state["items"]:

            stock = get_stock(
                item["product"]
            )

            if stock < item["quantity"]:

                available = False

                break

        if available:

            for item in state["items"]:

                reduce_stock(
                    item["product"],
                    item["quantity"]
                )

            state["inventory_status"] = "AVAILABLE"

            state["status"] = "INVENTORY_VERIFIED"

        else:

            state["inventory_status"] = "OUT_OF_STOCK"

            state["status"] = "FAILED"

        add_audit_log(
            state,
            "Inventory Agent completed",
            "INVENTORY_AGENT"
        )

        return state

    except Exception as e:

        state["status"] = "FAILED"

        state["error"] = str(e)

        return state