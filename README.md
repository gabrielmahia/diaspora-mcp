# diaspora-mcp
<!-- mcp-name: io.github.gabrielmahia/diaspora-mcp -->

[![diaspora-mcp Glama score](https://glama.ai/mcp/servers/gabrielmahia/diaspora-mcp/badges/score.svg)](https://glama.ai/mcp/servers/gabrielmahia/diaspora-mcp)
[![smithery badge](https://smithery.ai/badge/@gabrielmahia/diaspora-mcp)](https://smithery.ai/server/@gabrielmahia/diaspora-mcp)


---
**Compatible with `claude-sonnet-5`** (released 2026-06-30) — Anthropic's most agentic
Sonnet yet. Runs multi-step tool chains end-to-end without stopping short.
Install: `pip install diaspora-mcp` · Use with any MCP client.

---


> Kenya diaspora services via MCP — immigration, dual citizenship, diaspora taxes, homeland investment, community resources.

[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?logo=pypi)](https://pypi.org/project/diaspora-mcp/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/gabrielmahia/diaspora-mcp)

## Install

```bash
pip install diaspora-mcp
```

## What This Covers

This is distinct from `remit-mcp` (which covers remittance corridors and transfer rates). diaspora-mcp covers the full lifecycle of being Kenyan abroad:

| Tool | Function |
|------|----------|
| `dual_citizenship_guide` | Kenya dual citizenship — eligibility, process, rights retained |
| `diaspora_tax_guide` | Tax obligations in USA/UK/CA + Kenya cross-border tax guidance |
| `kenya_homeland_investment` | Investment options for diaspora: M-Akiba, NSE, REITs, unit trusts |
| `diaspora_verification` | Document authentication — apostille, foreign certificates for Kenya use |
| `diaspora_community_guide` | Kenya diaspora organisations by country |
| `immigration_status_guide` | Immigration status guidance: H-1B, green card, ILR, citizenship paths |

## Context

Kenya diaspora remitted **$4.1B** in 2024. The infrastructure for diaspora Kenyans to navigate immigration, taxes, and homeland investment has historically required expensive lawyers or simply didn't exist.

→ [The Nairobi Stack](https://gabrielmahia.github.io/nairobi-stack)

## Related MCPs

- `remit-mcp` — remittance corridor rates and transfer
- `faida-mcp` — Kenya capital markets and investment detail
- `familia-mcp` — inheritance, wills, diaspora property

## License

MIT © Gabriel Mahia | contact@aikungfu.dev

## Part of the East Africa Coordination Stack

This MCP server is one of 32 tools in the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All 32 servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Demo data is labeled DEMO and is not suitable for operational decisions. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).
