from langgraph.graph import StateGraph
from langgraph.graph import END

from models.state import OrderState

from agents.order_agent import order_agent
from agents.inventory_agent import inventory_agent
from agents.invoice_agent import invoice_agent
from agents.approval_agent import approval_agent
from agents.supervisor_agent import supervisor_agent


def build_workflow():

    workflow = StateGraph(OrderState)

    workflow.add_node(
        "supervisor",
        supervisor_agent
    )

    workflow.add_node(
        "order",
        order_agent
    )

    workflow.add_node(
        "inventory",
        inventory_agent
    )

    workflow.add_node(
        "invoice",
        invoice_agent
    )

    workflow.add_node(
        "approval",
        approval_agent
    )

    workflow.set_entry_point(
        "order"
    )

    workflow.add_edge(
        "order",
        "supervisor"
    )

    workflow.add_edge(
        "supervisor",
        "inventory"
    )

    workflow.add_edge(
        "inventory",
        "invoice"
    )

    workflow.add_edge(
        "invoice",
        "approval"
    )

    workflow.add_edge(
        "approval",
        END
    )

    return workflow.compile()