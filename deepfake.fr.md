# Article 50(4) — Divulgation d'hypertrucage (deepfake)

À utiliser lorsque : votre produit génère ou manipule du contenu image, audio ou vidéo représentant une personne réelle et identifiable, et susceptible d'être pris pour un enregistrement authentique.

Obligation : divulgation claire indiquant que le contenu a été généré ou manipulé artificiellement.

Source : Règlement (UE) 2024/1689, Article 50(4)
Mainteneur : équipe Disclos — https://www.disclos.eu

---

## La règle

Article 50(4) : les déployeurs d'IA générant ou manipulant un contenu constituant un hypertrucage doivent indiquer que le contenu a été généré ou manipulé artificiellement.

Un « hypertrucage » est défini à l'article 3(60) comme un contenu image, audio ou vidéo généré ou manipulé par une IA, ressemblant à des personnes, objets, lieux, entités ou événements existants, et qui apparaîtrait à tort comme authentique ou véridique aux yeux d'une personne.

## Divulgation visible exigée

Placez cette mention de manière à ce qu'elle ne puisse pas être recadrée, faire l'objet d'un défilement qui l'efface, ni être masquée par une lecture automatique :

```
Ce contenu a été généré ou manipulé artificiellement.
```

Pour la vidéo : filigrane persistant dans un coin, capable de résister aux ré-encodages courants.
Pour l'audio : introduction parlée avant le contenu.
Pour l'image : texte en surimpression et métadonnées EXIF/XMP.

## Marqueur lisible par machine exigé

Utilisez les Content Credentials C2PA avec l'action spécifique aux hypertrucages :

```json
{
  "claim_generator": "<votre entreprise> via <nom et version du modèle>",
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

Si C2PA n'est pas disponible dans votre stack, repliez-vous sur des métadonnées EXIF/XMP avec `AIGenerated: true`, `DeepfakeContent: true`, et `Subject: <personne représentée si connue>`.

## Exemption (étroite)

Deuxième alinéa de l'article 50(4) : l'obligation ne s'applique pas lorsque l'utilisation est autorisée par la loi pour détecter, prévenir, enquêter ou poursuivre des infractions pénales.

Une autre exception, plus étroite, s'applique lorsque le contenu fait manifestement partie d'une œuvre ou d'un programme artistique, créatif, satirique, fictionnel ou analogue. Dans ce cas, l'obligation de divulgation se limite à signaler l'existence d'un contenu généré ou manipulé « d'une manière appropriée qui n'entrave pas l'affichage ou la jouissance de l'œuvre ».

Ces exceptions sont étroites. Par défaut, divulguez intégralement.

## Ce que ce modèle NE couvre PAS

- Le contenu synthétique qui NE représente PAS une personne réelle — utilisez le modèle plus léger `generated-content.md`.
- Le clonage vocal de personnes réelles — même règle que pour les hypertrucages visuels, à traiter au titre de l'article 50(4).
- Les hypertrucages vidéo en direct (filtres, avatars virtuels) — l'article 50(4) s'applique également ; la divulgation doit apparaître au début de l'appel ou de la session.

## Liste de vérification de mise en œuvre

- [ ] L'étiquette visible est présente et résiste au recadrage / ré-encodage
- [ ] Le marqueur lisible par machine est intégré (C2PA de préférence, EXIF/XMP en repli)
- [ ] Si le contenu est partagé via votre plateforme, celle-ci préserve les marqueurs
- [ ] Si le contenu est téléchargé, le fichier téléchargé contient les marqueurs
- [ ] Une politique interne précise qui est autorisé à utiliser la fonctionnalité d'hypertrucage et à quelles fins

## Exposition aux sanctions

Les violations de l'article 50(4) relèvent de l'article 99(4) : jusqu'à 15 000 000 € ou 3 % du chiffre d'affaires annuel mondial total, le montant le plus élevé étant retenu.

Pour les traductions de la divulgation visible dans 24 langues et un bloc de divulgation d'hypertrucage prêt à copier-coller, utilisez https://www.disclos.eu/tools/article-50-disclosure-generator
