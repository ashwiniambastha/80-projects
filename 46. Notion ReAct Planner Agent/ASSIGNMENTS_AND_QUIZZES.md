# Assignments and Quizzes: Notion ReAct Planner Agent

## Part 1: Assignments (Practical Implementation)

These assignments are designed to extend your current project and deepen your understanding of ReAct Agents, Tool-Using AI, and Full-Stack AI Application Development.

---

### Assignment 1: Add a New Tool - Web Search Integration
**Objective**: Extend the agent's capabilities by adding a web search tool.

- **Task**:
    1. Create a new file `tools/web_search.py`.
    2. Implement a `search_web` function using a free API like SerpAPI, DuckDuckGo API, or Tavily.
    3. Decorate the function with `@tool` from LangChain and provide a clear docstring.
    4. Register the new tool in `agent/bot.py` by adding it to the `tools` list.
    5. Test the agent with queries like "Search for the latest news about AI" or "Find top restaurants in Mumbai".

- **Deliverable**: 
    - A working `tools/web_search.py` file.
    - Updated `agent/bot.py` with the new tool registered.
    - Screenshot or log output showing the agent using the web search tool.

- **Bonus**: Add rate limiting and caching to prevent excessive API calls.

---

### Assignment 2: Implement Conversation Memory
**Objective**: Enable the agent to remember previous conversations within a session.

- **Task**:
    1. Study LangChain's memory modules (`ConversationBufferMemory`, `ConversationSummaryMemory`).
    2. Modify `agent/bot.py` to incorporate memory into the ReAct agent.
    3. Update `api/server.py` to maintain conversation history per session (hint: use session IDs).
    4. Update the `/chat` endpoint to pass conversation history to the agent.
    5. Test with multi-turn conversations like:
        - User: "Add a meeting tomorrow at 3 PM"
        - User: "What did I just schedule?" (Agent should remember)

- **Deliverable**: 
    - Modified `agent/bot.py` with memory integration.
    - Updated `api/server.py` with session management.
    - Demo showing multi-turn conversation capabilities.

---

### Assignment 3: Add Update and Delete Operations to Notion Tools
**Objective**: Complete the CRUD operations for Notion integration.

- **Task**:
    1. In `tools/notion_notes.py`, add two new tools:
        - `update_note(note_id: str, new_content: str)` - Update an existing note.
        - `delete_note(note_id: str)` - Mark a note as "Completed" or delete it.
    2. In `tools/notion_calender.py`, add:
        - `update_calendar_event(event_id: str, date: str, time: str, event: str)` - Modify an existing event.
        - `delete_calendar_event(event_id: str)` - Remove a calendar event.
    3. Update `get_notes()` and `get_calendar_events()` to return page IDs along with content.
    4. Register all new tools in `agent/bot.py`.

- **Deliverable**: 
    - Updated tool files with full CRUD operations.
    - Test cases demonstrating update and delete functionality.

---

### Assignment 4: Implement Automated Testing with Pytest
**Objective**: Ensure code reliability through comprehensive testing.

- **Task**:
    1. Create a `tests/` directory in the project root.
    2. Write unit tests for:
        - `tests/test_weather.py` - Mock the API and test `get_weather()`.
        - `tests/test_notion_notes.py` - Mock Notion API and test `get_notes()`, `add_note()`.
        - `tests/test_api.py` - Test FastAPI endpoints using `TestClient`.
    3. Use `pytest` and `pytest-mock` for mocking external APIs.
    4. Add a `pytest.ini` or update `pyproject.toml` with pytest configuration.
    5. Ensure all tests pass with `pytest -v`.

- **Deliverable**: 
    - A `tests/` directory with at least 5 test cases.
    - All tests passing (provide screenshot or CI output).
    - Updated `requirements.txt` with testing dependencies.

---

### Assignment 5: Add CI/CD Pipeline with GitHub Actions
**Objective**: Automate testing and deployment workflows.

- **Task**:
    1. Create `.github/workflows/ci.yml` for Continuous Integration:
        - Trigger on push and pull requests.
        - Set up Python 3.12 environment.
        - Install dependencies.
        - Run `pytest` with coverage reporting.
        - Run linting with `ruff` or `flake8`.
    2. Create `.github/workflows/deploy.yml` for deployment:
        - Build and push Docker image to GitHub Container Registry (GHCR).
        - (Optional) Deploy to a cloud provider on merge to `main`.
    3. Add status badges to `README.md`.

- **Deliverable**: 
    - Working CI/CD workflow files.
    - Screenshot of passing GitHub Actions run.
    - README with status badges.

---

## Part 2: Quizzes (Conceptual Understanding)

### Quiz 1: ReAct Agent Pattern

**Q1. What does "ReAct" stand for in the context of AI agents?**

a) Reactive Actions  
b) Reason + Act  
c) Real-time Activation  
d) Response Activity  

*Answer: b) Reason + Act*

---

**Q2. In the ReAct pattern, what is the primary advantage over simple prompt-response LLMs?**

a) Faster response times  
b) Lower API costs  
c) The agent can reason through problems and use external tools iteratively  
d) Better grammar in responses  

*Answer: c) The agent can reason through problems and use external tools iteratively*

---

**Q3. In `agent/bot.py`, what is the purpose of the `@tool` decorator from LangChain?**

a) To make the function run faster  
b) To convert a Python function into a tool that the LLM agent can discover and use  
c) To add logging to the function  
d) To encrypt the function's output  

*Answer: b) To convert a Python function into a tool that the LLM agent can discover and use*

---

### Quiz 2: LangChain & Tool Integration

**Q4. Why is the docstring important in a LangChain tool function?**

a) It's optional and only for documentation  
b) The LLM uses the docstring to understand when and how to use the tool  
c) It determines the function's return type  
d) It sets the function's execution priority  

*Answer: b) The LLM uses the docstring to understand when and how to use the tool*

---

**Q5. In the `get_weather` tool, why do we first call the geocoding API before the weather API?**

a) To validate the API key  
b) To convert the city name into latitude and longitude coordinates required by the weather API  
c) To check if the city exists in the database  
d) To get the timezone information  

*Answer: b) To convert the city name into latitude and longitude coordinates required by the weather API*

---

**Q6. What happens when `agent.invoke()` is called with a user message?**

a) The message is directly sent to Notion  
b) The LLM reasons about the query, decides which tools to use, executes them, and formulates a response  
c) The message is stored in a database  
d) A random response is generated  

*Answer: b) The LLM reasons about the query, decides which tools to use, executes them, and formulates a response*

---

### Quiz 3: Notion API Integration

**Q7. What HTTP method is used to query a Notion database in `get_notes()`?**

a) GET  
b) PUT  
c) POST  
d) DELETE  

*Answer: c) POST*

---

**Q8. In the Notion API, what is the purpose of the `Notion-Version` header?**

a) To authenticate the request  
b) To specify which version of the Notion API to use for compatibility  
c) To set the response format  
d) To enable caching  

*Answer: b) To specify which version of the Notion API to use for compatibility*

---

**Q9. In `notion_notes.py`, what does the filter `{"property": "Status", "select": {"equals": "Pending"}}` do?**

a) Creates a new property called "Status"  
b) Filters the query results to only return notes where the Status property equals "Pending"  
c) Updates all notes to "Pending" status  
d) Deletes notes with "Pending" status  

*Answer: b) Filters the query results to only return notes where the Status property equals "Pending"*

---

### Quiz 4: FastAPI & Backend Architecture

**Q10. What is the purpose of `@app.on_event("startup")` in `api/server.py`?**

a) To handle user login events  
b) To execute code when the FastAPI application starts, used here to initialize the agent  
c) To restart the server periodically  
d) To send startup notifications  

*Answer: b) To execute code when the FastAPI application starts, used here to initialize the agent*

---

**Q11. Why is the agent stored in a global variable in `api/server.py`?**

a) It's a Python requirement  
b) To avoid reinitializing the expensive LLM connection on every request  
c) To share data between users  
d) For debugging purposes only  

*Answer: b) To avoid reinitializing the expensive LLM connection on every request*

---

**Q12. What does `app.mount("/", StaticFiles(directory="static", html=True), name='static')` do?**

a) Creates a new database  
b) Serves static files (HTML, CSS, JS) from the "static" directory at the root path  
c) Mounts an external hard drive  
d) Enables file uploads  

*Answer: b) Serves static files (HTML, CSS, JS) from the "static" directory at the root path*

---

### Quiz 5: Docker & Deployment

**Q13. In the Dockerfile, why do we `COPY requirements.txt .` before `COPY . .`?**

a) It's alphabetically ordered  
b) To leverage Docker's layer caching - dependencies change less frequently than code  
c) Requirements must be copied first by Docker rules  
d) To reduce the image size  

*Answer: b) To leverage Docker's layer caching - dependencies change less frequently than code*

---

**Q14. What does `restart: unless-stopped` mean in docker-compose.yml?**

a) The container will never restart  
b) The container will restart automatically unless explicitly stopped by the user  
c) The container will restart only on errors  
d) The container will stop after one hour  

*Answer: b) The container will restart automatically unless explicitly stopped by the user*

---

**Q15. What is the purpose of `env_file: - .env` in docker-compose.yml?**

a) To create a new .env file  
b) To load environment variables from the .env file into the container  
c) To backup the .env file  
d) To encrypt the .env file  

*Answer: b) To load environment variables from the .env file into the container*

---

### Quiz 6: Frontend & API Communication

**Q16. In `script.js`, why is `chatHistory` maintained on the client side?**

a) To reduce server load by tracking conversation context locally  
b) To display messages faster  
c) Because JavaScript requires it  
d) To encrypt messages  

*Answer: a) To reduce server load by tracking conversation context locally*

---

**Q17. What does `response.raise_for_status()` do in the Python tools?**

a) Increases the response priority  
b) Raises an HTTPError if the response status code indicates an error (4xx or 5xx)  
c) Returns the status code  
d) Logs the response status  

*Answer: b) Raises an HTTPError if the response status code indicates an error (4xx or 5xx)*

---

### Quiz 7: Error Handling & Best Practices

**Q18. Why do the Notion tools check for `api_key` and `db_id` at the start of each function?**

a) To slow down execution  
b) Fail-fast pattern: return early with clear error if required configuration is missing  
c) Because Python functions require parameters  
d) To log the values  

*Answer: b) Fail-fast pattern: return early with clear error if required configuration is missing*

---

**Q19. What is the advantage of using a centralized logger (`utils/logger.py`) instead of `print()` statements?**

a) Logger is faster than print  
b) Provides consistent formatting, log levels, timestamps, and can be configured for different outputs  
c) Python doesn't support print in production  
d) Logger uses less memory  

*Answer: b) Provides consistent formatting, log levels, timestamps, and can be configured for different outputs*

---

**Q20. In the project architecture, why is it better to separate tools into individual files rather than putting them all in one file?**

a) Python has a file size limit  
b) Modularity: easier to maintain, test, and extend individual tools independently  
c) It runs faster with separate files  
d) Docker requires separate files  

*Answer: b) Modularity: easier to maintain, test, and extend individual tools independently*

---

## Submission Guidelines

1. **Assignments**: Submit a GitHub repository link with:
   - Clear commit history showing your work
   - Updated README with setup instructions
   - Screenshots/recordings demonstrating features

2. **Quizzes**: Submit answers in a document or online form as specified by your instructor.

3. **Code Quality Expectations**:
   - Proper error handling
   - Clear variable and function names
   - Docstrings for all functions
   - No hardcoded credentials


