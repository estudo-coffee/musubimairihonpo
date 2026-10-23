"""Run python test_site.py before publishing; no external requests or submissions."""
from html.parser import HTMLParser
from pathlib import Path
import json, re, xml.etree.ElementTree as ET
root = Path(__file__).parent
source = (root / 'index.html').read_text()
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.links=[]; self.h1=0
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag == 'a': self.links.append(attrs.get('href',''))
        if tag == 'h1': self.h1 += 1
page=Page(); page.feed(source)
assert page.h1 == 1
assert len(page.ids)==len(set(page.ids))
assert all(link for link in page.links)
assert all(link[1:] in page.ids for link in page.links if link.startswith('#'))
for value in ['22,000','40,000','76,000','108,000','https://lin.ee/YBFB84u','047-701-5789','070-9158-1164','ocean_office2010@icloud.com']:
    assert value in source, value
assert 'submitForm' not in source and '送信完了' not in source
assert 'href="#"' not in source
assert 'prefers-reduced-motion' in source
assert 'name="viewport"' in source
assert 'rel="canonical" href="https://musubimairihonpo.com/"' in source
schema=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',source,re.S)[1])
assert schema['url']=='https://musubimairihonpo.com/'
assert 'aggregateRating' not in schema
ET.parse(root/'sitemap.xml')
assert 'https://musubimairihonpo.com/sitemap.xml' in (root/'robots.txt').read_text()
print('PASS: semantics, anchors, actual prices and destinations, no fake submission, accessibility hooks, SEO and XML/JSON syntax.')
