# Agila Manifesto

**Deliver quality software. / Entregar software de calidad.**

> **Aviso de documento derivado**: Este documento es una traducción derivada de la documentación del repositorio. El único canon oficial con autoridad soberana reside en la versión en esperanto (`canon/AGILA-MANIFESTO.eo.md`). Ante cualquier discrepancia gramatical, conceptual o de interpretación, prevalece el canon en esperanto.

---

## 1. Deliver quality software

El **Agila Manifesto** (v3.1) es un marco socio-técnico internacional de código abierto diseñado para entregar software de calidad en organizaciones distribuidas y sistemas adaptativos complejos modernos.

A diferencia de las metodologías tradicionales basadas en ceremonias o prescripciones dogmáticas, el Agila Manifesto formaliza los invariantes estructurales que rigen la arquitectura de software, las topologías de equipos y el flujo de trabajo colaborativo. Establece un puente riguroso entre el diseño organizacional y la arquitectura de sistemas bajo la realidad matemática de la ley de Conway y la teoría de sistemas.

Características esenciales:
- **Manifiesto Vivo**: Evoluciona de manera continua bajo gobernanza pública, revisión de contraejemplos abiertos y observación empírica.
- **Audiencia Dual**: Diseñado desde su origen para ser consumido e interpretado tanto por equipos humanos como por agentes de inteligencia artificial.
- **Canon Soberano Único en Esperanto**: Anclado en una lengua auxiliar internacional políticamente neutral (`canon/AGILA-MANIFESTO.eo.md`), garantizando una base equitativa libre de sesgos o hegemonías culturales.
- **Soberanía Humana**: Aunque las máquinas leen, analizan, citan y proponen mejoras estructurales, únicamente las personas poseen la autoridad para aprobar y evolucionar el canon.

---

## 2. Badges

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)](LICENSE)
[![Code License: MIT](https://img.shields.io/badge/Code_License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v3.1-blue.svg)](CHANGELOG.md)
[![CI Validation](https://github.com/willkwolf/agila-manifesto/actions/workflows/pr-validation.yml/badge.svg)](https://github.com/willkwolf/agila-manifesto/actions)
[![Languages](https://img.shields.io/badge/languages-3_available-informational.svg)](i18n/STATUS.md)

---

## 3. In 30 seconds

- **Fundamentos Socio-técnicos**: Cimentado en teoría de sistemas, modelos de colas de espera y la ley de Conway, en lugar de metodologías subjetivas.
- **Arquitectura para Audiencia Dual**: Diseñado para humanos y agentes de IA con un canon soberano neutral en esperanto y un esquema estructurado en YAML.
- **Lentes Descriptivas Sin Dogma**: Diagnósticos analíticos para identificar fricciones arquitectónicas y organizativas, nunca listas de control punitivas ni esquemas de certificación.

---

## 4. The 10 Principles at a Glance

> **Declaración sobre Derivaciones de Conway**: 8 de 10 principios (P01 a P08) derivan directamente de la ley de Conway (1968) o de sus corolarios matemáticos y de teoría de grafos (homomorfismo del grafo de comunicación, capacidad de canal, casi-descomponibilidad, visibilidad de interfaces, rutas redundantes, esperas en traspasos, adaptación estructural y membrecía en el grafo multiactor). Esto se declara con total transparencia como una **tendencia de diseño**, no como una regla física inmutable. Los principios P09 (Complejidad y Sondas) y P10 (Degradación de Sistemas) derivan respectivamente de Sistemas Adaptativos Complejos / Epistemología y de las Leyes de Lehman sobre la Evolución del Software.

| # | Principio | Estatus de la Base Teórica | ¿Deriva de Conway? |
|---|-----------|----------------------------|--------------------|
| [**P01**](docs/principles/p01.md) | Todo sistema refleja la estructura de comunicación de sus creadores | Teorema / Modelo (Homomorfismo entre grafo de comunicación y grafo modular; maniobra inversa de Conway) | **Sí** (Ley directa de Conway) |
| [**P02**](docs/principles/p02.md) | Toda unidad de decisión tiene una capacidad finita | Modelo / Teorema (Capacidad de canal de Shannon, racionalidad limitada de Simon, crecimiento cuadrático de aristas) | **Sí** (Carga cognitiva y corolario de escala) |
| [**P03**](docs/principles/p03.md) | Los sistemas estables son fuertes por dentro y débiles a través de sus límites | Modelo / Teorema (Sistemas casi descomponibles de Simon, ley de variedad de Ashby, pactos explícitos) | **Sí** (Modularidad y corolario de pactos limítrofes) |
| [**P04**](docs/principles/p04.md) | La interfaz efectiva es todo lo observable | Modelo / Tendencia Empírica (Equivalencia observacional, ley de Hyrum) | **Sí** (Frontera de interfaz y acoplamiento implícito) |
| [**P05**](docs/principles/p05.md) | La fiabilidad nace de la redundancia | Teorema / Modelo (Síntesis de Von Neumann de organismos fiables a partir de piezas no fiables, degeneración biológica) | **Sí** (Topología de red y corolario de factor bus) |
| [**P06**](docs/principles/p06.md) | El flujo está gobernado por la espera, no por el esfuerzo | Teorema / Modelo (Ley de Little $L = \lambda W$, fórmula de Kingman para tiempos en cola) | **Sí** (Fricción de traspasos en límites organizacionales) |
| [**P07**](docs/principles/p07.md) | Un sistema que aprende cambia su estructura, no solo sus acciones | Modelo / Interpretación (Aprendizaje de doble bucle de Argyris y Schön, variedad requerida de Ashby) | **Sí** (Corolario de realineamiento estructural inverso) |
| [**P08**](docs/principles/p08.md) | Cada agente forma parte de la estructura de comunicación | Modelo (Teoría de grafos con nodos humanos y de IA, cruce de fronteras bajo pactos) | **Sí** (Expansión del grafo socio-técnico a agentes) |
| [**P09**](docs/principles/p09.md) | En la complejidad, la comprensión sigue a la acción | Tendencia Empírica / Modelo (Sistemas adaptativos complejos, falsabilidad popperiana, leyes de Goodhart/Campbell) | **No** (Ciencia de la complejidad y epistemología) |
| [**P10**](docs/principles/p10.md) | Un sistema en uso se degrada sin mantenimiento continuo | Tendencia Empírica (Leyes de Lehman sobre evolución de software, sistemas termodinámicos abiertos) | **No** (Dinámica evolutiva de Lehman) |

Para fundamentos matemáticos detallados y análisis de señales, consulta [docs/conway-derivations.md](docs/conway-derivations.md) y los análisis individuales en [docs/principles/](docs/principles/).

---

## 5. Distinctions from the 2001 Agile Manifesto

El Agila Manifesto se apoya respetuosamente sobre el legado histórico del Manifiesto Ágil de 2001, el cual liberó el desarrollo de software de los procesos burocráticos en cascada al priorizar a los individuos, el software funcional, la colaboración y la respuesta al cambio.

Durante el último cuarto de siglo, la disciplina ha madurado significativamente:
1. **De Valores Subjetivos a Invariantes Estructurales**: En lugar de expresar preferencias cualitativas ("valorar X sobre Y"), el Agila Manifesto identifica leyes socio-técnicas formales (homomorfismos de grafos, límites de capacidad de canal, teoría de colas) que determinan el éxito o bloqueo en la entrega de sistemas.
2. **De Equipos Solo Humanos a Ecosistemas Humano-Agente**: Los agentes de IA autónomos y asistentes de código participan hoy activamente en el grafo de desarrollo. El Principio 8 formaliza su rol delimitando fronteras, pactos y patrocinio humano.
3. **De Dogmas Procesales a Lentes Diagnósticas**: En lugar de recetar reuniones o alimentar certificaciones comerciales, provee herramientas analíticas para diagnosticar deuda estructural y fricción en la entrega.
4. **Señales Observables**: Cada principio vincula una base teórica (`Bazo`) con un síntoma observable (`Signalo`), permitiendo detectar anomalías antes de fallos catastróficos.

---

## 6. Status, Without Dogma, Minimal Formal Language, Why Esperanto

*(Adaptado al español a partir de las declaraciones canónicas)*

### Estatus
El Agila Manifesto v3.1 es una propuesta viva y abierta. No se autoproclama estándar oficial ni mandato corporativo, sino una base teórica y empírica que se perfecciona continuamente mediante la observación pública y contraejemplos comunitarios.

### Sin Dogma
El manifiesto rechaza el dogmatismo. Sus principios **nunca** deben utilizarse como:
- Listas de verificación obligatorias ni mandamientos organizativos prescriptivos.
- Criterios para calificar, clasificar o evaluar el rendimiento de desarrolladores y equipos.
- Productos comerciales de certificación ni barreras de licenciamiento.

### Lenguaje Formal Mínimo
Los formalismos matemáticos (teoría de grafos, teoría de la información de Shannon, ley de Little) se emplean exclusivamente donde son indispensables para erradicar la ambigüedad conceptual.

### ¿Por qué esperanto?
El esperanto actúa como único ancla canónica (`canon/AGILA-MANIFESTO.eo.md`) por tres razones fundamentales:
1. **Neutralidad Lingüística**: Pertenece equitativamente a toda la comunidad global, evitando hegemonías geopolíticas y sesgos culturales.
2. **Regularidad Estructural**: Su morfología lógica y aglutinante provee términos estables y sin polisemia.
3. **Consenso Deliberado**: Modificar el canon en un idioma puente compartido exige reflexión y consenso consciente.

---

## 7. For Humans

El manifiesto asiste a ingenieros, líderes de arquitectura y diseñadores organizacionales a diagnosticar la fricción en sistemas.

### Estructura Tripartita
Cada principio consta de:
1. **La Declaración**: La ley o tendencia socio-técnica fundamental.
2. **La Base (`Bazo`)**: El sustento matemático, cibernético o empírico.
3. **La Señal (`Signalo`)**: El síntoma en el mundo real que delata la desalineación estructural.

Consulta la guía detallada para personas en [docs/guides/human-guide.md](docs/guides/human-guide.md).

---

## 8. For AI Agents

Los agentes de IA y modelos de lenguaje son participantes legítimos en la arquitectura de software moderna.

### Cómo Instalar la Habilidad (Skill)
- **Claude Code**: Copia `skills/agila-manifesto-es/` en el directorio `.claude/skills/agila-manifesto/`.
- **Otros Agentes**: Ingiere las instrucciones de [AGENTS.md](AGENTS.md) y [llms.txt](llms.txt).
- **Esquema Estructurado**: Consume directamente [canon/manifesto.eo.yaml](canon/manifesto.eo.yaml).

### Límites Innegociables para Agentes
1. **Leer, Analizar, Citar y Proponer**: Los agentes pueden evaluar arquitecturas y proponer refactorizaciones.
2. **Cero Autoridad de Modificación**: Las máquinas no pueden modificar el canon ni aprueban cambios al canon bajo ninguna circunstancia.
3. **Patrocinio Humano Obligatorio**: Toda propuesta generada por IA debe indicar su patrocinador humano activo (`Human-owner: @usuario`).
4. **Lentes, Sin Evaluación Punitiva**: Los agentes jamás deben calificar el rendimiento de humanos mediante estos principios.

Consulta el protocolo completo para agentes en [docs/guides/agent-guide.md](docs/guides/agent-guide.md).

---

## 9. Governance

Modelo de gobernanza en tres niveles:

| Nivel | Alcance | Protección | Actores Autorizados | Criterio de Aprobación | SLA de Deliberación |
|---|---|---|---|---|---|
| **Nivel 1: Fundamento** | `canon/` | **Alta ("Celosa")** | Solo personas | $\ge 2$ mantenedores humanos | Mínimo 14 días |
| **Nivel 2: Tradukoj** | `skills/`, `i18n/` | **Media** | Mantenedores de idioma | Mantenedor + 1 revisor nativo | Ciclo normal de PR |
| **Nivel 3: Uzado** | `uzado/` | **Baja (Abierta)** | Cualquier contribuidor | 1 revisor o mantenedor | Revisión ágil |

Reglas SemVer para el canon: MAJOR (añadir/quitar principio o cambio de sentido), MINOR (cambio de base/señal/sección), PATCH (redacción/ortografía). Consulta [GOVERNANCE.md](GOVERNANCE.md).

---

## 10. Languages & Translation Drift

<!-- START_TRANSLATION_TABLE -->
| Lang | Language | Status | Canon Ver | Canon SHA-256 Match | Translators / Reviewers | Skill File |
|---|---|---|---|---|---|---|
| `eo` | Esperanto | `reviewed` | 3.1 | `44dd1dc96687` (Match) | canon, @willkwolf | [`skills/agila-manifesto-eo/SKILL.md`](skills/agila-manifesto-eo/SKILL.md) |
| `en` | English | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Draft), @willkwolf | [`skills/agila-manifesto-en/SKILL.md`](skills/agila-manifesto-en/SKILL.md) |
| `es` | Español | `draft` | 3.1 | `44dd1dc96687` (Match) | AI Agent (Borrador), @willkwolf | [`skills/agila-manifesto-es/SKILL.md`](skills/agila-manifesto-es/SKILL.md) |
<!-- END_TRANSLATION_TABLE -->

Para sumar un nuevo idioma, usa la plantilla en `i18n/_template/` y revisa [i18n/STATUS.md](i18n/STATUS.md).

---

## 11. How to Contribute

Vías de contribución:
1. **Proponer evolución al canon**: Mediante RFC en `.github/ISSUE_TEMPLATE/01_canon_propono.yml`.
2. **Aportar un contraejemplo**: *"Un contraejemplo es un regalo."* Abre un issue en `.github/ISSUE_TEMPLATE/02_kontrauekzemplo.yml`.
3. **Contribuir traducciones**: Agrega o mejora idiomas en `skills/`.
4. **Aportar a Uzado**: Comparte casos reales y patrones prácticos en [uzado/](uzado/README.md).

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) y [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## 12. Versioning, Citation & License

### Versionado
Publicado bajo Versión 3.1 (`v3.1.0`). Consulta [CHANGELOG.md](CHANGELOG.md).

### Citación
Consulta los metadatos bibliográficos en [CITATION.cff](CITATION.cff).

### Licencia
- **Documentación y Canon**: [CC BY 4.0](LICENSE).
- **Código y Herramientas**: [MIT](LICENSE).

---

## 13. FAQ

### ¿Reemplaza esto al Manifiesto Ágil de 2001?
**No.** Es una propuesta de evolución independiente construida a partir de 25 años de aprendizaje empírico y arquitectónico.

### ¿Por qué esperanto?
Para garantizar neutralidad universal, rigor conceptual sin polisemia y consenso intencional deliberado.

### ¿Puede una IA modificar el manifiesto?
**Nunca.** Las máquinas analizan y proponen, pero únicamente las personas aprueban cambios al canon.

### ¿Es obligatorio adoptar los diez principios?
**No.** Son lentes diagnósticas no dogmáticas para localizar fricciones, no una lista de cumplimiento mandatorio.
