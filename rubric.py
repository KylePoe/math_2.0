"""Scoring rubric, output schema, and prompt construction for score.py.

Editing anything here changes PROMPT_VERSION, so score.py will re-score posts
instead of reusing cached results produced under the old rubric.
"""

from __future__ import annotations

import hashlib
import json
from typing import Literal

from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Dimensions. Each is scored in [-1, 1]. Keep keys stable: they become CSV columns.
# ---------------------------------------------------------------------------
DIMENSIONS: dict[str, str] = {
    "capability": (
        "AI as a research tool: how capable, reliable, and useful the author judges AI to be for "
        "actually doing mathematics (finding proofs, solving problems, checking work, literature "
        "search, formalisation). -1 = useless, unreliable, overhyped; 0 = mixed or modest; "
        "+1 = powerful, transformative, already doing real mathematics."
    ),
    "understanding": (
        "Effect on mathematical understanding and meaning: whether AI deepens or erodes human "
        "understanding, insight, rigor, the value of proof, and what mathematics is for. "
        "-1 = erodes understanding / hollows out the point of mathematics; +1 = deepens or "
        "expands understanding, frees humans for deeper questions."
    ),
    "community": (
        "Effect on mathematicians as people and as a community: careers, jobs, hiring, training of "
        "students, equity and access, credit, collaboration, the social fabric of the field. "
        "-1 = harmful (lost jobs, de-skilling, concentration of power, broken training pipeline); "
        "+1 = beneficial (democratisation, access for amateurs, new kinds of collaboration)."
    ),
    "institutions": (
        "Confidence that the field's institutions and norms (journals, refereeing, credit and "
        "authorship rules, disclosure, funding, societies, universities) can adapt well to AI. "
        "-1 = pessimistic, institutions will fail or be captured; +1 = optimistic, the community "
        "can and will build good norms. Score whether the author expects adaptation to go well, "
        "not merely whether they propose reforms."
    ),
    "adoption": (
        "Normative stance: should mathematicians embrace and integrate AI into research, or resist, "
        "restrict, or limit it? -1 = resist / restrict / keep mathematics human; 0 = cautious, "
        "conditional use; +1 = embrace, integrate, invest."
    ),
    "overall": (
        "Overall sentiment toward the role of AI in the future of mathematics, all things "
        "considered. -1 = very negative; 0 = balanced or ambivalent; +1 = very positive. "
        "Always addressed."
    ),
}

POST_TYPES = [
    "opinion_essay",        # argued personal view
    "practice_report",      # first-hand account of using (or not using) AI in research/teaching
    "proposal",             # concrete policy / institutional / community proposal
    "statement_or_letter",  # official statement, open letter, collective declaration
    "announcement",         # event, initiative, survey launch, site news
    "survey_or_data",       # reports results of a survey, poll, or data analysis
    "creative_or_satire",   # fiction, satire, poetry
    "other",
]

CAREER_STAGES = [
    "undergraduate_or_prospective",  # undergrad, high-school student, prospective PhD applicant
    "phd_student",
    "postdoc",                       # postdoc, research fellow, other fixed-term early-career
    "early_career_faculty",          # assistant professor, lecturer, junior permanent researcher
    "senior_faculty",                # associate/full professor, reader, director of research, chair
    "emeritus_or_retired",
    "non_academic_professional",     # industry, government, engineering (not primarily AI)
    "ai_industry",                   # works at an AI lab / AI company
    "amateur_or_independent",        # hobbyist, independent scholar, left academia
    "collective_or_organization",    # group of authors, society, editorial team, the site itself
    "unknown",
]

SECTORS = ["academia", "ai_industry", "other_industry", "independent", "mixed", "unknown"]

AI_RESEARCH_USE = [
    "substantial",   # AI is a regular, significant part of their mathematical work
    "occasional",    # uses it sometimes / for limited tasks (literature, checking, coding)
    "experimented",  # has tried it, reports on trying it, but not a regular part of their work
    "open_to_or_planning",  # no current use reported, but says they will / would use it
    "none",          # says they do not use it for research (and gives no plan to)
    "not_stated",
]

AI_WRITING_USE = [
    "substantial",    # AI drafted or substantially shaped the text
    "light_editing",  # grammar, translation, proofreading, formatting
    "none",           # explicitly states no AI used
    "not_stated",
]


# ---------------------------------------------------------------------------
# Pydantic models (used to validate the JSON Claude returns).
# ---------------------------------------------------------------------------
class DimensionScore(BaseModel):
    addressed: bool = Field(description="Does the post take a discernible position on this dimension?")
    score: float = Field(description="In [-1, 1]. Use 0 when not addressed.")
    evidence: str = Field(description="Short verbatim quote (<= 30 words) supporting the score, or '' if not addressed.")


class Dimensions(BaseModel):
    capability: DimensionScore
    understanding: DimensionScore
    community: DimensionScore
    institutions: DimensionScore
    adoption: DimensionScore
    overall: DimensionScore


class Tone(BaseModel):
    score: float = Field(description="Emotional register in [-1, 1]: -1 alarmed/grieving/angry, 0 neutral/analytical, +1 enthusiastic/hopeful.")
    evidence: str


class Author(BaseModel):
    career_stage: Literal[tuple(CAREER_STAGES)]  # type: ignore[valid-type]
    sector: Literal[tuple(SECTORS)]  # type: ignore[valid-type]
    n_authors: int = Field(description="Number of authors; use 0 for a collective/organisation of unstated size.")
    field: str = Field(description="Author's area of mathematics or discipline if stated (e.g. 'number theory', 'computer science'), else ''.")
    evidence: str = Field(description="The text the role was inferred from.")


class AIUse(BaseModel):
    in_research: Literal[tuple(AI_RESEARCH_USE)]  # type: ignore[valid-type]
    in_research_evidence: str
    in_writing_post: Literal[tuple(AI_WRITING_USE)]  # type: ignore[valid-type]
    in_writing_post_evidence: str


class PostScore(BaseModel):
    post_type: Literal[tuple(POST_TYPES)]  # type: ignore[valid-type]
    ai_in_math_relevance: Literal["central", "partial", "minimal"]
    summary: str = Field(description="One-sentence summary of the post's main argument.")
    dimensions: Dimensions
    emotional_tone: Tone
    author: Author
    ai_use: AIUse


def _strictify(schema: dict) -> dict:
    """Make a pydantic JSON schema acceptable to structured outputs: inline $defs,
    additionalProperties=false, every property required, no unsupported keywords."""
    defs = schema.pop("$defs", {})

    def walk(node):
        if isinstance(node, dict):
            if "$ref" in node:
                return walk(defs[node["$ref"].split("/")[-1]])
            node = {k: walk(v) for k, v in node.items() if k not in ("title", "default")}
            if node.get("type") == "object":
                node["additionalProperties"] = False
                node["required"] = list(node.get("properties", {}).keys())
            return node
        if isinstance(node, list):
            return [walk(x) for x in node]
        return node

    return walk(schema)


OUTPUT_SCHEMA = _strictify(PostScore.model_json_schema())


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------
def _dimension_block() -> str:
    return "\n".join(f"- {k}: {v}" for k, v in DIMENSIONS.items())


SYSTEM_PROMPT = f"""You are annotating posts from "Proofs and Prompts", a forum where mathematicians write about artificial intelligence and the future of mathematical research. The annotations feed a quantitative study of how the mathematical community views AI's role in mathematics, so consistency across posts matters more than nuance in any single post.

For each post, score the AUTHOR'S OWN position (not positions they describe and then reject) on these dimensions, each in [-1, 1]:

{_dimension_block()}

Scoring guidance:
- Anchors: -1 strongly negative, -0.5 leaning negative, 0 balanced / ambivalent, +0.5 leaning positive, +1 strongly positive. Use intermediate values freely.
- Score stance, not tone. An anxious, grieving post can still judge AI highly capable (capability > 0). A cheerful post can still argue AI is useless.
- The dimensions are deliberately separable: a post can rate capability +0.8 while rating community -0.7. Do not let one dimension bleed into another.
- Set addressed=false and score=0 when the post takes no discernible position on that dimension. Do not guess a position from the author's general mood. "overall" is always addressed.
- Satire and fiction: score the position the piece is evidently advocating.
- Evidence must be a short verbatim quote from the post (at most 30 words) that by itself shows the DIRECTION of the score: a negative score needs a quote expressing the negative position, a positive score a positive one. Do not quote a passage the author raises only to rebut or qualify. If you cannot find a quote that supports the direction, reconsider the score.
- emotional_tone is the register of the writing, separate from stance.

Author fields:
- Infer career_stage from the author line and any self-description in the text. If several authors, use the most senior author and record n_authors. Map titles across national systems sensibly (e.g. Directeur de Recherche, Reader, W3 Professor -> senior_faculty; Maître de conférences, Lecturer, Assistant Professor -> early_career_faculty). Use "unknown" rather than guessing.

AI use fields:
- in_research: does the author report using AI in their own mathematical research? Base this only on what the post says. Current or past use outranks stated plans; use "open_to_or_planning" only when the author reports no current use but says they will or would use it. Use "not_stated" only when the post gives nothing to go on, and then leave in_research_evidence empty.
- in_writing_post: did AI help write this post? Many posts include an "AI use:" or "AI disclosure" statement; use it if present, otherwise "not_stated".

Return only the JSON object matching the schema."""


def build_user_message(post: dict) -> str:
    meta = {
        "title": post["title"],
        "published": post["published"][:10],
        "received": post.get("received_date"),
        "categories": post["categories"],
        "tags": post["tags"],
        "contributors": post["contributors"],
    }
    return (
        f"<metadata>\n{json.dumps(meta, ensure_ascii=False, indent=1)}\n</metadata>\n\n"
        f"<author_line>\n{post['author_line']}\n</author_line>\n\n"
        f"<post>\n{post['text']}\n</post>"
    )


def prompt_version(model: str, effort: str) -> str:
    h = hashlib.sha256(
        json.dumps([SYSTEM_PROMPT, OUTPUT_SCHEMA, model, effort], sort_keys=True).encode()
    ).hexdigest()
    return h[:12]
