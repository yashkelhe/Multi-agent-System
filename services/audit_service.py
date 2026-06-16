from datetime import datetime


from datetime import datetime


def add_audit_log(
    state,
    event: str,
    agent: str = "SYSTEM"
):

    state["audit_logs"].append(
        {
            "timestamp": datetime.utcnow().isoformat(),
            "agent": agent,
            "event": event
        }
    )

    return state

