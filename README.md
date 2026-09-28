<div align="center">

# 김태희 · TaeHui Kim

### AI 제품을 만들고 운영하는 Product · Backend Developer

경북대학교 글로벌소프트웨어융합전공 · 카카오테크캠퍼스 4기<br/>
웹 서비스에서 시작해 백엔드, 실시간 AI, 모바일과 제품 운영으로 경험을 넓혀가고 있습니다.

<br/>

![GPA](https://img.shields.io/badge/GPA-4.21%20/%204.3-1f6feb?style=for-the-badge)
![TOEIC](https://img.shields.io/badge/TOEIC-925-0a7d33?style=for-the-badge)
![ADsP](https://img.shields.io/badge/ADsP-취득-5319e7?style=for-the-badge)
![SQLD](https://img.shields.io/badge/SQLD-취득-5319e7?style=for-the-badge)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-TaeHui%20Kim-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/taehui-kim-930713412/)
[![Velog](https://img.shields.io/badge/Velog-20C997?style=for-the-badge&logo=velog&logoColor=white)](https://velog.io/@kt_gml/posts)
[![Solved.ac](https://img.shields.io/badge/Solved.ac-1043tae-00C73C?style=for-the-badge)](https://solved.ac/1043tae/)
[![Email](https://img.shields.io/badge/tae1043@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tae1043@gmail.com)

</div>

---

## About Me

Flash로 만들어져 제대로 동작하지 않던 병원 홈페이지를 고치고 싶어 웹 개발을 시작했습니다.
직접 사이트를 제안하고 수년간 운영한 경험을 출발점으로 서버·DB·실시간 AI·모바일까지 영역을 넓혔습니다.

지금은 다음 세 가지를 개발의 기준으로 삼고 있습니다.

- **AI를 기능이 아니라 신뢰할 수 있는 제품 흐름으로 연결하기**
- **기술 선택의 이유와 트레이드오프를 수치와 기록으로 남기기**
- **구현에서 끝내지 않고 테스트·배포·운영까지 책임지기**

### Current Focus

- **Antony Studio** — 개미 투자자 키우기 Apps in Toss 출시·운영 및 사용자 피드백 기반 개선
- **Financial AI** — 미래에셋 AI Festival 제출작 RiskTwin · KB 머니룰 기반 안심보이스
- **Reqover** — Spring 요청별 실행 메서드를 기록하고 변경 코드가 닿는 API를 찾는 오픈소스 도구
- **TUG GUARD** — 예인줄 학습 데이터 생성부터 비전 모델 연동·위험 판단까지 연결한 해양 시뮬레이터
- **카카오테크캠퍼스 Agentic AI** — Tool Call → Structured Output → SQLite → 출처별 RAG 학습
- **Python · FastAPI** — AI Product/Backend 역량과 코딩테스트 기반 강화
- **종합설계프로젝트 준비** — 평가 가능한 신뢰성 중심 Agentic AI 주제 탐색

---

# Projects

## 1. 🏎️ AWS DeepRacer — Physical AI 경진대회 최우수상

<sub>강화학습 전략 · 보상 함수 · 실차 튜닝</sub>
<p align="center">
  <img width="620" alt="image" src="https://github.com/user-attachments/assets/e5486543-3981-4915-a043-5770d9361fc0" />
</p>

![Award](https://img.shields.io/badge/Physical%20AI-최우수상-d4a72c?style=flat-square)
![Models](https://img.shields.io/badge/Models-약%2050개-1f6feb?style=flat-square)
![Direction](https://img.shields.io/badge/Track-Counterclockwise-238636?style=flat-square)

- 학습·검증 병목을 줄이기 위해 가설 10개와 약 50개 모델을 병렬로 검증했습니다.
- 시뮬레이터 6초대의 좌표 기반 정책이 실차에서 이탈한 원인을 카메라 지연과
  전이되지 않는 위치 단서로 분석했습니다.
- 좌표를 버리고 중앙선 추종·워블 억제·±20도 조향과 구간별 속도 제어를 채택해
  **경북대 × 전남대 Physical AI 경진대회 최우수상**을 받았습니다.

[![Repository](https://img.shields.io/badge/GitHub-DeepRacer%20기록-181717?style=for-the-badge&logo=github)](https://github.com/TaeHuiKKIM/deepracer-physical-ai)

---

## 2. 🩺 Medirole — 의료인의 CPX 대비를 위한 AI 표준화환자 플랫폼

<sub>실시간 문진 · 자동 채점 · CODE-MEDI 해커톤 최우수상</sub>

<p align="center">
  <img src="assets/portfolio/cpx-final-home.png" alt="MediCPX 시나리오 대시보드" width="620"/>
</p>
<p align="center">
  <img src="assets/portfolio/cpx-final-room.png" alt="MediCPX 실시간 문진 화면" width="300"/>
  <img src="assets/portfolio/cpx-final-report.png" alt="MediCPX 자동 채점 리포트" width="300"/>
</p>

![Award](https://img.shields.io/badge/CODE--MEDI-최우수상-d4a72c?style=flat-square)
![Exam](https://img.shields.io/badge/Exam-12%20min-8E75B2?style=flat-square)
![Checklist](https://img.shields.io/badge/Checklist-40-8E75B2?style=flat-square)

- **FastAPI WebSocket으로 실시간 음성·텍스트 문진**을 구현했습니다.
- 학생이 정확히 질문하기 전에는 정보를 공개하지 않는 환자 상태와 **12분 시험 제한**을 설계했습니다.
- Gemini Structured Output이 근거 있는 항목을 반환하고 서버가 전체 **40개 체크리스트**를 복원하도록 구성했습니다.
- 채점이 지연되거나 실패해도 대화 기록을 잃지 않는 복구 리포트를 제공했습니다.

<p>
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socketdotio&logoColor=white" alt="WebSocket"/>
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white" alt="Supabase"/>
  <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
</p>

---

## 3. 🏥 Members Clinic — 첫 웹사이트에서 실제 운영 서비스까지

<sub>1인 기획·개발·운영 · Next.js 재구축</sub>

<p align="center">
  <img src="assets/portfolio/members-home.png" alt="Members Clinic 홈페이지 전체 화면" width="620"/>
</p>

![Status](https://img.shields.io/badge/Status-Live-238636?style=flat-square)
![Role](https://img.shields.io/badge/Role-Solo%20Product-1f6feb?style=flat-square)
![Transfer](https://img.shields.io/badge/Transfer-%E2%88%9275%25-238636?style=flat-square)
![SEO](https://img.shields.io/badge/SEO-100-238636?style=flat-square)

- Flash 기반 사이트를 보고 웹을 독학한 뒤 병원에 직접 개선을 제안해 **기획·디자인·개발·배포**를 맡았습니다.
- 운영 경험을 바탕으로 복잡한 예약 서버보다 검색 가능한 콘텐츠, 상담 접근성과 낮은 운영 복잡도를 우선했습니다.
- 메타데이터, sitemap, robots와 의료·FAQ·Breadcrumb 구조화 데이터를 적용했습니다.
- 동일 Lighthouse 데스크톱 프리셋에서 전송량을 **10,420KB → 2,567KB(약 75% 감소)**, SEO를 **92 → 100**으로 개선했습니다.

| 지표 | 기존 HTML/CSS/JS | Next.js 운영 버전 | 변화 |
| --- | :---: | :---: | :---: |
| 총 전송 용량 | 10,420KB | **2,567KB** | **약 75% 감소** |
| SEO | 92 | **100** | **+8** |
| Performance | **94** | 89 | −5 |
| LCP | **1.6초** | 2.2초 | +0.6초 |

검색 가능한 콘텐츠와 유지보수성을 중심으로 재구축하고, 전후 측정 결과를 다음 최적화의 기준으로 기록했습니다.

<p>
  <img src="https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js 16"/>
  <img src="https://img.shields.io/badge/React%2019-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React 19"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/Tailwind%204-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS 4"/>
</p>

[![Live](https://img.shields.io/badge/▶%20Live-membersclinic.com-000000?style=for-the-badge&logo=googlechrome&logoColor=white)](https://membersclinic.com)

---

## 4. 🛍️ MERCI — JSP·Servlet 커머스

<sub>백엔드 기본기 · 주문 트랜잭션 · 최우수 평가 및 장학금</sub>

<p align="center">
  <img src="assets/portfolio/merci-main.png" alt="MERCI 쇼핑몰 메인 화면" width="620"/>
</p>
<p align="center">
  <img src="assets/portfolio/merci-detail.png" alt="MERCI 상품 상세 화면" width="300"/>
  <img src="assets/portfolio/merci-cart.png" alt="MERCI 장바구니와 주문 화면" width="300"/>
</p>

![Result](https://img.shields.io/badge/Result-Top%20Evaluation-d4a72c?style=flat-square)
![Integrity](https://img.shields.io/badge/Integrity-Atomic%20Order-238636?style=flat-square)
![Scale](https://img.shields.io/badge/Scale-56%20JSP-6e7681?style=flat-square)

- JSP·Servlet·JDBC·MySQL로 요청, 세션, 인증과 DB 반영 흐름을 직접 구현했습니다.
- 주문 생성, 주문 항목 삽입과 재고 차감을 하나의 트랜잭션으로 묶고 실패 시 rollback했습니다.
- `WHERE stock >= ?` 조건으로 초과 판매를 차단했습니다.
- PG 테스트 결제, 카카오 OAuth2, 상품·주문·Q&A 관리자 기능까지 커머스 흐름을 완성했습니다.
- DAO 9개, 모델 10개, JSP 56개, 처리 컨트롤러 22개와 Java 2,127 LOC 규모로 완성해 **최우수 평가와 장학금**을 받았습니다.

<p>
  <img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white" alt="Java"/>
  <img src="https://img.shields.io/badge/JSP%20%2F%20Servlet-E76F00?style=flat-square&logo=apachetomcat&logoColor=white" alt="JSP and Servlet"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/JDBC-59666C?style=flat-square" alt="JDBC"/>
</p>

---

## 5. 🛡️ KB 머니룰 기반 안심보이스 — 시니어 금융 Agentic AI

<sub>2026 KB AI Challenge · 팀 프로젝트 진행 중</sub>
<p align="center">
  <img width="620" alt="image" src="https://github.com/user-attachments/assets/4ae8d9ff-d05b-4a2b-b41e-f4497555bf0c" />
</p>

![Status](https://img.shields.io/badge/Status-In%20Progress-d4a72c?style=flat-square)
![Safety](https://img.shields.io/badge/Safety-Deterministic%20Rules-238636?style=flat-square)
![Approval](https://img.shields.io/badge/Approval-One--time%20Token-1f6feb?style=flat-square)

- 시니어 사용자가 음성과 텍스트로 금융 업무를 요청할 수 있는 에이전트를 개발하고 있습니다.
- LLM은 의도 구조화와 설명을 담당하고, 실제 실행 가능 여부는 **결정론 규칙과 서버 코드**가 판단하도록 권한을 분리했습니다.
- 중요한 거래는 사용자가 확인한 규칙과 **일회용 승인 토큰**을 모두 검증한 뒤에만 실행되도록 설계했습니다.
- 외부 API 없이 재현하는 offline 모드와 실제 연동을 분리하고, 골든셋으로 안전 개입 단계를 평가하고 있습니다.

> [공개 저장소와 구현 기록](https://github.com/TaeHuiKKIM/kb-ansimvoice)

---

## 6. 🐜 개미 투자자 키우기 — Apps in Toss 출시·운영

<sub>Antony Studio · 제품 기획·개발·아트 검수·출시·운영</sub>

<p align="center">
  <img src="assets/portfolio/ant-worker-home.png" alt="일개미와 강남 아파트 배경의 실제 게임 홈" width="240"/>
  <img src="assets/portfolio/ant-stock-current.png" alt="실제 게임 내 가상 종목 차트 · 별도 촬영" width="240"/>
</p>
<p align="center"><sub>가상 투자 게임 · 홈과 종목 차트</sub></p>

- 가상 주식 매매와 방치형 성장을 결합하고, 개미 진화·집·수집품·꾸미기로 이어지는 게임을 기획·개발해 **Apps in Toss에 출시·운영**했습니다.
- 출시 초기 신규 게임·시뮬레이션 분야 **1위 달성**.
- **누적 이용자 10,336명 · D1 리텐션 52.8% · D7 리텐션 30.3%**.
- **Threads(스레드) 콘텐츠 조회수 419,443회 확보**.
- 튜토리얼 문장 중복 출력, 선택 이미지 로딩과 첫 플레이의 경합, PC·모바일 화면 충돌을 재현하고 수정·회귀검사 기록을 남겼습니다.
- HTML·CSS·JavaScript 공통 게임과 플랫폼별 어댑터를 분리하고, AI 생성 아트 후보를 실제 화면에서 검수해 최종 자산을 선정했습니다.

[게임 웹 버전](https://ant-idle-game.vercel.app/)

---

## 7. 💼 RiskTwin — 미래에셋 AI Festival 제출작

<sub>금융 AI 기획 · DART 공시 근거 · 다중 Agent 역할 설계</sub>

<p align="center">
  <img src="assets/portfolio/risktwin-design.svg" alt="RiskTwin 입력·4개 Agent 역할·근거 검증 설계 개념도" width="720"/>
</p>
<p align="center"><sub>RiskTwin · Agent 설계 개념도</sub></p>

- 공시 요약을 넘어 **보유자산·소득·연금과 기업 위험의 겹침**을 설명하는 문제를 정의했습니다.
- 장기투자 콘텐츠 23개와 대표 사례 5개를 검토해 기존 공시 요약 서비스와의 차이를 정리했습니다.
- **추천·반대 검토·적합성 판단·근거 검증**의 4개 Agent 역할을 설계하고, 자연어 설명과 규칙 계산·원문 검증의 책임을 분리했습니다.
- 2026년 7월 미래에셋 AI Festival에 제출했으며, 문제 정의·조사·Agent 구조 설계를 맡았습니다.

---

## 8. 🔧 Reqover — 요청별 실행 관계를 추적하는 Java Agent

<sub>2인 오픈소스 팀 · 핵심 MVP 설계·구현 · Java Agent · ASM · Spring</sub>

<p align="center">
  <img src="assets/portfolio/reqover-request-report.png" alt="Reqover 요청별 실제 실행 메서드 리포트" width="620"/>
</p>
<p align="center">
  <img src="assets/portfolio/reqover-code-index.png" alt="Reqover 코드 변경 영향 API 역조회 리포트" width="620"/>
</p>
<p align="center"><sub>공개 저장소의 요청별 실행 및 코드 → API 영향도 예제 리포트</sub></p>

- **문제 정의:** 기존 커버리지 리포트로는 메서드가 실행됐다는 사실은 알 수 있어도 어떤 HTTP 요청이 실행했는지 알기 어려웠습니다. 요청 단위로 실행 관계를 기록하는 방향을 공동 설계했습니다.
- **내 구현:** 요청별 실행 bucket과 probe 라우팅, ASM 메서드 진입 계측, `-javaagent` 패키징, API → 메서드 리포트와 코드 → API 역방향 인덱스, 별도 JVM 에이전트 검증·데모를 만들었습니다.
- **팀의 확장:** Spring MVC/WebFlux 어댑터는 함께 개선했습니다. 팀은 JSON 내보내기와 CLI `render`·`diff`·`impact`, GitHub Action을 더해 변경 파일에서 다시 확인할 API 후보를 제시하는 흐름으로 확장했습니다.
- **검증 범위:** 메서드 진입과 실제 관측된 요청을 연결합니다. 줄·분기 커버리지를 측정하는 도구와 함께 사용할 수 있습니다.

[reqover-labs/reqover](https://github.com/reqover-labs/reqover)

---

## 9. ⚓ TUG GUARD — 시뮬레이션부터 비전 추론까지 잇는 해양 안전 디지털 트윈

<sub>Three.js · React Three Fiber · 학습용 합성 데이터 · YOLO-Seg 연동 · FastAPI</sub>

<p align="center">
  <img src="assets/portfolio/tugguard-live.png" alt="TUG GUARD 실제 Three.js 전체 보기와 시연 조작 패널" width="720"/>
</p>
<p align="center"><sub>TUG GUARD · 3D 시뮬레이터와 시연 조작 패널</sub></p>

- **시뮬레이터:** 본선·ASD 예인선·예인줄을 조작하는 Three.js 장면과 고정 CCTV 시점을 구현했습니다. 방향·줄 길이·속력·시간대를 바꿔 시나리오를 재현합니다.
- **내가 만든 학습 데이터 흐름:** 예인줄 Sag 단계와 시점·조명·해상 조건을 달리한 RGB 이미지, 픽셀 마스크, YOLO-Seg 폴리곤 라벨을 생성했습니다. 렌더 지오메트리로 정답을 만들고 가려진 줄은 마스크에서 제외했습니다.
- **멀티모달 기록:** 하나의 시뮬레이션 시계를 기준으로 24 FPS 영상과 100 Hz 합성 IMU를 기록하고 시각·프레임·센서값의 정합성을 검사했습니다.
- **AI 연동과 위험 판단:** 팀이 학습한 예인줄 분할 모델을 FastAPI 분석 서버에 연결했습니다. 예측 마스크의 품질, 줄 처짐 변화, 영상 각도와 IMU 횡경사를 시간에 따라 결합해 경보 상태를 계산했습니다.
- **검증:** 분할 라벨 변환·영상/IMU 동기화·서버 응답·경보 지속/회복 조건을 재현 가능한 시나리오와 테스트로 확인했습니다. 모델 학습·평가는 팀 작업이며, 실선 사고 데이터로 검증한 안전 인증 시스템은 아닙니다.

[ShipTugging/tugboat-safety-twin](https://github.com/ShipTugging/tugboat-safety-twin)

[시뮬레이터 열기](https://tugboat-safety-twin.vercel.app/)

---

<details>
<summary><strong>📦 More Products & Experiments — 추가 프로젝트 펼쳐보기</strong></summary>

<br/>

| 프로젝트 | 문제와 구현 | 핵심 기술 · 결과 |
| --- | --- | --- |
| **🧭 Agent SEO Kit** | 읽기 전용 SEO 점검·승인된 수정·근거 기반 재검증을 분리 | Codex·Claude Code Agent Skills |
| **🤖 카카오테크캠퍼스 팀 프로젝트** | 일정 Tool·구조화 요청·SQLite 기록·RAG 및 팀 프론트엔드 구현 | Python · TypeScript · Agentic AI |
| **🗓️ 시간모아** | 로그인 없이 링크로 일정을 모으고 연속 가능한 시간을 추천 | Next.js, TypeScript, Supabase Postgres, SHA-256 토큰 |
| **📄 ReadmePDF** | 파일을 서버에 보내지 않고 브라우저에서 Markdown·PDF 처리 | Next.js Static Export, pdf-lib, JSZip, 4개 언어 56개 경로 |
| **💤 Free-Tier Sleep** | 12일 해커톤에서 두 장르를 연결한 메타픽션 게임 | Unity, C#, 인트로·팝업·절차적 오디오 담당 |
| **🧹 Photo Sweep** | 사진·EXIF를 서버에 보내지 않는 로컬 우선 Android 정리 앱 | Expo, React Native, TypeScript, 시스템 삭제 확인 |
| **🎥 Virtual Face Cam** | OBS 기반 크로스플랫폼 버전과 macOS 네이티브 카메라 확장 도전 | Python, SwiftUI, CoreMediaIO |
| **✨ Clinic Website Productization** | 병원 홈페이지 제작·SEO·영업 흐름을 반복 가능한 제품으로 구조화 | Next.js, 6개 테마, SEO Automation, Sales Kit |

### Links

- [개미 투자자 키우기](https://ant-idle-game.vercel.app)
- [ReadmePDF](https://web-readme-pdf-free-mrgf3o4gbe0b862a.sel3.cloudtype.app/)
- [Virtual Face Cam](https://github.com/TaeHuiKKIM/virtual-face-cam)
- [Virtual Face Cam for macOS](https://github.com/TaeHuiKKIM/virtual-face-cam-mac)

</details>

---

## 기록하고 검증하는 방식

- 같은 Todo 앱을 **Vanilla JS + localStorage → React + Vite → Next.js + FastAPI + SQLAlchemy**로 다시 만들며 상태·컴포넌트·서버 경계를 비교했습니다.
- 카카오테크캠퍼스 학습은 GitHub Issue에 **주차별 회고와 리뷰 반영 과정**을 기록합니다.
- AI가 작성한 코드도 tool arguments, 저장 결과, 반환 계약과 경계 조건을 직접 실행해 확인합니다.
- 프로젝트마다 `docs/`에 기획, 아키텍처, 트러블슈팅과 검증 근거를 남기고 README를 현재 상태와 맞춥니다.

→ [kakaotech-learning-log](https://github.com/TaeHuiKKIM/kakaotech-learning-log)

## Tech Stack

| Area | Tools |
| --- | --- |
| **AI Product & Backend** | Python · FastAPI · LangChain · Structured Output · WebSocket · Java · Spring Boot |
| **Web Product** | TypeScript · React · Next.js · JavaScript · Tailwind CSS |
| **Data** | MySQL · PostgreSQL · SQLite · Supabase · ChromaDB |
| **Delivery & Test** | Docker · GitHub Actions · Vercel · Cloudtype · Vitest · Playwright · Pytest |
| **Other Platforms** | React Native · Expo · Unity · C# · SwiftUI |
| **3D & Vision** | Three.js · React Three Fiber · YOLO-Seg 학습 데이터 · 합성 비전/IMU |

## Credentials & Activities

### 🏆 Awards

<p align="center">
  <img src="assets/portfolio/kakaotech-ideathon-award.png" alt="카카오테크캠퍼스 아이디어톤 우수상" width="620"/>
</p>

- **경북대 × 전남대 Physical AI 경진대회(AWS DeepRacer) 최우수상**
- **카카오테크캠퍼스 아이디어톤 우수상**
- **2026 CODE-MEDI 의료 AI·SW 융합 해커톤 최우수상** — 대한민국의학한림원 · 2026.06.29
- **2026 해달 해커톤 인기상** — 경북대학교 IT대학 학술동아리 해달 · 2026.06.09
- **2025 TU 소프트웨어 경진대회 장려상(교내 SW경진대회)** — 한국공학대학교 · 2025.11.19
- **2025 시흥실록지리지 장려상** — 학생주도형 지역문제 해결 프로젝트 · 한국공학대학교 창업교육센터 · 2025.12.05
- 백엔드 프로젝트 최우수 평가 및 **장학금** 수혜

### Credentials & Programs

- **GPA 4.21 / 4.3** · **TOEIC 925** · **ADsP** · **SQLD**
- 카카오테크캠퍼스 4기 · IT 프로그래밍 동아리 해달

## Links

[![LinkedIn](https://img.shields.io/badge/프로필-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/taehui-kim-930713412/)
[![Velog](https://img.shields.io/badge/개발%20기록-Velog-20C997?style=for-the-badge&logo=velog&logoColor=white)](https://velog.io/@kt_gml/posts)
[![Solved.ac](https://img.shields.io/badge/알고리즘-Solved.ac-00C73C?style=for-the-badge)](https://solved.ac/1043tae/)
[![Email](https://img.shields.io/badge/연락-tae1043@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tae1043@gmail.com)
