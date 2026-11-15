# NeighborCare — Team C01

Progetto universitario di Ingegneria del Software e Gestione dei Progetti Software, Università di Salerno.
NeighborCare mette in relazione Beneficiari e Neighbor verificati per commissioni non sanitarie, con la supervisione dei Coordinatori.

## Stato del progetto

Il RAD disponibile è in revisione e l’SDD è una bozza;
l’approvazione della baseline per lo sviluppo non è attestata.

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
| RAD v1.0, 09/11/2026 | [RAD](docs/rad/C01_RAD.pdf) | REVIEW: contiene commenti di revisione; approvazione non attestata   |
| SDD v0.0             | [SDD](docs/sdd/C01_SDD.pdf)  | DRAFT: incompleto; copertina e footer riportano versioni discordanti |

I PDF sono conservati integralmente. La loro presenza non costituisce approvazione.
La struttura include esempi didattici inventati (“Invia un saluto”) per UC, sorgenti PlantUML, Category Partition e Test Frame: mostrano come organizzare gli artefatti e non costituiscono specifiche di NeighborCare.
Prima dello sviluppo vanno risolti i commenti rilevanti del RAD e le incoerenze dello SDD, inclusi i segnaposto tecnologici in §3.1 e i riferimenti ai contenuti in §1.6.
Occorrono inoltre contratti condivisi, modelli pertinenti e Test Frame approvati; non sono ancora disponibili in forma separata.

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

## Allineamento alla struttura delle slide

La struttura segue il passo 1 delle slide (p. 68): regole comuni nella radice,
ruoli condivisi in `agents/` con adattatori in `.claude/agents/`, moduli in `.github/`, documenti in
`docs/rad/uc/`, `docs/sdd/`, `docs/modelli/` e `docs/test/`.
Il Class Diagram ristrutturato è soltanto in `docs/modelli/sdd/class.puml`.

La slide mostra un progetto Java/Maven: in NeighborCare si conservano `frontend/`
e `backend/`; `pom.xml` e `src/` del backend saranno definiti al bootstrap approvato.
La pipeline agentica delle slide non è attiva: per ora il team usa manualmente
gli assistenti scelti, seguendo le istruzioni condivise. Non si introducono servizi
o API a pagamento. Eventuali integrazioni gratuite richiedono prima la verifica
di condizioni, quote e assenza di addebiti automatici. Non ci sono automazioni operative.

## Uso con agenti diversi e prima prova

I file condivisi sono [agents/tester.md](agents/tester.md) e
[agents/revisore.md](agents/revisore.md), nella cartella `agents/` della radice.
Sono normali file Markdown. Per usare il tester o il revisore,
indicare nel task: «Leggi AGENTS.md e agents/tester.md» oppure
«Leggi AGENTS.md e agents/revisore.md», in una sessione separata.
Gli adattatori Claude non sono necessari per gli altri strumenti. Nei task i percorsi
`agents/tester.md` e `agents/revisore.md` partono dalla radice della repository,
non dalla cartella `.claude/agents/`.

Per provare il processo adesso, usare un task documentale: lettura degli artefatti,
piano, approvazione del TM, modifica minima e revisione separata. L’esempio “Invia un
saluto” serve a leggere e collegare i modelli; non è una funzionalità da implementare.
Una Issue da sola non avvia agenti: il TM la passa manualmente allo strumento scelto.
Non occorre un workflow “Saluto” per questa prova. Si verifica il percorso manuale
Issue → piano → approvazione → modifica → test pertinenti → revisione umana, senza
nuove integrazioni API o costi aggiuntivi. Le azioni su GitHub richiedono l’autorizzazione
prevista da AGENTS.md; questo setup non crea Issue o PR automaticamente.
