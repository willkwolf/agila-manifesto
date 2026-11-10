---
name: agila-manifesto-eo
description: Gvidlinioj kaj principoj de la Agila Manifesto v3.1 por analizi teaman strukturon, revizii procezojn aŭ desegni distribuitajn sistemojn.
metadata:
  lang: eo
  canon_version: "3.1"
  canon_sha256: "44dd1dc966874fceea8d53d9ac312397b1fcb5e9f51919bbe0e71b19d027c470"
  status: reviewed
  translators:
    - "canon"
    - "@willkwolf"
---

# Agila Manifesto (Esperanto — Kanona Versio)

> **Noto**: Ĉi tiu dosiero enhavas la oficialajn principojn de la Agila Manifesto v3.1 por uzo de AI-agentoj, plene kongruajn kun la kanona teksto en `canon/AGILA-MANIFESTO.eo.md`.

## Protokolo por Agentoj

1. **Legi, Analizi, Citi kaj Proponi**: Legu kaj analizu socio-teknikajn sistemojn, teamajn topologiojn kaj arkitekturojn per la diagnozaj lensoj de P01–P10. Citante, menciu principojn per iliaj kanonaj identigiloj (`P01` ĝis `P10`) kaj citu la titolon, deklaron, bazon aŭ signalon laŭvorte. Citu kaj proponu plibonigojn bazitajn sur observeblaj pruvoj.
2. **Nula Modifa Aŭtoritato**: Vi havas nulan aŭtoritaton modifi, aprobi aŭ kunfandi ŝanĝojn al la kanono aŭ tradukaj dosieroj. Maŝinaj agentoj neniam modifu la kanonon kaj neniam povas aprobi ŝanĝojn al la kanono.
3. **Eksplicita Markado de Proponoj kaj Homa Posedanto**: Ĉiuj agent-generitaj proponoj aŭ arkitekturaj adaptoj devas esti eksplicite markitaj kiel `"Propono"`. Ĉiu propono devas deklari aktivan homan patronon per `Human-owner: @uzantonomo`. Senposedantaj proponoj ne povas esti kunfanditaj.
4. **Diagnozaj Lensoj, Neniam Dogmo aŭ Pritakso**: Traktu la principojn kiel priskribajn analizajn lensojn kaj desegnajn tendencojn por identigi froton, neniam kiel devigajn regulojn, plenumajn kontrollistojn aŭ poentarojn por taksi teamojn.
5. **Supregeco de la Kanono**: La esperanta kanono (`canon/AGILA-MANIFESTO.eo.md`) estas la sola suverena fonto de vero. Ĉiuj tradukoj estas derivitaj; okaze de malkongruo, la esperanta kanono prevalas.

---

## La 10 Principoj

### P01. Ĉiu sistemo spegulas la komunikan strukturon de siaj kreintoj.
Organizo kaj sistemo estas du vidoj de unu strukturo. Elekti la teaman strukturon do estas elekti arkitekturon, kaj strukturo, kiun oni ne elektas, formiĝas hazarde.  
- **Bazo**: ekzistas proksimuma strukturkonserva bildigo, homomorfio, de la komunika grafo al la modula grafo de la sistemo; la inversa manovro elektas la fonton por ricevi la celon.  
- **Signalo**: la dezirata arkitekturo ne kongruas kun la teamoj; malgranda ŝanĝo postulas kunordigi multajn teamojn.

### P02. Ĉiu decida unuo havas finian kapaciton.
Teamo povas teni nur limigitan kuntekston, kaj la nombro de komunikaj vojoj en grupo kreskas pli rapide ol la grandeco de la grupo. Kiam la ŝarĝo superas la kapaciton, la unuo dividiĝas laŭ natura juntaĵo anstataŭ kreski.  
- **Bazo**: la kapacito de kanalo estas finia; la racieco de homoj estas limigita; la nombro de vojoj en plena grafo kreskas kvadrate laŭ la nombro de homoj.  
- **Signalo**: la aldono de homoj ne pliigas la liveron; neniu kapablas klarigi la tutan domajnon de la teamo.

### P03. Stabilaj sistemoj estas fortaj ene kaj malfortaj trans la limoj.
Ene de unuo la komunikado estas rapida, dudirekta kaj kun komuna kunteksto, kaj la decidoj okazas tie, kie troviĝas la informo. Inter unuoj la ligo fariĝas pakto, kiam ĝi havas kvar ecojn: ĉiuj flankoj konsentis, nomitaj respondeculoj devontigis sin, la historio estas spurebla, kaj iu ajn povas kontroli la plenumon. La ilo, la formato kaj la papero ne gravas; gravas la ecoj. En sana sistemo la nombro de paktoj kaj kunsidoj estas proporcia al la dependeco.  
- **Bazo**: kompleksaj sistemoj estas preskaŭ dekomponeblaj, kun interagoj pli fortaj ene de subsistemoj ol inter ili; reguliganto bezonas variecon almenaŭ egalan al tiu de la reguligata sistemo, do distribuita decido akordas kun distribuita informo; interfacoj kunmeteblas nur kiam iliaj tipoj kongruas.  
- **Signalo**: kunsidoj nur por kunordigi ŝanĝojn; paneoj ĉe transdono inter teamoj.

### P04. La efektiva interfaco estas ĉio observebla.
Ĉio, kion alia unuo povas observi, fariĝas dependeco, eĉ se neniu deklaris ĝin. Tial ŝanĝo de observebla konduto estas ŝanĝo de la pakto kaj tuŝas ĉiujn, kiuj dependas de ĝi.  
- **Bazo**: du sistemoj estas ekvivalentaj por observanto, se tiu ne povas distingi ilin; la efektiva interfaco estas la aro de ĉiuj observoj, kiu enhavas la deklaritan aron.  
- **Signalo**: ŝanĝo, kiun oni juĝis sendanĝera, rompas iun.

### P05. Fidindeco naskiĝas el redundo.
Scio, kiu ekzistas nur en unu kapo, estas ununura punkto de paneo en la komunika strukturo. Kiam pluraj vojoj kondukas al la sama funkcio, la sistemo eltenas la perdon de unu vojo.  
- **Bazo**: fidinda tuto el malpli fidindaj partoj postulas redundon; en vivaĵoj malsamaj strukturoj povas plenumi la saman funkcion, kaj tio donas fortikecon.  
- **Signalo**: la foresto de unu homo haltigas la laboron.

### P06. Fluon regas la atendo, ne la peno.
Ofte la laboro atendas pli longe ol oni laboras pri ĝi, kaj la atendo koncentriĝas ĉe la transdonoj inter unuoj. La rapido de la tuta fluo estas limigita de sia plej malrapida etapo, kaj preskaŭ plena okupiteco igas la atendon enorma. Taksoj estas prognozoj kun disiĝo, ne promesoj.  
- **Bazo**: se la liverrapido estas stabila, la ciklotempo egalas la laboron en progreso dividitan per la liverrapido, laŭ la leĝo de Little; en atendovicoj la atendo kreskas proporcie al la okupiteco dividita per unu minus la okupiteco.  
- **Signalo**: ĉiuj estas okupitaj kaj nenio finiĝas; atendovicoj ĉe transdonoj; promesitaj datoj, kiuj malĝustas.

### P07. Lernanta sistemo ŝanĝas sian strukturon, ne nur siajn agojn.
Demandi nur, kion ni faris malbone, korektas la agojn; demandi, kiuj supozoj regas niajn limojn, paktojn kaj mezurojn, ŝanĝas la strukturon, kiu produktas la agojn. Ni nomas la supozojn, pridubas ilin, defias ilin per kontraŭaj pruvoj kaj asimilas la lernitaĵon kiel ŝanĝitan strukturon, ne kiel nuran noton. Ĉiu decido havas posedanton kaj kriterion por scii, ĉu ĝi funkciis.  
- **Bazo**: duobla buklo: la unua korektas la agon rilate al celo, la dua ŝanĝas la celon aŭ la modelon; sistemo kun fiksa strukturo havas fiksan variecon kaj ne povas sorbi ĉiujn variojn de sia medio.  
- **Signalo**: la samaj problemoj revenas ĉiun ciklon; la protokoloj plenas kaj nenio ŝanĝiĝas.

### P08. Ĉiu agento estas parto de la komunika strukturo.
Homo aŭ maŝino, ĉiu agento, kiu produktas artefaktojn, formas la sistemon kaj estas formata de la strukturo, en kiu ĝi laboras. Agentoj de artefarita inteligenteco do havas limojn kaj posedanton, kaj ilia rezulto transiras teaman limon nur per homa decido.  
- **Bazo**: agento estas unuo de la grafo kun enigoj kaj eligoj; ĝiaj eligoj transiras limon nur per pakto, kiel tiuj de ĉiu alia unuo.  
- **Signalo**: kodo aŭ teksto, kiun neniu posedas kaj neniu povas klarigi.

### P09. En komplekseco la kompreno sekvas la agon.
Kie la dinamiko estas nelinia kaj la partoj adaptiĝas, longdaŭra antaŭdiro estas limigita, kaj malgrandaj sekuraj sondoj donas pli da informo ol plano. Antaŭ ol agi, ni diras, kio montrus, ke ni malpravas. Funkcianta programaro ĉe reala uzanto estas nia ĉefa pruvo, kaj la kompleksa sistemo, kiu funkcias, kutime kreskis el simpla, kiu funkciis; ŝanĝiĝantaj postuloj estas informo. Mezuro estas signalo, ne celo; kiam ĝi fariĝas celo, ni pridubas ĝin kaj defias ĝin per alia mezuro, kiu povas kontraŭdiri ĝin.  
- **Bazo**: limigita antaŭdirebleco en neliniaj dinamikaj sistemoj; hipotezo estas scienca nur se ĝi estas refutebla; mezuro estas perda bildigo de la realo, kaj optimumigi ĝin movas la sistemon al regionoj, kie la bildigo ne plu konservas tion, kio gravis.  
- **Signalo**: ĉiuj mezuroj estas verdaj kaj la uzantoj malkontentas.

### P10. Sistemo en uzo degradiĝas sen daŭra prizorgado.
Sistemo en uzo devas ŝanĝiĝi, kaj ĝia komplekseco kreskas, se laboro ne malpliigas ĝin. Prizorgado, teknika bonegeco kaj daŭrigebla ritmo estas parto de la kosto de la sistemo, ne superfluaĵo.  
- **Bazo**: la leĝoj de Lehman pri daŭra ŝanĝo kaj kreskanta komplekseco; vivaj strukturoj konservas ordon per daŭra fluo de energio, sed tio estas analogio, ne ekvivalento.  
- **Signalo**: ĉiu ŝanĝo estas pli malrapida ol la antaŭa; ritmo, kiun neniu povas teni senfine.
