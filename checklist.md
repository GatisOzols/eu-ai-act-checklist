# EU AI Act Self-Audit Checklist

A 7-step audit for SaaS companies and AI product teams to map their product against Regulation (EU) 2024/1689 before the **2 August 2026** main application date.

Time to complete: 1 afternoon for a single-product SaaS. Longer for multi-product platforms.

Output: a written record of each AI feature, its risk classification, the obligations it triggers, and the disclosures or controls you've implemented. Keep it. That's your audit trail.

---

## Step 1 — Inventory every AI feature in your product

List every place where your product uses AI, machine learning, large language models, recommendation systems, or generative content. Don't just list the visible ones.

For each, write down:

- Feature name
- Where it lives (URL, screen, API endpoint)
- What model or service powers it (own model, OpenAI, Anthropic, Hugging Face, etc.)
- What input it takes from the user
- What output it produces
- Whether EU users interact with it
- Whether the output influences a decision about a person

Output template:

```
| Feature | Location | Model | Input | Output | EU users? | Decision impact? |
|---------|----------|-------|-------|--------|-----------|------------------|
| Resume scorer | /candidates/score | own ML | CV PDF | match score 0-100 | yes | yes — hiring |
| Support chatbot | help widget | gpt-4o | natural language | text reply | yes | no |
```

If you're not sure whether something counts as an AI system, check Article 3(1) of Regulation (EU) 2024/1689: "a machine-based system designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment and that, for explicit or implicit objectives, infers from the input it receives, how to generate outputs."

Heuristic: if it makes inferences from inputs to produce outputs (predictions, content, recommendations, decisions), it's likely an AI system.

---

## Step 2 — Determine territorial scope

For each feature from Step 1, answer:

- Is the provider (you) established in the EU? **Yes / No**
- Is the feature placed on the EU market or used by people located in the EU? **Yes / No**

If either answer is yes, the AI Act applies to that feature.

The relevant article is Article 2(1). "Established in the EU" means a legal entity or branch in any EU Member State. "Placed on the market" includes any product accessible online from the EU.

If you answered no to both: the EU AI Act does not apply to that feature. You may still have GDPR obligations.

---

## Step 3 — Check for prohibited practices (Article 5)

For each in-scope feature, check whether it does any of the following. If yes, you must stop using it. This is already in force (since 2 February 2025).

Prohibited practices under Article 5:

1. Subliminal techniques beyond a person's consciousness or purposefully manipulative techniques that materially distort behavior and cause significant harm.
2. Exploiting vulnerabilities of a specific group due to age, disability, or social or economic situation, with the same effect.
3. Social scoring by public authorities or on their behalf, leading to detrimental or unfavorable treatment.
4. Risk assessment of natural persons to predict the likelihood of committing a criminal offence based solely on profiling.
5. Untargeted scraping of facial images from the internet or CCTV to create or expand facial recognition databases.
6. Emotion recognition in the workplace or in education, except for medical or safety reasons.
7. Biometric categorisation systems that categorise people based on sensitive attributes (race, political opinions, trade union membership, religion, sexual orientation).
8. Real-time remote biometric identification in public spaces for law enforcement (with narrow exceptions).

Most B2B SaaS will tick no on every line. Verify anyway.

---

## Step 4 — Check for high-risk classification (Annex III)

For each in-scope, non-prohibited feature, check whether it falls into one of the 8 Annex III high-risk areas. The full list with sub-categories and examples is in [`annex-iii-categories.json`](./annex-iii-categories.json).

The 8 areas:

1. Biometric identification and categorisation
2. Critical infrastructure (water, gas, electricity, traffic management)
3. Education and vocational training (admissions, grading, monitoring)
4. Employment and worker management (CV screening, performance evaluation, task allocation, termination)
5. Access to essential public and private services (creditworthiness, public benefits, emergency services dispatch, health and life insurance)
6. Law enforcement
7. Migration, asylum, border control
8. Administration of justice and democratic processes

If any of your features fall into one of these, you're a high-risk provider for that feature, and the obligations in Step 6 apply. Common SaaS cases: resume screening, candidate ranking, employee performance scoring, credit scoring, insurance underwriting.

---

## Step 5 — Identify Article 50 transparency obligations

For each in-scope feature, check whether Article 50 applies. There are four categories:

| Article 50 category | Trigger | Required disclosure |
|---------------------|---------|---------------------|
| 50(1) — AI interacting with humans | Chatbots, voice assistants, AI customer support | Inform users they're interacting with an AI, in a clear and distinguishable way, at the start of the interaction. |
| 50(2) — Synthetic content generation | Image / audio / video / text generators | Mark the output in a machine-readable format (watermark, metadata) AND provide a visible label when the content is published. |
| 50(3) — Emotion recognition or biometric categorisation | Any product feature that infers emotional state or categorises a person by biometric features | Inform users they're being subjected to it. |
| 50(4) — Deepfakes | Content depicting real persons that has been generated or manipulated | Disclose as artificially generated or manipulated. Narrow artistic / satirical exception. |

Article 50 applies from 2 August 2026.

Document each disclosure you've implemented, where it appears in the UI, and a screenshot.

---

## Step 6 — High-risk obligations (only if Step 4 returned high-risk)

If any feature is high-risk under Annex III, you must implement the following before 2 August 2026:

- A risk management system (Article 9)
- Data and data governance (Article 10) — training, validation, and testing data must be relevant, representative, and free of errors to the extent feasible
- Technical documentation (Article 11) — kept up-to-date, listed in Annex IV
- Record-keeping (Article 12) — automatic logging of events during the AI system's lifecycle
- Transparency and provision of information to deployers (Article 13)
- Human oversight (Article 14) — measures enabling natural persons to oversee
- Accuracy, robustness, and cybersecurity (Article 15)
- Quality management system (Article 17)
- Conformity assessment (Article 43) before placing on market
- EU declaration of conformity (Article 47)
- CE marking (Article 48)
- Registration in the EU database for high-risk AI systems (Article 49 and Article 71)

This is heavy. If you operate a high-risk feature, plan for a conformity assessment process of 1-3 months and a formal technical file. Self-audit is not enough at this tier.

---

## Step 7 — Penalty exposure and final record

Once you've completed steps 1-6, calculate your worst-case penalty exposure under Article 99.

| Violation type | Maximum penalty |
|----------------|-----------------|
| Prohibited AI (Article 5) | €35,000,000 or 7% of total worldwide annual turnover, whichever is higher |
| High-risk or Article 50 violations | €15,000,000 or 3% of total worldwide annual turnover |
| Supplying incorrect or misleading information to authorities | €7,500,000 or 1% of total worldwide annual turnover |

SMEs (Article 99(6)) get proportional treatment, but the upper bound still applies and the lower bound is at the Member State's discretion.

**Output the final audit record.** A markdown file with one section per AI feature, each containing:

- The feature description (from Step 1)
- The territorial scope answer (Step 2)
- Confirmation of no prohibited practice (Step 3)
- Classification: prohibited / high-risk / Article 50 / minimal (Steps 4-5)
- Implemented obligations and links to where in your product they live (Steps 5-6)
- Worst-case penalty exposure (Step 7)
- Date and reviewer

Keep this. Update it when you add new AI features. This is your audit trail.

---

## What to do next

- If everything in your product is minimal risk: you're done with the AI Act. Re-audit every 6 months or after every major feature launch.
- If Article 50 applies: implement the disclosures from [`article-50-templates/`](./article-50-templates/) before 2 August 2026.
- If Annex III high-risk applies: budget 1-3 months for a formal conformity assessment process. Self-audit is necessary but not sufficient.
- If you want a productized 5-day audit with a deliverable PDF and refund guarantee: https://www.disclos.eu/audit
