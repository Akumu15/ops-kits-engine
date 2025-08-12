import pandas as pd, os, datetime as dt
from jinja2 import Template

SITE_BASE = ""  # set to https://<user>.github.io/<repo> for absolute links if you like

os.makedirs("docs", exist_ok=True)
prod = pd.read_csv("data/products.csv")
inds = pd.read_csv("data/industries.csv")

with open("template.html", encoding="utf-8") as f:
    tpl = Template(f.read())

items = []
for _, p in prod.iterrows():
    for _, i in inds.iterrows():
        ctx = {**p.to_dict(), **i.to_dict()}
        # Map tokens like {{industry}} to i['name'] within strings
        for k, v in list(ctx.items()):
            if isinstance(v, str):
                ctx[k] = v.replace("{{industry}}", i["name"])
        slug = f"{p['slug']}-{i['slug']}"
        html = tpl.render(**ctx)
        path = f"docs/{slug}.html"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        url = (SITE_BASE + "/" if SITE_BASE else "") + f"{slug}.html"
        items.append({"title": f"{p['title']} for {i['name']}", "url": url})

# Build index
index_html = "<h1>Ops Kits Engine</h1><ul>" + "".join([f'<li><a href="{x["url"]}">{x["title"]}</a></li>' for x in items[:300]]) + "</ul>"
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

# Build RSS (latest 50 items)
now = dt.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
rss = ['<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel>',
       '<title>Ops Kits</title>',
       '<link>'+ (SITE_BASE or './') +'</link>',
       f'<lastBuildDate>{now}</lastBuildDate>']
for x in items[:50]:
    rss.append(f'<item><title>{x["title"]}</title><link>{x["url"]}</link></item>')
rss.append("</channel></rss>")
with open("docs/feed.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(rss))

# Copy static embed dir into docs
import shutil
if os.path.isdir("embed"):
    dst = "docs/embed"
    if os.path.isdir(dst): shutil.rmtree(dst)
    shutil.copytree("embed", dst)

print(f"Built {len(items)} pages → docs/")
