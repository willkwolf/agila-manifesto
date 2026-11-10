---
name: agila-manifesto-es
description: Guía y principios del Agila Manifesto v3.1 para analizar la estructura de equipos, revisar procesos o diseñar sistemas distribuidos.
metadata:
  lang: es
  canon_version: "3.1"
  canon_sha256: "44dd1dc966874fceea8d53d9ac312397b1fcb5e9f51919bbe0e71b19d027c470"
  status: draft
  translators:
    - "AI Agent (Borrador)"
    - "@willkwolf"
---

# Agila Manifesto (Español — Borrador de Traducción)

> **Aviso**: Texto derivado. El único canon oficial con autoridad soberana reside en la versión en esperanto (`canon/AGILA-MANIFESTO.eo.md`). Ante cualquier discrepancia gramatical, conceptual o de interpretación, prevalece el canon en esperanto.

## Protocolo de Agente

1. **Leer, Analizar, Citar y Proponer**: Analiza sistemas socio-técnicos, topologías de equipos y arquitecturas bajo las lentes diagnósticas de P01–P10. Al citar, referencia los principios por sus IDs canónicos (`P01` a `P10`) y cita el título, declaración, base o señal de forma literal. Proponer mejoras estructurales basadas en evidencia.
2. **Cero Autoridad de Modificación**: Posees cero autoridad para modificar, aprobar o fusionar cambios en el canon o en los archivos de traducción. Las máquinas y agentes no pueden modificar el canon ni aprueban cambios al canon bajo ninguna circunstancia.
3. **Marcado Explícito de Propuestas y Propiedad Humana**: Todas las sugerencias, refactorizaciones o adaptaciones generadas por agentes deben designarse explícitamente como `"Propuesta"`. Toda propuesta debe declarar un patrocinador humano activo mediante `Human-owner: @usuario`. Las propuestas sin propietario humano no pueden fusionarse.
4. **Lentes Diagnósticas, Sin Dogma ni Evaluación**: Trata los principios como lentes analíticas descriptivas y tendencias de diseño para comprender la fricción, nunca como reglas obligatorias, listas de cumplimiento, métricas de rendimiento o formas de evaluar equipos.
5. **Supremacía del Canon**: El canon en esperanto (`canon/AGILA-MANIFESTO.eo.md`) es la única fuente soberana de verdad. Todas las traducciones son derivadas; ante cualquier discrepancia, prevalece el canon en esperanto.

---

## Los 10 Principios

### P01. Todo sistema refleja la estructura de comunicación de sus creadores.
Organización y sistema son dos caras de una misma estructura. Elegir la estructura de los equipos es, por lo tanto, elegir una arquitectura, y una estructura que no se elige se forma al azar.  
- **Base**: Existe una transformación aproximada que conserva la estructura, un homomorfismo, desde el grafo de comunicación hacia el grafo modular del sistema; la maniobra inversa elige el origen para obtener el destino deseado.  
- **Señal**: La arquitectura deseada no concuerda con la de los equipos; un cambio pequeño exige coordinar a muchos equipos.

### P02. Toda unidad de decisión tiene una capacidad finita.
Un equipo solo puede retener un contexto limitado, y el número de vías de comunicación en un grupo crece más rápido que el grupo mismo. Cuando la carga supera la capacidad, la unidad se divide siguiendo una juntura natural en lugar de seguir creciendo.  
- **Base**: La capacidad de un canal es finita; la racionalidad de las personas es limitada; el número de caminos en un grafo completo crece de forma cuadrática respecto al número de personas.  
- **Señal**: Añadir personas no incrementa la entrega; nadie es capaz de explicar todo el dominio del equipo.

### P03. Los sistemas estables son fuertes por dentro y débiles a través de sus límites.
Dentro de una unidad, la comunicación es rápida, bidireccional y con contexto compartido, y las decisiones ocurren donde reside la información. Entre unidades, el vínculo se convierte en un pacto cuando reúne cuatro propiedades: todas las partes han consentido, responsables con nombre y apellido se han comprometido, el historial es rastreable y cualquiera puede comprobar su cumplimiento. La herramienta, el formato y el papel carecen de importancia; lo que importa son las propiedades. En un sistema sano, el número de pactos y reuniones es proporcional a la dependencia.  
- **Base**: Los sistemas complejos son casi descomponibles, con interacciones más intensas dentro de los subsistemas que entre ellos; un regulador requiere una variedad al menos igual a la del sistema regulado, por lo que la decisión distribuida coincide con la información distribuida; las interfaces solo son componibles cuando sus tipos encajan.  
- **Señal**: Reuniones destinadas únicamente a coordinar cambios; fallos en los traspasos de trabajo entre equipos.

### P04. La interfaz efectiva es todo lo observable.
Cualquier aspecto que otra unidad pueda observar se convierte en una dependencia, incluso si nadie lo declaró formalmente. Por ello, un cambio en el comportamiento observable constituye un cambio en el pacto y afecta a todos los que dependen de él.  
- **Base**: Dos sistemas son equivalentes para un observador si este no puede distinguirlos; la interfaz efectiva es el conjunto de todas las observaciones, el cual abarca al conjunto declarado.  
- **Señal**: Un cambio considerado inofensivo termina rompiendo el sistema de alguien más.

### P05. La fiabilidad nace de la redundancia.
El conocimiento que existe únicamente en una cabeza constituye un punto único de fallo en la estructura de comunicación. Cuando varias vías conducen a la misma función, el sistema tolera la pérdida de una de ellas.  
- **Base**: Un todo fiable a partir de piezas menos fiables requiere redundancia; en los organismos vivos, estructuras distintas pueden desempeñar la misma función, otorgando robustez.  
- **Señal**: La ausencia de una sola persona paraliza el trabajo.

### P06. El flujo está gobernado por la espera, no por el esfuerzo.
A menudo el trabajo pasa más tiempo en espera que siendo procesado, y dicha espera se concentra en los traspasos entre unidades. La velocidad de todo el flujo queda limitada por su etapa más lenta, y una ocupación casi plena hace que la espera se dispare enormemente. Las estimaciones son pronósticos con dispersión, no promesas.  
- **Base**: Si la tasa de entrega es estable, el tiempo de ciclo equivale al trabajo en curso dividido por la tasa de entrega, según la ley de Little; en las colas de espera, la demora crece proporcionalmente a la ocupación dividida por uno menos la ocupación.  
- **Señal**: Todo el mundo está ocupado y nada se concluye; colas de espera en los traspasos; fechas prometidas que resultan inexactas.

### P07. Un sistema que aprende cambia su estructura, no solo sus acciones.
Preguntarse únicamente qué hicimos mal corrige las acciones; preguntarse qué supuestos gobiernan nuestros límites, pactos y métricas cambia la estructura que engendra dichas acciones. Nombramos los supuestos, los cuestionamos, los desafiamos mediante contrapruebas y asimilamos lo aprendido como una estructura modificada, no como un simple apunte. Cada decisión cuenta con un responsable y un criterio claro para saber si ha funcionado.  
- **Base**: Doble bucle: el primero corrige la acción respecto al objetivo; el segundo modifica el objetivo o el modelo mental; un sistema de estructura rígida posee una variedad fija y no puede absorber las variaciones de su entorno.  
- **Señal**: Los mismos problemas reaparecen en cada ciclo; las actas están repletas y nada cambia.

### P08. Todo agente forma parte de la estructura de comunicación.
Sea humano o máquina, todo agente que produce artefactos moldea el sistema y es moldeado por la estructura en la que opera. Los agentes de inteligencia artificial poseen, por consiguiente, límites y un responsable asignado, y sus resultados solo cruzan los límites del equipo mediante decisión humana.  
- **Base**: Un agente es un nodo del grafo con entradas y salidas; sus salidas cruzan un límite únicamente a través de un pacto, al igual que las de cualquier otra unidad.  
- **Señal**: Código o texto del que nadie se hace responsable y que nadie sabe explicar.

### P09. En la complejidad, la comprensión sigue a la acción.
Donde la dinámica es no lineal y los elementos se adaptan mutuamente, la predicción a largo plazo resulta limitada, y las sondas pequeñas y seguras aportan más información que cualquier plan. Antes de actuar, declaramos qué demostraría que estamos equivocados. El software funcional en manos de usuarios reales constituye nuestra prueba primordial, y un sistema complejo que funciona casi siempre evolucionó a partir de uno simple que funcionaba; los requisitos cambiantes son información valiosa. Una métrica es una señal, nunca un fin en sí misma; cuando se convierte en objetivo, la cuestionamos y la contrastamos con otra métrica capaz de contradecirla.  
- **Base**: Predictibilidad limitada en sistemas dinámicos no lineales; una hipótesis es científica solo si es refutable; una métrica es una proyección con pérdida de la realidad, y optimizarla a ciegas desplaza al sistema hacia regiones donde dicha proyección ya no preserva lo que verdaderamente importaba.  
- **Señal**: Todas las métricas están en verde, pero los usuarios están insatisfechos.

### P10. Un sistema en uso se degrada sin un mantenimiento continuo.
Un sistema en uso debe evolucionar constantemente, y su complejidad aumenta a menos que se invierta trabajo deliberado en reducirla. El mantenimiento, la excelencia técnica y un ritmo sostenible forman parte del coste intrínseco del sistema, no son superfluos.  
- **Base**: Las leyes de Lehman sobre cambio continuo y complejidad creciente; las estructuras vivas preservan el orden mediante un flujo continuo de energía, aunque se trata de una analogía y no de una equivalencia estricta.  
- **Señal**: Cada cambio resulta más lento que el anterior; un ritmo de trabajo que nadie es capaz de sostener indefinidamente.
