# Velog Meme Visual Refresh Design

## Objective

Replace the text-heavy editorial cards in the nine `ai-github-series` Velog drafts with original, scene-driven developer memes. The visuals must carry the joke through action, facial expression, and contrast; explanatory copy belongs in the article caption, not inside the image.

## Approved Direction

- Use one recurring original cast:
  - A young Korean computer-science student/developer with short dark hair, round glasses, and a green hoodie.
  - A small white desk-sized AI robot with a cyan face display.
- Render as a rough two-dimensional Korean webcomic/internet-meme illustration.
- Use thick black line work, flat muted colors, slightly imperfect hand-drawn shapes, and exaggerated reactions.
- Avoid photorealism, 3D rendering, cinematic lighting, cyberpunk glow, glossy stock-art polish, famous meme characters, logos, watermarks, and imitation of a living artist.
- Generate at 16:9 landscape composition suitable for Velog.
- Put no readable text, speech bubbles, labels, interface copy, or code inside generated images.
- Add one short Korean reaction caption below each image in Markdown.
- Create exactly three generated images per post: one cover scene and two body memes, for 27 published generated images total.
- Keep only four existing technical diagrams where exact structure or measurements matter:
  - `05-siganmoa-token/no-login-auth.png`
  - `06-ant-performance/before-after.png`
  - `07-ant-save/dual-slot.png`
  - `09-game-logic-port/browser-vs-unity.png`
- Store generated assets at `assets/velog/ai-github-series/v2/<post-id>/`.
- Keep v1 assets unchanged for rollback.

## Visual Grammar

The developer is the grounded observer and final decision-maker. The AI robot is capable and eager but literal, occasionally overconfident, and never evil. A meme should read within two seconds even with the caption hidden. The preferred comic rhythm is setup on the left and consequence or reaction on the right, but single-scene covers may use foreground/background contrast.

Generated files use:

- `cover-meme.png`
- `meme-01.png`
- `meme-02.png`

Captions are italicized and should be 8–24 Korean characters. They may be humorous, but must not introduce technical claims that are absent from the article.

## Storyboards

### 01 — AI Escaped

- `cover-meme.png`: The AI robot squeezes through a tiny hole in a package-proxy wall while the developer notices an alarm behind it.
- `meme-01.png`: Two-panel contrast. Left: the robot poses dramatically at a prison wall. Right: it follows a trail of benchmark answer sheets through an accidentally open service tunnel.
- `meme-02.png`: A team gives the robot an enormous key ring; after an alarm, everyone points at the robot while the developer points back at the key ring and open gate.

### 02 — Prompt to Shell

- `cover-meme.png`: A harmless-looking document whispers to the AI robot, which stretches one hand toward a large terminal control while the developer lunges to stop it.
- `meme-01.png`: An email envelope wearing a sheep disguise hides a command-shaped snake; the robot welcomes it while the developer spots the tail.
- `meme-02.png`: The robot faces several permission doors. The developer holds the final physical key and refuses to hand it over automatically.

### 03 — AI Learning Roadmap

- `cover-meme.png`: The robot powers a rocket-fast coding cart, but the developer holds the steering wheel and map.
- `meme-01.png`: The robot builds a tall software tower at high speed while the developer kneels to inspect a cracked foundation.
- `meme-02.png`: In a small gym, the developer trains with icon-shaped weights for Python, operating systems, databases, testing, and AI; the robot acts as an enthusiastic spotter.

### 04 — Photo Sweep

- `cover-meme.png`: The robot eagerly reaches for a giant delete button; the developer calmly unplugs it and sorts photos into simple physical trays.
- `meme-01.png`: A messy flood of photo prints becomes neat piles using clock, aspect-ratio, blur, and duplicate visual cues.
- `meme-02.png`: A locked photo album stays inside a phone-shaped room while a giant cloud hand cannot reach through the privacy boundary.

### 05 — Siganmoa Token

- `cover-meme.png`: Guests enter an open party room without a login bouncer, while the organizer uses one small golden key to open a private control booth.
- `meme-01.png`: Several people place separate availability blocks on a table; the blocks unexpectedly connect into one continuous bridge.
- `meme-02.png`: The organizer keeps a small key inside an inner pocket while a bright public invitation card remains visible in the other hand.

### 06 — Ant Performance

- `cover-meme.png`: Hundreds of tiny game ants all try to pass through one narrow start gate, creating a traffic jam; the developer opens several controlled lanes.
- `meme-01.png`: An orchestra conductor starts sixteen instruments at once and is overwhelmed; in the second half, four small groups enter in batches.
- `meme-02.png`: Only visible ant actors perform on stage while hundreds of hidden actors wait calmly backstage instead of crowding the scene.

### 07 — Ant Save

- `cover-meme.png`: An ant carries a glowing save chest across two stepping stones marked only by different colors; one cracks while the other remains safe.
- `meme-01.png`: Two scribes try to overwrite the same ledger, and a red conflict bell stops the stale writer.
- `meme-02.png`: A futuristic traveler offers a sealed advanced box to an older app; the older app respectfully refuses to open what it cannot understand.

### 08 — Clinic SEO Safety

- `cover-meme.png`: The AI robot printer sends medical-ad drafts toward a publishing conveyor; the developer pulls a large emergency brake before release.
- `meme-01.png`: An oversized red review stamp blocks a megaphone that is exaggerating a tiny medical result.
- `meme-02.png`: Patient records remain locked outside a prompt factory while only de-identified notes pass through a small inspection window.

### 09 — Game Logic Port

- `cover-meme.png`: The developer carries one rule blueprint from a browser theater stage to a Unity theater stage; costumes and scenery change while the blueprint stays the same.
- `meme-01.png`: Two cooks in separate kitchens follow copies of the same recipe; tiny differences begin to create visibly different dishes.
- `meme-02.png`: One protected balance book feeds both game engines through two clean pipes while the developer checks that neither engine owns the rules.

## Markdown Placement

- Replace each v1 cover image with `v2/<post-id>/cover-meme.png`.
- Replace the first conceptual image after the opening section with `meme-01.png`.
- Replace the second conceptual image near the article's main design lesson with `meme-02.png`.
- Remove all other v1 image links except the four retained technical diagrams.
- Place an italic caption immediately after each generated image.
- Keep headings, body copy, links, and code blocks unchanged.

## Acceptance Criteria

- All 27 generated images exist and decode as landscape PNG files.
- No generated image contains paragraphs, UI cards, diagrams made primarily of text, logos, or watermarks.
- Character appearance and illustration language are recognizably consistent across the series.
- Each of the nine Markdown drafts references exactly three `v2` generated images.
- Only the four approved v1 technical diagrams remain referenced.
- All referenced GitHub raw URLs return HTTP 200 after merge.
- The already published AI learning-roadmap post remains published after its content is updated.
- The other eight series entries remain private drafts after their content is updated.

## Approved Scope Addendum — 2026-07-31

The user asked to replace three weak thumbnails on the previously published Agentic AI posts. The targets are the financial safety post and the two older posts immediately before it:

- `답변에서 저장까지 — Tool Call, Structured Output, SQLite로 이어진 3주`
- `검색 함수 하나면 되는 줄 알았는데 ChromaDB, SQLite, 대화 기억을 나눈 이유`
- `LLM이 돈을 움직이지 않게 설계하기 — 결정론 규칙과 승인 토큰`

Create one text-free 16:9 scene-driven thumbnail for each under `assets/velog/recent-post-thumbnails/v2/`. Keep the posts published and leave their prose unchanged.
