# Reqover·TUG GUARD 프로필 근거

2026-09-28 저장소 README, 코드, 설계·검증 문서와 기여 이력을 다시 대조했다. 본문은 개인 구현과 팀의 후속 작업을 나눠 적었다.

## Reqover

- 개인 핵심 MVP: 요청별 bucket·probe routing, ASM 메서드 진입 계측, Java Agent, 정방향·역방향 리포트와 별도 JVM E2E. [프로젝트 README](https://github.com/reqover-labs/reqover), [아키텍처](https://github.com/reqover-labs/reqover/blob/main/docs/02_architecture.ko.md), 구현 이력 `5974136`, `a613718`, `fdcda68`, `a63bbd1`.
- MVC/WebFlux 어댑터 및 CI는 공동 작업이다. CLI impact/diff, JSON 저장·복원, starter 등의 후속 확장은 팀 전체 제품 성과로만 설명한다.
- 121개 테스트 통과는 당시 v0.2.0 기록이며 현재 HEAD 테스트 수로 표기하지 않는다. 이번 프로필 갱신에서 전체 테스트를 재실행한 것은 아니다.

## TUG GUARD

- 개인 구현: [예인줄 Sag 데이터 생성](https://github.com/ShipTugging/tugboat-safety-twin/blob/main/docs/2026-09-07-towline-sag-dataset.md) `e823e10`, [영상·IMU 공유 시계 기록](https://github.com/ShipTugging/tugboat-safety-twin/blob/main/docs/MULTIMODAL_RECORDING_V1.md) `d3910e0`, 추론 서버 연동 `ffbb8f4`, [위험 판단 V2](https://github.com/ShipTugging/tugboat-safety-twin/blob/main/docs/2026-09-16-risk-v2.md) `9e350f0`.
- 팀 모델 학습·평가와 체크포인트 반입은 개인 학습 성과로 주장하지 않는다. 120장 V2 파일럿의 높은 IoU는 라벨 변환 품질이지 모델 성능이 아니다. 실측 센서·실선 사고 예측 성능으로 확장 해석하지 않는다.
- 실제 데모 화면은 본 저장소의 `assets/portfolio/tugguard-live.png`에 있으며 서버 연결 전 상태다.

## 공개 프로필 표현

각 프로젝트를 문제 → 개인 구현 → 팀 확장·결과 → 검증 범위 순으로 기술했다. 구체적 구현과 출처가 있는 수치만 사용한다.
