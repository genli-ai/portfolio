# Claude 改动说明 — MicType iPhone 上架支持（2026-06-16）

为 MicType iPhone 版上 App Store（需公开的「支持 URL」+「隐私政策 URL」）做的两处改动。**纯前端/文案，未引入任何 iPhone 源码**（iPhone 仓库闭源、与本公开站隔离）。

## 改了什么
1. **新增隐私政策页** `public/mictype/privacy.html`（中英双语，自包含静态页）。
   - 上线后 URL = `https://genli-ai.github.io/portfolio/mictype/privacy.html`
   - 用途：App Store Connect 必填的「隐私政策 URL」。
   - 联系邮箱用了 `ligen.thu@gmail.com`（如想和 App 内「开发者」那行的 `gen.li@sternad.nyu.edu` 统一，改这一处即可）。

2. **软件页加 iPhone 版块** `src/pages/software.astro`（MicType hero 与 Features 之间）。
   - 介绍 iPhone 版（本地听写 + BYOK AI、一次买断不订阅、闭源、海外首发），含「即将上架 App Store」徽章 + 隐私政策链接。
   - App Store 链接现为占位（上架后把徽章换成真实 App Store 链接）。

## 验证
- `BASE=/portfolio npm run build` 通过（10 页）；`dist/mictype/privacy.html` 已生成、软件页含 iPhone 版块与隐私链接。

## 你要做的
- review 后 **commit + push**（GitHub Actions 自动构建部署），隐私政策页即上线。
- App 上架后：把软件页「即将上架 App Store」徽章换成真实 App Store 链接。

## 2026-07-06 — 隐私政策更新（MicType iOS 1.0.4 云端识别）
- `public/mictype/privacy.html`：新增可选「云端识别」披露（默认关、独立音频同意、发往用户自己配置的端点、失败回落本机）——修订 EN/CN 的「语音与转写」「AI 功能」两条 + meta description；生效日期 → 2026-07-06。与 MicType 仓库 `docs/releases/shared/privacy-policy-EN/CN.md` 逐句对应。
- `BASE=/portfolio npm run build` 通过（10 页）；push 后 GitHub Actions 自动部署。

- 2026-07-06 追加：隐私页改为**仅英文**（海外定位，用户要求）——移除简体中文半区。
