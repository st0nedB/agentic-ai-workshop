"""Render the workshop handout. Requires ReportLab."""

import argparse
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

PROMPTS = [
    ("Find the biggest issues", "Review [repo/file] for [focus]. Rank up to 10 issues by impact. Cite the relevant code, explain the consequence, and give an example where applicable."),
    ("Decide one issue at a time", "Take the findings one at a time. Recommend a fix, explain the trade-off, then wait for my decision. Record each as accepted, deferred, or rejected. Build a plan from the accepted items."),
    ("Trace unfamiliar code", "Trace [input] from its source to [output]. Name the functions it passes through and explain each transformation. Keep this pass read-only."),
    ("Clarify what matters", "Read [files] first. If a missing requirement would change your implementation, ask me the most important question first. State any smaller assumptions."),
    ("Define an Agent Contract", "Your goal is [goal]. Use [inputs]. Respect [constraints]. The task is complete when [acceptance criteria]. Verify the result before reporting completion."),
    ("Manage context", "Identify the files, documentation and prior decisions relevant to [task]. Explain what information is missing. Avoid loading unrelated material."),
    ("Compare options", "Compare [option A] and [option B] for [task]. Consider [constraints]. Explain the trade-offs and recommend an approach."),
    ("Reproduce a bug", "With [input], [command] gives [actual result]. I expected [expected result]. Capture the mismatch in a failing test, apply the smallest fix, and rerun the test."),
    ("Bound the edit", "Implement [change] in [component]. Preserve [interfaces and formats]. Follow [reference implementation]. List unrelated cleanup separately."),
    ("Verify the result", "Check each acceptance criterion. Report the command you ran and what it showed. Identify anything you couldn't verify and explain why."),
]

INTRO = "Choose a prompt for the task at hand. Replace bracketed text with your details."
PLAN_NOTE = "Use Plan Mode in OpenCode or Codex while discussing changes. It is intended to avoid implementation, but may still allow read-only commands. Switch to execution when ready."

GUIDES = [
    ('GitHub', 'https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-engineering'),
    ('Anthropic', 'https://www.anthropic.com/research/claude-code-best-practices'),
    ('OpenAI', 'https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex'),
]

NAVY = "#003359"
TEAL = "#00747A"
INK = "#17324D"
MUTED = "#607487"


def render(output_dir):
    pdf = Canvas(str(output_dir / "prompting-cheat-sheet.pdf"), pagesize=A4, invariant=True)
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
    label(left, height - 105, INTRO, 11, INK)
    note = paragraph(PLAN_NOTE, "Helvetica", INK, 10.5, 13)
    _, note_height = note.wrap(right - left, height)
    note.drawOn(pdf, left, height - 116 - note_height)
    y = height - 128 - note_height
    for number, (title, prompt) in enumerate(PROMPTS, 1):
        pdf.setStrokeColor(HexColor(TEAL if number == 1 else "#DCE6EA"))
        pdf.setLineWidth(1.5 if number == 1 else 0.6)
        pdf.line(left, y, right, y)
        top = y - 7
        label(left, top - 10, f"{number:02}", 10.5, TEAL, "Helvetica-Bold")
        heading = paragraph(title, "Helvetica-Bold", NAVY, 11, 14)
        body = paragraph(re.sub(r"\[([^\]]+)\]", r"<i>[\1]</i>", escape(prompt)), "Helvetica", INK, 11, 13.5)
        body_x = left + 143
        _, h1 = heading.wrap(109, height)
        _, h2 = body.wrap(right - body_x, height)
        heading.drawOn(pdf, left + 23, top - h1)
        body.drawOn(pdf, body_x, top - h2)
        y = top - max(h1, h2) - 8

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


def markdown(output_dir):
    lines = ["# Prompting cheat sheet", "", INTRO, "", PLAN_NOTE, ""]
    for number, (title, prompt) in enumerate(PROMPTS, 1):
        lines.extend([f"## {number}. {title}", "", prompt, ""])
    lines.extend(["## Prompting guides", ""] + [f"- [{name}]({url})" for name, url in GUIDES])
    (output_dir / "prompting-cheat-sheet.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--markdown-only", action="store_true")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    markdown(args.output_dir)
    if not args.markdown_only:
        render(args.output_dir)
