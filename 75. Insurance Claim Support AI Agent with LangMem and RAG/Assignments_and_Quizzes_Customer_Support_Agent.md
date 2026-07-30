# Assignments and Quizzes: Insurance Claims Support AI Agent with LangMem and RAG

## Part 1: Assignments (Practical Implementation)

These assignments are aligned to the current project: an insurance-claims support copilot built with FastAPI, Streamlit, Groq, LangMem, ChromaDB, and SQLite.

---

### Assignment 1: Add a New Tool - Claim Risk and Escalation Analyzer
**Objective**: Extend the copilot with risk-aware claim handling support.

- **Task**:
  1. Create a new file `customer_support_agent/integrations/tools/claim_risk_tools.py`.
  2. Implement a function `analyze_claim_risk(subject: str, description: str)`.
  3. Decorate it with `@tool` from LangChain.
  4. Return structured JSON with:
     - `risk_level`
     - `confidence`
     - `fraud_signals`
     - `summary`
     - `recommended_action`
  5. Register this tool in `customer_support_agent/integrations/tools/support_tools.py`.
  6. Ensure the tool can appear in `tool_calls` inside `context_used`.
  7. Test with examples such as:
     - `"Vehicle was stolen last night and all keys are missing."`
     - `"Minor bumper scratch in parking lot."`

- **Deliverable**:
  - New tool file
  - Updated tool registry
  - Example draft context showing tool execution

- **Bonus**:
  - Add keyword fallback rules for risk scoring
  - Add a "high-risk claim" highlight in Streamlit

---

### Assignment 2: Improve LangMem Reliability and Observability
**Objective**: Make memory behavior safer and more transparent in production-style runs.

- **Task**:
  1. Update `customer_support_agent/services/copilot_service.py` so memory access degrades gracefully if LangMem or embedding initialization is unavailable.
  2. Guard memory usage in:
     - `_search_memory_scopes()`
     - `list_customer_memories()`
     - `save_accepted_resolution()`
  3. Add explicit markers in `context_used["errors"]` when memory is skipped.
  4. Add runtime fields in `context_used["signals"]` such as:
     - `memory_enabled`
     - `memory_backend`
     - `memory_query_time_ms`
  5. Update memory API responses to include a note when semantic memory is unavailable.
  6. Test both modes:
     - with `GOOGLE_API_KEY`
     - without `GOOGLE_API_KEY`

- **Deliverable**:
  - Updated memory-safe copilot behavior
  - Demo of working draft generation with semantic memory enabled
  - Demo of working draft generation with fallback memory mode

- **Bonus**:
  - Add a small health/debug endpoint for memory backend status

---

### Assignment 3: Add Full Draft Lifecycle and History Support
**Objective**: Make the draft workflow more realistic for insurance operations.

- **Task**:
  1. Add `POST /api/drafts/{draft_id}/regenerate`.
  2. Add `POST /api/drafts/{draft_id}/mark-pending`.
  3. Add repository method `get_all_for_ticket(ticket_id)`.
  4. Add `GET /api/tickets/{ticket_id}/draft-history`.
  5. Update `app.py` to:
     - display draft history
     - allow selection of previous versions
     - regenerate from current claim context
  6. Ensure accepted drafts still:
     - set ticket status to `resolved`
     - save accepted resolution into LangMem

- **Deliverable**:
  - Updated routers, repositories, and services
  - UI demo showing multiple draft versions

- **Bonus**:
  - Add "adjuster notes" on approval and store them in `context_used`

---

### Assignment 4: Expand Testing for Core Insurance Workflows
**Objective**: Improve confidence in the most important paths.

- **Task**:
  1. Expand `tests/` with at least 6 additional tests:
     - `test_health.py`
     - `test_tickets_api.py`
     - `test_drafts_api.py`
     - `test_knowledge_service.py`
     - `test_support_tools.py`
     - `test_customers_repository.py`
  2. Add tests for:
     - LangMem fallback mode
     - accepted-draft memory persistence
     - claim history search behavior
  3. Mock Groq and external embedding dependencies where needed.
  4. Add clean pytest config in `pyproject.toml`.
  5. Run `uv run pytest -v`.

- **Deliverable**:
  - Minimum 6 meaningful passing tests
  - Test output log
  - Updated test configuration if needed

- **Bonus**:
  - Add coverage reporting with `pytest --cov`

---

### Assignment 5: Strengthen Claims-Specific RAG and KB Quality
**Objective**: Improve retrieval quality for insurance claim recommendations.

- **Task**:
  1. Add at least 3 more insurance knowledge documents under `knowledge_base/`.
  2. Improve metadata in `customer_support_agent/integrations/rag/chroma_kb.py` to include:
     - claim type
     - document category
     - source file
  3. Add filtering or ranking improvements for specific claim scenarios.
  4. Demonstrate retrieval for:
     - deductible question
     - required documents question
     - fraud-indicator question
  5. Show how RAG evidence is reflected in `context_used["knowledge_hits"]`.

- **Deliverable**:
  - Expanded KB files
  - Improved ingestion/search behavior
  - Example recommendation using new KB sources

- **Bonus**:
  - Add source grouping in the Streamlit "Context used" view

---

### Assignment 6: Improve CI/CD and Deployment Workflow
**Objective**: Make the delivery pipeline cleaner and safer.

- **Task**:
  1. Update `.github/workflows/ci.yml` to:
     - trigger on push and PR
     - run linting with `ruff` or `flake8`
     - run tests with verbosity
  2. Improve deploy workflow to:
     - deploy only after test success
     - log health-check output clearly
     - document rollback steps
  3. Add badges to `README.md`.
  4. Add a short "deployment checks" section to the EC2 docs.

- **Deliverable**:
  - Updated workflow files
  - Updated `README.md`
  - Updated deployment documentation

- **Bonus**:
  - Add a manual approval gate for production deploy

---

## Part 2: Quizzes (Conceptual Understanding)

### Quiz 1: Agent Orchestration and Tool Calling

**Q1. What is the main role of `create_agent` in this project?**

a) To render the Streamlit dashboard  
b) To orchestrate LLM reasoning and tool usage before drafting a response  
c) To initialize SQLite tables  
d) To replace FastAPI routers  

*Answer: b) To orchestrate LLM reasoning and tool usage before drafting a response*

---

**Q2. Why are tool results captured inside `context_used["tool_calls"]`?**

a) Only to reduce token usage  
b) To improve transparency and debugging of agent behavior  
c) To avoid using RAG  
d) To skip database writes  

*Answer: b) To improve transparency and debugging of agent behavior*

---

**Q3. What does `@tool` do for a function in this project?**

a) Converts it into a FastAPI route  
b) Makes it available to the agent as a callable tool  
c) Encrypts its output  
d) Stores its result in SQLite automatically  

*Answer: b) Makes it available to the agent as a callable tool*

---

### Quiz 2: LangMem and Memory Design

**Q4. Why does this project use both LangMem memory and RAG?**

a) They serve the same purpose  
b) Memory stores prior claim/customer history, while RAG retrieves general insurance knowledge  
c) RAG is only for UI rendering  
d) LangMem is only for logging  

*Answer: b) Memory stores prior claim/customer history, while RAG retrieves general insurance knowledge*

---

**Q5. What is the purpose of customer-level and company-level memory scopes?**

a) To duplicate data for no reason  
b) To let the copilot use both individual history and organization-level patterns  
c) To support two databases  
d) To separate draft and ticket tables  

*Answer: b) To let the copilot use both individual history and organization-level patterns*

---

**Q6. What happens when semantic memory search is unavailable?**

a) Draft generation stops completely  
b) The memory layer can fall back to recent-memory listing behavior  
c) SQLite is deleted  
d) Streamlit crashes immediately  

*Answer: b) The memory layer can fall back to recent-memory listing behavior*

---

### Quiz 3: RAG and Knowledge Base

**Q7. What is the role of `KnowledgeBaseService` in this project?**

a) It stores customer passwords  
b) It ingests insurance KB files into ChromaDB and retrieves relevant chunks  
c) It manages Streamlit forms  
d) It generates Groq API keys  

*Answer: b) It ingests insurance KB files into ChromaDB and retrieves relevant chunks*

---

**Q8. Why are KB files chunked before indexing?**

a) To make files smaller on disk only  
b) To improve retrieval relevance and embedding quality for long documents  
c) To disable metadata  
d) To avoid using ChromaDB  

*Answer: b) To improve retrieval relevance and embedding quality for long documents*

---

**Q9. What is the purpose of `knowledge_hits` inside `context_used`?**

a) To expose retrieved policy/document evidence used during drafting  
b) To replace customer memories  
c) To track Docker logs  
d) To store API secrets  

*Answer: a) To expose retrieved policy/document evidence used during drafting*

---

### Quiz 4: API and Backend Architecture

**Q10. What does FastAPI lifespan setup do in `app_factory.py`?**

a) It restarts the server every request  
b) It ensures required directories and DB schema are initialized at startup  
c) It clears all tickets automatically  
d) It deploys the app to EC2  

*Answer: b) It ensures required directories and DB schema are initialized at startup*

---

**Q11. Why is `get_copilot()` cached with `@lru_cache`?**

a) To reuse expensive copilot initialization across requests  
b) To cache all HTTP responses  
c) To store Streamlit session state  
d) To avoid importing FastAPI  

*Answer: a) To reuse expensive copilot initialization across requests*

---

**Q12. What happens when a draft is accepted?**

a) Nothing changes in the system  
b) Ticket status is updated and the accepted recommendation is attempted to be saved into memory  
c) The ticket is deleted  
d) The KB is re-ingested automatically  

*Answer: b) Ticket status is updated and the accepted recommendation is attempted to be saved into memory*

---

### Quiz 5: Data Layer and Reliability

**Q13. Why are repositories split into separate customer, ticket, and draft modules?**

a) SQLite requires it  
b) It improves maintainability, testability, and separation of concerns  
c) Streamlit cannot read combined repositories  
d) It reduces Docker image size  

*Answer: b) It improves maintainability, testability, and separation of concerns*

---

**Q14. What kind of issue can happen if `get_by_email()` queries by `id` instead of `email`?**

a) ChromaDB corruption  
b) False "customer not found" results in tool logic  
c) FastAPI route duplication  
d) Mermaid rendering failure  

*Answer: b) False "customer not found" results in tool logic*

---

**Q15. Why does the project include fallback draft generation when the main agent output is empty?**

a) To improve color styling in the UI  
b) To maintain user-facing reliability and avoid blank responses  
c) To disable tools  
d) To skip logging  

*Answer: b) To maintain user-facing reliability and avoid blank responses*

---

### Quiz 6: Streamlit and Human-in-the-Loop Design

**Q16. Why does the dashboard expose "Context used for recommendation"?**

a) To help humans inspect memory, RAG, and tool usage behind the draft  
b) To allow direct database editing  
c) To hide tool results  
d) To avoid using FastAPI  

*Answer: a) To help humans inspect memory, RAG, and tool usage behind the draft*

---

**Q17. Why is human approval important in this insurance claims workflow?**

a) Because the UI requires a button click  
b) Because sensitive recommendations should not become autonomous final decisions  
c) Because Groq cannot return text  
d) Because ChromaDB requires approval  

*Answer: b) Because sensitive recommendations should not become autonomous final decisions*

---

**Q18. What is the value of the claim history probe in the UI?**

a) It provides random demo output  
b) It helps validate whether LangMem is storing and retrieving relevant prior claim context  
c) It replaces KB ingestion  
d) It deletes old memories  

*Answer: b) It helps validate whether LangMem is storing and retrieving relevant prior claim context*

---

### Quiz 7: Docker, CI/CD, and Deployment

**Q19. Why are dependency files copied before application code in Docker build?**

a) Docker requires alphabetical order  
b) To leverage layer caching and speed up rebuilds  
c) To disable environment variables  
d) To avoid exposing ports  

*Answer: b) To leverage layer caching and speed up rebuilds*

---

**Q20. Why does the deploy workflow verify the `/health` endpoint after deployment?**

a) To improve markdown formatting  
b) To confirm the API is actually running successfully after rollout  
c) To rebuild ChromaDB  
d) To clear Streamlit cache  

*Answer: b) To confirm the API is actually running successfully after rollout*

---

## Submission Guidelines

1. Submit a GitHub repository link with clear commits for each assignment.
2. Update `README.md` with setup, run, and test instructions.
3. Include screenshots or recordings for completed features.
4. Keep API keys and credentials out of source code.
5. Ensure tests pass before submission.
6. Prefer modular, well-named functions and clean file organization.
