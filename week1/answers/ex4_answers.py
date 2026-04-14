"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = """
It seems there are no Edinburgh venues currently available that can accommodate 300 guests with vegan options. Would you like me to:

1. Search for venues with a lower minimum capacity (e.g., 250-299)?
2. Look for venues without vegan requirements but with other dietary options?
3. Check availability for a different date?

Let me know how you'd like to proceed.
"""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Initially, Query 1 returned two available venues: "The Haymarket Vaults" and
"The Albanach". After changing The Albanach's status from "available" to "full"
in the venue list in `sovereign_agent/tools/mcp_venue_server.py` and rerunning
the client, Query 1 returned only "The Haymarket Vaults". No client-side code
changes were needed, and the MCP interface and tool logic stayed the same. This
shows that the venue data in the server acts as the single source of truth for
the agent's results.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 8   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 43   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides a unified interface that can be used by different clients. Both
the LangGraph agent and Rasa CALM can connect to the same server, discover the
same tools, and use the same underlying data without duplicating tool code.
This keeps the tool interface and implementation centralized, so clients are
easier to maintain, reuse, and extend.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- The Planner breaks an incoming task into a clear sequence of research and
  execution steps. It is a stronger-reasoning model than the Executor. It sits
  before the ReAct loop so the Executor receives a concrete plan instead of an
  ambiguous prompt.

- The Executor is the worker that carries out the plan produced by the Planner.
  It runs the ReAct loop, calling tools, writing artifacts, and deciding when
  to delegate.

- The Structured Agent (Rasa CALM) handles human-facing interactions through
  explicit flows and business rules. It lives outside the ReAct loop and
  represents the second half of PyNanoClaw.

- The Shared MCP Tool Server keeps tools centralized and makes them available
  to both halves of PyNanoClaw, and it lives in the shared layer between the
  autonomous loop and the structured agent.

- The Persistent Memory Store keeps task state, prior findings, and outputs
  across turns. It lives in the shared layer so both the autonomous loop and
  the structured agent can continue from the same context.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The research work fits the LangGraph-style agent, and the phone call fits the
Rasa CALM agent. In Exercise 2, LangGraph showed the flexibility needed for
research by pivoting from The Bow Bar to The Haymarket Vaults after seeing that
The Bow Bar was full and too small. In Exercise 4, it also recovered from the
first `search_venues` validation error by retrying with the nested `input`
shape and still finding The Haymarket Vaults.

The call should stay with CALM because the call behavior needs structure,
boundaries, and deterministic business rules. In the Exercise 3 run, CALM asked
for guest count, vegan meals, and deposit in order, escalated when the deposit
exceeded the £300 limit, refused off-topic requests, and brought the
conversation back to booking.

Swapping them feels wrong because a booking confirmation call needs a narrow,
repeatable process, while research needs flexibility and more freedom.
"""