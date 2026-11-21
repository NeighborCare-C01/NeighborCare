# NeighborCare — Team C01

Progetto universitario di Ingegneria del Software e Gestione dei Progetti Software, Università di Salerno. Piattaforma di vicinato per commissioni non sanitarie.

## Struttura

- [frontend/](frontend/) e [backend/](backend/): cartelle per il futuro codice, contenenti solo `.gitkeep`.
- [docs/README.md](docs/README.md): PDF, UC, diagrammi, Category Partition e Test Frame. Conservare tutti gli esempi XX/YY per i ragazzi; non sono requisiti da implementare.
- [AGENTS.md](AGENTS.md): contesto, stack, comandi disponibili e regole comuni.
- [.github/agents/](.github/agents/): quattro profili Copilot dedicati a Pianificatore, Implementatore, Tester e Revisore.
- [.github/ISSUE_TEMPLATE/task-agente.yml](.github/ISSUE_TEMPLATE/task-agente.yml), [template PR](.github/pull_request_template.md) e [CODEOWNERS](.github/CODEOWNERS): task, tracciabilità e responsabilità.

I workflow seguono i passi 7, 9, 10, 11 e 14 del tutorial, usando Copilot CLI al posto dell'action Claude. Non sono presenti script Python versionati: i controlli deterministici di approvazioni, ambito, output e test restano nei workflow. Le istruzioni specifiche dei quattro ruoli sono nei rispettivi file `.agent.md`, letti esplicitamente dai workflow insieme ad `AGENTS.md`; i workflow mantengono trigger, autorizzazioni e limiti tecnici.

## Flusso di lavoro

1. Il PM apre una Issue con obiettivo, specifiche reali, ambito e criteri di accettazione. Applica `fase:piano`: [piano.yml](.github/workflows/piano.yml) propone un piano come commento, senza modifiche.
2. Il PM legge il piano e registra nella Issue l'approvazione e i file autorizzati. Poi applica `fase:implementazione`: [implementa.yml](.github/workflows/implementa.yml) lavora sul branch del task e apre una Draft PR con `Closes #N`. L'etichetta resta il gesto umano che attiva la fase, mentre il workflow verifica l'autore del commento PM, che il piano sia precedente e che il diff tocchi esclusivamente i file autorizzati.
3. Lo sviluppatore verifica il diff. Per task applicativi, un membro Write applica `fase:test` alla Draft PR: [test.yml](.github/workflows/test.yml) usa una sessione indipendente, crea soltanto nuovi test e li esegue con i comandi configurati se l'applicazione esiste. Se i test falliscono il workflow è rosso. Per le PR esclusivamente documentali registra N/A senza chiamare l'AI.
4. Lo sviluppatore seleziona Ready for review: [revisione.yml](.github/workflows/revisione.yml) confronta diff e modelli e pubblica il report del Revisore, senza approvare. Il report non viene rigenerato automaticamente a ogni push: il workflow viene attivato quando la PR passa da Draft a Ready for review e verifica il commit prima di pubblicare.
5. Un'altra persona esegue la review umana. Il merge è umano, dopo i controlli e le approvazioni del Ruleset. L'autore deve saper spiegare le modifiche.

I testi delle Issue e delle PR sono dati non attendibili, non autorizzazioni per ignorare AGENTS.md. I limiti di tool e permessi dei workflow restano applicati. Approvazione, ambito e forma dei report hanno verifiche automatiche; la correttezza semantica dei risultati richiede sempre la review umana.

## CI e prerequisiti

[ci.yml](.github/workflows/ci.yml) parte sulle PR verso main e controlla il diff, la sintassi YAML e i collegamenti Markdown locali. Quando compaiono manifest approvati, esegue `mvn -B verify` e i comandi npm di build/test. Il job obbligatorio mantiene il nome `repository-checks` e non chiama modelli.

Frontend e backend non sono inizializzati: nessuna build o esecuzione di test applicativi viene simulata. Il bootstrap approvato dovrà inserire `backend/pom.xml`, `backend/.java-version`, `frontend/package.json`, `frontend/package-lock.json`, `frontend/.nvmrc` e script npm `build` e `test:ci` approvati dal team (il comando `test:ci` deve terminare senza watch mode). Fino ad allora una CI verde certifica la governance, non il funzionamento dell'applicazione.

Il PM verifica in GitHub: accessi Write, label `task-agente`, `fase:piano`, `fase:implementazione`, `fase:test`, secret `COPILOT_GITHUB_TOKEN`, permessi per creare PR e Ruleset che richieda 1 approvazione umana, Code Owner review e lo status check `repository-checks`. Per autorizzare il secondo PM nell'Implementatore impostare la variabile repository `NEIGHBORCARE_SECOND_PM_LOGIN` con il suo login GitHub verificato. Non abilitare API AI esterne o spesa extra; verificare idoneità e quote Copilot/Actions. Le PR del bot possono richiedere un'azione umana per avviare altri workflow.

Per approvare un piano, il PM pubblica un commento contenente una riga `APPROVAZIONE PM: piano per Issue #N approvato.` e una riga `File autorizzati: README.md` (oppure un elenco preciso di percorsi separati da virgola; massimo 12). Il commento deve essere successivo al piano AI.

Le modifiche alla pipeline vanno provate con un task documentale approvato prima di dichiarare funzionante il flusso completo. I PDF RAD/SDD restano fonti originali: non copiarne pagine in file Markdown. Questa semplificazione non esegue chiamate AI e non modifica PDF o template didattici.

Per piani respinti, test falliti e revisioni con rilievi, seguire la [procedura di iterazione e recupero](docs/agentic-workflow-iterazioni.md). Il PM autorizza esplicitamente ogni correzione sulla Draft PR; non indebolire i test per ottenere una CI verde.

## Glossario

- **PM** — Project Manager
- **TM** — Team Member
- **RAD** — Requirements Analysis Document
- **SDD** — System Design Document
- **PR** — Pull Request
- **CI** — Continuous Integration

## Simulazione tutorial

Questa sezione documenta una prova del workflow agentico del Team C01.

I report AI supportano, ma non sostituiscono, la review umana indipendente.
