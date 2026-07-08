<div align="center">

# 김태희 · TaeHui Kim

### 문제를 발견하면 배워서 직접 만들고, 만든 것을 데이터로 다시 개선하는 개발자

경북대학교 글로벌소프트웨어융합전공 · 카카오테크캠퍼스 4기<br/>
웹 풀스택을 기반으로 **투자·금융 도메인**과 **핀테크·수익형 서비스**를 지향합니다.

<br/>

![GPA](https://img.shields.io/badge/GPA-4.18%20/%204.3-1f6feb?style=for-the-badge)
![TOEIC](https://img.shields.io/badge/TOEIC-925-0a7d33?style=for-the-badge)
![ADsP](https://img.shields.io/badge/ADsP-취득-5319e7?style=for-the-badge)
![SQLD](https://img.shields.io/badge/SQLD-취득-5319e7?style=for-the-badge)

[![Velog](https://img.shields.io/badge/Velog-20C997?style=for-the-badge&logo=velog&logoColor=white)](https://velog.io/@kt_gml/posts)
[![Solved.ac](https://img.shields.io/badge/Solved.ac-1043tae-00C73C?style=for-the-badge)](https://solved.ac/1043tae/)
[![Email](https://img.shields.io/badge/tae1043@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tae1043@gmail.com)

</div>

---

## 🧭 나의 개발 여정

> "동작하지 않는 웹사이트"를 보고 시작해, 스스로 배워 만들고, 만든 것을 **숫자로 다시 개선**하는 과정을 반복해 왔습니다.

**① 시작 — 문제를 보고 뛰어들다.**
Adobe Flash로 만들어져 제대로 동작하지 않던 한 병원 웹사이트를 보고, 직접 고칠 수 있겠다는 생각에 **HTML·CSS·JS를 독학**했습니다. 그리고 먼저 연락을 드려 웹사이트의 **총책임자**를 맡게 되었습니다.

**② 성장 — 기획부터 배포까지 혼자.**
기획, 디자인, 정보 수집, 개발, 그리고 실제 **배포·운영**까지 전 과정을 직접 해냈습니다. 어렵고 오래 걸렸지만 제품의 전체 흐름을 몸으로 익혔고, 이 사이트([membersclinic.com](https://membersclinic.com))를 **수년째 총책임자로 유지보수**하고 있습니다.

**③ 확장 — 백엔드의 원리를 직접.**
프론트를 넘어 서버로 넓히기 위해 **JSP·Servlet·MySQL**로 쇼핑몰(MERCI)을 만들었습니다. 프레임워크가 대신 해 주던 **트랜잭션·커넥션 풀·세션·결제·인증**을 직접 구현하며 백엔드 동작 원리를 체득했고, 이 프로젝트로 **최우수 평가를 받아 장학금**을 받았습니다.

**④ 회귀 — 배운 것을 데이터로 증명.**
백엔드와 모던 웹에서 배운 것을 수년간 운영하던 Members에 되돌려 적용했습니다. Lighthouse로 **모바일 성능 문제(LCP 8.8s · 전송 8.3MB)를 실측으로 인지**하고, 이를 해결하고자 **Next.js 16 + Spring Boot 4**로 재구축, `next/image`·서버 컴포넌트·다국어 라우팅을 도입했습니다. 그 결과 **전송 용량을 약 75% 줄이고 SEO를 만점(92→100)**으로 끌어올렸으며, 남은 첫 렌더 지연은 트레이드오프로 인지해 계속 최적화 중입니다. *(측정 근거는 아래 표)*

**⑤ 현재 — 창업과 금융으로.**
지금은 **창업에 도전**하며 게임을 개발하고 **수익형 서비스 창출**을 목표로 나아가고 있고, 개인 웹 개발 공부도 병행합니다. **투자·금융 분야에 관심**이 많아 ADsP·SQLD를 취득했고 **모의투자대회·실전투자대회**에 참가하며 **금융권**을 목표로 준비하고 있습니다.

---

## 🚀 Projects

### 1. Members Clinic — Next.js 16 + Spring Boot 4 풀스택 <sub>(총책임자 · 수년째 운영)</sub>

<img src="assets/portfolio/members-home.png" alt="Members Clinic" width="560"/>

순수 HTML/CSS/JS로 시작해 **풀스택으로 재구축**한, 실제 운영 중인 병원 웹사이트입니다.

- **백엔드 (Spring Boot 4.0.6 / Java 23)** — `config·controller·domain·repository` 계층 분리, `Auth/Reservation/Question/Admin` 컨트롤러, `AdminInterceptor` 인증, Spring Data JPA + Bean Validation, 로컬 H2 · 운영 MySQL 이중 프로파일.
- **프론트엔드 (Next.js 16 · React 19 · TypeScript · Tailwind 4)** — App Router 서버 컴포넌트, `next-intl` **4개 언어(한/영/일/중)**, 설정 파일 하나로 병원 정보를 교체하는 템플릿 구조, `MedicalClinic` 구조화 데이터 + SEO.

<p>
<img src="https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/React%2019-61DAFB?style=flat-square&logo=react&logoColor=black"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
<img src="https://img.shields.io/badge/Spring%20Boot%204-6DB33F?style=flat-square&logo=springboot&logoColor=white"/>
<img src="https://img.shields.io/badge/JPA-59666C?style=flat-square&logo=hibernate&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/>
</p>

[![Live](https://img.shields.io/badge/▶%20Live-membersclinic.com-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://membersclinic.com)

---

### 2. MERCI — JSP · Servlet · MySQL 커머스 <sub>(백엔드 · 🎓 최우수 평가 → 장학금)</sub>

프레임워크 없이 서버 사이드 웹의 기본기를 직접 구현한 의류 쇼핑몰. **이 프로젝트로 최우수 평가를 받아 장학금을 받았습니다.**

<img src="assets/portfolio/merci-main.png" alt="MERCI 메인" width="560"/>
<p>
<img src="assets/portfolio/merci-detail.png" alt="상품 상세" width="272"/>
<img src="assets/portfolio/merci-cart.png" alt="장바구니/주문" width="272"/>
</p>

- **주문·결제 트랜잭션** — `setAutoCommit(false)`로 주문 생성 → 항목 삽입 → 재고 차감을 하나의 트랜잭션으로 묶고 예외 시 `rollback()`. 재고 차감은 `WHERE stock >= ?`로 **초과 판매를 원천 차단**.
- **PG 결제(PortOne V2)** — 카카오페이/일반결제 채널 분기, 결제 콜백 서버 검증.
- **카카오 OAuth2** — SDK 없이 Authorization Code 흐름(토큰 교환 → 사용자 조회 → 신규 가입)을 직접 구현.
- **커넥션 풀·계층 구조** — Apache Commons DBCP를 `load-on-startup` 서블릿으로 초기화, `DAO·Model·Util` 3계층 분리, DAO가 `Connection`을 주입받아 컨트롤러에서 트랜잭션 제어.
- **관리자** — 상품 CRUD(이미지 업로드), 주문 상태·송장 관리, 일자별 매출 집계, 페이지네이션 Q&A, 비동기 찜/장바구니(AJAX).
- **규모(실측)** — DAO 9 · 모델 10 · JSP 56 · `_proc` 컨트롤러 22 · Java 2,127 LOC. 로컬 Tomcat + MySQL 구동 검증(홈 **HTTP 200**).

<p>
<img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white"/>
<img src="https://img.shields.io/badge/JSP%20%2F%20Servlet-E76F00?style=flat-square&logo=apachetomcat&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL%208.0-4479A1?style=flat-square&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/Commons%20DBCP-D22128?style=flat-square&logo=apache&logoColor=white"/>
<img src="https://img.shields.io/badge/PortOne%20PG-5C6AC4?style=flat-square"/>
<img src="https://img.shields.io/badge/Kakao%20OAuth-FFCD00?style=flat-square&logo=kakao&logoColor=black"/>
</p>

---

### 3. MediCPX — FastAPI · Supabase · Gemini AI 표준화환자 <sub>(🏆 CODE-MEDI 해커톤 최우수상)</sub>

<img src="assets/portfolio/cpx-final-home.png" alt="MediCPX 대시보드" width="560"/>
<p>
<img src="assets/portfolio/cpx-final-room.png" alt="문진 화면" width="272"/>
<img src="assets/portfolio/cpx-final-report.png" alt="채점 리포트" width="272"/>
</p>

의대생 CPX 실기 연습용 AI 표준화환자 플랫폼.

- **실시간 대화** — FastAPI + WebSocket으로 음성/텍스트 문진 스트리밍, Web Speech API 연동. 올바르게 질문해야만 정보를 공개하는 상태 설계.
- **자동 채점** — **40개 항목** Yes/No(항목당 2.5점), 실제 시험과 동일한 **12분(720초)** 제한과 진찰 유형별 즉시 차감, 근거 기반 피드백 리포트.
- **인프라** — Supabase(PostgreSQL·Auth·RLS), Gemini 2.5 Flash Lite Structured Output, 단일 Dockerfile로 Cloudtype 배포.

<p>
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socketdotio&logoColor=white"/>
<img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white"/>
<img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
</p>

---

### 4. 개미 투자자 키우기 (Ant Investor Idle) — 토스·Google Play 배포형 주식 시뮬레이션 <sub>(창업 · 수익형 서비스 도전)</sub>

<p><img src="assets/portfolio/ant-share-banner.png" alt="개미 투자자 키우기 대표 키비주얼" width="560"/></p>

투자·금융 관심과 창업 목표를 담아 **토스 미니앱과 Google Play 웹앱 배포**를 겨냥해 만든 PWA 게임입니다.

- **실전/모의투자 경험 기반 기획** — 실전투자와 모의투자대회 순위권 경험을 바탕으로, 한국 개인투자자들이 급등주, 물타기, 익절/손절 타이밍, 숏스퀴즈성 급등, 뉴스에 흔들리는 심리에서 강한 재미를 느낀다는 점에 주목했습니다.
- **차트 엔진 직접 설계** — GBM 랜덤워크 기반 **10종** 종목 시세에 뉴스 충격, 추세 지속/반전, 개미털기 후 되돌림, 바이오 테마 점프 이벤트, 섹터 동조 이벤트를 결합했습니다. 숏스퀴즈, 차익실현, 루머 적중/실패가 차트에 남기는 움직임을 게임 알고리즘으로 해석했고, 정보력은 51~60% 신뢰도의 찌라시로 제한해 무위험 복리 전략이 수렴하지 않게 설계했습니다.
- **성장 루프** — 개미 **10티어** 진화 도감, **20종** 업적, 환생(프레스티지), **5시간·진행 자산 55% 이중 캡** 휴식 보상, 일일 출석.
- **수익 다변화** — 애널리스트 자동매매, 배당, 예금 복리, 부동산 임대, 장중 단타 미니게임.
- **최적화와 안정성** — 빌드리스 Vanilla JS + ES 모듈로 초기 실행을 가볍게 유지하고, 캔들 차트는 SVG 노드 재사용 방식으로 갱신해 모바일 웹뷰에서 불필요한 DOM 재생성을 줄였습니다. PWA 서비스워커 캐싱, 로컬 저장 + 세이브 코드, 광고 SDK 교체 대비 `AdService`/`ShareService` 인터페이스 분리, **108개** Vitest 회귀 테스트, Playwright 최종 UI 30개·전문 QA 4개 시나리오, 사치템 **16,384개 조합** 비주얼 스윕으로 배포 전 검증 흐름을 만들었습니다.
- **밸런스 안정화** — 가격 클램프, 오프라인 노이즈 댐핑, 진행 자산 기반 휴식 보상 캡, 정보력 적중률 상한을 함께 적용해 방치 보상이나 예측 업그레이드가 게임 경제를 붕괴시키지 않도록 튜닝했습니다.
- **책임감 있는 설계** — "엔터테인먼트 시뮬레이션 · 실제 투자 조언 아님" 고지, 실제 상장사와 무관한 가상 패러디 종목명.

<p>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/PWA-5A0FC8?style=flat-square&logo=pwa&logoColor=white"/>
<img src="https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white"/>
</p>

[![Live](https://img.shields.io/badge/▶%20Play-ant--investor--toss--review.vercel.app-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://ant-investor-toss-review.vercel.app)

---

### 5. Free-Tier Sleep — Unity 2D 게임 <sub>(해달 해커톤 · 팀 LastDance)</sub>

<img src="assets/portfolio/game-intro.png" alt="Free-Tier Sleep intro" width="520"/>

정보 과잉·AI 노동 착취를 풍자한 메타픽션 아케이드. **수직 플랫포머 + 탑다운 드로잉 디펜스** 2단 구성을 12일 만에 개발했습니다.

- **담당(Phase 1 클라이언트·연출)** — 인트로 씬 타이핑 이펙트·케이블 데이터 흐름 연출, 팝업 광고 스폰 매니저(`AdPopupManager`), 절차적 오디오(`ProceduralAudioHelper`).
- **팀 적용 기법** — 코요테 타임(`Physics2D.Raycast`), 청크 기반 절차적 맵 생성 + 오브젝트 풀링, `EdgeCollider2D` 실시간 드로잉 GC 스파이크 최적화.

<p>
<img src="https://img.shields.io/badge/Unity-000000?style=flat-square&logo=unity&logoColor=white"/>
<img src="https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white"/>
</p>

---

### 6. BELLEART — 프리미엄 클리닉 프론트엔드 <sub>(디자인 시스템 · 설정 기반 템플릿)</sub>

동일한 코드베이스로 브랜드마다 다른 무드를 뽑아내는 프론트엔드 템플릿. 아래는 다크·풀스크린 히어로의 프리미엄 테마로, 밝은 톤의 Members와 대비되는 결과물입니다.

<img src="assets/portfolio/belleart-home.png" alt="BELLEART premium theme" width="520"/>

<p>
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
<img src="https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white"/>
</p>

---

## 📊 성능 최적화 실측 — Members (Vanilla JS → Next.js 재구축)

같은 홈페이지를 **동일한 Lighthouse 데스크톱 프리셋**으로 측정한 재구축 전후 비교입니다.

| 지표 | 기존 (Vanilla JS) | 재구축 (Next.js 16) | 변화 |
| --- | :---: | :---: | :---: |
| **총 전송 용량** | 10,420 KB | **2,567 KB** | 🟢 **약 75% ↓** |
| **SEO** | 92 | **100** | 🟢 +8 |
| Best Practices | 100 | 100 | ⚪ |
| Performance | 94 | 89 | 🔴 −5 |
| LCP | 1.6 s | 2.2 s | 🔴 +0.6 s |

**해석.** 재구축의 목표는 속도 경신이 아니라 **다국어·관리자 기능·유지보수성 확보**였고, 그 과정에서 **전송 용량 약 75% 감축 + SEO 만점**을 달성했습니다(모바일도 8,270 KB → 2,528 KB, −69%로 동일 경향). 반대로 하이드레이션 비용 때문에 첫 렌더는 정적 사이트가 여전히 빠르며, 이 트레이드오프를 숫자로 인지하고 `next/image` 이미지 최적화로 회복하는 것을 다음 과제로 두고 있습니다.

<sub>※ Lighthouse 데스크톱·모바일. 기존은 라이브, 재구축은 로컬 프로덕션 빌드 측정. 전송량·SEO는 구조적 지표라 비교가 유효하고, 지연 지표는 네트워크 조건차가 있어 참고용입니다.</sub>

---

## 📈 성장 방식

같은 Todo 앱을 **세 번**, 매번 아키텍처를 끌어올리며 다시 만들었습니다: Vanilla JS + localStorage → React 19 + Vite → **Next.js 16 App Router + FastAPI + SQLAlchemy**. 배운 것은 매주 GitHub 이슈에 **KPT 회고**로 기록하고 다음 주에 반영했습니다. "이론만 많다"는 자기 지적 이후엔 로그에 반드시 직접 디버깅한 코드를 넣고, AI 코드도 한 줄씩 주석 달아 셀프 리뷰합니다. → [kakaotech-learning-log](https://github.com/TaeHuiKKIM/kakaotech-learning-log)

## 💰 투자 · 금융

- **관심 분야** — 투자·금융, 핀테크·수익형 서비스. 창업에 도전하며 게임/서비스 개발 병행.
- **자격** — ![ADsP](https://img.shields.io/badge/ADsP-5319e7?style=flat-square) ![SQLD](https://img.shields.io/badge/SQLD-5319e7?style=flat-square) · SQL/데이터 분석 기반
- **활동** — 모의투자대회·실전투자대회 참가, 백준 약 70문제 ([Solved.ac](https://solved.ac/1043tae/))
- **목표** — 금융권 / 데이터·백엔드 직무

## 🧰 Tech Stack

| Area | Tools |
| --- | --- |
| **Frontend** | ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black) ![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white) ![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white) |
| **Backend** | ![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white) `JSP/Servlet` ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) |
| **Data & DevOps** | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white) |
| **Game / Test** | ![Unity](https://img.shields.io/badge/Unity-000000?style=flat-square&logo=unity&logoColor=white) ![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white) ![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white) ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) |

## 🎓 Credentials & Activities

- **학점** GPA 4.18 / 4.3 · **TOEIC** 925 · **자격** ADsP, SQLD
- **CODE-MEDI 해커톤 최우수상** · 해달 해커톤 인기상 · 시흥 로컬 창업경진대회 장려상
- 백엔드 프로젝트 최우수 평가 **장학금** 수혜
- 카카오테크캠퍼스 4기 · IT 프로그래밍 동아리 해달

## 🔗 Links

[![Velog](https://img.shields.io/badge/개발%20기록-Velog-20C997?style=for-the-badge&logo=velog&logoColor=white)](https://velog.io/@kt_gml/posts)
[![Solved.ac](https://img.shields.io/badge/알고리즘-Solved.ac-00C73C?style=for-the-badge)](https://solved.ac/1043tae/)
[![Email](https://img.shields.io/badge/연락-tae1043@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tae1043@gmail.com)
