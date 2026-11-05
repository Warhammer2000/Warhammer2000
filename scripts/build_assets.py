#!/usr/bin/env python3
"""Build every SVG the profile README shows, in a dark and a light variant.

    python scripts/build_assets.py

The README picks a variant with <picture> + prefers-color-scheme; GitHub maps
that media query to the viewer's GitHub theme, so both files must exist.

Why hand-made SVGs: the community-hosted card services this profile used
(github-readme-stats, trophies, activity graph) were shut down on Vercel and
left broken images behind. Static files in the repository cannot go down.

Constraints of an SVG shown through <img>: no web fonts, no scripts, no
external images, no clickable links. Text uses the system font stack; motion
is CSS/SMIL and switches off under prefers-reduced-motion.

Edit the CONTENT section below and re-run; then commit assets/.
"""
from __future__ import annotations

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

# ── CONTENT ────────────────────────────────────────────────────────────────

HEADER = {
    "status": "Open to remote B2B · EU/EMEA",
    "name": "Rustam Pulatov",
    "role": ".NET Backend Developer",
    "company": " @ Vention",
    "focus": "High-load systems · Microservices · Azure · AI/LLM tooling",
    "meta": "Tashkent · UTC+5 · EN / RU / UZ",
    "stats": [
        ("7×", "throughput improvement"),
        ("5M+", "users reached"),
        ("50+", "mentees"),
        ("Rising Star", "Vention · 2025"),
    ],
}

PROJECTS = [
    {
        "slug": "kafka",
        "title": "Kafka hands-on",
        "sub": "kafka-na-palcah",
        "badge": ("LIVE DEMO", "green"),
        "accent": "blue",
        "glyph": "kafka",
        "desc": "Apache Kafka explained with demos you can click: partitions, offsets, "
                "consumer groups, lag, ISR and rebalances. Fifteen chapters, RU / EN, "
                "zero dependencies.",
        "lang": ("JavaScript", "#f1e05a"),
        "tags": "interactive · no build step",
    },
    {
        "slug": "council",
        "title": "Consilium council",
        "sub": "claude-plugins",
        "badge": ("CLAUDE CODE", "violet"),
        "accent": "violet",
        "glyph": "council",
        "desc": "Ask a hard question, get a council: 2–6 sub-agents locked to opposing "
                "stances, blind to each other, with anti-sycophancy guards, then an "
                "honest synthesis.",
        "lang": ("Plugin", None),
        "tags": "multi-agent · /council-tech",
    },
    {
        "slug": "architect",
        "title": "Software Architect track",
        "sub": "Yandex Practicum · 10 repos",
        "badge": ("CASE STUDIES", "green"),
        "accent": "green",
        "glyph": "layers",
        "desc": "Systems designed end to end: to-be architecture in C4, Kubernetes HPA "
                "under Locust load, Privacy by Design, SSO + BFF + CDC, "
                "Terraform and Data Mesh.",
        "lang": ("Architecture", None),
        "tags": "C4 · Terraform · Kubernetes",
    },
    {
        "slug": "ai-challenge",
        "title": "Vention AI Challenge 2.0",
        "sub": "Task-1 · Task-2 · Task-3 · Task-4",
        "badge": ("2 LIVE", "green"),
        "accent": "amber",
        "glyph": "bolt",
        "desc": "Four tasks, four stacks: a pixel-faithful React leaderboard, a Lovable "
                "events app, an n8n + Telegram interview coach and a C# MCP server for "
                "air-traffic coordination.",
        "lang": ("TypeScript", "#3178c6"),
        "tags": "React · n8n · MCP · C#",
    },
]

STACK = [
    ("Backend", "blue", ["C#", ".NET 8", "ASP.NET Core", "EF Core", "REST", "Microservices"]),
    ("Azure", "violet", ["Functions", "Service Bus", "API Management", "Blob Storage"]),
    ("Data", "green", ["SQL Server", "PostgreSQL", "MySQL", "Oracle", "Redis", "MongoDB", "Kafka"]),
    ("AI / LLM", "pink", ["OpenAI", "LangChain", "RAG", "Embeddings", "NLP", "GPT fine-tuning",
                          "MCP", "Python"]),
    ("Architecture", "amber", ["Clean Architecture", "DDD", "CQRS", "Event-Driven", "SOLID"]),
    ("Tooling", "blue", ["Docker", "Linux", "Bash", "Git", "GitHub Actions"]),
    ("Also", "faint", ["TypeScript", "JavaScript", "C++", "Unity", "Xamarin"]),
]
CORE = {"C#", ".NET 8", "ASP.NET Core", "Functions", "Service Bus", "SQL Server", "RAG"}

CERTS = [
    ("Microsoft", "Azure Developer Associate", "AZ-204", "blue"),
    ("Microsoft", "Azure Fundamentals", "AZ-900", "blue"),
    ("IBM", "Generative AI with RAG & LangChain", None, "violet"),
    ("Yandex Practicum", "Algorithms & Data Structures", None, "amber"),
]

BUTTONS = [("linkedin", "LinkedIn"), ("email", "Email"), ("telegram", "Telegram")]

# ── THEMES ─────────────────────────────────────────────────────────────────
# Neutrals follow GitHub's Primer palette so the cards sit naturally on the page.

THEMES = {
    "dark": {
        "bg0": "#0d1117", "bg1": "#121a2c", "card": "#0f141b", "card2": "#151b23",
        "border": "#2b333d", "line": "#21272f",
        "fg": "#e6edf3", "text": "#c3ccd5", "muted": "#9198a1", "faint": "#6e7681",
        "blue": "#58a6ff", "violet": "#a78bfa", "green": "#3fb950", "amber": "#e3b341",
        "pink": "#f778ba",
        "chip": "#151b23", "chip_border": "#2f3742",
        "glow1": "#7c3aed", "glow1_op": 0.30, "glow2": "#1f6feb", "glow2_op": 0.18,
        "dots": "#c9d1d9", "dots_op": 0.13, "grad0": "#79c0ff", "grad1": "#b392f0",
    },
    "light": {
        "bg0": "#ffffff", "bg1": "#f4f2fc", "card": "#ffffff", "card2": "#f6f8fa",
        "border": "#d1d9e0", "line": "#e6eaef",
        "fg": "#1f2328", "text": "#3d444d", "muted": "#59636e", "faint": "#818b98",
        "blue": "#0969da", "violet": "#7c3aed", "green": "#1a7f37", "amber": "#9a6700",
        "pink": "#bf3989",
        "chip": "#f6f8fa", "chip_border": "#d1d9e0",
        "glow1": "#a78bfa", "glow1_op": 0.20, "glow2": "#54aeff", "glow2_op": 0.13,
        "dots": "#1f2328", "dots_op": 0.10, "grad0": "#0969da", "grad1": "#7c3aed",
    },
}

REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}.packet{display:none}}"

# ── TEXT METRICS ───────────────────────────────────────────────────────────
# SVG has no text wrapping and no font metrics, so widths are estimated from a
# per-glyph table close to Segoe UI / SF Pro. Layout keeps ~10% slack for wider
# fallback fonts.

_EM: dict[str, float] = {" ": 0.27, "·": 0.27, "–": 0.5, "—": 0.95, "×": 0.58, "+": 0.58,
                         "&": 0.70, "→": 0.85, "@": 0.90, "#": 0.60, "/": 0.38, "-": 0.36}
for _c in "iljI|!.,:;'ʻ":
    _EM[_c] = 0.25
for _c in "frt()[]":
    _EM[_c] = 0.36
for _c in "mw":
    _EM[_c] = 0.80
for _c in "MW":
    _EM[_c] = 0.88


def _em(ch: str) -> float:
    if ch in _EM:
        return _EM[ch]
    if ch.isdigit():
        return 0.56
    if 0x0400 <= ord(ch) <= 0x04FF:  # Cyrillic
        if ch in "мшщжюыМШЩЖЮЫ":
            return 0.78
        return 0.66 if ch.isupper() else 0.55
    if ch.isupper():
        return 0.65
    if ch.islower():
        return 0.53
    return 0.60


def tw(s: str, size: float, weight: int = 400, mono: bool = False) -> float:
    if mono:
        return len(s) * 0.602 * size
    w = sum(_em(c) for c in s) * size
    return w * 1.05 if weight >= 600 else w


def wrap(s: str, size: float, max_w: float, weight: int = 400, max_lines: int = 9) -> list[str]:
    lines: list[str] = []
    cur = ""
    # split on plain spaces only, so a no-break space ("SSO + BFF") keeps a phrase whole
    for word in filter(None, s.split(" ")):
        cand = f"{cur} {word}".strip()
        if not cur or tw(cand, size, weight) <= max_w:
            cur = cand
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        raise SystemExit(f"text needs {len(lines)} lines, room for {max_lines}: {s!r}")
    return lines


def fits(s: str, size: float, max_w: float, weight: int = 400, mono: bool = False) -> None:
    w = tw(s, size, weight, mono)
    if w > max_w:
        raise SystemExit(f"text is ~{w:.0f}px, room for {max_w:.0f}px: {s!r}")


# ── SVG HELPERS ────────────────────────────────────────────────────────────

def esc(s: str) -> str:
    return escape(s, quote=True)


def n(v: float) -> str:
    return f"{round(v, 1):g}"


def text(x, y, s, size, fill, *, weight=400, mono=False, anchor=None, spacing=None,
         cls=None) -> str:
    a = [f'x="{n(x)}"', f'y="{n(y)}"', f'font-size="{n(size)}"']
    if weight != 400:
        a.append(f'font-weight="{weight}"')
    if mono:
        a.append(f'font-family="{MONO}"')
    if anchor:
        a.append(f'text-anchor="{anchor}"')
    if spacing is not None:
        a.append(f'letter-spacing="{spacing}"')
    if cls:
        a.append(f'class="{cls}"')
    a.append(f'fill="{fill}"')
    return f"<text {' '.join(a)}>{esc(s)}</text>"


def rect(x, y, w, h, rx, fill="none", stroke=None, *, fo=None, so=None, sw=1, cls=None,
         style=None) -> str:
    a = [f'x="{n(x)}"', f'y="{n(y)}"', f'width="{n(w)}"', f'height="{n(h)}"', f'rx="{n(rx)}"',
         f'fill="{fill}"']
    if fo is not None:
        a.append(f'fill-opacity="{fo}"')
    if stroke:
        a += [f'stroke="{stroke}"', f'stroke-width="{sw}"']
    if so is not None:
        a.append(f'stroke-opacity="{so}"')
    if cls:
        a.append(f'class="{cls}"')
    if style:
        a.append(f'style="{style}"')
    return f"<rect {' '.join(a)}/>"


def svg(w, h, title, body, *, style="", defs="") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{n(w)}" height="{n(h)}" '
        f'viewBox="0 0 {n(w)} {n(h)}" role="img" aria-labelledby="title" font-family="{SANS}">\n'
        f'<title id="title">{esc(title)}</title>\n'
        + (f"<style>{style}</style>\n" if style else "")
        + (f"<defs>{defs}</defs>\n" if defs else "")
        + body
        + "\n</svg>\n"
    )


# ── HEADER ─────────────────────────────────────────────────────────────────

def header(t: dict) -> str:
    W, H, X = 850, 316, 40
    h = HEADER

    css = (
        "@keyframes flow{to{stroke-dashoffset:-16}}"
        ".dash{stroke-dasharray:3 5;animation:flow 1.4s linear infinite}"
        "@keyframes pulse{0%,100%{stroke-opacity:.4}50%{stroke-opacity:1}}"
        ".lane{animation:pulse 3.6s ease-in-out infinite}"
        "@keyframes ping{0%{transform:scale(1);opacity:.7}80%,100%{transform:scale(2.8);opacity:0}}"
        ".ping{transform-box:fill-box;transform-origin:center;"
        "animation:ping 2.4s cubic-bezier(0,0,.2,1) infinite}"
        "@keyframes blink{50%{fill-opacity:0}}"
        ".caret{animation:blink 1.1s steps(1) infinite}"
        + REDUCED
    )
    defs = (
        f'<clipPath id="clip"><rect width="{W}" height="{H}" rx="18"/></clipPath>'
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{t["bg0"]}"/><stop offset="1" stop-color="{t["bg1"]}"/>'
        f"</linearGradient>"
        f'<radialGradient id="glow1" cx="0.85" cy="0.05" r="0.55">'
        f'<stop offset="0" stop-color="{t["glow1"]}" stop-opacity="{t["glow1_op"]}"/>'
        f'<stop offset="1" stop-color="{t["glow1"]}" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="glow2" cx="0.05" cy="1" r="0.5">'
        f'<stop offset="0" stop-color="{t["glow2"]}" stop-opacity="{t["glow2_op"]}"/>'
        f'<stop offset="1" stop-color="{t["glow2"]}" stop-opacity="0"/></radialGradient>'
        f'<pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse">'
        f'<circle cx="8" cy="8" r="1" fill="{t["dots"]}" fill-opacity="{t["dots_op"]}"/></pattern>'
        f'<radialGradient id="fadeg" cx="0.55" cy="0.5" r="0.55">'
        f'<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>'
        f"</radialGradient>"
        f'<mask id="fade"><rect x="430" y="0" width="420" height="236" fill="url(#fadeg)"/></mask>'
        f'<linearGradient id="num" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{t["grad0"]}"/><stop offset="1" stop-color="{t["grad1"]}"/>'
        f"</linearGradient>"
        f'<marker id="arrow" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="6" markerHeight="6" '
        f'orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{t["faint"]}"/></marker>'
    )

    p: list[str] = [
        '<g clip-path="url(#clip)">',
        f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
        f'<rect width="{W}" height="{H}" fill="url(#glow1)"/>',
        f'<rect width="{W}" height="{H}" fill="url(#glow2)"/>',
        '<rect x="430" y="0" width="420" height="236" fill="url(#dots)" mask="url(#fade)"/>',
        "</g>",
        rect(0.5, 0.5, W - 1, H - 1, 18, "none", t["border"]),
    ]

    # availability pill
    sw = tw(h["status"], 12.5, 600)
    p.append(rect(X, 34, 30 + sw + 14, 26, 13, t["green"], t["green"], fo=0.10, so=0.4))
    p.append(f'<circle class="ping" cx="{X + 15}" cy="47" r="4" fill="{t["green"]}"/>')
    p.append(f'<circle cx="{X + 15}" cy="47" r="4" fill="{t["green"]}"/>')
    p.append(text(X + 27, 51.5, h["status"], 12.5, t["fg"], weight=600))

    # identity
    fits(h["name"], 44, 400, 700)
    p.append(text(X, 113, h["name"], 44, t["fg"], weight=700, spacing=-0.8))
    p.append(
        f'<text x="{X}" y="146" font-size="19" font-weight="600" fill="{t["fg"]}">'
        f'{esc(h["role"])}<tspan fill="{t["muted"]}" font-weight="500">{esc(h["company"])}</tspan></text>'
    )
    fits(h["focus"], 14.5, 425)
    p.append(text(X, 175, h["focus"], 14.5, t["muted"]))
    # the caret rides in the same <text>, so it lands after the last glyph whatever
    # monospace font the viewer has (Consolas is ~9% narrower than Menlo/SF Mono)
    p.append(
        f'<text x="{X}" y="203" font-size="12.5" font-family="{MONO}" fill="{t["faint"]}">'
        f'{esc(h["meta"])}<tspan class="caret" dx="5" font-size="11" fill="{t["blue"]}">█</tspan>'
        f"</text>"
    )

    # "what I build": a request flowing through the kind of system I work on
    p.append(text(478, 58, "// what I build", 11, t["faint"], mono=True))
    cols, rows = [509, 598, 690, 783], [92, 146, 200]
    nodes = {
        "client": (0, 0, None), "apim": (1, 0, None), "domain": (2, 0, "blue"),
        "sql": (3, 0, "blue"), "bus": (2, 1, "green"), "func": (3, 1, "green"),
        "ai": (1, 2, "violet"), "rag": (2, 2, "violet"), "llm": (3, 2, "violet"),
    }
    geo = {}
    for name, (c, r, lane) in nodes.items():
        w = max(46.0, len(name) * 0.602 * 11.5 + 20)
        geo[name] = (cols[c], rows[r], w, 26.0, lane)
    edges = [
        ("client", "apim", "blue"), ("apim", "domain", "blue"), ("domain", "sql", "blue"),
        ("domain", "bus", "green"), ("bus", "func", "green"),
        ("apim", "ai", "violet"), ("ai", "rag", "violet"), ("rag", "llm", "violet"),
    ]
    for a, b, lane in edges:
        ax, ay, aw, ah, _ = geo[a]
        bx, by, bw, bh, _ = geo[b]
        if ay == by:
            d = f"M{n(ax + aw / 2 + 3)} {ay} H{n(bx - bw / 2 - 4)}"
        else:
            d = f"M{ax} {n(ay + ah / 2 + 3)} V{n(by - bh / 2 - 4)}"
        p.append(f'<path d="{d}" stroke="{t["border"]}" stroke-width="1.3" fill="none" '
                 f'marker-end="url(#arrow)"/>')
        p.append(f'<path class="dash" d="{d}" stroke="{t[lane]}" stroke-width="1.3" fill="none" '
                 f'stroke-opacity="0.85"/>')
    packets = [
        ("blue", f"M{cols[0]} {rows[0]} H{cols[3]}", "0s"),
        ("green", f"M{cols[2]} {rows[0]} V{rows[1]} H{cols[3]}", "1.2s"),
        ("violet", f"M{cols[1]} {rows[0]} V{rows[2]} H{cols[3]}", "2.4s"),
    ]
    for lane, path, begin in packets:
        p.append(
            f'<circle class="packet" r="3" fill="{t[lane]}" opacity="0">'
            f'<animateMotion dur="3.6s" begin="{begin}" repeatCount="indefinite" path="{path}"/>'
            f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.9;1" '
            f'dur="3.6s" begin="{begin}" repeatCount="indefinite"/></circle>'
        )
    for i, (name, (x, y, w, hh, lane)) in enumerate(geo.items()):
        stroke = t[lane] if lane else t["border"]
        p.append(rect(x - w / 2, y - hh / 2, w, hh, 7, t["card2"], stroke, sw=1.2,
                      cls="lane" if lane else None,
                      style=f"animation-delay:{i * 0.4:.1f}s" if lane else None))
        p.append(text(x, y + 4, name, 11.5, t["fg"] if lane else t["muted"], mono=True,
                      anchor="middle"))

    # highlights
    p.append(f'<path d="M{X} 230 H{W - X}" stroke="{t["line"]}" stroke-width="1"/>')
    col_w = (W - 2 * X) / 4
    for i, (num, label) in enumerate(h["stats"]):
        x = X + i * col_w
        if i:
            p.append(f'<path d="M{n(x - 16)} 252 V298" stroke="{t["line"]}" stroke-width="1"/>')
        fits(num, 27, col_w - 24, 700)
        fits(label, 12.5, col_w - 24)
        p.append(text(x, 274, num, 27, "url(#num)", weight=700, spacing=-0.4))
        p.append(text(x, 295, label, 12.5, t["muted"]))

    title = (f'{h["name"]} — {h["role"]}{h["company"]}. {h["focus"]}. '
             + " · ".join(f"{a} {b}" for a, b in h["stats"]))
    return svg(W, H, title, "\n".join(p), style=css, defs=defs)


# ── PROJECT CARDS ──────────────────────────────────────────────────────────

def g_kafka(x, y, c):
    out = []
    for r, count in enumerate([4, 3, 4]):
        for i in range(count):
            out.append(rect(x + 8 + i * 6.5, y + 10 + r * 7.5, 5, 5, 1.2, c,
                            fo=round(0.3 + 0.7 * (i + 1) / count, 2)))
    return "".join(out)


def g_council(x, y, c):
    pts = [(x + 20, y + 10.5), (x + 10.5, y + 27.5), (x + 29.5, y + 27.5)]
    d = "M" + " L".join(f"{n(px)} {n(py)}" for px, py in pts) + " Z"
    out = [f'<path d="{d}" fill="none" stroke="{c}" stroke-width="1.4" stroke-opacity="0.55" '
           f'stroke-linejoin="round"/>']
    out += [f'<circle cx="{n(px)}" cy="{n(py)}" r="4" fill="{c}"/>' for px, py in pts]
    out.append(f'<circle cx="{x + 20}" cy="{y + 22}" r="2.2" fill="{c}" fill-opacity="0.7"/>')
    return "".join(out)


def g_layers(x, y, c):
    top = f"M{x + 20} {y + 9} L{x + 31} {y + 15} L{x + 20} {y + 21} L{x + 9} {y + 15} Z"
    mid = f"M{x + 9} {y + 20} L{x + 20} {y + 26} L{x + 31} {y + 20}"
    bot = f"M{x + 9} {y + 25} L{x + 20} {y + 31} L{x + 31} {y + 25}"
    line = (f'fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round"')
    return (f'<path d="{top}" fill="{c}"/>'
            f'<path d="{mid}" {line} stroke-opacity="0.75"/>'
            f'<path d="{bot}" {line} stroke-opacity="0.45"/>')


def g_bolt(x, y, c):
    pts = [(23, 7), (11.5, 22.5), (19, 22.5), (17, 33), (28.5, 17), (21, 17)]
    d = "M" + " L".join(f"{n(x + px)} {n(y + py)}" for px, py in pts) + " Z"
    return f'<path d="{d}" fill="{c}" stroke="{c}" stroke-width="1" stroke-linejoin="round"/>'


GLYPHS = {"kafka": g_kafka, "council": g_council, "layers": g_layers, "bolt": g_bolt}


def project_card(t: dict, pr: dict) -> str:
    W, H = 420, 176
    acc = t[pr["accent"]]
    p = [rect(0.5, 0.5, W - 1, H - 1, 14, t["card"], t["border"]),
         rect(20, 20, 40, 40, 10, acc, acc, fo=0.12, so=0.35),
         GLYPHS[pr["glyph"]](20, 20, acc)]

    badge, bkey = pr["badge"]
    bc = t[bkey]
    dot = "LIVE" in badge
    bw = tw(badge, 10.5, mono=True) + 18 + (11 if dot else 0)
    bx = W - 20 - bw
    fits(pr["title"], 17, bx - 74 - 12, 700)
    p.append(text(74, 39, pr["title"], 17, t["fg"], weight=700, spacing=-0.2))
    fits(pr["sub"], 11.5, W - 74 - 20, mono=True)
    p.append(text(74, 57.5, pr["sub"], 11.5, t["muted"], mono=True))
    p.append(rect(bx, 21, bw, 22, 11, bc, bc, fo=0.12, so=0.45))
    if dot:
        p.append(f'<circle cx="{n(bx + 12)}" cy="32" r="3" fill="{bc}"/>')
    p.append(text(bx + 9 + (11 if dot else 0), 35.8, badge, 10.5, bc, weight=700, mono=True))

    # wrap well short of the card edge: SF Pro (macOS) sets ~8-10% wider than the
    # Segoe UI this table approximates
    for i, line in enumerate(wrap(pr["desc"], 13.5, W - 56, max_lines=3)):
        p.append(text(20, 93 + i * 19.5, line, 13.5, t["text"]))

    lang, color = pr["lang"]
    p.append(f'<circle cx="26" cy="151.5" r="5" fill="{color or acc}"/>')
    p.append(text(37, 156, lang, 12, t["muted"], weight=500))
    tx = 37 + tw(lang, 12, 500) + 14
    fits(pr["tags"], 11.5, W - 20 - tx, mono=True)
    p.append(text(tx, 156, pr["tags"], 11.5, t["faint"], mono=True))

    title = f'{pr["title"]} ({pr["sub"]}) — {pr["desc"]}'
    return svg(W, H, title, "\n".join(p))


# ── TECH STACK ─────────────────────────────────────────────────────────────

def stack(t: dict) -> str:
    W, PAD, CHIP_X = 850, 24, 170
    CH, GAP, LINE_GAP, ROW_GAP, FS = 30, 8, 8, 17, 13.5
    p: list[str] = []
    y = PAD
    for i, (label, key, items) in enumerate(STACK):
        color = t[key]
        lines: list[list[tuple]] = [[]]
        x = CHIP_X
        for item in items:
            core = item in CORE
            w = tw(item, FS, 600 if core else 500) + 24
            if x + w > W - PAD and lines[-1]:
                lines.append([])
                x = CHIP_X
            lines[-1].append((item, x, w, core))
            x += w + GAP
        if i:
            p.append(f'<path d="M{PAD} {n(y - ROW_GAP / 2)} H{W - PAD}" stroke="{t["line"]}" '
                     f'stroke-width="1"/>')
        p.append(f'<circle cx="{PAD + 4}" cy="{y + CH / 2:g}" r="4" fill="{color}"/>')
        p.append(text(PAD + 16, y + CH / 2 + 4, label.upper(), 11, t["muted"], weight=600,
                      mono=True, spacing=0.8))
        for li, line in enumerate(lines):
            cy = y + li * (CH + LINE_GAP)
            for item, x, w, core in line:
                if core:
                    p.append(rect(x, cy, w, CH, 8, color, color, fo=0.12, so=0.55))
                else:
                    p.append(rect(x, cy, w, CH, 8, t["chip"], t["chip_border"]))
                p.append(text(x + w / 2, cy + CH / 2 + 4.7, item, FS,
                              t["fg"] if core else t["text"], weight=600 if core else 500,
                              anchor="middle"))
        y += len(lines) * (CH + LINE_GAP) - LINE_GAP + ROW_GAP
    H = y - ROW_GAP + PAD
    body = rect(0.5, 0.5, W - 1, H - 1, 14, t["card"], t["border"]) + "\n" + "\n".join(p)
    title = "Tech stack — " + "; ".join(f"{label}: {', '.join(items)}" for label, _, items in STACK)
    return svg(W, H, title, body)


# ── CERTIFICATIONS ─────────────────────────────────────────────────────────

def certs(t: dict) -> str:
    W, H, GAP = 850, 98, 12
    tile = (W - 3 * GAP) / 4
    p: list[str] = []
    for i, (issuer, name, code, key) in enumerate(CERTS):
        x = i * (tile + GAP)
        c = t[key]
        p.append(rect(x + 0.5, 0.5, tile - 1, H - 1, 12, t["card"], t["border"]))
        p.append(f'<circle cx="{n(x + 20)}" cy="24.5" r="3.5" fill="{c}"/>')
        p.append(text(x + 30, 28.5, issuer.upper(), 10.5, t["muted"], weight=600, mono=True,
                      spacing=0.6))
        if code:
            p.append(text(x + tile - 16, 28.5, code, 10.5, c, weight=700, mono=True, anchor="end"))
        for li, line in enumerate(wrap(name, 14, tile - 44, 600, max_lines=2)):
            p.append(text(x + 18, 57 + li * 19, line, 14, t["fg"], weight=600))
    title = "Certifications — " + "; ".join(
        f"{issuer}: {name}" + (f" ({code})" if code else "") for issuer, name, code, _ in CERTS)
    return svg(W, H, title, "\n".join(p))


# ── CONTACT BUTTONS ────────────────────────────────────────────────────────

LINKEDIN_LOGO = (
    '<rect width="24" height="24" rx="4.6" fill="#0A66C2"/><g fill="#ffffff">'
    '<path d="M5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065z"/>'
    '<path d="M7.119 20.452H3.555V9h3.564v11.452z"/>'
    '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445'
    '-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 '
    '4.267 5.455v6.286z"/></g>'
)


def button(t: dict, kind: str, label: str) -> str:
    H, FS = 40, 13.5
    W = 14 + 18 + 10 + tw(label, FS, 600) + 16
    p = [rect(0.5, 0.5, W - 1, H - 1, 10, t["card"], t["border"])]
    if kind == "linkedin":
        p.append(f'<g transform="translate(14 11) scale(0.75)">{LINKEDIN_LOGO}</g>')
    elif kind == "email":
        p.append(rect(14.5, 13.5, 17, 13, 2.5, "none", t["blue"], sw=1.6))
        p.append(f'<path d="M16 15.5 L23 20.6 L30 15.5" fill="none" stroke="{t["blue"]}" '
                 f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
    elif kind == "telegram":
        p.append('<circle cx="23" cy="20" r="9" fill="#229ED9"/>')
        p.append('<path d="M17.6 19.7 L27.6 15.8 L25.9 24.6 L22.9 22.3 L21.3 23.8 L21.5 21.2 '
                 'L25.6 17.5 L20.5 20.7 Z" fill="#ffffff"/>')
    p.append(text(42, 24.8, label, FS, t["fg"], weight=600))
    return svg(W, H, label, "\n".join(p))


# ── LINKEDIN CARD (light variant of the hand-made dark card) ───────────────

def linkedin_light() -> str:
    s = (OUT / "linkedin-card.svg").read_text(encoding="utf-8")
    swaps = [
        ('fill="#0d1117"', 'fill="#ffffff"'),
        ('stroke="#30363d"', 'stroke="#d1d9e0"'),
        ('fill="#e6edf3"', 'fill="#1f2328"'),
        ('fill="#8b949e"', 'fill="#59636e"'),
        ('fill="#6e7681"', 'fill="#6e7781"'),
        ('stop-opacity="0.30"', 'stop-opacity="0.12"'),
    ]
    for old, new in swaps:
        if old not in s:
            raise SystemExit(f"linkedin-card.svg changed: {old} not found")
        s = s.replace(old, new)
    return s


# ── MAIN ───────────────────────────────────────────────────────────────────

def write(name: str, content: str) -> None:
    (OUT / name).write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    count = 0
    for mode, t in THEMES.items():
        files = {f"header-{mode}.svg": header(t), f"stack-{mode}.svg": stack(t),
                 f"certs-{mode}.svg": certs(t)}
        files.update({f"project-{pr['slug']}-{mode}.svg": project_card(t, pr) for pr in PROJECTS})
        files.update({f"btn-{kind}-{mode}.svg": button(t, kind, label) for kind, label in BUTTONS})
        for name, content in files.items():
            write(name, content)
            count += 1
    write("linkedin-card-light.svg", linkedin_light())
    print(f"wrote {count + 1} files to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
