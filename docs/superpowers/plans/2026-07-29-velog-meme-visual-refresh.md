# Velog Meme Visual Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace text-heavy Velog artwork with 27 original scene-driven developer memes and update all nine private drafts without changing article prose.

**Architecture:** Generate one reusable character reference, then generate three standalone 16:9 scenes per post from the approved storyboard. Store selected images under a versioned GitHub asset path, rewrite local Markdown image blocks and captions, publish assets, and update the matching Velog drafts through the browser.

**Tech Stack:** OpenAI image generation, PNG, Markdown, PowerShell, Git, GitHub raw content, Velog editor

## Global Constraints

- Use the recurring developer and AI robot cast defined in the design spec.
- Generated images contain no readable text, logos, watermarks, or copied meme characters.
- Exactly 27 generated images are published: `cover-meme.png`, `meme-01.png`, and `meme-02.png` for each of nine posts.
- Preserve all v1 assets for rollback.
- Never add `.env`, API keys, browser storage, cookies, session tokens, or other credentials to Git.
- Keep article prose unchanged except generated-image blocks and their italic captions.

---

### Task 1: Freeze the approved storyboard and repository layout

**Files:**
- Create: `docs/superpowers/specs/2026-07-29-velog-meme-visual-refresh-design.md`
- Create: `docs/superpowers/plans/2026-07-29-velog-meme-visual-refresh.md`
- Modify: `assets/velog/ai-github-series/README.md`

**Interfaces:**
- Consumes: User approval for the recurring webcomic approach.
- Produces: Exact file names, scene descriptions, and acceptance criteria for Tasks 2–6.

- [ ] **Step 1: Confirm the asset tree is clean**

Run: `git status --short --branch`

Expected: current branch is `agent/velog-meme-visual-refresh` and no unrelated changes exist.

- [ ] **Step 2: Add the design and implementation documents**

Write the exact constraints and 27 storyboards from the approved design into the two files listed above.

- [ ] **Step 3: Validate that the plan contains no placeholders**

Review both documents for unfinished markers, deferred work, and generic instructions that do not name an exact file or result.

Expected: every requirement names an exact action and expected result.

- [ ] **Step 4: Commit the approved design**

Run:

```powershell
git add docs/superpowers
git commit -m "docs: plan Velog meme visual refresh"
```

Expected: one commit containing only the design and plan.

### Task 2: Generate and curate the recurring meme assets

**Files:**
- Create: `assets/velog/ai-github-series/v2/<post-id>/cover-meme.png`
- Create: `assets/velog/ai-github-series/v2/<post-id>/meme-01.png`
- Create: `assets/velog/ai-github-series/v2/<post-id>/meme-02.png`

**Interfaces:**
- Consumes: The exact cast, style, and 27 storyboards in the design spec.
- Produces: 27 landscape PNG files with predictable paths for Markdown rewriting.

- [ ] **Step 1: Generate a private character reference**

Generate a clean character sheet for the green-hoodie developer and white cyan-faced AI robot. Keep it outside the published asset tree and use it only as a visual reference.

- [ ] **Step 2: Generate the 27 storyboard scenes**

For each scene, use the shared style clause and the exact scenario from the design spec. Require 16:9 landscape composition, no text, no speech bubbles, no logo, no watermark, flat colors, and a rough hand-drawn webcomic finish.

- [ ] **Step 3: Copy selected outputs into the versioned asset tree**

Create exactly the three named PNG files for every post ID. Do not overwrite v1 files.

- [ ] **Step 4: Inspect all generated images**

Create contact sheets for visual review and inspect each source image at full resolution when text artifacts, duplicated limbs, broken props, or inconsistent characters are suspected. Regenerate rejected scenes.

- [ ] **Step 5: Validate file count and dimensions**

Run:

```powershell
$files = Get-ChildItem assets/velog/ai-github-series/v2 -Recurse -Filter *.png
if ($files.Count -ne 27) { throw "Expected 27 PNG files, found $($files.Count)" }
```

Expected: 27 PNG files.

### Task 3: Rewrite the nine local Markdown drafts

**Files:**
- Modify: `outputs/ai-github-velog-series/posts/01-ai-escaped.md`
- Modify: `outputs/ai-github-velog-series/posts/02-prompt-to-shell.md`
- Modify: `outputs/ai-github-velog-series/posts/03-ai-learning-roadmap.md`
- Modify: `outputs/ai-github-velog-series/posts/04-photo-sweep.md`
- Modify: `outputs/ai-github-velog-series/posts/05-siganmoa-token.md`
- Modify: `outputs/ai-github-velog-series/posts/06-ant-performance.md`
- Modify: `outputs/ai-github-velog-series/posts/07-ant-save.md`
- Modify: `outputs/ai-github-velog-series/posts/08-clinic-seo-safety.md`
- Modify: `outputs/ai-github-velog-series/posts/09-game-logic-port.md`

**Interfaces:**
- Consumes: Stable `v2` asset paths from Task 2.
- Produces: Velog-ready Markdown with three meme assets per post.

- [ ] **Step 1: Replace image blocks**

For each post, link the new cover and two meme files at their approved positions. Retain only the four approved technical-diagram URLs.

- [ ] **Step 2: Add reaction captions**

Place one short italic Korean caption immediately below each generated image. Keep captions factual and consistent with the surrounding paragraph.

- [ ] **Step 3: Verify prose integrity**

Compare a copy with all image blocks and captions removed against the original article text.

Expected: headings, paragraphs, lists, code blocks, and source links are unchanged.

- [ ] **Step 4: Validate image reference counts**

Run the series validator and require exactly three `/v2/` references per post and exactly four remaining v1 technical-diagram references across the series.

Expected: validator exits with status 0.

### Task 4: Document and commit the published asset set

**Files:**
- Modify: `assets/velog/ai-github-series/README.md`
- Create: `assets/velog/ai-github-series/v2/**`

**Interfaces:**
- Consumes: Curated PNG files from Task 2.
- Produces: A Git commit ready for a focused pull request.

- [ ] **Step 1: Update the asset README**

Document that `v2` uses scene-driven, text-free original meme illustrations and that v1 remains available for rollback.

- [ ] **Step 2: Scan staged paths for secrets**

Run:

```powershell
git status --short
git diff --cached --name-only
```

Expected: only documentation and PNG assets are staged; no `.env`, credential, cookie, browser-profile, or session file appears.

- [ ] **Step 3: Commit the assets**

Run:

```powershell
git add assets/velog/ai-github-series README.md docs
git commit -m "feat: add scene-driven Velog meme artwork"
```

Expected: one focused asset commit after the earlier documentation commit.

### Task 5: Publish and verify GitHub raw assets

**Files:**
- No additional local files.

**Interfaces:**
- Consumes: Clean committed branch from Task 4.
- Produces: Merged `main` paths that Velog can fetch anonymously.

- [ ] **Step 1: Push the feature branch**

Run: `git push -u origin agent/velog-meme-visual-refresh`

Expected: remote branch created successfully.

- [ ] **Step 2: Create and merge a focused pull request**

Use a pull request titled `Refresh Velog artwork with scene-driven memes`. The body must summarize the 27 new images, versioned paths, preserved v1 rollback set, and validation.

- [ ] **Step 3: Verify raw URLs**

Request all 27 URLs under:

`https://raw.githubusercontent.com/TaeHuiKKIM/TaeHuiKKIM/main/assets/velog/ai-github-series/v2/<post-id>/<file>.png`

Expected: every request returns HTTP 200 with `Content-Type: image/png`.

### Task 6: Update and verify all Velog private drafts

**Files:**
- No additional local files.

**Interfaces:**
- Consumes: Validated local Markdown and public GitHub raw URLs.
- Produces: Nine updated private Velog drafts.

- [ ] **Step 1: Open each existing draft by ID**

Use the nine recorded `/write?id=...` URLs. Do not create duplicate drafts.

- [ ] **Step 2: Replace editor content with validated Markdown**

Update one draft at a time, wait for the editor save indicator, and keep the publication state private.

- [ ] **Step 3: Reopen each draft**

Verify the title remains unchanged, the three `v2` image URLs are present, the approved technical diagram remains only where specified, and the draft has not been published.

- [ ] **Step 4: Finalize the browser session**

Close all task tabs and leave no Velog editor tab open.

### Task 7: Refresh three existing published-post thumbnails

**Files:**
- Create: `assets/velog/recent-post-thumbnails/v2/01-tool-call-to-sqlite.png`
- Create: `assets/velog/recent-post-thumbnails/v2/02-source-aware-rag.png`
- Create: `assets/velog/recent-post-thumbnails/v2/03-deterministic-financial-agent.png`

**Interfaces:**
- Consumes: The connected Velog profile order and recurring meme cast from the design spec.
- Produces: Three public thumbnail URLs and three updated published posts.

- [ ] **Step 1: Generate and inspect the three thumbnails**

Use scene-driven metaphors for the structured-output pipeline, source-aware RAG, and deterministic financial approval. Require the same no-text, no-logo, no-watermark constraints as the main series.

- [ ] **Step 2: Publish the assets**

Include the three files in the same focused GitHub pull request as the main v2 artwork.

- [ ] **Step 3: Replace the first image in each published post**

Keep titles, prose, tags, URLs, and publication state unchanged.

- [ ] **Step 4: Verify profile cards**

Reload `https://velog.io/@kt_gml/posts` and confirm the three post cards use the new scene thumbnails.
