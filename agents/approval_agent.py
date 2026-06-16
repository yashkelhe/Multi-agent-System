from services.audit_service import add_audit_log
from services.llm_service import ask_llm


APPROVAL_LIMIT = 5000


def approval_agent(state):

    try:

        prompt = f"""
You are a finance approval agent.

Customer:

{state['customer']}

Order Value:

${state['invoice_total']}

Policy:

Orders above $5000 require approval.

Determine:

1. Approval Required?
2. Risk Level
3. Explanation

Keep under 100 words.
"""

        reasoning = ask_llm(prompt)

        state["approval_reasoning"] = reasoning

        if state["invoice_total"] > APPROVAL_LIMIT:

            state["approval_required"] = True

            state["approved"] = False

        else:

            state["approval_required"] = False

            state["approved"] = True

        state["status"] = "APPROVED"

        add_audit_log(
            state,
            "Approval Agent completed",
            "APPROVAL_AGENT"
        )

        return state

    except Exception as e:

        state["status"] = "FAILED"

        state["error"] = str(e)

        return state