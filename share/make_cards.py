#!/usr/bin/env python3
"""Generate 1080x1350 WeChat-Moments cards for the Market Research design-philosophy series.
Run: python3 share/make_cards.py  -> writes PNGs to share/moments/
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1080, 1350
MARGIN = 96
CONTENT_W = W - 2 * MARGIN

INK = (10, 14, 26)          # background
WHITE = (245, 245, 240)
MUTED = (150, 162, 178)     # body text
FAINT = (95, 105, 122)      # footer
ACCENT = (201, 123, 76)     # terracotta

HIRA = "/System/Library/Fonts/Hiragino Sans GB.ttc"
def font(size, bold=False):
    return ImageFont.truetype(HIRA, size, index=1 if bold else 0)

def wrap(draw, text, fnt, max_w):
    """Greedy wrap; breaks per character (works for CJK). Honors explicit \n."""
    out = []
    for para in text.split("\n"):
        if para == "":
            out.append("")
            continue
        line = ""
        for ch in para:
            if draw.textlength(line + ch, font=fnt) <= max_w:
                line += ch
            else:
                out.append(line)
                line = ch
        out.append(line)
    return out

def draw_tracked(draw, xy, text, fnt, fill, track=6):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + track

cards = [
    {
        "file": "01_intro.png",
        "eyebrow": "MARKET RESEARCH · 设计理念",
        "title": "做投研 AI，\n我最在意的是「严谨」",
        "body": "速度，AI 已经够快了。难的是让它产出的每一个数字都站得住脚。这套 skill，把投研的纪律写成了 LLM 能从头跑到尾的流程。",
    },
    {
        "file": "02_provenance.png",
        "eyebrow": "原则 01 · 来源可追溯",
        "title": "任何数字，\n都要追得到原始来源",
        "body": "追不到的，就标记存疑并剔除——绝不写进结论。宁可写「未公开」，也不给一个看似合理的猜测。",
    },
    {
        "file": "03_three_state.png",
        "eyebrow": "原则 02 · 三态标注",
        "title": "事实 / 估算 / 推断，\n分清楚",
        "body": "三者用不同措辞标注，绝不混为一谈。「据 IMF」和「据市场估算」，从来不是一回事。",
    },
    {
        "file": "04_human.png",
        "eyebrow": "原则 03 · 人机分工",
        "title": "AI 是副驾，\n不是主驾",
        "body": "假设、scope、最终签字，都由人决定。流程里写死了人工节点和质量门——AI 提供素材和初稿，结论由人拍板。",
    },
    {
        "file": "05_judgment.png",
        "eyebrow": "设计思路 · 核心判断",
        "title": "把 AI 当成\n一个初级分析师",
        "body": "快、知识面广，但直觉没经过训练。所以我的活儿不是让它更聪明，而是给它铺一条轨道，在错误进正文之前拦下来。",
    },
    {
        "file": "06_structure.png",
        "eyebrow": "设计思路 · 把严谨写进结构",
        "title": "严谨，不靠提醒，\n靠写死",
        "body": "「记得要严谨」没用。我把人工确认和质量门写死进 8 步工作流——AI 跑得再顺，关键处也得停下等人拍板。",
    },
]

FOOTER = "Gen · genli-ai.github.io/portfolio"

f_eyebrow = font(30, bold=True)
f_title = font(64, bold=True)
f_body = font(38, bold=False)
f_foot = font(28, bold=False)

outdir = Path(__file__).parent / "moments"
outdir.mkdir(exist_ok=True)

for c in cards:
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)

    # top accent bar
    d.rectangle([MARGIN, 130, MARGIN + 72, 130 + 5], fill=ACCENT)
    # eyebrow
    draw_tracked(d, (MARGIN, 168), c["eyebrow"], f_eyebrow, ACCENT, track=4)

    # title (upper-middle)
    y = 360
    for line in wrap(d, c["title"], f_title, CONTENT_W):
        d.text((MARGIN, y), line, font=f_title, fill=WHITE)
        y += 86

    # body
    y += 40
    for line in wrap(d, c["body"], f_body, CONTENT_W):
        d.text((MARGIN, y), line, font=f_body, fill=MUTED)
        y += 62

    # footer
    d.line([MARGIN, H - 150, W - MARGIN, H - 150], fill=(36, 42, 56), width=2)
    d.text((MARGIN, H - 120), FOOTER, font=f_foot, fill=FAINT)

    img.save(outdir / c["file"], "PNG")
    print("wrote", c["file"])

print("done ->", outdir)
