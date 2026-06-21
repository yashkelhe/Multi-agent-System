# AI Multi-Agent Order Management System

> Route natural language queries to specialized AI agents across Orders, Inventory, and Invoices — powered by **LangGraph**, **OpenAI Agents SDK**, and **FastAPI**.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-1C3C3C?style=flat)](https://langchain-ai.github.io/langgraph/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

---

## The Problem

**This project replaces that workflow with a single natural language interface.** Users just ask a question. The system figures out which business domain owns the answer, queries the right data, and responds — no API knowledge, no dashboard navigation required.

---

## What This Is

Instead of maintaining dozens of REST endpoints, users send a single natural language message. A **Supervisor Agent** understands the intent and delegates to the right specialist:

```
User: "Is Laptop in stock?"
         │
         ▼
  Supervisor Agent          ← understands intent, routes request
         │
   ┌─────┴──────────────┐
   ▼                     ▼                     ▼
Order Agent        Invoice Agent        Inventory Agent
   │                     │                     │
   └─────────────────────┴─────────────────────┘
                         │
                  SQLite via SQLAlchemy
                         │
         "Laptop has 24 units available."
```

Each agent is **domain-scoped** — it only knows its own data, tools, and business rules. This mirrors how real enterprise teams are structured (Finance, Warehouse, Operations), and how Oracle's own AI Agent Studio works.

---

## Tech Stack

| Layer         | Technology                          | Purpose                       |
| ------------- | ----------------------------------- | ----------------------------- |
| Language      | Python 3.11+                        | Core backend                  |
| API           | FastAPI                             | REST interface                |
| AI Agents     | OpenAI Agents SDK                   | Agent creation & tool calling |
| Orchestration | LangGraph                           | Stateful multi-agent workflow |
| LLM           | OpenAI / Gemini (OpenAI-compatible) | Reasoning                     |
| ORM           | SQLAlchemy                          | Database access               |
| Database      | SQLite                              | Data persistence              |
| Validation    | Pydantic                            | Request/response schemas      |

---

## Architecture

```
                    ┌──────────────────┐
                    │   FastAPI /chat  │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  LangGraph Graph │  ← stateful workflow
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │ Supervisor Agent │  ← intent detection + routing
                    └──┬───────┬───────┘
                       │       │       │
              ┌────────▼┐ ┌───▼────┐ ┌▼──────────┐
              │  Order  │ │Invoice │ │ Inventory │
              │  Agent  │ │ Agent  │ │   Agent   │
              └────┬────┘ └───┬────┘ └─────┬─────┘
                   │          │             │
              ┌────▼──────────▼─────────────▼────┐
              │         SQLAlchemy ORM            │
              └──────────────┬────────────────────┘
                             │
                      SQLite Database
```

### LangGraph State

The graph passes a single shared state object through each node:

```python
{
    "query": "Check stock for Laptop",
    "intent": "inventory",
    "selected_agent": "inventory_agent",
    "tool_result": { "product": "Laptop", "stock": 25 },
    "response": "Laptop has 25 units available."
}
```

---

## Project Structure

```
multi-agent-system/
│
├── agents/
│   ├── supervisor.py        # Intent detection + routing logic
│   ├── order_agent.py
│   ├── invoice_agent.py
│   └── inventory_agent.py
│
├── graph/
│   ├── builder.py           # LangGraph graph construction
│   ├── nodes.py             # Node definitions
│   └── state.py             # Shared state schema
│
├── database/
│   ├── db.py                # SQLAlchemy engine + session
│   ├── models.py            # ORM models
│   ├── seed.py              # Seed data
│   └── tools.py             # Agent-callable DB tools
│
├── api/
│   └── routes.py            # FastAPI route handlers
│
├── schemas/
│   └── request.py           # Pydantic request models
│
├── main.py
├── requirements.txt
└── .env
```

---

## Quickstart

**1. Clone & enter the repo**

```bash
git clone <repository-url>
cd multi-agent-system
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
MODEL=gpt-4.1-mini
```

> Using Gemini? Set the matching `base_url`, model name, and API key for the OpenAI-compatible endpoint.

**5. Seed the database**

```bash
python database/seed.py
```

**6. Run the server**

```bash
uvicorn main:app --reload

streamlit run ui/dashboard.py
```

**7. Open interactive docs**

```
http://localhost:8000/docs
```

---

## API

The system exposes two endpoints.

### `GET /` — Health check

```json
{ "message": "AI Multi-Agent System Running" }
```

### `POST /chat` — Send a query

**Request**

```json
{ "message": "Check stock for Laptop" }
```

**Response**

```json
{
  "agent": "inventory_agent",
  "response": "Laptop has 24 units available."
}
```

**Example queries to try**

```
"Show me order ORD-101"
"What is the invoice amount for ORD-203?"
"Is a Mouse in stock?"
"Check inventory for Keyboard"
"What's the status of order ORD-305?"
```

---

## Database Schema

**Orders**

| Column   | Type    | Description                      |
| -------- | ------- | -------------------------------- |
| id       | Integer | Primary key                      |
| order_id | String  | Business order ID (e.g. ORD-101) |
| customer | String  | Customer name                    |
| status   | String  | Order status                     |

**Invoices**

| Column   | Type    | Description                |
| -------- | ------- | -------------------------- |
| id       | Integer | Primary key                |
| order_id | String  | References Orders.order_id |
| amount   | Float   | Billing amount             |

**Inventory**

| Column  | Type    | Description     |
| ------- | ------- | --------------- |
| id      | Integer | Primary key     |
| product | String  | Product name    |
| stock   | Integer | Available units |

---

## License

MIT — free to use, modify, and distribute.
