# Article 50(2) — Divulgation de contenu synthétique

À utiliser lorsque : votre produit génère du texte, des images, du son ou de la vidéo qui pourraient être confondus avec un contenu créé par un humain.

Obligation : marquage lisible par machine du contenu généré ET étiquette visible lorsque le contenu est publié ou partagé.

Source : Règlement (UE) 2024/1689, Article 50(2)
Mainteneur : équipe Disclos — https://www.disclos.eu

---

## Étiquette visible

Rattachez cette étiquette à chaque artefact publié (texte alternatif d'image, incrustation d'angle dans une vidéo, pied de page d'un document, introduction sonore d'un fichier audio).

```
Ce contenu a été généré par un système d'intelligence artificielle.
```

Les traductions de cette unique phrase dans les 24 langues officielles de l'UE se trouvent dans `translations.json` (dans ce dossier), ce qui vous permet de choisir la bonne version selon la langue de l'utilisateur.

## Marqueur lisible par machine — contenu textuel

Intégrez un manifeste C2PA (Content Credentials) si votre chaîne de production le permet. Pour les sorties Markdown ou HTML, ajoutez ce bloc de métadonnées en tête du fichier :

```yaml
---
content-type: AI-generated
ai-system-provider: <nom de votre entreprise>
ai-model: <nom et version du modèle, ex. gpt-4o-2024-08>
generated-at: <horodatage ISO 8601>
prompt-id: <identifiant opaque optionnel pour la traçabilité interne>
human-review: <yes | no | partial>
disclosure-uri: https://www.disclos.eu/tools/article-50-disclosure-generator
---
```

Pour une sortie en texte brut sans support YAML, ajoutez une ligne en fin de contenu :

```
[Généré par une IA — <nom de votre entreprise> via <modèle>. Date : <horodatage>.]
```

## Marqueur lisible par machine — image, audio, vidéo

Utilisez les Content Credentials C2PA. Implémentation de référence : https://github.com/contentauth/c2pa-rs

Champs minimaux du manifeste :
- `claim_generator` : nom de votre entreprise et du modèle
- `assertions[].label` : `c2pa.actions`
- `assertions[].data.actions[0].action` : `c2pa.created` (et `c2pa.ai_generated` si la version de votre manifeste le prévoit)
- `signature` : signature cryptographique avec la clé de votre fournisseur

Solution de repli si C2PA n'est pas disponible : intégrez des métadonnées EXIF ou XMP avec un champ `Generator` indiquant le nom du système d'IA et un drapeau `AIGenerated: true`.

## Exemptions

L'article 50(2) n'impose PAS de divulgation lorsque :
- L'IA est utilisée dans un processus d'édition standard qui ne modifie pas substantiellement l'entrée (dernière phrase de l'article 50(2)).
- Le contenu fait manifestement partie d'une œuvre artistique, créative, satirique, fictionnelle ou analogue (exception artistique de l'article 50(4), applicable aux hypertrucages ; le principe comparable oriente en pratique la divulgation du contenu synthétique).

Ces exceptions sont étroites. Par défaut, divulguez.

## Liste de vérification de mise en œuvre

- [ ] L'étiquette visible figure sur chaque artefact publié
- [ ] L'étiquette visible est dans la langue de l'utilisateur (voir `translations.json`)
- [ ] Le marqueur lisible par machine est intégré au moment de la génération et n'est pas supprimé par les traitements en aval
- [ ] La divulgation survit aux transformations courantes (redimensionnement, ré-encodage, copier-coller)
- [ ] La documentation du mécanisme de divulgation figure dans votre dossier technique (Article 11 / Annexe IV)

## Ce que ce modèle NE couvre PAS

- Les hypertrucages de personnes réelles — voir `deepfake.md` dans ce dossier. Les hypertrucages relèvent d'obligations supplémentaires au titre de l'article 50(4).
- La classification de contenu à haut risque — si le contenu généré nourrit une décision dans un domaine de l'Annexe III, la divulgation au titre de l'article 50 est nécessaire mais pas suffisante.

Pour les traductions de l'étiquette visible dans 24 langues, voir `translations.json` dans ce dossier, ou utilisez le générateur sur https://www.disclos.eu/tools/article-50-disclosure-generator
