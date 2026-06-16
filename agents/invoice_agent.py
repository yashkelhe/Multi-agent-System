from services.audit_service import add_audit_log
from services.llm_service import ask_llm


PRICE_LIST = {
    "Laptop": 1000,
    "Mouse": 20,
    "Keyboard": 50
}


def invoice_agent(state):

    try:

        total = 0

        for item in state["items"]:

            total += (
                PRICE_LIST[item["product"]]
                * item["quantity"]
            )

        state["invoice_total"] = total

        prompt = f"""
You are a finance invoice agent.

Customer:

{state['customer']}

Items:

{state['items']}

Total:

${total}

Generate:

1. Invoice summary
2. Business explanation
3. Pricing explanation

Keep under 100 words.
"""

        reasoning = ask_llm(prompt)

        state["invoice_reasoning"] = reasoning

        state["status"] = "INVOICE_GENERATED"

        add_audit_log(
            state,
            f"Invoice Generated ${total}",
            "INVOICE_AGENT"
        )

        return state

    except Exception as e:

        state["status"] = "FAILED"

        state["error"] = str(e)

        return state