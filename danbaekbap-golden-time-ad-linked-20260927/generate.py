#!/usr/bin/env python3
"""광고 연결형 수정 시안 4종 × 3장. 원본 gen.py는 수정하지 않는다."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

HEAD = '''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=860,initial-scale=1">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap" rel="stylesheet">
<style>
:root{--red:#e60000;--yellow:#fdc916;--ink:#101010;--cream:#f7f1e5}
*{box-sizing:border-box}html,body{width:860px;height:1600px;margin:0;overflow:hidden}
body{font-family:Pretendard,'Apple SD Gothic Neo',sans-serif;letter-spacing:-.035em;word-break:keep-all;background:#111;color:#fff}
.bh{font-family:Pretendard,'Apple SD Gothic Neo',sans-serif;font-weight:900;letter-spacing:-.065em}
.abs{position:absolute}.star{color:#ffbd00}.small{font-size:23px;line-height:1.35}.shadow{filter:drop-shadow(0 25px 32px rgba(0,0,0,.38))}
</style></head><body>'''

def page(body): return HEAD + body + '</body></html>'

def product(top=855,left=92,width=676,side=False):
    name='orig_side.png' if side else 'orig.png'
    return f'<img class="abs shadow" src="assets/{name}" alt="단백밥 오리지널 L" style="top:{top}px;left:{left}px;width:{width}px">'

def bg_feast(bright=.47):
    return f'<img class="abs" src="assets/feast.jpg" alt="명절 음식" style="inset:0;width:860px;height:1250px;object-fit:cover;object-position:center 25%;filter:brightness({bright})"><div class="abs" style="inset:0;background:linear-gradient(180deg,transparent 25%,#0b0b0b 81%)"></div>'

def stats(color='#fdc916'):
    return f'<div style="display:flex;gap:18px"><div style="flex:1;border:2px solid {color};border-radius:26px;padding:25px;text-align:center"><div class="small">단백질</div><b style="font-size:64px">50g</b></div><div style="flex:1;border:2px solid {color};border-radius:26px;padding:25px;text-align:center"><div class="small">당류</div><b style="font-size:64px">1g</b></div><div style="flex:1;border:2px solid {color};border-radius:26px;padding:25px;text-align:center"><div class="small">중량</div><b style="font-size:64px">420g</b></div></div>'

def proof_card(style='white'):
    bg,fg,muted=('#fff','#111','#555') if style=='white' else ('#1b1b1b','#fff','#aaa')
    return f'''<div style="background:{bg};color:{fg};border-radius:36px;padding:45px 42px;box-shadow:0 22px 55px #0004">
      <div style="font-size:29px;font-weight:900;color:var(--red)">실구매 고객이 남긴 평가</div>
      <div style="display:flex;align-items:end;justify-content:space-between;margin-top:10px">
        <div><div style="font-size:25px;color:{muted};font-weight:700">구매평</div><div style="font-size:91px;line-height:1.08;font-weight:900">19,580<span style="font-size:38px">개</span></div></div>
        <div style="text-align:right"><div style="font-size:25px;color:{muted};font-weight:700">평점</div><div style="font-size:84px;line-height:1.08;font-weight:900"><span class="star">★</span>4.9</div></div>
      </div></div>'''

def price_card(style='white'):
    bg,fg=('#fff','#111') if style=='white' else ('#151515','#fff')
    return f'''<div style="background:{bg};color:{fg};border-radius:36px;padding:48px 42px;box-shadow:0 22px 55px #0003">
      <div style="font-size:31px;font-weight:900;color:var(--red)">광고에서 본 그 가격</div>
      <div style="font-size:29px;color:#888;text-decoration:line-through;margin-top:20px">정가 6,290원</div>
      <div class="bh" style="font-size:160px;line-height:1.04;white-space:nowrap">5,190<span style="font-size:75px">원</span></div>
      <div style="font-size:27px;font-weight:750;margin-top:7px">오리지널 L 1팩 기준</div></div>'''

def common2_header(tone):
    return f'<div style="font-size:29px;font-weight:900;color:{tone}">급찐급빠 골든타임 · 다음 한 끼</div><div class="bh" style="font-size:99px;line-height:1.1;margin-top:25px">완벽한 한 끼로<br><span style="color:var(--red)">바꿔보세요</span></div>'

pages={}

# 01: 원본 광고의 어두운 명절 사진과 붉은 띠를 살린 정석형.
pages['01_정석형_1'] = page(f'''{bg_feast(.47)}
<div class="abs" style="top:76px;left:50px;right:50px;text-align:center">
 <div style="font-size:39px;font-weight:900;background:var(--red);border-radius:100px;padding:18px">🚨 지금은 식단을 다시 시작할 때</div>
 <div class="bh" style="font-size:114px;line-height:1.08;color:var(--yellow);margin-top:40px">급찐급빠<br>골든타임</div>
 <div class="bh" style="font-size:83px;line-height:1.15;margin-top:54px">명절 끝났다<br>식단은 오늘부터</div>
 <div style="font-size:30px;font-weight:700;margin-top:25px">기름진 연휴 다음 한 끼, 단백밥으로</div></div>
{product(910)}
<div class="abs" style="top:1120px;left:34px;background:var(--yellow);color:#111;border-radius:90px;padding:24px;font-size:31px;font-weight:900">단백질 50g</div>
<div class="abs" style="top:1120px;right:34px;background:var(--yellow);color:#111;border-radius:90px;padding:24px;font-size:31px;font-weight:900">당류 1g</div>
<div class="abs" style="bottom:0;left:0;right:0;height:160px;background:var(--red);display:grid;place-items:center;text-align:center;font-size:44px;font-weight:900">광고에서 보신 단백밥, 여기 맞습니다</div>''')

pages['01_정석형_2'] = page(f'''<div class="abs" style="inset:0;background:#111"></div>
<div class="abs" style="top:100px;left:65px;right:65px">{common2_header('var(--yellow)')}
<div style="font-size:32px;line-height:1.45;font-weight:650;color:#ddd;margin-top:36px">명절 뒤 식단, 한 팩으로 든든하게 시작하세요.</div></div>
<div class="abs" style="top:580px;left:65px;right:65px">{stats()}</div>
{product(790,110,640)}
<div class="abs" style="bottom:0;left:0;right:0;background:var(--red);padding:40px 65px 50px;font-size:34px;line-height:1.35;font-weight:850">밥·닭가슴살·채소를 한 팩에.<br>오늘의 다음 한 끼부터 시작해요.</div>
<div class="abs" style="bottom:178px;left:65px;font-size:19px;color:#aaa">*오리지널 L 영양성분표 기준: 단백질 50.1g · 당류 0.8g · 총중량 420g</div>''')

pages['01_정석형_3'] = page(f'''<div class="abs" style="inset:0;background:#111"></div><div class="abs" style="inset:0 0 auto;height:355px;background:var(--red)"></div>
<div class="abs" style="top:68px;left:55px;right:55px;text-align:center"><div class="bh" style="font-size:89px">골든타임의 한 끼</div><div style="font-size:35px;font-weight:800;margin-top:16px">가격과 구매평을 한눈에</div></div>
<div class="abs" style="top:335px;left:50px;right:50px">{price_card()}
<div style="height:34px"></div>{proof_card()}</div>
<div class="abs" style="bottom:85px;left:70px;right:70px;text-align:center;font-size:30px;font-weight:750;line-height:1.4">명절 뒤 첫 식단, 부담 없이 맛있게.<br><span style="color:var(--yellow)">오리지널 L부터 시작해보세요.</span></div>
<div class="abs" style="bottom:17px;left:25px;right:25px;text-align:center;font-size:18px;color:#aaa">*표시 가격·평점·구매평은 제작 시점 상품 페이지 기준 · 구성에 따라 판매가 상이</div>''')

# 02: 전광판처럼 시간을 알리는 긴급형.
pages['02_긴급형_1'] = page(f'''<div class="abs" style="inset:0;background:#111"></div>
<div class="abs" style="top:0;left:0;right:0;height:535px;background:var(--yellow);color:#111;padding:75px 58px 25px">
 <div style="font-size:40px;font-weight:900">명절 과식, 다음 한 끼가 중요합니다</div>
 <div class="bh" style="font-size:130px;line-height:1.03;margin-top:38px">급찐급빠<br>골든타임</div></div>
<div class="abs" style="top:600px;left:58px;right:58px"><div class="bh" style="font-size:82px;line-height:1.15">명절은 끝.<br><span style="color:var(--yellow)">식단은 오늘부터.</span></div></div>
<img class="abs" src="assets/feast.jpg" alt="명절 음식" style="top:835px;left:0;width:860px;height:575px;object-fit:cover;filter:brightness(.35)">
{product(880,120,620)}
<div class="abs" style="bottom:0;left:0;right:0;background:var(--red);padding:42px 60px;text-align:center;font-size:42px;font-weight:900">다음 한 끼는 단백밥으로</div>''')

pages['02_긴급형_2'] = page(f'''<div class="abs" style="inset:0;background:var(--yellow);color:#111"></div>
<div class="abs" style="top:70px;left:55px;right:55px;color:#111">{common2_header('#111')}</div>
<div class="abs" style="top:495px;left:55px;right:55px;background:#111;color:#fff;border-radius:35px;padding:45px 45px 42px">
 <div style="font-size:32px;font-weight:800">한 팩으로 채우는 식단</div><div style="font-size:28px;color:#ccc;margin-top:15px">밥 · 닭가슴살 · 채소를 한 팩에</div>
 <div style="font-size:59px;font-weight:900;margin-top:35px;line-height:1.35">단백질 <span style="color:var(--yellow)">50g</span><br>당류 <span style="color:var(--yellow)">1g</span><br>총중량 <span style="color:var(--yellow)">420g</span></div></div>
{product(1000,70,720,True)}
<div class="abs" style="bottom:34px;left:55px;right:55px;text-align:center;font-size:19px;color:#555">*오리지널 L 기준: 단백질 50.1g · 당류 0.8g</div>''')

pages['02_긴급형_3'] = page(f'''<div class="abs" style="inset:0;background:var(--yellow);color:#111"></div>
<div class="abs" style="top:65px;left:55px;right:55px;color:#111"><div class="bh" style="font-size:90px;line-height:1.15">고르기 전에<br>이 숫자부터</div></div>
<div class="abs" style="top:365px;left:48px;right:48px">{price_card('dark')}<div style="height:30px"></div>{proof_card('dark')}</div>
<div class="abs" style="bottom:70px;left:54px;right:54px;color:#111;border-top:5px solid #111;padding-top:35px;font-size:29px;font-weight:850;line-height:1.4">광고에서 본 가격, 실제 구매평까지.<br>이제 오늘의 한 끼를 바꿔보세요.</div>
<div class="abs" style="bottom:16px;left:20px;right:20px;text-align:center;font-size:18px;color:#555">*오리지널 L 1팩 기준 · 제작 시점 상품 페이지 표시값</div>''')

# 03: 명절 음식과 다음 끼니를 나누어 보여주는 대비형.
pages['03_대비형_1'] = page(f'''<div class="abs" style="inset:0;background:var(--cream);color:#111"></div>
<div class="abs" style="top:0;left:0;right:0;height:610px;background:#111;overflow:hidden"><img src="assets/feast.jpg" alt="명절 음식" style="width:100%;height:100%;object-fit:cover;filter:brightness(.39)"></div>
<div class="abs" style="top:75px;left:60px;right:60px;text-align:center"><div style="font-size:36px;font-weight:900;color:#fff">명절 과식 뒤</div><div class="bh" style="font-size:115px;line-height:1.06;color:var(--yellow);margin-top:28px">급찐급빠<br>골든타임</div></div>
<div class="abs" style="top:670px;left:57px;right:57px;color:#111"><div class="bh" style="font-size:76px;line-height:1.12">명절은 지나갔고<br><span style="color:var(--red)">식단은 오늘부터.</span></div><div style="font-size:31px;font-weight:720;margin-top:26px">다음 한 끼를 바꾸는 가장 쉬운 시작</div></div>
{product(1060,145,570,True)}
<div class="abs" style="bottom:38px;left:70px;right:70px;color:#111;border-top:4px solid var(--red);padding-top:22px;text-align:center;font-size:34px;font-weight:900">단백밥 오리지널 L</div>''')

pages['03_대비형_2'] = page(f'''<div class="abs" style="inset:0;background:var(--cream);color:#111"></div>
<div class="abs" style="top:85px;left:55px;right:55px;color:#111">{common2_header('var(--red)')}</div>
<div class="abs" style="top:475px;left:55px;right:55px;color:#111;font-size:32px;font-weight:700;line-height:1.45">명절 다음 끼니를 준비하는 방법.<br>한 팩에 필요한 것을 채웠습니다.</div>
{product(690,128,604)}
<div class="abs" style="bottom:80px;left:55px;right:55px;background:#111;color:#fff;border-radius:30px;padding:34px">{stats('var(--yellow)')}</div>
<div class="abs" style="bottom:21px;left:55px;right:55px;text-align:center;font-size:18px;color:#666">*오리지널 L 기준: 단백질 50.1g · 당류 0.8g · 총중량 420g</div>''')

pages['03_대비형_3'] = page(f'''<div class="abs" style="inset:0;background:var(--cream);color:#111"></div>
<div class="abs" style="top:70px;left:55px;right:55px;color:#111"><div style="font-size:30px;font-weight:900;color:var(--red)">연휴 후 첫 식단의 선택</div><div class="bh" style="font-size:87px;margin-top:20px">가격도, 평가도<br>확인하고 시작</div></div>
<div class="abs" style="top:430px;left:50px;right:50px">{proof_card()}<div style="height:34px"></div>{price_card()}</div>
<div class="abs" style="bottom:67px;left:65px;right:65px;color:#111;text-align:center;font-size:30px;font-weight:800">다음 한 끼는 <span style="color:var(--red)">단백밥</span>으로.</div>
<div class="abs" style="bottom:18px;left:20px;right:20px;text-align:center;font-size:18px;color:#777">*오리지널 L 1팩 기준 · 제작 시점 상품 페이지 표시값</div>''')

# 04: 제품과 구매평을 먼저 보여주는 신뢰형.
pages['04_신뢰형_1'] = page(f'''<div class="abs" style="inset:0;background:#101010"></div>
<div class="abs" style="top:0;left:0;right:0;height:280px;background:var(--red)"></div>
<div class="abs" style="top:60px;left:55px;right:55px;text-align:center"><div class="bh" style="font-size:104px;line-height:1.05">급찐급빠<br>골든타임</div></div>
<div class="abs" style="top:360px;left:55px;right:55px;text-align:center"><div class="bh" style="font-size:75px;line-height:1.16">명절 끝,<br><span style="color:var(--yellow)">식단은 오늘부터</span></div><div style="font-size:29px;font-weight:700;margin-top:24px">명절 뒤 첫 식단, 한 끼부터 다시.</div></div>
{product(760,68,724)}
<div class="abs" style="bottom:0;left:0;right:0;background:var(--yellow);color:#111;padding:48px 35px 50px;text-align:center;font-size:37px;font-weight:900">단백질 50g · 당류 1g · 총중량 420g</div>
<div class="abs" style="bottom:179px;left:44px;right:44px;text-align:center;font-size:19px;color:#bbb">*오리지널 L 영양성분표 기준: 단백질 50.1g · 당류 0.8g</div>''')

pages['04_신뢰형_2'] = page(f'''<div class="abs" style="inset:0;background:#161616"></div>
<div class="abs" style="top:0;left:0;right:0;height:470px;background:var(--red)"></div>
<div class="abs" style="top:74px;left:55px;right:55px">{common2_header('#fff')}</div>
<div class="abs" style="top:570px;left:55px;right:55px"><div style="font-size:34px;font-weight:850;line-height:1.5">한 끼를 바꾸면, 식단의 시작이 쉬워집니다.</div>
 <div style="margin-top:44px;display:flex;flex-direction:column;gap:22px">
 <div style="background:#242424;border-radius:28px;padding:33px 38px;font-size:39px;font-weight:900"><span style="color:var(--yellow)">50g</span> 단백질</div>
 <div style="background:#242424;border-radius:28px;padding:33px 38px;font-size:39px;font-weight:900"><span style="color:var(--yellow)">1g</span> 당류</div>
 <div style="background:#242424;border-radius:28px;padding:33px 38px;font-size:39px;font-weight:900"><span style="color:var(--yellow)">420g</span> 든든한 한 팩</div></div></div>
{product(1130,225,410)}
<div class="abs" style="bottom:25px;left:40px;right:40px;text-align:center;font-size:19px;color:#aaa">*오리지널 L 기준: 단백질 50.1g · 당류 0.8g · 총중량 420g</div>''')

pages['04_신뢰형_3'] = page(f'''<div class="abs" style="inset:0;background:#111"></div>
<div class="abs" style="top:0;left:0;right:0;height:360px;background:var(--red)"></div>
<div class="abs" style="top:65px;left:58px;right:58px;text-align:center"><div class="bh" style="font-size:90px;line-height:1.14">오늘 한 끼,<br>확신하고 선택</div></div>
<div class="abs" style="top:350px;left:50px;right:50px">{proof_card()}<div style="height:36px"></div>{price_card()}</div>
<div class="abs" style="bottom:68px;left:65px;right:65px;text-align:center;color:var(--yellow);font-size:33px;font-weight:900">실구매 평가를 보고, 가볍게 시작하세요.</div>
<div class="abs" style="bottom:17px;left:20px;right:20px;text-align:center;font-size:18px;color:#aaa">*오리지널 L 1팩 기준 · 제작 시점 상품 페이지 표시값</div>''')

if __name__=='__main__':
    for name, html in pages.items():
        (ROOT/(name+'.html')).write_text(html,encoding='utf-8')
    print(f'{len(pages)} HTML pages generated')
