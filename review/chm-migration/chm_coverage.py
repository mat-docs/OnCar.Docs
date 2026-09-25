"""Measure how much of each CHM topic's text appears on the SystemMonitor.Site docs.

Coverage = share of the topic's word 5-grams found anywhere in the docs corpus.
Also records the single docs page contributing the most matching 5-grams.
"""
import html, json, re, sys
from pathlib import Path

SCRATCH = Path(__file__).parent
CHM = SCRATCH / "chm"  # decompile first: hh.exe -decompile chm ATLAS9/OCSHelp/Main/SMV7HtmlHelp/SystemMonitor.chm
DOCS = Path(r"C:\MclDev\SystemMonitor.Site\docs")
N = 5

def words(text):
    text = text.lower().replace("\u2019", "'").replace("\u2018", "'")
    text = re.sub(r"[\u201c\u201d]", '"', text)
    return re.findall(r"[a-z0-9]+(?:['.][a-z0-9]+)*", text)

def grams(ws):
    return {" ".join(ws[i:i + N]) for i in range(len(ws) - N + 1)}

def htm_text(p):
    raw = p.read_bytes().decode("utf-8", errors="ignore")
    if "charset=windows-1252" in raw.lower() or "\ufffd" in raw:
        raw = p.read_bytes().decode("cp1252", errors="ignore")
    raw = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<!--.*?-->", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return html.unescape(raw)

def md_text(p):
    t = p.read_text(encoding="utf-8", errors="ignore")
    t = re.sub(r"(?s)\A---.*?---", " ", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\]\([^)]*\)", "] ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return html.unescape(t)

# TOC
hhc = (CHM / "SystemMonitor.hhc").read_text(encoding="utf-8", errors="ignore")
toc, stack = [], []
for m in re.finditer(r"(?is)(<ul>|</ul>|<object type=\"text/sitemap\">(.*?)</object>)", hhc):
    tok = m.group(1).lower()
    if tok == "<ul>":
        stack.append(None)
    elif tok == "</ul>":
        if stack: stack.pop()
    else:
        body = m.group(2)
        name = re.search(r'name="Name" value="([^"]*)"', body, re.I)
        local = re.search(r'name="local" value="([^"]*)"', body, re.I)
        name = html.unescape(name.group(1)) if name else "?"
        if stack: stack[-1] = name
        path = " > ".join(s for s in stack if s)
        if local:
            toc.append((path, local.group(1).replace("\\", "/")))

docs = {}
for p in DOCS.rglob("*.md"):
    docs[p.relative_to(DOCS).as_posix()] = grams(words(md_text(p)))
corpus = set().union(*docs.values())

rows, seen = [], set()
all_htm = sorted((CHM / "htm_files").glob("*.htm"))
entries = [(path, CHM / f) for path, f in toc] + [("(not in TOC)", p) for p in all_htm]
for path, p in entries:
    key = p.name.lower()
    if key in seen or not p.exists():
        continue
    seen.add(key)
    ws = words(htm_text(p))
    g = grams(ws)
    if not g:
        rows.append(dict(toc=path, file=p.name, words=len(ws), coverage=None, best=None, best_share=0))
        continue
    hit = g & corpus
    best, best_n = None, 0
    for d, dg in docs.items():
        n = len(g & dg)
        if n > best_n:
            best, best_n = d, n
    rows.append(dict(toc=path, file=p.name, words=len(ws),
                     coverage=round(len(hit) / len(g), 3), best=best,
                     best_share=round(best_n / len(g), 3)))

(SCRATCH / "chm_coverage.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
def band(c):
    if c is None: return "empty"
    return "migrated(>=80%)" if c >= .8 else "partial(40-80%)" if c >= .4 else "low(10-40%)" if c >= .1 else "missing(<10%)"
from collections import Counter
print(Counter(band(r["coverage"]) for r in rows))
print("topics:", len(rows), "in TOC:", sum(r["toc"] != "(not in TOC)" for r in rows))
