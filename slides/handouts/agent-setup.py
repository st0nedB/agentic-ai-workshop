"""Render the workshop agent setup handouts. Requires ReportLab."""

from pathlib import Path
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

NAVY = "#003359"
TEAL = "#00747A"
INK = "#17324D"
MUTED = "#607487"


def render(pdf, title, rows, guides):
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
    label(left, height - 40, "Agentic AI Workshop  ·  Agent setup", 10, MUTED)
    label(left, height - 81, title, 32, NAVY, "Helvetica-Bold")
    label(left, height - 105, "Connect to OpenRouter from your workshop Codespace.", 11, INK)
    y = height - 132
    for number, (title, prompt) in enumerate(rows, 1):
        pdf.setStrokeColor(HexColor(TEAL if number == 1 else "#DCE6EA"))
        pdf.setLineWidth(1.5 if number == 1 else 0.6)
        pdf.line(left, y, right, y)
        top = y - 10
        label(left, top - 10, f"{number:02}", 10.5, TEAL, "Helvetica-Bold")
        heading = paragraph(title, "Helvetica-Bold", NAVY, 11, 14)
        body = paragraph(prompt, "Helvetica", INK, 10, 12.5)
        body_x = left + 120
        _, h1 = heading.wrap(86, height)
        _, h2 = body.wrap(right - body_x, height)
        heading.drawOn(pdf, left + 23, top - h1)
        body.drawOn(pdf, body_x, top - h2)
        y = top - max(h1, h2) - 7

    if y < 46:
        raise ValueError("Handout content overlaps the footer")
    pdf.setStrokeColor(HexColor("#FF7900"))
    pdf.setLineWidth(2)
    pdf.line(left, 29, left, 42)
    label(left + 7, 32, "TU Ilmenau  ·  AI Agent Workshop", 9, MUTED)
    x = right
    for title, url in reversed(guides):
        extent = pdf.stringWidth(title, "Helvetica", 9)
        x -= extent
        label(x, 32, title, 9, TEAL)
        pdf.linkURL(url, (x, 30, x + extent, 42))
        x -= 10
    label(x - pdf.stringWidth("Documentation", "Helvetica", 9), 32, "Documentation", 9, MUTED)
    pdf.showPage()



def code(value):
    from xml.sax.saxutils import escape
    return '<font name="Courier">' + escape(value).replace(" ", "&#160;").replace("\n", "<br/>") + '</font>'


KEY = ('Get an API key', 'Sign in at <link href="https://openrouter.ai">openrouter.ai</link>. Add credits for paid models. Create a key at <link href="https://openrouter.ai/settings/keys">API Keys</link> and set a spending limit if available. Never share the key in prompts, Git or screenshots. OpenRouter bills separately from GitHub.')
TERMINAL = ('Open the terminal', 'In the Codespace, select <b>Terminal &gt; New Terminal</b>. The agent is preinstalled. Check the repository root with ' + code('git rev-parse --show-toplevel') + '. Start the agent in the relevant exercise folder to focus its context; this is not a security boundary.')
TEST = ('Verify the connection', 'Prompt: <i>Run pwd and report its output. Do not modify files.</i> Check the actual tool call and verify the expected model appears in <link href="https://openrouter.ai/activity">OpenRouter Activity</link>. ')
OPEN_CODE = [
    KEY, TERMINAL,
    ('Start and connect', 'Run ' + code('opencode') + ' in the terminal. Inside OpenCode, enter ' + code('/connect') + ', select OpenRouter, paste the key and confirm. Slash commands are entered in the agent, not Bash. The saved login normally survives a restart; reconnect after a rebuild or deletion if needed.'),
    ('Select a model', 'Enter ' + code('/models') + ' and choose an OpenRouter model with tool-calling support. Check prices at <link href="https://openrouter.ai/models">OpenRouter Models</link> and verify the selected model.'),
    ('Plan and build', 'Use Shift+Tab to switch between Plan and Build in OpenCode 2.x; check the on-screen shortcut if it differs. Review the plan before allowing edits.'),
    TEST,
    ('Troubleshoot', 'Unauthorized: reconnect and check the key. Insufficient credits: check your balance. Model unavailable: choose another via ' + code('/models') + '. Exit with ' + code('/exit') + '; reopen with ' + code('opencode') + '.'),
]
CODEX = [
    KEY, TERMINAL,
    ('Load the key', 'In Bash, run the following and paste the key when prompted. Input is hidden; repeat in each new terminal or after a Codespace restart.<br/>' + code('read -rsp "OpenRouter API key: " OPENROUTER_API_KEY\nexport OPENROUTER_API_KEY\necho')),
    ('Open configuration', code('mkdir -p ~/.codex\nnano ~/.codex/config.toml') + '<br/>Preserve existing settings. Home-directory config may be lost on rebuild; deletion removes the Codespace.'),
    ('Configure provider', code('model = "openai/gpt-5.6-luna"\nmodel_provider = "openrouter"\n\n[model_providers.openrouter]\nname = "OpenRouter"\nbase_url = "https://openrouter.ai/api/v1"\nwire_api = "responses"\n\n[model_providers.openrouter.auth]\ncommand = "sh"\nargs = ["-c", "echo $OPENROUTER_API_KEY"]') + '<br/>Save with Ctrl+O, Enter; exit with Ctrl+X.'),
    ('Start Codex', 'Start with the cheaper example model, or choose another compatible full ID from <link href="https://openrouter.ai/models">OpenRouter Models</link> with Responses API and tool support. Run ' + code('codex') + ' in the same terminal. Use ' + code('/model') + ' or ' + code('/status') + ' inside Codex.'),
    TEST,
    ('Troubleshoot', 'Check the key, credits, TOML syntax and model compatibility. Exit with ' + code('/quit') + '.'),
]


def markdown_body(value):
    import re
    from html import unescape

    def convert_code(match):
        source = unescape(match.group(1).replace("<br/>", "\n"))
        if "\n" in source:
            return "\n\n" + chr(96) * 3 + "\n" + source + "\n" + chr(96) * 3 + "\n\n"
        return chr(96) + source + chr(96)

    value = re.sub(r'<font name="Courier">(.*?)</font>', convert_code, value, flags=re.S)
    value = re.sub(r'<link href="([^"]+)">(.*?)</link>', r'[\2](\1)', value)
    value = value.replace("<b>", "**").replace("</b>", "**")
    value = value.replace("<i>", "*").replace("</i>", "*").replace("<br/>", "\n\n")
    return re.sub(r"\n{3,}", "\n\n", unescape(value).replace("\xa0", " ")).strip()


def render_markdown():
    parts = ["# Agent setup", "Connect to OpenRouter from your workshop Codespace.",
             "Generated from agent-setup.py; edit that source, not this file."]
    for name, rows in [("OpenCode", OPEN_CODE), ("Codex", CODEX)]:
        parts.append("## " + name)
        for n, (heading, body) in enumerate(rows, 1):
            parts.extend([f"### {n}. {heading}", markdown_body(body)])
    return "\n\n".join(parts) + "\n"


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--markdown-only", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "Agent-Setup.md").write_text(render_markdown(), encoding="utf-8")
    if args.markdown_only:
        raise SystemExit(0)
    pdf = Canvas(str(args.output_dir / "Agent-Setup.pdf"), pagesize=A4, invariant=True)
    pdf.setTitle("Agent Setup")
    pdf.setAuthor("Agentic AI Workshop")
    render(pdf, "OpenCode setup", OPEN_CODE,
           [("Providers", "https://opencode.ai/docs/providers/"), ("Models", "https://opencode.ai/docs/models/")])
    render(pdf, "Codex setup", CODEX,
           [("Codex / OpenRouter", "https://openrouter.ai/blog/tutorials/codex-cli-openrouter/")])

    pdf.save()
