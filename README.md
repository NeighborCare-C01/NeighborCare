# NeighborCare — Team C01

Progetto universitario di Ingegneria del Software e Gestione dei Progetti Software, Università di Salerno.
NeighborCare mette in relazione Beneficiari e Neighbor verificati per commissioni non sanitarie, con la supervisione dei Coordinatori.

## Stato del progetto

**Decisione dei PM:** RAD e SDD versionati sono adottati come **baseline di progetto definitiva** per la pianificazione. Le diciture REVIEW/DRAFT nei PDF originali non vengono riscritte; eventuali incoerenze si risolvono con decisioni tecniche tracciate. Vedi [baseline](docs/BASELINE.md).

L'architettura prevista dallo SDD è Three-Tier:

- Frontend: React/PWA.
- Backend: Java/Spring Boot.
- Database: PostgreSQL.

Le versioni degli strumenti e i comandi di build,
test e avvio saranno definiti durante il bootstrap
dei rispettivi progetti.

Il codice applicativo non è ancora stato inizializzato.

## Documentazione

[Guida rapida e struttura degli artefatti](docs/README.md).

| Artefatto            | Percorso                                | Stato                                                                |
| -------------------- | --------------------------------------- | -------------------------------------------------------------------- |
| RAD v1.0, 09/11/2026 | [RAD](docs/rad/C01_RAD.pdf) | Baseline definitiva adottata dai PM; PDF originale invariato |
| SDD v0.0             | [SDD](docs/sdd/C01_SDD.pdf)  | Baseline definitiva adottata dai PM; PDF originale invariato |

I PDF sono conservati integralmente; la decisione operativa dei PM è registrata in `docs/BASELINE.md`.
La struttura include esempi didattici inventati (“Invia un saluto”) per UC, sorgenti PlantUML, Category Partition e Test Frame: mostrano come organizzare gli artefatti e non costituiscono specifiche di NeighborCare.
Eventuali discrepanze tra i documenti o riferimenti non fruibili da un agente vanno chiariti nella relativa Issue prima di implementare; non si inventano contratti o Test Frame mancanti.

## Struttura

- `frontend/`: client, non ancora inizializzato.
- `backend/`: server, non ancora inizializzato.
- `docs/rad/` e `docs/sdd/`: PDF originali; `docs/rad/uc/` contiene il modello di file per i casi d’uso.
- `docs/modelli/rad/` e `docs/modelli/sdd/`: sorgenti UML distinti per documento, con file di esempio da compilare.
- `docs/test/`: file di esempio per Category Partition e Test Frame.
- `agents/`: istruzioni di tester e revisore utilizzabili con qualsiasi agente, subordinate ad AGENTS.md.
- `.claude/agents/`: adattatori Claude Code che rimandano ai ruoli condivisi.
- `.github/ISSUE_TEMPLATE/`: moduli `task-agente.yml` e `bug.yml`.
- `.github/`: template Pull Request e adattatore Copilot.

[AGENTS.md](AGENTS.md) è l’unica fonte delle regole di sviluppo per TM e agenti AI.
`CLAUDE.md`, `GEMINI.md` e l’adattatore Copilot rinviano alle stesse regole.
Le Issue contengono specifica tecnica, piano e approvazioni; le PR collegano modifiche e verifiche.
Trello resta il riferimento per il coordinamento operativo, Ganttfather per la pianificazione.

## Workflow agentico e CI

La repository usa **GitHub Copilot CLI in GitHub Actions** e i profili di ruolo in [.github/agents/](.github/agents/) per Pianificatore, Implementatore, Tester e Revisore. La guida operativa è [docs/processo-agentico.md](docs/processo-agentico.md): prima di implementare il TM approva un piano registrato nella Issue, poi il lavoro procede su branch e Draft PR, con test indipendenti, review umana e merge controllato.

La [CI](.github/workflows/ci.yml) controlla le Pull Request verso `main` con strumenti locali senza API AI; finché i progetti `frontend/` e `backend/` non saranno inizializzati non esegue build/test applicativi. La configurazione [CODEOWNERS](.github/CODEOWNERS) include PM e team Developers; attivare i requisiti di review e lo status check `repository-checks` in Settings → Rules.

I file `XX/YY`, `docs/modelli/sdd/class.puml` e gli esempi di test sono **template didattici da conservare**: aiutano i ragazzi a organizzare casi d'uso, UML e Test Frame, ma non rappresentano le specifiche da implementare. Sostituirli o affiancarli con i **modelli reali approvati** prima di avviare un UC di prodotto.

Copilot e le Actions hanno quote e condizioni diverse; non attivare servizi o API a pagamento. Le fasi partono da gesti umani (label o Ready for review), con controlli espliciti e gate di approvazione. La pipeline automatica è descritta in [processo-agentico](docs/processo-agentico.md). Chi usa un agente rimane responsabile del suo codice.

## Stato di sviluppo

- Frontend React/PWA e backend Java/Spring Boot da inizializzare previa approvazione di stack e comandi.
- PostgreSQL proposto nell'SDD; l'eventuale uso di PostGIS richiede una decisione tecnica documentata.
- Per ogni task applicativo, allegare riferimenti esatti ai veri modelli e Test Frame contenuti nella baseline, con eventuali trasposizioni testuali approvate.
- Trello resta lo strumento di coordinamento operativo e Ganttfather per la pianificazione.
