# 🚀 AI-Powered Multi-Agent Order Management System

> A production-inspired Multi-Agent AI System built using **LangGraph**, **OpenAI Agents SDK**, **FastAPI**, **SQLAlchemy**, and **SQLite** that intelligently routes business queries to specialized AI agents capable of handling Orders, Inventory, and Invoices.

---

# 1. Project Overview

## Introduction

This project demonstrates how modern enterprises can build an **AI-native backend** using **multiple specialized AI agents** instead of relying on one large general-purpose chatbot.

Rather than asking one AI model to know everything about an entire business, this architecture follows the same principle used inside large organizations:

- Customer Support handles customer issues.
- Finance handles invoices.
- Warehouse manages inventory.
- Operations manage orders.

Similarly, this system creates **domain-specific AI agents**, each responsible for one business capability.

A central **Supervisor Agent** understands the user's request, determines which department should handle it, and delegates the task to the appropriate AI agent.

The system is orchestrated using **LangGraph**, allowing deterministic workflow execution while still leveraging LLM reasoning for decision making.

This architecture closely resembles real-world AI systems being built by companies using **OpenAI Agents SDK**, **LangGraph**, **MCP Servers**, and **Tool Calling**.

---

## What does the system do?

The application acts like an AI employee capable of answering business questions such as:

> Show me Order ORD-101

> Check inventory for Laptop

> Generate invoice for Order ORD-203

> What is the stock available for Mouse?

Instead of writing dozens of REST endpoints manually for every query, users simply communicate in natural language.

The AI understands the request, selects the correct business domain, queries the database through tools, and returns a human-readable response.

---

## Core Idea

Instead of

```
User
   ↓
One Giant AI Model
   ↓
Everything
```

the architecture becomes

```
User
   ↓
Supervisor Agent
        ↓
 ┌───────────────┐
 │Order Agent    │
 ├───────────────┤
 │Invoice Agent  │
 ├───────────────┤
 │Inventory Agent│
 └───────────────┘
```

Each agent only understands **its own business domain**, making the system more accurate, scalable, and easier to maintain.

---

# 2. Why This Project?

Traditional business applications expose dozens or even hundreds of APIs.

For example:

```
GET /orders

GET /orders/{id}

GET /inventory

GET /invoice

GET /invoice/{id}

GET /customer

...
```

As systems grow, APIs become increasingly difficult for end users to remember and consume.

Modern AI systems introduce a better interaction model:

Instead of calling APIs directly,

users simply ask:

> "Is Laptop available in inventory?"

The AI decides:

- Which department owns the information
- Which database to query
- Which tool to call
- How to present the answer

This project demonstrates that transformation.

---

## Why Multi-Agent instead of One Agent?

Imagine asking a single employee to simultaneously be:

- Accountant
- Warehouse Manager
- Sales Executive
- Customer Support
- CEO

That employee would eventually make mistakes.

The same principle applies to AI.

A single large prompt eventually becomes:

- harder to maintain
- slower
- more expensive
- more hallucination-prone

Instead, dividing responsibilities among specialized agents improves:

- Accuracy
- Maintainability
- Scalability
- Performance
- Explainability

---

# 3. Business Problem

Most enterprise systems suffer from several common problems:

### Problem 1

Business information is scattered across multiple systems.

Orders live in one database.

Inventory lives somewhere else.

Invoices are stored separately.

Users need to navigate multiple dashboards.

---

### Problem 2

Employees spend time searching for information instead of making decisions.

Example:

```
Customer:
Where is my order?

Employee:
Opens CRM

Searches Order

Checks Inventory

Checks Payment

Replies after several minutes
```

---

### Problem 3

Traditional applications require users to know:

- APIs
- Database structure
- Dashboard navigation

Business users often don't.

---

### Problem 4

Large monolithic AI assistants become difficult to scale as more departments are added.

Every new department increases prompt complexity.

Eventually the AI begins confusing one domain with another.

---

# 4. Solution Overview

This project solves the above problems by introducing a **Supervisor-Agent Architecture**.

Instead of exposing database tables directly, users interact with AI.

The workflow becomes:

```
User

↓

Supervisor Agent

↓

Identifies Intent

↓

Routes Request

↓

Specialized Agent

↓

Database Tool

↓

Response

↓

User
```

Each AI agent only knows about its own business domain.

The Supervisor Agent coordinates the overall workflow without containing business logic itself.

This separation of concerns keeps the architecture modular and scalable.

---

## Benefits

✔ Natural language interface

✔ Modular AI architecture

✔ Clear separation of responsibilities

✔ Easier debugging

✔ Production-inspired workflow

✔ Easy to extend with new departments

---

# 5. Features

### AI Capabilities

- Natural language understanding
- Intelligent routing
- Multi-Agent orchestration
- Tool calling
- Structured responses

---

### Business Agents

#### Order Agent

Responsible for:

- Fetching order details
- Checking order status
- Retrieving customer information

---

#### Inventory Agent

Responsible for:

- Product lookup
- Stock availability
- Inventory validation

---

#### Invoice Agent

Responsible for:

- Invoice lookup
- Billing amount
- Payment information

---

### LangGraph Features

- Graph-based execution
- Stateful workflows
- Deterministic routing
- Modular nodes
- Extensible architecture

---

### Backend Features

- REST API
- SQLAlchemy ORM
- SQLite Database
- FastAPI Server
- Async support
- Tool abstraction

---

# 6. Technology Stack

| Layer                 | Technology                              | Purpose                   |
| --------------------- | --------------------------------------- | ------------------------- |
| Programming Language  | Python                                  | Backend development       |
| API Framework         | FastAPI                                 | REST API                  |
| AI Framework          | OpenAI Agents SDK                       | Agent creation            |
| Workflow Engine       | LangGraph                               | Multi-agent orchestration |
| LLM                   | OpenAI / Gemini (OpenAI-compatible API) | Reasoning                 |
| ORM                   | SQLAlchemy                              | Database interaction      |
| Database              | SQLite                                  | Data persistence          |
| Validation            | Pydantic                                | Data models               |
| Dependency Management | uv / pip                                | Package management        |

---

# 7. High-Level Architecture

```text
                    +----------------------+
                    |        User          |
                    +----------+-----------+
                               |
                               |
                     Natural Language Query
                               |
                               ▼
                +------------------------------+
                |         FastAPI Server       |
                +--------------+---------------+
                               |
                               ▼
                +------------------------------+
                |      LangGraph Workflow      |
                +--------------+---------------+
                               |
                               ▼
                +------------------------------+
                |      Supervisor Agent        |
                +--------------+---------------+
                               |
             decides which specialized agent
             should handle the request
                               |
      ┌───────────────┬───────────────┬───────────────┐
      ▼               ▼               ▼
+-------------+ +-------------+ +-------------+
| Order Agent | |Invoice Agent| |Inventory Ag.|
+------+------+ +------+------+ +------+------+
       |               |               |
       ▼               ▼               ▼
 Order Tools      Invoice Tools   Inventory Tools
       |               |               |
       └───────────────┼───────────────┘
                       ▼
             SQLAlchemy Database Layer
                       ▼
                  SQLite Database
                       ▼
                  Response Returned
```

---

# 8. Complete Workflow Diagram

```text
                  User asks a question
                           |
                           ▼
               FastAPI receives request
                           |
                           ▼
            LangGraph creates initial state
                           |
                           ▼
                Supervisor analyzes query
                           |
           +---------------+----------------+
           |               |                |
           ▼               ▼                ▼
     Order Intent    Invoice Intent   Inventory Intent
           |               |                |
           ▼               ▼                ▼
     Order Agent     Invoice Agent   Inventory Agent
           |               |                |
           ▼               ▼                ▼
     Tool Execution  Tool Execution  Tool Execution
           |               |                |
           ▼               ▼                ▼
      SQLAlchemy ORM accesses SQLite database
                           |
                           ▼
                Structured business result
                           |
                           ▼
                LangGraph updates state
                           |
                           ▼
                 Final response to user
```

---

# 9. Multi-Agent Architecture

```text
                     Supervisor Agent
                            |
      +---------------------+----------------------+
      |                     |                      |
      ▼                     ▼                      ▼
+--------------+     +--------------+     +--------------+
| Order Agent  |     |Invoice Agent |     |Inventory Ag. |
+--------------+     +--------------+     +--------------+
| Order Tools  |     |Invoice Tools |     |InventoryTool |
+--------------+     +--------------+     +--------------+
        |                    |                    |
        +--------- Database Layer ---------------+
```

## Responsibilities

### Supervisor Agent

- Understands user intent
- Routes requests
- Manages orchestration
- Coordinates workflow

### Order Agent

- Order retrieval
- Customer lookup
- Order status

### Invoice Agent

- Invoice information
- Payment amount
- Billing details

### Inventory Agent

- Product lookup
- Stock verification
- Availability checks

---

# 10. LangGraph State Management

The entire workflow is driven by a shared state object.

Each node reads the current state, performs its task, and updates the state before passing execution to the next node.

```text
Initial State

↓

User Query

↓

Intent

↓

Selected Agent

↓

Tool Output

↓

Final Response
```

### Example State

```python
{
    "query": "Check stock for Laptop",
    "intent": "inventory",
    "selected_agent": "inventory_agent",
    "tool_result": {
        "product": "Laptop",
        "stock": 25
    },
    "response": "Laptop has 25 units available."
}
```

This centralized state ensures every node operates on the latest information without tightly coupling components together.

---

# 11. Database Design

The project uses a lightweight relational database modeled around three core business entities.

```text
                 +----------------+
                 |    Orders      |
                 +----------------+
                 | id             |
                 | order_id       |
                 | customer       |
                 | status         |
                 +----------------+

                 +----------------+
                 |   Invoices     |
                 +----------------+
                 | id             |
                 | order_id       |
                 | amount         |
                 +----------------+

                 +----------------+
                 |   Inventory    |
                 +----------------+
                 | id             |
                 | product        |
                 | stock          |
                 +----------------+
```

### Entity Relationships

```text
Orders
   |
   | order_id
   |
Invoices

Inventory remains independent and is queried by product name.
```

---

# 12. API Architecture

The API layer acts as the gateway between users and the multi-agent system.

```text
Client

↓

POST /chat

↓

FastAPI

↓

LangGraph

↓

Supervisor

↓

Specialized Agent

↓

Database

↓

JSON Response
```

### Example Request

```json
{
  "message": "Show invoice for order ORD-101"
}
```

### Example Response

```json
{
  "agent": "invoice_agent",
  "response": "Invoice amount for ORD-101 is $420.50"
}
```

The API remains intentionally minimal: clients send natural language, while the backend handles routing, reasoning, tool execution, and response generation transparently.

# 13. Folder Structure

A clean and modular project structure is one of the most important aspects of building scalable AI applications. Each folder in this project has a single responsibility, making the system easy to understand, extend, and maintain.

```text
multi-agent-system/
│
├── agents/
│   ├── supervisor.py
│   ├── order_agent.py
│   ├── invoice_agent.py
│   └── inventory_agent.py
│
├── graph/
│   ├── builder.py
│   ├── nodes.py
│   └── state.py
│
├── database/
│   ├── db.py
│   ├── models.py
│   ├── seed.py
│   └── tools.py
│
├── api/
│   └── routes.py
│
├── schemas/
│   └── request.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## Folder Explanation

### `agents/`

Contains all AI agents used by the system.

- Supervisor Agent
- Order Agent
- Invoice Agent
- Inventory Agent

Each agent is responsible for a single business domain.

---

### `graph/`

Contains the complete LangGraph workflow.

Responsible for:

- Graph creation
- State management
- Workflow execution
- Node definitions

---

### `database/`

Contains all database-related code.

Includes:

- SQLAlchemy models
- Database connection
- Tool functions
- Seed data

---

### `api/`

Contains FastAPI routes.

Acts as the public entry point into the AI system.

---

### `schemas/`

Contains Pydantic request and response models.

Responsible for validating incoming API requests.

---

### `main.py`

Application entry point.

Starts the FastAPI server and initializes the application.

---

# 14. Agent Responsibilities

The system follows a **Supervisor → Specialized Agent** architecture.

Each AI agent owns one business capability.

---

## Supervisor Agent

### Responsibility

The Supervisor Agent acts as the orchestrator of the entire system.

It never queries the database directly.

Instead, it:

- Reads the user query
- Understands user intent
- Chooses the correct business agent
- Routes execution

Example:

```text
User:
Show invoice for Order ORD-105

↓

Supervisor

↓

Invoice Agent
```

---

## Order Agent

Responsible for:

- Finding orders
- Order status
- Customer information
- Order lookup

Example queries

```text
Show order ORD-100

Where is my order?

Who placed ORD-103?
```

---

## Invoice Agent

Responsible for:

- Invoice lookup
- Order billing
- Invoice amount
- Payment details

Example queries

```text
Generate invoice

Invoice amount

Billing details
```

---

## Inventory Agent

Responsible for:

- Product lookup
- Stock verification
- Inventory availability

Example queries

```text
Check Laptop stock

How many Mouse are available?

Inventory for Keyboard
```

---

# 15. Workflow Execution

The following diagram illustrates how every request moves through the system.

```text
User
 │
 ▼
FastAPI receives request
 │
 ▼
LangGraph creates initial state
 │
 ▼
Supervisor Agent
 │
 ▼
Intent Classification
 │
 ├──────────────┐
 ▼              ▼
Order      Invoice      Inventory
Agent       Agent          Agent
 │            │              │
 ▼            ▼              ▼
Database Tools (SQLAlchemy)
 │
 ▼
SQLite Database
 │
 ▼
Business Result
 │
 ▼
LangGraph updates state
 │
 ▼
Response returned to FastAPI
 │
 ▼
Client receives answer
```

---

## Internal Execution Flow

Every request follows exactly the same lifecycle.

1. Receive user query.
2. Create LangGraph state.
3. Execute Supervisor node.
4. Determine user intent.
5. Route to specialized agent.
6. Execute database tools.
7. Update graph state.
8. Generate final response.
9. Return JSON response.

This deterministic workflow ensures predictable and debuggable execution.

---

# 16. Example Execution

## Example 1

### User Request

```text
Check stock for Laptop
```

Execution

```text
User

↓

Supervisor Agent

↓

Inventory Intent

↓

Inventory Agent

↓

Inventory Tool

↓

SELECT * FROM inventory
WHERE product='Laptop'

↓

Stock = 24

↓

Response Generated

↓

Laptop has 24 units available.
```

---

## Example 2

### User Request

```text
Show Order ORD-102
```

Execution

```text
User

↓

Supervisor

↓

Order Agent

↓

Order Tool

↓

Orders Table

↓

Return Order Details

↓

Response
```

---

## Example 3

### User Request

```text
Show invoice for ORD-205
```

Execution

```text
User

↓

Supervisor

↓

Invoice Agent

↓

Invoice Tool

↓

Invoices Table

↓

Amount Found

↓

Response
```

---

# 17. API Endpoints

The project exposes a minimal REST API that accepts natural language queries.

---

## Health Check

```http
GET /
```

Response

```json
{
  "message": "AI Multi-Agent System Running"
}
```

---

## Chat Endpoint

```http
POST /chat
```

### Request

```json
{
  "message": "Check stock for Laptop"
}
```

---

### Response

```json
{
  "agent": "inventory_agent",
  "response": "Laptop has 24 units available."
}
```

---

## Why only one endpoint?

Unlike traditional applications that expose dozens of endpoints, this architecture exposes a single intelligent endpoint.

The AI decides:

- Which business domain is relevant.
- Which tools to execute.
- Which data source to query.
- How to present the response.

This dramatically simplifies API design while providing a more natural user experience.

---

# 18. Database Tables

The application uses three business tables.

---

## Orders

Stores customer order information.

| Column   | Type    | Description          |
| -------- | ------- | -------------------- |
| id       | Integer | Primary Key          |
| order_id | String  | Business Order ID    |
| customer | String  | Customer Name        |
| status   | String  | Current Order Status |

---

## Invoices

Stores billing information.

| Column   | Type    | Description    |
| -------- | ------- | -------------- |
| id       | Integer | Primary Key    |
| order_id | String  | Related Order  |
| amount   | Float   | Invoice Amount |

---

## Inventory

Stores product stock information.

| Column  | Type    | Description        |
| ------- | ------- | ------------------ |
| id      | Integer | Primary Key        |
| product | String  | Product Name       |
| stock   | Integer | Available Quantity |

---

## Entity Relationship

```text
Orders
   │
   │ order_id
   │
Invoices

Inventory is independent.
```

---

# 19. Running the Project

## Clone Repository

```bash
git clone <repository-url>

cd multi-agent-system
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key

MODEL=gpt-4.1-mini
```

> If using Gemini through the OpenAI-compatible endpoint, configure the appropriate `base_url`, model name, and API key according to your provider.

---

## Seed Database

```bash
python database/seed.py
```

---

## Run Application

```bash
uvicorn main:app --reload
```

---

## Open API Documentation

FastAPI automatically generates interactive API documentation.

```
http://localhost:8000/docs
```

---

# 20. Screenshots Placeholder

Include screenshots after running the project.

Suggested images:

```
📷 Project Architecture

📷 LangGraph Flow

📷 Swagger UI

📷 Terminal Output

📷 Chat API Response

📷 Database Tables

📷 Agent Routing Example

📷 Supervisor Decision Flow
```

A visual walkthrough significantly improves the readability and professionalism of the repository.

---

# 21. Future Improvements

This project provides a strong foundation for enterprise AI systems.

Potential future enhancements include:

### Authentication

- JWT Authentication
- OAuth
- Role-Based Access Control (RBAC)

---

### Memory

- Conversation history
- User preferences
- Persistent memory
- Context-aware interactions

---

### Multi-Step Planning

Allow the Supervisor Agent to coordinate multiple agents in a single request.

Example:

```text
Find Order

↓

Check Inventory

↓

Generate Invoice

↓

Send Email
```

---

### Additional Business Agents

Examples:

- Customer Agent
- Shipping Agent
- Payment Agent
- HR Agent
- Sales Agent
- CRM Agent
- Analytics Agent

---

### RAG Integration

Connect enterprise knowledge sources.

Examples:

- PDFs
- Policies
- Documentation
- Wikis
- SharePoint
- Confluence

---

### Observability

- LangSmith
- OpenTelemetry
- Agent tracing
- Token monitoring
- Cost analysis

---

# 22. Production Improvements

To deploy this architecture in production, additional capabilities would be required.

## Infrastructure

- PostgreSQL instead of SQLite
- Redis for caching
- Docker
- Kubernetes
- CI/CD pipelines

---

## Reliability

- Retry mechanisms
- Circuit breakers
- Timeouts
- Graceful error handling

---

## Security

- API authentication
- Secrets management
- Audit logs
- Request validation
- Rate limiting

---

## Monitoring

- Centralized logging
- Metrics collection
- Health checks
- Performance dashboards
- Alerting

---

## AI Enhancements

- Model fallbacks
- Multi-model routing
- Prompt versioning
- Human-in-the-loop review
- Tool usage analytics

---

## Scalability

- Distributed workers
- Queue-based execution
- Horizontal scaling
- Async tool execution

These improvements align the architecture with patterns commonly used in production AI platforms.

---

# 23. Learning Outcomes

This project demonstrates practical concepts used in modern AI application development.

After completing this project, you will understand:

- Multi-Agent system design
- LangGraph workflow orchestration
- AI agent routing
- State management with LangGraph
- Tool calling patterns
- SQLAlchemy ORM integration
- FastAPI application development
- Modular software architecture
- Prompt engineering for specialized agents
- Enterprise API design
- Separation of concerns
- Production-oriented project organization

Beyond learning individual technologies, this project highlights how they work together to build intelligent, maintainable, and extensible AI systems.

---

# 24. License

This project is released under the **MIT License**.

You are free to:

- Use
- Modify
- Distribute
- Extend

