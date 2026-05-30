# Article 50(3) — Divulgation de reconnaissance des émotions et de catégorisation biométrique

À utiliser lorsque : votre produit utilise l'IA pour déduire l'état émotionnel d'une personne OU pour catégoriser une personne sur la base de données biométriques (visage, voix, démarche, etc.).

Obligation : informer les personnes physiques exposées au système qu'elles y sont soumises.

Source : Règlement (UE) 2024/1689, Article 50(3)
Mainteneur : équipe Disclos — https://www.disclos.eu

---

## La règle

Article 50(3) : les déployeurs de systèmes de reconnaissance des émotions ou de catégorisation biométrique informent les personnes physiques exposées au fonctionnement du système de ce fait.

Le traitement des données personnelles doit respecter le RGPD (Règlement (UE) 2016/679), la directive RGPD pour les services répressifs (Directive (UE) 2016/680) et le Règlement (UE) 2018/1725, selon le cas applicable.

## Vérifiez d'abord les interdictions de l'article 5

Les pratiques suivantes sont INTERDITES par l'article 5(1) et ne peuvent pas être sauvées par une simple divulgation :

- Reconnaissance des émotions sur le lieu de travail ou dans l'éducation (Article 5(1)(f)), sauf exceptions médicales ou de sécurité limitées.
- Catégorisation biométrique fondée sur la race, les opinions politiques, l'appartenance syndicale, la religion ou les convictions philosophiques, la vie sexuelle ou l'orientation sexuelle (Article 5(1)(g)).

Si votre cas d'usage relève de l'un de ces interdits, la divulgation ne vous protège pas. Arrêtez d'utiliser la fonctionnalité.

## Divulgation visible exigée

À placer au début de l'interaction :

```
Ce service utilise l'IA pour analyser [signaux émotionnels | caractéristiques biométriques | profils vocaux | expressions faciales] afin de [finalité : ex. détecter l'insatisfaction client, recommander du contenu, vérifier l'identité]. L'analyse est effectuée automatiquement. Vous pouvez vous y opposer via [méthode d'opt-out].
```

Adaptez les éléments entre crochets à votre usage spécifique. Ne dissimulez pas cette mention dans un sous-menu « Paramètres de confidentialité » : elle doit être présentée au point d'interaction.

## Divulgation lisible par machine exigée

Lorsque l'analyse s'exécute côté serveur ou via une API, ajoutez un en-tête de réponse :

```
X-AI-Analysis: emotion-recognition; purpose=customer-service-quality; consent-id=<identifiant opaque>
```

Lorsque l'analyse s'exécute côté client (navigateur, application mobile), exposez dans l'interface un indicateur signalant que l'analyse est active pendant la session.

## Données de catégorie particulière au sens de l'article 9 du RGPD

Les données biométriques utilisées pour l'identification unique d'une personne constituent des données de catégorie particulière au sens de l'article 9 du RGPD. Vous avez besoin d'une base juridique au titre de l'article 9 (consentement explicite dans la plupart des cas B2C) en plus de la base juridique au titre de l'article 6. La divulgation au titre de l'AI Act ne remplace pas l'exigence de consentement RGPD.

## Liste de vérification de mise en œuvre

- [ ] Confirmé que l'usage n'est pas interdit par l'article 5(1)(f) ou 5(1)(g)
- [ ] La divulgation visible apparaît au début de l'interaction, pas enterrée dans les paramètres
- [ ] L'utilisateur peut s'opposer (et l'opt-out est réellement respecté en aval)
- [ ] La base juridique RGPD article 9 est documentée (consentement explicite pour les données biométriques)
- [ ] Minimisation des données : ne collecter que ce qui est nécessaire à la finalité déclarée
- [ ] La durée de conservation est documentée et appliquée
- [ ] Une politique interne précise qui peut accéder aux catégories inférées

## Exposition aux sanctions

Violations des interdictions de l'article 5 : jusqu'à 35 000 000 € ou 7 % du chiffre d'affaires annuel mondial total.
Violations de l'article 50(3) : jusqu'à 15 000 000 € ou 3 % du chiffre d'affaires annuel mondial total.
Plus les sanctions RGPD éventuelles.

## Ce que ce modèle NE couvre PAS

- Les polygraphes et outils similaires utilisés par les services répressifs, en matière migratoire ou aux frontières — ces usages relèvent du haut risque au titre de l'Annexe III, et non du risque limité de l'article 50.
- La vérification biométrique (correspondance un-à-un, ex. déverrouillage par empreinte digitale) — généralement hors du champ de l'article 50(3) car elle ne « catégorise » pas l'utilisateur, mais vérifiez les définitions de l'article 3 pour les cas limites.

Pour les traductions de la divulgation visible dans 24 langues, utilisez https://www.disclos.eu/tools/article-50-disclosure-generator
