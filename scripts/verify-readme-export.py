"""Read-only checks before publishing the profile and its PDF."""
from pathlib import Path
import re
from bs4 import BeautifulSoup
from pypdf import PdfReader

root=Path(__file__).resolve().parents[1]
source=(root/'README.md').read_text(encoding='utf-8')
for image in BeautifulSoup(source,'html.parser').find_all('img'):
    src=image.get('src','')
    if src.startswith('assets/'):
        assert (root/src).is_file(),src
reader=PdfReader(root/'output/pdf/github-profile-readme-20260928.pdf')
assert len(reader.pages)==13
for project_index in range(1,10):
    text=reader.pages[project_index].extract_text()
    assert re.search(rf'\b{project_index}\. ',text),project_index
assert 'RiskTwin' in reader.pages[7].extract_text()
assert 'Reqover' in reader.pages[8].extract_text()
assert 'TUG GUARD' in reader.pages[9].extract_text()
assert 'Credentials & Activities' in reader.pages[12].extract_text()
for filename in ['README.md','docs/2026-09-28-readme-update.md','docs/portfolio-image-sources.md']:
    text=(root/filename).read_text(encoding='utf-8')
    assert not re.search(r'gh[pousr]_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9]{24,}|-----BEGIN .*PRIVATE KEY-----|AKIA[A-Z0-9]{16}',text),filename
print('PASS: local image paths, 13 pages, nine project boundaries, credentials, credential-pattern scan')
