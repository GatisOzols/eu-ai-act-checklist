# Article 50(4) — Deepfake disclosure

Use when: your product generates or manipulates image, audio, or video content that depicts a real, identifiable person and could be mistaken for an authentic recording.

Required: clear disclosure that the content has been artificially generated or manipulated.

Source: Regulation (EU) 2024/1689, Article 50(4)
Maintainer: Disclos team — https://www.disclos.eu

---

## The rule

Article 50(4): deployers of AI that generates or manipulates content constituting a deep fake shall disclose that the content has been artificially generated or manipulated.

A "deep fake" is defined in Article 3(60) as AI-generated or manipulated image, audio, or video content that resembles existing persons, objects, places, entities, or events and would falsely appear to a person to be authentic or truthful.

## Required visible disclosure

Place this label so it cannot be cropped, scrolled away, or hidden by autoplay:

```
This content has been artificially generated or manipulated.
```

For video: persistent watermark in a corner that survives common re-encoding.
For audio: spoken intro before the content begins.
For image: overlay text plus EXIF/XMP metadata.

## Required machine-readable marker

Use C2PA Content Credentials with the deepfake-specific action tag:

```json
{
  "claim_generator": "<your company> via <model name and version>",
  "assertions": [
    {
      "label": "c2pa.actions",
      "data": {
        "actions": [
          { "action": "c2pa.created" },
          { "action": "c2pa.ai_generated" },
          { "action": "c2pa.synthetic_media" }
        ]
      }
    }
  ]
}
```

If C2PA is not available in your stack, fall back to EXIF/XMP metadata with `AIGenerated: true`, `DeepfakeContent: true`, and `Subject: <depicted person if known>`.

## Exemption (narrow)

Article 50(4) second subparagraph: the obligation does not apply where the use is authorised by law to detect, prevent, investigate, or prosecute criminal offences.

A separate, narrower exception applies where the content is part of an evidently artistic, creative, satirical, fictional, or analogous work or programme. In that case, the disclosure obligation is limited to disclosure of the existence of generated or manipulated content "in an appropriate manner that does not hamper the display or enjoyment of the work."

These exceptions are narrow. Default to full disclosure.

## What this template does NOT cover

- Synthetic content that does NOT depict a real person — use the lighter `generated-content.md` template.
- Voice cloning of real persons — same rule as visual deepfakes, treat under Article 50(4).
- Real-time live deepfake video (filters, virtual avatars) — Article 50(4) still applies; the disclosure must appear at the start of the call or session.

## Implementation checklist

- [ ] Visible label is present and survives cropping / re-encoding
- [ ] Machine-readable marker is embedded (C2PA preferred, EXIF/XMP fallback)
- [ ] If the content is shared via your platform, the platform preserves the markers
- [ ] If the content is downloaded, the download includes the markers
- [ ] Internal policy documents who is authorised to use the deepfake feature and for what purposes

## Penalty exposure

Article 50(4) violations fall under Article 99(4): up to €15,000,000 or 3% of total worldwide annual turnover, whichever is higher.

For 24-language translations of the visible disclosure and a copy-paste deepfake disclosure block, use https://www.disclos.eu/tools/article-50-disclosure-generator
