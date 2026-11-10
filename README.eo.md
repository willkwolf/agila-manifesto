# Agila Manifesto

**Deliver quality software. / Liveri kvalitan programaron.**

> **Aviso pri derivaĵo**: Ĉi tiu dosiero estas la esperantlingva enkonduko al la deponejo. Ĉiuj klarigaj tekstoj estas derivitaj. La oficiala teksto de la manifesto troviĝas en `canon/AGILA-MANIFESTO.eo.md`, kaj okaze de iu ajn malkongruo, ambiguo aŭ dubo, la kanono en esperanto plene regas.

---

## 1. Deliver quality software

La **Agila Manifesto** (v3.1) estas internacia, malfermfonta sociteĥnika kadro por liveri kvalitan programaron en modernaj distribuitaj organizoj kaj kompleksaj adaptiĝantaj sistemoj.

Male al tradiciaj metodaroj, kiuj trudas ceremoniojn aŭ dogmajn praktikojn, la Agila Manifesto formaligas la strukturajn invariantojn, kiuj regas programaran arkitekturon, teamajn topologiojn kaj kunlaboran fluon. Ĝi ligas organizan dezajnon kaj sisteman arkitekturon laŭ la matematika realo de la leĝo de Conway kaj sistema teorio.

Ĉefaj trajtoj:
- **Vivanta Manifesto**: Kontinue evoluanta sub publika regado, malfermitaj kontraŭekzemploj kaj empiria observado.
- **Dudirekta Celgrupo**: Dezajnita ekde la unua tago por esti egale legebla kaj komprenebla de homaj teamoj kaj artefarit-inteligentaj agentoj.
- **Ununura Suverena Kanono en Esperanto**: Ankrumita en neŭtrala internacia lingvo (`canon/AGILA-MANIFESTO.eo.md`) por certigi egalan fundamenton liberan de kultura aŭ lingva hegemonio.
- **Homa Suvereneco**: Dum maŝinoj povas legi, analizi, citi kaj proponi strukturajn plibonigojn, nur homoj posedas la aŭtoritaton aprobi kaj evoluigi la kanonon.

---

## 2. Badges

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)](LICENSE)
[![Code License: MIT](https://img.shields.io/badge/Code_License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v3.1-blue.svg)](CHANGELOG.md)
[![CI Validation](https://github.com/willkwolf/agila-manifesto/actions/workflows/pr-validation.yml/badge.svg)](https://github.com/willkwolf/agila-manifesto/actions)
[![Languages](https://img.shields.io/badge/languages-3_available-informational.svg)](i18n/STATUS.md)

*Noto pri travideblo de insignoj*: Ĉiuj montritaj insignoj spegulas kontrolitajn deponejajn atributojn. Konforme al nia honesteca mandato, ĉi tiu deponejo malakceptas falsajn insignojn, aĉetitajn stelojn aŭ fabrikitajn subtenojn.

---

## 3. In 30 seconds

- **Sociteĥnikaj Fundamentoj**: Bazita sur sistema teorio, atendovicaj modeloj kaj la leĝo de Conway anstataŭ subjektivaj metodaroj.
- **Dudirekta Arkitekturo**: Kreita por homoj kaj AI-agentoj kun ununura neŭtrala kanona fonto en Esperanto kaj maŝinlegebla YAML.
- **Priskribaj, Nedogmaj Lensoj**: Analizaj diagnozaj iloj por taksi organizan kaj arkitekturan frikcion, neniam deviga kontrololisto aŭ atestila skemo.

---

## 4. The 10 Principles at a Glance

> **Deklaro pri Deveno de Conway**: 8 el 10 principoj (P01 ĝis P08) rekte deriviĝas de la leĝo de Conway (1968) aŭ de ĝiaj matematikaj kaj grafteoriaj korolarioj (komunika grafa homomorfio, kanala kapacito, preskaŭ-dekomponebleco, interfaca videblo, redundaj vojoj, atendovicoj ĉe transdonoj, struktura adaptiĝo kaj plurnoda grafa membreco). Ĉi tio estas deklarita kun plena travideblo kiel **dezajna tendenco**, ne neŝanĝebla fizika regulo. La principoj P09 (Komplekseco kaj Sondoj) kaj P10 (Sistemo en Uzo) devenas respektive de Kompleksaj Adaptiĝantaj Sistemoj / Epistemologio kaj la Leĝoj de Lehman pri Programara Evoluo.

| # | Principo | Teoria Bazo | Deveno de Conway? |
|---|----------|-------------|-------------------|
| [**P01**](docs/principles/p01.md) | Ĉiu sistemo spegulas la komunikan strukturon de siaj kreintoj | Teoremo / Modelo (Homomorfio de komunika grafo al modula grafo; inversa manovro) | **Jes** (Rekta leĝo de Conway) |
| [**P02**](docs/principles/p02.md) | Ĉiu decida unuo havas finian kapaciton | Modelo / Teoremo (Kanala kapacito de Shannon, limigita racieco de Simon, kvadrata grafa kresko) | **Jes** (Kogna ŝarĝo kaj skala korolario) |
| [**P03**](docs/principles/p03.md) | Stabilaj sistemoj estas fortaj ene kaj malfortaj trans la limoj | Modelo / Teoremo (Preskaŭ dekomponeblaj sistemoj de Simon, leĝo de Ashby pri necesa vario, paktoj) | **Jes** (Modulareco kaj lima pakto) |
| [**P04**](docs/principles/p04.md) | La efektiva interfaco estas ĉio observebla | Modelo / Empiria Tendenco (Observebla ekvivalenteco, leĝo de Hyrum) | **Jes** (Interfaca limo kaj implicita kuplo) |
| [**P05**](docs/principles/p05.md) | Fidindeco naskiĝas el redundo | Teoremo / Modelo (Von Neumann fidinda tuto el malpli fidindaj partoj, biologia degeneracio) | **Jes** (Grafa topologio kaj busa faktoro) |
| [**P06**](docs/principles/p06.md) | Fluon regas la atendo, ne la peno | Teoremo / Modelo (Leĝo de Little $L = \lambda W$, formulo de Kingman por atendovicoj) | **Jes** (Transdona frikcio inter teamaj limoj) |
| [**P07**](docs/principles/p07.md) | Lernanta sistemo ŝanĝas sian strukturon, ne nur siajn agojn | Modelo / Interpreto (Duobla buklo de Argyris & Schön, necesa vario de Ashby) | **Jes** (Inversa struktura realigo) |
| [**P08**](docs/principles/p08.md) | Ĉiu agento estas parto de la komunika strukturo | Modelo (Grafa teorio kun homaj kaj artefaritaj nodoj, limtransiro nur per paktoj) | **Jes** (Pluragenta grafa vastiĝo) |
| [**P09**](docs/principles/p09.md) | En komplekseco la kompreno sekvas la agon | Empiria Tendenco / Modelo (Neliniaj dinamikaj sistemoj, refutebleco de Popper, leĝo de Goodhart) | **Ne** (Komplekseca scienco kaj epistemologio) |
| [**P10**](docs/principles/p10.md) | Sistemo en uzo degradiĝas sen daŭra prizorgado | Empiria Tendenco (Leĝoj de Lehman pri softvara evoluo, malfermitaj termodinamikaj sistemoj) | **Ne** (Evolua dinamiko de Lehman) |

Por profundaj klarigoj, vidu [docs/conway-derivations.md](docs/conway-derivations.md) kaj la principajn dosierojn en [docs/principles/](docs/principles/).

---

## 5. Distinctions from the 2001 Agile Manifesto

La Agila Manifesto baziĝas sur la historia heredaĵo de la Agila Manifesto de 2001, kiu liberigis programaron de burokratio centrigante individuojn, funkciantan programaron, kunlaboron kaj respondemon al ŝanĝo.

Dum la lastaj 25 jaroj, la realo profunde evoluis:
1. **De Subjektivaj Valoroj al Strukturaj Invariantoj**: Dum la manifesto de 2001 esprimis preferojn ("valori X super Y"), la Agila Manifesto identigas formalajn sociteĥnikajn leĝojn (homomorfiojn, grafajn kapacitojn, atendovicojn).
2. **De Nurhomaj Teamoj al Homa-Agenta Ekosistemo**: AI-agentoj partoprenas la komunikadan grafon. Principo 8 formale integras ilin kun eksplicitaj paktoj kaj homa posedanto.
3. **De Procezaj Dogmoj al Diagnozaj Lensoj**: Ĝi provizas analizajn lensojn por diagnozi arkitekturan kaj organizan frikcion, sen krei atestilajn industriojn.
4. **Observeblaj Signaloj**: Ĉiu principo havas teorian bazon (`Bazo`) kaj observeblan simptomon (`Signalo`).

---

## 6. Status, Without Dogma, Minimal Formal Language, Why Esperanto

*(Derivita el la kanonaj deklaroj)*

### Statuso
La Agila Manifesto v3.1 estas malfermita, vivanta propono. Ĝi ne estas oficiala deviga normo, sed empiria kaj teoria bazo rafinata per publika observado kaj kontraŭekzemploj.

### Sen Dogmo
La manifesto malakceptas ĉian dogmon. Ĝiaj principoj **neniam** devas esti uzataj kiel:
- Devigaj obeo-kontrololistoj aŭ preskribaj ordonoj.
- Kriterioj por taksi aŭ rangi programistojn kaj teamojn.
- Komercaj atestiloj aŭ licencaj produktoj.

### Minimuma Formala Lingvo
Formalismoj (grafa teorio, informteorio de Shannon, leĝo de Little) estas uzataj nur kiam necese por forigi ambiguecon kaj certigi klaran difinon.

### Kial Esperanto?
Esperanto estas la sola kanona ankro (`canon/AGILA-MANIFESTO.eo.md`) pro tri kialoj:
1. **Lingva Neŭtraleco**: Ĝi apartenas egale al ĉiuj kontribuantoj tutmonde, sen geopolitika supereco.
2. **Struktura Reguleco**: Ĝia logika kaj aglutina morfologio donas stabilajn kaj precizajn terminojn.
3. **Intenca Konsento**: Ĝi postulas konscian kaj pripensitan konsenton por ĉiu kanona ŝanĝo.

---

## 7. For Humans

La manifesto helpas inĝenierojn, arkitektojn kaj gvidantojn diagnozi sisteman frikcion.

### Triparta Strukturo
Ĉiu principo enhavas:
1. **La Deklaron**: La universala sociteĥnika tendenco.
2. **La Bazon (`Bazo`)**: La matematika aŭ teoria klarigo.
3. **La Signalon (`Signalo`)**: La observebla simptomo de struktura misakordo.

Legu la kompletan homan gvidilon en [docs/guides/human-guide.md](docs/guides/human-guide.md).

---

## 8. For AI Agents

Agentoj kaj LLM-iloj estas partoprenantoj en la hodiaŭa kreado de programaro.

### Kiel Instali la Lertecon (Skill)
- **Claude Code**: Kopiu `skills/agila-manifesto-eo/` en `.claude/skills/agila-manifesto/`.
- **Aliaj Agentoj**: Uzu [AGENTS.md](AGENTS.md) kaj [llms.txt](llms.txt).
- **Strukturita Datumaro**: Uzu [canon/manifesto.eo.yaml](canon/manifesto.eo.yaml).

### Limoj de Agentoj
1. **Legi, Analizi, Citi, Proponi**: Agentoj rajtas analizi sistemojn kaj proponi plibonigojn.
2. **Nula Ŝanĝrajto**: Maŝinoj neniam modifas nek aprobas ŝanĝojn al la kanono.
3. **Homa Posedanto**: Ĉiu propono devas enhavi `Human-owner: @uzanto`.
4. **Lensoj, Ne Dogmo**: Agentoj neniam taksas homan laboron per poentaroj.

Vidu [docs/guides/agent-guide.md](docs/guides/agent-guide.md).

---

## 9. Governance

Tri-tavola regada modelo:

| Tavolo | Amplekso | Protekta Nivelo | Rajtigitaj Aktoroj | Aprobo | Diskut-tempo |
|---|---|---|---|---|---|
| **Tavolo 1: Fundamento** | `canon/` | **Alta ("Zelota")** | Nur homoj | $\ge 2$ homaj gardantoj | Min. 14 tagoj |
| **Tavolo 2: Tradukoj** | `skills/`, `i18n/` | **Meza** | Lingvaj mantenebluloj | Manteneblulo + 1 denaskulo | Normala PR |
| **Tavolo 3: Uzado** | `uzado/` | **Malalta (Malferma)** | Iu ajn kontribuanto | 1 kontrolanto | Rapida |

Vidu detalojn en [GOVERNANCE.md](GOVERNANCE.md).

---

## 10. Languages & Translation Drift

<!-- START_TRANSLATION_TABLE -->
| Lang | Language | Status | Canon Ver | Canon SHA-256 Match | Translators / Reviewers | Skill File |
|---|---|---|---|---|---|---|
| `eo` | Esperanto | `reviewed` | 3.1 | `44dd1dc96687` (Match) | canon, @willkwolf | [`skills/agila-manifesto-eo/SKILL.md`](skills/agila-manifesto-eo/SKILL.md) |
| `en` | English | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Draft), @willkwolf | [`skills/agila-manifesto-en/SKILL.md`](skills/agila-manifesto-en/SKILL.md) |
| `es` | Español | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Borrador), @willkwolf | [`skills/agila-manifesto-es/SKILL.md`](skills/agila-manifesto-es/SKILL.md) |
<!-- END_TRANSLATION_TABLE -->

Por aldoni lingvon, uzu la ŝablonon en `i18n/_template/` kaj vidu [i18n/STATUS.md](i18n/STATUS.md).

---

## 11. How to Contribute

Kvar ĉefaj vojoj:
1. **Proponi kanonan ŝanĝon**: Per la ŝablono de RFC en `.github/ISSUE_TEMPLATE/01_canon_propono.yml`.
2. **Kontraŭekzemplo**: *"Kontraŭekzemplo estas donaco."* Uzu `.github/ISSUE_TEMPLATE/02_kontrauekzemplo.yml`.
3. **Tradukoj**: Aldonu aŭ plibonigu tradukojn en `skills/`.
4. **Uzado**: Kunhavigu praktikajn ekzemplojn en `uzado/`.

Vidu [CONTRIBUTING.md](CONTRIBUTING.md) kaj [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## 12. Versioning, Citation & License

### Versiado
Publikigita sub Versio 3.1 (`v3.1.0`). Vidu [CHANGELOG.md](CHANGELOG.md).

### Citado
Vidu [CITATION.cff](CITATION.cff).

### Permesilo
- **Dokumentaro kaj Kanono**: [CC BY 4.0](LICENSE).
- **Kodo kaj Skriptoj**: [MIT](LICENSE).

---

## 13. FAQ

### Ĉu ĉi tio anstataŭas la Agilan Manifeston de 2001?
**Ne.** Ĝi estas sendependa evolua propono konstruita sur 25 jaroj da empiria kaj arkitektura progreso.

### Kial Esperanto?
Por certigi tutmondan lingvan neŭtralecon, regulan precizecon kaj intencan konsenton.

### Ĉu artefarit-inteligenta agento povas modifi la manifeston?
**Neniam.** Agentoj povas analizi kaj proponi, sed nur homoj aprobas ŝanĝojn al la kanono.

### Ĉu ni devas apliki ĉiujn dek principojn?
**Ne.** La principoj estas nedogmaj diagnozaj lensoj, ne deviga kontrololisto.
