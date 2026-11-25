"""Render the workshop handout. Requires ReportLab."""

from pathlib import Path
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

PROMPTS = [
    (
        'Find the biggest issues',
        'Review <i>[repo/file]</i> for <i>[focus]</i>. Rank up to 10 issues by impact. For each, cite the file and line, give an example that triggers it, and explain the consequence.',
    ),
    (
        'Decide one issue at a time',
        'Take the findings one at a time. Recommend a fix, explain the trade-off, then wait for my decision. Record each as accepted, deferred, or rejected. Build a plan from the accepted items.',
    ),
    (
        'Trace unfamiliar code',
        'Trace one measurement from the HDF5 file to the final plot. Name the functions it passes through and show where its shape or units change. Keep this pass read-only.',
    ),
    (
        'Clarify what matters',
        'Read <i>[files]</i> first. If a missing requirement would change your implementation, ask me the most important question first. State any smaller assumptions and proceed.',
    ),
    (
        'Give an example',
        'Implement <font name="Courier">mean_reading</font>. For <font name="Courier">[2, 4]</font>, return <font name="Courier">3.0</font>. For an empty list, raise <font name="Courier">ValueError</font>. Follow the error style in <i>[existing function]</i>.',
    ),
    (
        'Define success',
        'I should be able to run <i>[command]</i> in the Codespace and get a PNG with labeled axes and units. Run it on <i>[sample file]</i> and inspect the plot.',
    ),
    (
        'Compare options',
        'Compare loading the whole dataset with reading it in chunks. The file is 8 GB and I have 4 GB of RAM. Which approach supports <i>[operation]</i>, and what does it cost?',
    ),
    (
        'Reproduce a bug',
        'With <i>[input]</i>, <i>[command]</i> gives <i>[actual result]</i>. I expected <i>[expected result]</i>. Capture the mismatch in a failing test, apply the smallest fix, and rerun the test.',
    ),
    (
        'Bound the edit',
        'Implement <i>[change]</i> in <i>[component]</i>. Preserve the public API and file format. Follow <i>[reference implementation]</i>. List unrelated cleanup separately.',
    ),
    (
        'Verify the result',
        "Check each acceptance criterion. For each, report the command you ran and what it showed. Identify anything you couldn't verify and explain why.",
    ),
]

GUIDES = [
    ('GitHub', 'https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-engineering'),
    ('Anthropic', 'https://www.anthropic.com/research/claude-code-best-practices'),
    ('OpenAI', 'https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex'),
]

NAVY = "#003359"
TEAL = "#00747A"
INK = "#17324D"
MUTED = "#607487"


def render():
    pdf = Canvas(str(Path(__file__).with_suffix(".pdf")), pagesize=A4, invariant=True)
    pdf.setTitle("Prompting cheat sheet")
    pdf.setAuthor("Agentic AI Workshop")
    width, height = A4
    left, right = 15 * mm, width - 15 * mm

    def label(x, y, value, size, color, font="Helvetica"):
        pdf.setFillColor(HexColor(color))
        pdf.setFont(font, size)
        pdf.drawString(x, y, value)

    def paragraph(value, font, color, size, leading):
        return Paragraph(value, ParagraphStyle("cell", fontName=font, fontSize=size,
                                               leading=leading, textColor=HexColor(color),
                                               alignment=TA_LEFT))

    pdf.setFillColor(HexColor(TEAL))
    pdf.rect(0, height - 8, width, 8, stroke=0, fill=1)
    label(left, height - 40, "Agentic AI Workshop  ·  Block 2  ·  Directing AI Agents", 10, MUTED)
    label(left, height - 81, "Prompting cheat sheet", 32, NAVY, "Helvetica-Bold")
    label(left, height - 105, "Choose a prompt for the task at hand. Replace bracketed text with your details.", 11, INK)
    y = height - 132
    for number, (title, prompt) in enumerate(PROMPTS, 1):
        pdf.setStrokeColor(HexColor(TEAL if number == 1 else "#DCE6EA"))
        pdf.setLineWidth(1.5 if number == 1 else 0.6)
        pdf.line(left, y, right, y)
        top = y - 10
        label(left, top - 10, f"{number:02}", 10.5, TEAL, "Helvetica-Bold")
        heading = paragraph(title, "Helvetica-Bold", NAVY, 11, 14)
        body = paragraph(prompt, "Helvetica", INK, 11.5, 15.5)
        body_x = left + 143
        _, h1 = heading.wrap(109, height)
        _, h2 = body.wrap(right - body_x, height)
        heading.drawOn(pdf, left + 23, top - h1)
        body.drawOn(pdf, body_x, top - h2)
        y = top - max(h1, h2) - 11

    if y < 46:
        raise ValueError("Handout content overlaps the footer")
    pdf.setStrokeColor(HexColor("#FF7900"))
    pdf.setLineWidth(2)
    pdf.line(left, 29, left, 42)
    label(left + 7, 32, "TU Ilmenau  ·  AI Agent Workshop", 9, MUTED)
    x = right
    for title, url in reversed(GUIDES):
        extent = pdf.stringWidth(title, "Helvetica", 9)
        x -= extent
        label(x, 32, title, 9, TEAL)
        pdf.linkURL(url, (x, 30, x + extent, 42))
        x -= 10
    label(x - pdf.stringWidth("Prompting guides", "Helvetica", 9), 32, "Prompting guides", 9, MUTED)
    pdf.save()


if __name__ == "__main__":
    render()
