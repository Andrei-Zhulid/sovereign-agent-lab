"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
Part A was straightforward for the chosen model (meta-llama/Llama-3.3-70B-Instruct).
All three prompt formats returned a valid venue. With a short, clean list the model
did not need extra structure to find a correct answer. The difference between the
plain and XML-based prompts shows that formatting can affect which correct answer
the model picks.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
With the additional distractors, the model still performed well and all answers
remained correct. The Holyrood Arms was the stronger distractor because it
matched the capacity and vegan requirements and only failed on availability. It
was close enough to the target that a model checking criteria separately, rather
than verifying all three constraints together, could choose it.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C was needed because Parts A and B were both fully correct. Even the
smaller model (meta-llama/Meta-Llama-3.1-8B-Instruct) got all three conditions
right, which suggests the original dataset was still too easy to expose a
formatting effect.

In an additional test, I extended the list with 40 extra venues and saved the
results in `ex1_results2.json`. The longer prompt lowered the signal-to-noise
ratio, and the smaller model failed in the plain format by choosing The
Guilford Arms, which met capacity and availability but not the vegan
requirement. The XML and sandwich formats still returned the correct answer,
suggesting that added structure helped the model track all constraints.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
This experiment showed that prompt structure matters most when the task becomes
harder. In the original setup, both the large model and the smaller model
handled the short venue list well, even with near-miss distractors. But when
the context was made longer and noisier (`ex1_results2.json` results), the
smaller model failed in the plain format while the structured formats still
worked. This suggests that XML-based prompts help models track multiple
constraints more reliably when the signal-to-noise ratio drops.
"""
