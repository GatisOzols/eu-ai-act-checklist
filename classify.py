#!/usr/bin/env python3
"""
EU AI Act risk-tier classifier.

Asks five yes/no questions about an AI feature and prints the most likely
risk classification under Regulation (EU) 2024/1689.

Usage:
    python3 classify.py

Or, for batch use:
    python3 classify.py --feature "Resume scorer" --annex-iii 4 --decision-impact yes --eu-users yes --gen-content no --emotion-bio no

Notes:
- This is a self-audit aid, not legal advice.
- The classification follows the regulation text but does not consider every
  edge case (e.g. Article 6(3) narrow exceptions for high-risk areas).
- Verify against the full text on EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689
"""
import argparse
import sys


PROHIBITED_PRACTICES = [
    "Subliminal techniques or purposefully manipulative techniques causing significant harm (Art. 5(1)(a))",
    "Exploiting vulnerabilities of a specific group (age, disability, social or economic situation) causing significant harm (Art. 5(1)(b))",
    "Social scoring by public authorities or on their behalf, leading to detrimental treatment (Art. 5(1)(c))",
    "Risk assessment predicting commission of a criminal offence based solely on profiling (Art. 5(1)(d))",
    "Untargeted scraping of facial images from internet or CCTV to build facial recognition DBs (Art. 5(1)(e))",
    "Emotion recognition in the workplace or in education (Art. 5(1)(f), narrow medical/safety exception)",
    "Biometric categorisation based on sensitive attributes (race, politics, union membership, religion, sexual orientation) (Art. 5(1)(g))",
    "Real-time remote biometric identification in public spaces for law enforcement (Art. 5(1)(h), narrow exceptions)",
]


ANNEX_III_AREAS = [
    "1. Biometrics (remote identification, biometric categorisation on sensitive attributes, emotion recognition)",
    "2. Critical infrastructure (water, gas, electricity, traffic, digital infrastructure)",
    "3. Education and vocational training (admissions, grading, monitoring during tests)",
    "4. Employment, worker management, self-employment access (CV screening, performance, task allocation, termination)",
    "5. Access to essential public and private services (welfare eligibility, creditworthiness, insurance pricing, emergency dispatch)",
    "6. Law enforcement (risk of victimhood or offending, polygraph, evidence reliability, predictive policing by profiling)",
    "7. Migration, asylum, and border control (polygraph, risk assessments, visa/asylum applications, border face matching)",
    "8. Administration of justice and democratic processes (legal research aid for judges, election influence systems)",
]


def ask_yn(prompt: str) -> bool:
    while True:
        ans = input(f"{prompt} [y/n]: ").strip().lower()
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print("Please answer y or n.")


def classify(
    annex_iii_index: int,
    decision_impact: bool,
    eu_users: bool,
    gen_content: bool,
    emotion_bio: bool,
    prohibited: bool,
) -> str:
    if prohibited:
        return "PROHIBITED — STOP USING THIS FEATURE. Article 5 violations carry fines up to €35M or 7% of global turnover."
    if not eu_users:
        return "OUT OF SCOPE for the EU AI Act. No EU users means Article 2 does not apply. (You may still have GDPR or other obligations.)"
    if annex_iii_index in range(1, 9) and decision_impact:
        return (
            "HIGH-RISK under Annex III §"
            + str(annex_iii_index)
            + ". Article 6 obligations apply (risk management, technical documentation, record-keeping, human oversight, accuracy/robustness, conformity assessment, CE marking, EU database registration). "
            "Verify whether the Article 6(3) narrow exception applies before concluding."
        )
    if gen_content or emotion_bio:
        return (
            "LIMITED-RISK (Article 50 transparency). You must disclose to users that they are interacting with an AI system, "
            "mark AI-generated content in machine-readable form, disclose deepfakes, and inform users when emotion recognition or "
            "biometric categorisation is used. Applies from 2 August 2026."
        )
    return (
        "MINIMAL-RISK. No specific obligations under the EU AI Act beyond voluntary codes of conduct. Re-audit when the feature changes scope."
    )


def interactive() -> None:
    print("EU AI Act risk classifier — Disclos / eu-ai-act-checklist")
    print("Reference: Regulation (EU) 2024/1689")
    print()
    feature = input("Feature name (free text): ").strip() or "Untitled feature"

    print()
    print("Q1. Does this feature do ANY of the following practices prohibited under Article 5?")
    for p in PROHIBITED_PRACTICES:
        print(f"   - {p}")
    prohibited = ask_yn("Any of the above match this feature?")

    print()
    eu_users = ask_yn("Q2. Will users located in the EU interact with this feature OR will its output be used in the EU? (Article 2 territorial scope)")

    print()
    print("Q3. Does this feature fall into one of the Annex III high-risk areas?")
    for a in ANNEX_III_AREAS:
        print(f"   - {a}")
    annex_iii_idx_raw = input("Enter the matching area number (1-8), or 0 if none match: ").strip()
    try:
        annex_iii_index = int(annex_iii_idx_raw)
    except ValueError:
        annex_iii_index = 0

    decision_impact = False
    if annex_iii_index in range(1, 9):
        print()
        decision_impact = ask_yn("Q3a. Does this feature materially influence the decision-making outcome, or does it only do a narrow procedural / preparatory task? (Yes = materially influences, No = only narrow / preparatory)")

    print()
    gen_content = ask_yn("Q4. Does this feature interact with humans (chatbot/voice), generate synthetic content (text/image/audio/video), or generate deepfakes?")

    print()
    emotion_bio = ask_yn("Q5. Does this feature perform emotion recognition or biometric categorisation (outside the Article 5 prohibited list)?")

    print()
    print("=" * 70)
    print(f"FEATURE: {feature}")
    print("=" * 70)
    result = classify(
        annex_iii_index=annex_iii_index,
        decision_impact=decision_impact,
        eu_users=eu_users,
        gen_content=gen_content,
        emotion_bio=emotion_bio,
        prohibited=prohibited,
    )
    print(result)
    print()
    print("Save this output as part of your audit trail. See checklist.md step 7.")
    print()
    print("For a productized audit with a deliverable PDF: https://www.disclos.eu/audit")


def from_args(args: argparse.Namespace) -> int:
    feature = args.feature or "Unnamed"
    result = classify(
        annex_iii_index=args.annex_iii,
        decision_impact=args.decision_impact == "yes",
        eu_users=args.eu_users == "yes",
        gen_content=args.gen_content == "yes",
        emotion_bio=args.emotion_bio == "yes",
        prohibited=args.prohibited == "yes",
    )
    print(f"FEATURE: {feature}")
    print(result)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Classify an AI feature against the EU AI Act risk tiers."
    )
    parser.add_argument("--feature", help="Free-text feature name")
    parser.add_argument("--annex-iii", type=int, default=0, help="Annex III area 1-8 if applicable, 0 otherwise")
    parser.add_argument("--decision-impact", choices=["yes", "no"], default="no")
    parser.add_argument("--eu-users", choices=["yes", "no"], default="yes")
    parser.add_argument("--gen-content", choices=["yes", "no"], default="no")
    parser.add_argument("--emotion-bio", choices=["yes", "no"], default="no")
    parser.add_argument("--prohibited", choices=["yes", "no"], default="no")
    parser.add_argument("--batch", action="store_true", help="Run from CLI args instead of interactive prompts")
    args = parser.parse_args()

    if args.batch or args.feature:
        return from_args(args)
    interactive()
    return 0


if __name__ == "__main__":
    sys.exit(main())
