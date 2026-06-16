from services.audit_service import add_audit_log


def supervisor_agent(state):

    state["supervisor_reasoning"] = (
        f"Supervisor reviewed status: "
        f"{state['status']}"
    )

    add_audit_log(
        state,
        "Supervisor reviewed workflow",
        "SUPERVISOR"
    )

    return state