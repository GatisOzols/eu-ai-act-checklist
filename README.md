# eu-ai-act-checklist

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/GatisOzols/eu-ai-act-checklist?style=social)](https://github.com/GatisOzols/eu-ai-act-checklist/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/GatisOzols/eu-ai-act-checklist)](https://github.com/GatisOzols/eu-ai-act-checklist/commits/main)
[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-Regulation%202024%2F1689-blue)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689)
[![Article 50](https://img.shields.io/badge/Article%2050-2%20Aug%202026-red)](https://artificialintelligenceact.eu/article/50/)
[![Annex III](https://img.shields.io/badge/Annex%20III-2%20Dec%202027-orange)](https://artificialintelligenceact.eu/annex/3/)
[![Annex I](https://img.shields.io/badge/Annex%20I-2%20Aug%202028-yellow)](https://artificialintelligenceact.eu/annex/1/)

A practical, open-source compliance checklist for the EU AI Act (Regulation (EU) 2024/1689), built for SaaS founders and AI product teams.

After the **AI Omnibus** (political agreement 7 May 2026, adopted 19 November 2025), the Act has three independent application dates for SaaS:

- **2 August 2026** — Article 50 transparency obligations, GPAI provider obligations under Chapter V, governance framework under Chapter VII.
- **2 December 2027** — Annex III high-risk obligations (biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice). Moved from the original 2 August 2026.
- **2 August 2028** — Annex I high-risk obligations (AI as a safety component of products covered by Union harmonisation legislation: Machinery, MDR, IVDR, lifts, toys, RED). Moved from the original 2 August 2027.

This repo is designed so a developer can run through it in one afternoon and produce a defensible self-audit trail for each wave that applies to their product.

## What's in this repo

- [`checklist.md`](./checklist.md) — the 7-step self-audit. Plain English, article references, copy-paste friendly.
- [`annex-iii-categories.json`](./annex-iii-categories.json) — machine-readable list of the 8 high-risk categories from Annex III with sub-categories and examples.
- [`classify.py`](./classify.py) — a tiny decision-tree script. Answer 5 questions about your AI feature, get back: prohibited / high-risk / limited-risk (Article 50) / minimal-risk.
- [`penalty-bands.json`](./penalty-bands.json) — the three Article 99 penalty tiers as data.
- Article 50 disclosure templates, copy-paste, English:
  - [`chatbot.html`](./chatbot.html) — Article 50(1), AI interaction disclosure for chatbots and voice assistants.
  - [`generated-content.md`](./generated-content.md) — Article 50(2), synthetic content disclosure.
  - [`deepfake.md`](./deepfake.md) — Article 50(4), deepfake disclosure.
  - [`emotion-recognition.md`](./emotion-recognition.md) — Article 50(3), emotion recognition and biometric categorisation disclosure.
  - [`translations.json`](./translations.json) — the disclosure labels translated to 6 EU languages.

## How this compares to other EU AI Act tools

| | This repo | Holistic AI | Credo AI | IBM watsonx.governance |
|---|---|---|---|---|
| Price | Free, MIT | Enterprise SaaS | Enterprise SaaS | Enterprise SaaS |
| Setup time | One afternoon | Sales call required | Sales call required | Sales call required |
| Article 50 templates | Yes, copy-paste | Generated via tool | Generated via tool | Generated via tool |
| Annex III triage | JSON + Python script | Yes | Yes | Yes |
| Self-hostable | Yes | No | No | Partial |
| Built for | Founders, small SaaS teams | Enterprises | Enterprises | Enterprises |

This repo will not replace an enterprise GRC platform if you have a 50-person compliance team. It is built for the SaaS founder who has 65 days, no compliance budget, and needs a defensible self-audit trail.

## How to use it

1. Read [`checklist.md`](./checklist.md) start to finish (15 minutes).
2. Run `python3 classify.py` for each AI feature in your product. Save the output.
3. Open [`annex-iii-categories.json`](./annex-iii-categories.json) and check whether any of your features map to a high-risk category.
4. Open the Article 50 template files (`chatbot.html`, `generated-content.md`, `deepfake.md`, `emotion-recognition.md`) and pick the templates that apply to your product. Paste them into your UI.
5. Keep a copy of all the outputs in a folder named `eu-ai-act-audit-YYYY-MM-DD/`. That's your self-audit trail.

## What this repo is not

- Not legal advice. The text is factual and references the regulation directly, but a self-audit is not a substitute for a formal compliance assessment if you operate in a high-risk category under Annex III.
- Not exhaustive. Article 50 transparency obligations are covered. High-risk conformity assessments under Annex III are summarized but not templated — they require a formal technical file.
- Not auto-updating. The EU AI Office may issue clarifying guidelines after the entry-into-application date. Check the official portal (https://artificialintelligenceact.eu) periodically.

## When you need more than self-audit

For SaaS companies that want a productized audit with a deliverable PDF, Loom walkthrough, and refund guarantee, [Disclos](https://www.disclos.eu) maintains this repo and offers a €997 5-business-day audit. The repo will always stay free under MIT.

Free tools (no signup):
- [Annex III high-risk triage](https://www.disclos.eu/tools/annex-iii-triage)
- [Article 50 disclosure generator (24 EU languages)](https://www.disclos.eu/tools/article-50-disclosure-generator)
- [EU AI Act penalty calculator](https://www.disclos.eu/tools/penalty-calculator)

## Contributing

Pull requests welcome. Especially:
- Translations of the Article 50 templates into other EU languages.
- Corrections to the Annex III mapping as the EU AI Office publishes clarifying guidelines.
- Real-world examples of how teams classified edge-case features (anonymized).

Open an issue first for substantial changes so we can discuss scope.

## License

MIT. Use freely in commercial and open-source projects.

## References

- Regulation (EU) 2024/1689 (the EU AI Act): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689
- AI Act Explorer (consolidated text + article search): https://artificialintelligenceact.eu
- EU AI Office: https://digital-strategy.ec.europa.eu/en/policies/ai-office
- Disclos guide: https://www.disclos.eu/eu-ai-act
