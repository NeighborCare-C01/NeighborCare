# Documentazione NeighborCare

Percorsi allineati alla slide 68 del professore: `rad/uc/`, `sdd/`, `modelli/` e `test/`. Le sottocartelle `modelli/rad/` e `modelli/sdd/` distinguono l’origine dei diagrammi.

I file con `XX`/`YY` e `modelli/sdd/class.puml` contengono **esempi inventati**, non modelli di NeighborCare. Il caso guida è “Invia un saluto”; il file dei livelli usa un esempio generico autonomo. La struttura distingue i tipi di diagramma presenti nei documenti; non li traspone. Il **Class Diagram sarà solo quello ristrutturato dell’SDD**, unico riferimento per le classi: nella bozza SDD attuale non è ancora presente e il team dovrà inserirlo.

| Artefatto | Qui va il file (esempio inventato) | Riferimento nel documento |
| --- | --- | --- |
| Caso d’uso | [rad/uc/UC_XX_YY.md](rad/uc/UC_XX_YY.md) | RAD §3.5 |
| Use Case Diagram | [modelli/rad/UCD_XX.puml](modelli/rad/UCD_XX.puml) | RAD pp. 48–51, UCD_01…05 |
| Sequence Diagram | [modelli/rad/SQ_XX_YY.puml](modelli/rad/SQ_XX_YY.puml) | RAD §3.7, pp. 67–69 |
| Statechart | [modelli/rad/ST_XX_YY.puml](modelli/rad/ST_XX_YY.puml) | RAD §3.8, pp. 70–71 |
| Activity sistema attuale | [Solo nel RAD, nessun esempio separato](rad/C01_RAD.pdf#page=8) | RAD §2.2, p. 8, AD_SA |
| Activity sistema proposto | [modelli/rad/AD_XX_SistemaProposto.puml](modelli/rad/AD_XX_SistemaProposto.puml) | RAD §3.9, p. 72 |
| Navigational Path | [modelli/rad/NP_XX_YY.puml](modelli/rad/NP_XX_YY.puml) | RAD §3.10, pp. 73–74, NP_C / NP_NB / NP_B |
| Class Diagram ristrutturato | [modelli/sdd/class.puml](modelli/sdd/class.puml) | Da inserire nell’SDD dal team |
| Dipendenze dei sottosistemi | [modelli/sdd/Sottosistemi_XX_YY.puml](modelli/sdd/Sottosistemi_XX_YY.puml) | SDD §3.2.1, p. 11 |
| Architettura a livelli | [modelli/sdd/Livelli_XX_YY.puml](modelli/sdd/Livelli_XX_YY.puml) | SDD §3.2.2, p. 12 |
| Deployment Diagram | [modelli/sdd/Deployment_XX_YY.puml](modelli/sdd/Deployment_XX_YY.puml) | SDD §3.3.1, p. 13 |
| Category Partition | [test/CP_UC_XX.md](test/CP_UC_XX.md) | Artefatti di testing del team |
| Test Frame | [test/TF_UC_XX.md](test/TF_UC_XX.md) | Artefatti di testing del team |

PDF originali: [RAD REVIEW](rad/C01_RAD.pdf) e [SDD DRAFT](sdd/C01_SDD.pdf). I mockup restano consultabili nel RAD §3.11, pp. 75–84: non sono sostituiti dai Navigational Path.

## Come usare la struttura

1. Sostituire gli esempi con gli artefatti reali. Rinominare `XX`/`YY` con ID e nomi originali; `AD_XX_…`, `Sottosistemi_…`, `Livelli_…` e `Deployment_…` sono nomi didattici, non nuovi ID del progetto. Un file per ciascun diagramma; riportare versione, sezione, pagina e stato di approvazione della fonte.
2. Collegare nell’UC sequence, Class Diagram SDD, stati, navigazione e test pertinenti. Nel sequence indicare l’UC di riferimento: i loro ID possono essere diversi. L’Activity attuale descrive il processo precedente; quello proposto descrive il processo da realizzare. I sottosistemi mostrano le dipendenze logiche, i livelli separano le responsabilità e il deployment colloca il software sui nodi di esecuzione.
3. Nella Issue usare **Copy permalink** sui file GitHub. Esempio di riferimenti: `docs/rad/uc/UC_XX_YY.md`, `docs/modelli/rad/SQ_XX_YY.puml`, `docs/modelli/sdd/class.puml`, `docs/test/TF_UC_XX.md`; aggiungere gli altri diagrammi pertinenti. I file didattici non autorizzano implementazioni del progetto.
4. Dopo approvazione aggiornare insieme codice, modelli e riferimenti. Non sovrascrivere i PDF originali: aggiungere le revisioni approvate. Le regole comuni sono in [AGENTS.md](../AGENTS.md).

## Esempio didattico di Issue documentale

> Gli artefatti seguenti sono esempi inventati: non rappresentano requisiti reali di NeighborCare e non autorizzano a implementare la funzione del saluto.

**Issue di collaudo:** [#4 — Aggiungere un esempio di Issue documentale al README](https://github.com/NeighborCare-C01/NeighborCare/issues/4).

**Obiettivo:** mostrare come collegare una Issue agli artefatti dell’esempio “Invia un saluto”. **UC/requisiti reali: N/A**, attività esclusivamente documentale.

| Riferimento da indicare nella Issue | File da consultare |
| --- | --- |
| Caso d’uso UC_XX | [UC_XX_YY.md](rad/uc/UC_XX_YY.md) |
| Sequence Diagram SQ_XX | [SQ_XX_YY.puml](modelli/rad/SQ_XX_YY.puml) |
| Class Diagram ristrutturato SDD | [class.puml](modelli/sdd/class.puml) |
| Test Frame dell’UC | [TF_UC_XX.md](test/TF_UC_XX.md) |

**Verifica prevista:** controllare che i file esistano e che i collegamenti siano corretti. I Test Frame sono citati per mostrare la tracciabilità; i test applicativi sono N/A per questa attività documentale.

Questi link relativi funzionano dal README. Nel corpo di una Issue incollare i corrispondenti URL GitHub o permalink, indicando versione e stato didattico degli artefatti.
