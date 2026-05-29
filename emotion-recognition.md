# Article 50(3) — Emotion recognition and biometric categorisation disclosure

Use when: your product uses AI to infer emotional state from a person OR categorises a person based on biometric data (face, voice, gait, etc.).

Required: inform the natural persons subjected to the system that they are being subjected to it.

Source: Regulation (EU) 2024/1689, Article 50(3)
Maintainer: Disclos team — https://www.disclos.eu

---

## The rule

Article 50(3): deployers of emotion recognition or biometric categorisation systems shall inform the natural persons exposed to the operation of the system of that fact.

Personal data processing must comply with GDPR (Regulation (EU) 2016/679), GDPR for law enforcement (Directive (EU) 2016/680), and Regulation (EU) 2018/1725, as applicable.

## Check Article 5 prohibitions first

The following are PROHIBITED under Article 5(1), not allowed with disclosure:

- Emotion recognition in the workplace or in education (Article 5(1)(f)), with limited medical or safety exceptions.
- Biometric categorisation based on race, political opinions, trade union membership, religion or philosophical beliefs, sex life, or sexual orientation (Article 5(1)(g)).

If your use case falls into one of these, disclosure does not save you. Stop using the feature.

## Required visible disclosure

Place this at the start of the interaction:

```
This service uses AI to analyse [emotional cues | biometric characteristics | voice patterns | facial expressions] in order to [purpose: e.g. detect customer dissatisfaction, recommend content, verify identity]. The analysis is performed automatically. You can opt out by [opt-out method].
```

Customise the bracketed terms to your specific use. Do not hide this in a "Privacy Settings" submenu — it must be presented at the point of interaction.

## Required machine-readable disclosure

Where the analysis runs server-side or as an API, include a response header:

```
X-AI-Analysis: emotion-recognition; purpose=customer-service-quality; consent-id=<opaque id>
```

Where the analysis runs in the client (browser, mobile app), expose an in-app indicator that the analysis is active during the session.

## GDPR Article 9 special-category data

Biometric data used for unique identification is special-category personal data under GDPR Article 9. You need an Article 9 legal basis (explicit consent in most B2C cases) in addition to the Article 6 legal basis. The EU AI Act disclosure does not replace the GDPR consent requirement.

## Implementation checklist

- [ ] Confirmed the use is not prohibited under Article 5(1)(f) or 5(1)(g)
- [ ] Visible disclosure is shown at the start of the interaction, not buried in settings
- [ ] User can opt out (and the opt-out is actually honored downstream)
- [ ] GDPR Article 9 legal basis is documented (explicit consent for biometrics)
- [ ] Data minimisation: only collect what's needed for the stated purpose
- [ ] Retention period is documented and enforced
- [ ] Internal policy records who can access the inferred categories

## Penalty exposure

Article 5 prohibition violations: up to €35,000,000 or 7% of total worldwide annual turnover.
Article 50(3) violations: up to €15,000,000 or 3% of total worldwide annual turnover.
Plus GDPR fines if applicable.

## What this template does NOT cover

- Polygraph and similar tools used in law enforcement, migration, or border control — those are high-risk under Annex III, not just limited-risk under Article 50.
- Biometric verification (one-to-one matching, e.g. unlock by fingerprint) — usually not in scope for Article 50(3) because it does not "categorise" the user, but check Article 3 definitions for edge cases.

For 24-language translations of the visible disclosure, use https://www.disclos.eu/tools/article-50-disclosure-generator
