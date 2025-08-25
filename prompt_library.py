from typing import Dict, List
import textwrap

def _ctx_block(ctx: Dict) -> str:
    return textwrap.dedent(f"""
    CONTEXT
    ----
    Idea: {ctx.get('idea')}
    Industry: {ctx.get('industry')}
    Geography: {ctx.get('geo')}
    Audience: {ctx.get('audience')}
    Traction: {ctx.get('traction')}
    Team: {ctx.get('team')}
    Pricing/Model: {ctx.get('pricing')}
    GTM Channels: {ctx.get('channels')}
    """).strip()

def prompt_investor_summary(ctx: Dict) -> str:
    return f"""{_ctx_block(ctx)}

    TASK: Write a crisp investor-ready summary (120-180 words).
    Style: clear, specific, non-hype; include problem, solution, target user, business model, and traction snapshot.
    Output headers: Problem · Solution · Why Now · Business Model · Traction · Ask (one line).
    """

def prompt_elevator_pitch(ctx: Dict) -> str:
    return f"""{_ctx_block(ctx)}

    TASK: Craft a 30-second elevator pitch (~60-80 words). 
    Include a relatable analogy only if it helps clarity.
    End with a memorable one-liner tagline.
    """

def prompt_swot(ctx: Dict) -> str:
    return f"""{_ctx_block(ctx)}

    TASK: Produce a SWOT analysis as short bullet points (4-6 bullets each). 
    Keep it practical and investor-focused.
    Format:
    - Strengths:
    - Weaknesses:
    - Opportunities:
    - Threats:
    """

def prompt_pitch_email(ctx: Dict) -> str:
    return f"""{_ctx_block(ctx)}

    TASK: Write a concise investor outreach email (≤160 words).
    Tone: professional, confident, data-oriented; avoid fluff.
    Subject line + email body. Include a short CTA for a 20-min call.
    """

def prompt_storytelling(ctx: Dict) -> str:
    return f"""{_ctx_block(ctx)}

    TASK: Suggest 3 hook options, 2 metaphors/analogies, and 1 brief origin story narrative.
    Keep it founder-authentic and audience-appropriate.
    """

def prompt_risks(ctx: Dict) -> str:
    return f"""{_ctx_block(ctx)}

    TASK: Identify key risks (legal, tech, financial, market) and propose specific mitigations.
    Output as a table with columns: Risk · Likelihood · Impact · Mitigation · Owner.
    """

def prompt_team_analyzer(ctx: Dict) -> str:
    return f"""{_ctx_block(ctx)}

    TASK: Assess the team's strengths and gaps. Recommend 2-3 strategic hires with role charters.
    Include a skills matrix overview (Current · Gap · Priority).
    """

def prompt_funding_ask(ctx: Dict) -> str:
    return f"""{_ctx_block(ctx)}

    TASK: Recommend a funding amount, stage, and 18-month allocation plan (percentages).
    Include key milestones, expected runway, and top 3 KPIs for the next 2 quarters.
    """

def prompt_competitor_table(ctx: Dict, competitors: List[str]) -> str:
    comp_str = ", ".join(competitors) if competitors else "N/A"
    return f"""{_ctx_block(ctx)}

    TASK: Compare the following competitors: {comp_str}
    Output a markdown table with columns: Company · Positioning · Strengths · Weaknesses · Pricing/Model · Differentiation.
    Keep each cell short (≤15 words).
    """

def prompt_qna(ctx: Dict) -> str:
    return f"""{_ctx_block(ctx)}

    TASK: Simulate a tough investor Q&A: 10 sharp questions with suggested answers.
    Style: candid, data-led, non-defensive.
    """

