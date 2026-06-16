import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT))

import streamlit as st
import requests

st.title("Order To Cash AI")

customer = st.text_input(
    "Customer"
)

laptop_qty = st.number_input(
    "Laptop Quantity",
    min_value=0,
    value=1
)

if st.button("Submit Order"):

    payload = {

        "order_id": "ORD-1001",

        "customer": customer,

        "items": [
            {
                "product": "Laptop",
                "quantity": laptop_qty
            }
        ]
    }

    response = requests.post(
        "http://127.0.0.1:8000/orders",
        json=payload
    )

    result = response.json()

    st.success("Workflow Completed")

    st.subheader("Inventory Agent")

    st.write(
        result["inventory_reasoning"]
    )

    st.subheader("Invoice Agent")

    st.write(
        result["invoice_reasoning"]
    )

    st.subheader("Approval Agent")

    st.write(
        result["approval_reasoning"]
    )

    st.subheader("Audit Logs")

    st.json(
        result["audit_logs"]
    )