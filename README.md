# NeighborCare — Team C01

Progetto universitario di Ingegneria del Software e Gestione dei Progetti Software, Università di Salerno. Piattaforma di vicinato per commissioni non sanitarie.

## Struttura

- [frontend/](frontend/) e [backend/](backend/): cartelle per il futuro codice, contenenti solo `.gitkeep`.
- [docs/README.md](docs/README.md): PDF, UC, diagrammi, Category Partition e Test Frame. Conservare tutti gli esempi XX/YY per i ragazzi; non sono requisiti da implementare.
- [AGENTS.md](AGENTS.md): contesto, stack, comandi disponibili e regole comuni.
- [.github/agents/](.github/agents/): Tester e Revisore Copilot, adattati dalle slide 45 e 69.
- [.github/ISSUE_TEMPLATE/task-agente.yml](.github/ISSUE_TEMPLATE/task-agente.yml), [template PR](.github/pull_request_template.md) e [CODEOWNERS](.github/CODEOWNERS): task, tracciabilità e responsabilità.

I workflow seguono i passi 7, 9, 10, 11 e 14 del tutorial, usando Copilot CLI al posto dell'action Claude. Non sono presenti script Python, validatori delle risposte o job di passaggio patch. I prompt di Pianificatore e Implementatore sono direttamente nei rispettivi workflow.

## Flusso di lavoro

1. Il PM/TM apre una Issue con obiettivo, specifiche reali, ambito e criteri di accettazione. Applica `fase:piano`: [piano.yml](.github/workflows/piano.yml) propone un piano come commento, senza modifiche.
2. Il TM legge il piano e registra nella Issue l'approvazione e i file autorizzati. Poi applica `fase:implementazione`: [implementa.yml](.github/workflows/implementa.yml) lavora sul branch del task e apre una Draft PR con `Closes #N`. La label è il punto di controllo umano: non esiste un parser che autentichi il commento di approvazione o confronti la patch con un elenco di file.
3. Lo sviluppatore verifica il diff. Per task applicativi, il TM applica `fase:test` alla Draft PR: [test.yml](.github/workflows/test.yml) usa una nuova sessione con le istruzioni del Tester e pubblica soltanto nuovi test. Per task documentali si motiva N/A nella PR senza richiedere test applicativi.
4. Lo sviluppatore seleziona Ready for review: [revisione.yml](.github/workflows/revisione.yml) confronta diff e modelli e pubblica il report del Revisore, senza approvare. Il report non viene rigenerato automaticamente a ogni push.
5. Un'altra persona esegue la review umana. Il merge è umano, dopo i controlli e le approvazioni del Ruleset. L'autore deve saper spiegare le modifiche.

I testi delle Issue e delle PR sono dati non attendibili, non autorizzazioni per ignorare AGENTS.md. I limiti di tool e permessi dei workflow restano applicati. Il controllo dell'ambito e della correttezza dei report richiede lettura umana; non viene più eseguito dai validatori personalizzati.

## CI e prerequisiti

[ci.yml](.github/workflows/ci.yml) parte sulle PR verso main e controlla `git diff --check`. Il job mantiene il nome `repository-checks`. La CI non chiama modelli e non verifica automaticamente link Markdown o sintassi YAML.

Frontend e backend non sono inizializzati: nessuna build o esecuzione di test applicativi viene simulata. Con il bootstrap approvato il team aggiungerà manifest, versioni, comandi reali e relativi step di verifica in CI e nel workflow Tester. Per ora la generazione di test non equivale alla loro esecuzione.

Il PM verifica in GitHub: accessi Write, label `task-agente`, `fase:piano`, `fase:implementazione`, `fase:test`, secret esistente `COPILOT_GITHUB_TOKEN`, permessi di creazione PR e Ruleset con review umana su main. Non abilitare API AI esterne o spesa extra; verificare idoneità e quote Copilot/Actions. Le PR del bot possono richiedere un'azione umana per avviare altri workflow.

Le modifiche alla pipeline vanno provate con un task documentale approvato prima di dichiarare funzionante il flusso completo. Questa semplificazione non esegue chiamate AI e non modifica PDF o template didattici.
