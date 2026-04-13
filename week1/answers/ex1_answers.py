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
smaller model (`google/gemma-2-2b-it`) returned a correct answer in all three
formats. In the plain condition it answered with "Haymarket Vaults" instead of
"The Haymarket Vaults", likely because the plain format encouraged a more
natural-language response. In the XML and sandwich formats, the venue names
followed exact list items. Overall, the original dataset was still too easy to
expose a formatting effect.

In an additional test, I extended the list with 40 extra venues and saved the
results in `ex1_results2.json`. The longer prompt lowered the signal-to-noise
ratio, and the smaller model failed in both the plain and XML formats by
choosing venues that matched some constraints but were too small. The sandwich
prompt still returned the correct answer, suggesting that adding structure and
repeating the query at the end of the promtp helped the model keep all three
constraints active in the longer context.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the model has to track several constraints
in a longer, noisier context. In the short original dataset, both the large
model and the smaller model produced correct answers across formats. But after
the list was extended with many extra venues, the smaller model failed in the
plain and XML formats while the sandwich prompt still worked. This shows that
stronger prompt structure becomes more useful when the context is noisier and
contains more distractors.
"""
