"""Run python test_site.py; no network or external submissions."""
from pathlib import Path
from html.parser import HTMLParser
import xml.etree.ElementTree as ET
s=(Path(__file__).parent/'index.html').read_text()
p=HTMLParser();p.feed(s)
assert s.count('<img ')==5
assert 'musubi-restored-20261023-02' in s
assert 'submitForm' not in s and '送信完了' not in s
for v in ['22,000','40,000','76,000','108,000','https://lin.ee/YBFB84u','047-701-5789','070-9158-1164','ocean_office2010@icloud.com']:
    assert v in s,v
assert 'メールアプリから送信' in s
assert 'rel="canonical"' in s
ET.parse(Path(__file__).parent/'sitemap.xml')
print('PASS: restored images, prices, contacts, honest contact flow, canonical and sitemap syntax.')
