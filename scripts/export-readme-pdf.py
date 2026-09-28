"""Export the actual README, expanding details and preserving links and image ratios."""
from pathlib import Path
import re
from html import escape
from urllib.request import urlopen, Request
from urllib.parse import unquote
import markdown
from bs4 import BeautifulSoup, NavigableString
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, HRFlowable, KeepTogether, PageBreak
from svglib.svglib import svg2rlg
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'output/pdf/github-profile-readme-20260928.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
CACHE = ROOT/'tmp/pdf-assets'
CACHE.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('K', 'C:/Windows/Fonts/malgun.ttf'))
pdfmetrics.registerFont(TTFont('KB', 'C:/Windows/Fonts/malgunbd.ttf'))
pdfmetrics.registerFontFamily('K', normal='K', bold='KB', italic='K', boldItalic='KB')
styles = {
 'p': ParagraphStyle('p',fontName='K',fontSize=9,leading=14,spaceAfter=7,wordWrap='CJK'),
 'h1': ParagraphStyle('h1',fontName='KB',fontSize=21,leading=29,spaceBefore=12,spaceAfter=13,keepWithNext=True),
 'h2': ParagraphStyle('h2',fontName='KB',fontSize=14,leading=21,spaceBefore=14,spaceAfter=10,keepWithNext=True),
 'h3': ParagraphStyle('h3',fontName='KB',fontSize=11,leading=17,spaceBefore=10,spaceAfter=8,keepWithNext=True),
 'small': ParagraphStyle('small',fontName='K',fontSize=7.5,leading=11,spaceAfter=5,wordWrap='CJK',textColor=colors.HexColor('#57606a')),
}
def clean(s):
 return re.sub('[\U0001F000-\U0001FAFF\u2600-\u27BF\ufe0f]', '', s).replace('−','-')
def badge(n):
 src=n.get('src','')
 if '/badge/' in src:
  s=unquote(src.split('/badge/')[1].split('?')[0]).replace('--','\0')
  parts=s.split('-')
  return ' · '.join(parts[:-1]).replace('\0','-')
 return n.get('alt','')
def inline(n):
 if isinstance(n,NavigableString): return escape(clean(str(n)))
 if n.name=='img': return escape(clean(badge(n)))+'  '
 content=''.join(inline(c) for c in n.children)
 if n.name in ('strong','b'): return '<b>'+content+'</b>'
 if n.name=='br': return '<br/>'
 if n.name=='a': return '<a color="#0969da" href="'+escape(n.get('href',''),quote=True)+'">'+content+'</a>'
 return content

source=(ROOT/'README.md').read_text(encoding='utf-8')
source=re.sub(r'</?(?:div|details)[^>]*>','',source)
source=re.sub(r'<summary>(.*?)</summary>',r'\n### \1\n',source,flags=re.S)
soup=BeautifulSoup(markdown.markdown(source,extensions=['tables']), 'html.parser')
flow=[]
image_count=0
def paragraph(n,style='p',prefix=''):
 t=inline(n).strip()
 if t: flow.append(Paragraph(prefix+t,styles[style]))
def image_group(nodes):
 global image_count
 nodes=[n for n in nodes if 'img.shields.io' not in n.get('src','')]
 if not nodes:return
 width=491/len(nodes)-8
 cells=[]
 for n in nodes:
  src=n['src']
  if src.startswith('https://'):
   path=CACHE/(src.rstrip('/').rsplit('/',1)[-1]+'.png')
   if not path.exists():
    path.write_bytes(urlopen(Request(src,headers={'User-Agent':'README-PDF'}),timeout=30).read())
  else:path=ROOT/src
  if not path.exists(): raise FileNotFoundError(path)
  if path.suffix=='.svg':
   im=svg2rlg(str(path))
   factor=min(width/im.width,195/im.height)
   im.scale(factor,factor);im.width*=factor;im.height*=factor
  else:
   im=Image(str(path))
   max_height=195
   if path.name.startswith('ant-'):max_height=300
   elif path.name=='tugguard-live.png':max_height=265
   elif path.name=='reqover-request-report.png':max_height=250
   elif path.name=='reqover-code-index.png':max_height=225
   factor=min(width/im.imageWidth,max_height/im.imageHeight)
   im.drawWidth=im.imageWidth*factor; im.drawHeight=im.imageHeight*factor
  cells.append(im);image_count+=1
 t=Table([cells],colWidths=[491/len(nodes)]*len(nodes))
 t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
 flow.append(t)
for n in soup.children:
 if isinstance(n,NavigableString):continue
 if n.name in ('h1','h2','h3'):
  heading=clean(n.get_text()).strip()
  # Print-only pagination. Do not insert page-break markup in the GitHub README.
  if heading=='Projects':
   continue
  if re.match(r'\d+\.',heading) or heading.startswith('More Products') or heading in ('기록하고 검증하는 방식','Credentials & Activities'):
   flow.append(PageBreak())
  paragraph(n,n.name)
 elif n.name=='hr': flow.extend([Spacer(1,5),HRFlowable(width='100%',color=colors.HexColor('#d0d7de'),thickness=.5),Spacer(1,5)])
 elif n.name in ('ul','ol'):
  for li in n.find_all('li',recursive=False):paragraph(li,prefix='• ')
 elif n.name=='table':
  rows=[[Paragraph(inline(c),styles['small']) for c in tr.find_all(['th','td'])] for tr in n.find_all('tr')]
  cols=len(rows[0]); widths=([120,210,161] if cols==3 else [491/cols]*cols)
  t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
  t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#f6f8fa')),('LINEBELOW',(0,0),(-1,-1),.4,colors.HexColor('#d0d7de')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
  flow.extend([t,Spacer(1,9)])
 else:
  imgs=n.find_all('img')
  if any('img.shields.io' not in x.get('src','') for x in imgs):image_group(imgs)
  else:paragraph(n,'small' if imgs or n.name=='sub' else 'p')
# Keep each project heading, screenshots and explanation together when they fit.
grouped=[]
pending=[]
for item in flow:
 if isinstance(item,PageBreak):
  if pending:grouped.append(KeepTogether(pending));pending=[]
  grouped.append(item)
 elif isinstance(item,Paragraph) and item.style.name=='h2' and re.match(r'\d+\.',item.getPlainText()):
  if pending: grouped.append(KeepTogether(pending)); pending=[]
  pending=[item]
 elif pending and isinstance(item,HRFlowable):
  grouped.append(KeepTogether(pending));pending=[];grouped.append(item)
 elif pending:pending.append(item)
 else:grouped.append(item)
if pending:grouped.append(KeepTogether(pending))
def page(c,d):
 c.setFont('K',7);c.setFillColor(colors.HexColor('#57606a'))
 c.drawString(52,815,'TaeHuiKKIM / README · 2026-09-28')
 c.drawRightString(543,26,str(d.page))
doc=SimpleDocTemplate(str(OUT),pagesize=(595.28,841.89),leftMargin=52,rightMargin=52,topMargin=48,bottomMargin=45,title='김태희 GitHub README',author='김태희')
doc.build(grouped,onFirstPage=page,onLaterPages=page)
print({'output':str(OUT),'images':image_count,'bytes':OUT.stat().st_size})
