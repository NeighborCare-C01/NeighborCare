# NeighborCare — Team C01

Progetto universitario di Ingegneria del Software e Gestione dei Progetti Software, Università di Salerno. NeighborCare mette in relazione Beneficiari e Neighbor verificati per commissioni non sanitarie, con supervisione dei Coordinatori.

## Documenti e struttura

Per decisione operativa dei PM del **20 novembre 2026**, [RAD](docs/rad/C01_RAD.pdf) e [SDD](docs/sdd/C01_SDD.pdf) versionati sono la baseline definitiva per lo sviluppo. I PDF restano invariati, comprese eventuali diciture REVIEW/DRAFT: la decisione non introduce firme o revisioni editoriali. Discrepanze fra modelli e dettagli tecnici mancanti si risolvono con una decisione tracciata prima del codice.

- [AGENTS.md](AGENTS.md): unica fonte delle regole comuni.
- [.claude/agents/tester.md](.claude/agents/tester.md) e [revisore.md](.claude/agents/revisore.md): ruoli del tutorial, leggibili anche dagli altri strumenti.
- [.github/agents/](.github/agents/): profili Copilot necessari alla pipeline adottata, subordinati alle regole comuni.
- [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/), [template PR](.github/pull_request_template.md) e [CODEOWNERS](.github/CODEOWNERS): tracciabilità e responsabilità.
- [docs/README.md](docs/README.md): guida a `docs/rad/uc/`, `docs/sdd/`, `docs/modelli/` e `docs/test/`.
- [.github/workflows/](.github/workflows/): Pianificatore, Implementatore, Tester, Revisore e CI. Gli script richiamati sono in [.github/scripts/](.github/scripts/).

Gli script Python sono parte dei controlli esistenti e usano solo la libreria standard:

- `check_repository.py`: verifica i collegamenti Markdown locali (non URL remoti o anchor).
- `prepare_plan.py` e `validate_plan.py`: preparano il contesto e validano il piano prima della pubblicazione.
- `agent_changes.py`: prepara i task di implementazione/test e blocca modifiche fuori ambito.
- `prepare_review.py`: prepara e valida il report del revisore.
- `test_plan.py` e `test_agent_pipeline.py`: verificano offline i vincoli degli script, senza chiamare modelli.


**Conservare tutti i template didattici**: UC, UML, Category Partition e Test Frame con XX/YY aiutano i ragazzi a organizzare gli artefatti, ma non sono requisiti reali. Il Class Diagram di implementazione è solo quello ristrutturato dell'SDD. Per un task reale citare UC, pagine/versioni dei PDF e modelli pertinenti; se il contenuto non è fruibile dall'agente, fornire una trasposizione approvata o fermarsi.

`CLAUDE.md`, `GEMINI.md` e l'adattatore Copilot rinviano ad AGENTS.md. Trello resta il coordinamento operativo e Ganttfather la pianificazione.

## Workflow del team

Il PM definisce le fasi; il TM assegna il lavoro e approva i passaggi. Gli agenti non decidono autonomamente ambito, stack o merge. Si usa Copilot CLI con il secret Actions esistente `COPILOT_GITHUB_TOKEN`, mai credenziali nel codice; niente API AI esterne a consumo o fallback a pagamento. Chi non dispone di Copilot può seguire manualmente lo stesso processo con gli strumenti scelti dal TM.

| Fase | Azione umana e automazione configurata |
| --- | --- |
| Issue e piano | Aprire il modulo Task con riferimenti e criteri, poi applicare `fase:piano` all'Issue. [piano.yml](.github/workflows/piano.yml) verifica l'attore autorizzato e propone un unico piano in commento, senza modifiche. |
| Approvazione e implementazione | Il PM approva in un nuovo commento umano, poi il TM applica `fase:implementazione` all'Issue. [implementa.yml](.github/workflows/implementa.yml) valida approvazione e file autorizzati, genera una patch limitata e propone una Draft PR su branch dedicato. |
| Tester indipendente | Dopo controllo della Draft PR, applicare `fase:test` alla PR. [test.yml](.github/workflows/test.yml) usa un contesto separato per nuovi test derivati da UC/TF, senza modificare codice o test esistenti. Per attività documentali motiva i test applicativi N/A. |
| CI e revisione | Lo sviluppatore seleziona Ready for review. [ci.yml](.github/workflows/ci.yml) verifica link, sintassi YAML, guardrail e diff del repository; [revisione.yml](.github/workflows/revisione.yml) produce un report AI, senza approvare. |
| Review umana e merge | Un membro diverso dall'autore verifica modelli, diff, test, dipendenze e CI. Il merge resta umano e soggetto al Ruleset. |

Formato del commento di approvazione richiesto dall'automazione (esempio documentale):

```text
APPROVAZIONE TM: piano per Issue #N approvato.
File autorizzati: README.md
Note: nessuna nuova dipendenza o modifica ai modelli.
```

`#N` va sostituito con il numero reale. `File autorizzati` contiene percorsi esatti separati da virgola, massimo 12; niente file di governance, PDF o file fuori piano. Il gate attuale riconosce il PM verificato `Antonio-Caiazzo`: aggiungere altri PM solo dopo verifica dei login. Il Tester non deve inventare gli esiti dal codice; se un test fallisce, segnalare il difetto senza indebolire il test.

Prima dell'uso, un PM verifica accessi Write del team, secret esistente e label `task-agente`, `fase:piano`, `fase:implementazione`, `fase:test`; `fase:bloccato` segnala intervento umano. Le label si gestiscono dalle impostazioni GitHub, come nel tutorial, senza un workflow aggiuntivo di provisioning. Le PR create dal token del bot possono richiedere il passaggio umano Ready for review per avviare i controlli successivi.

Verificare inoltre in GitHub: PR obbligatorie e review umana su main, accesso del team CODEOWNERS, controllo `repository-checks` dopo il primo run valido e permessi di creazione PR autorizzati dai PM. Questi file non dimostrano che i Ruleset siano attivi. I profili dei ruoli non concedono permessi aggiuntivi.

## Quando inizierà il codice applicativo

Il codice non è ancora inizializzato. Lo stack dell'SDD è React/PWA, Java/Spring Boot e PostgreSQL Three-Tier. Prima di creare `backend/` e `frontend/`, PM e referenti tecnici approvano in Issue versioni, dipendenze, package, contratti API, configurazione e comandi di build/test. Nessuna versione o dipendenza è decisa da questa pulizia.

Il bootstrap seguirà lo stesso processo con piano, Draft PR, test e review. I comandi applicativi vanno aggiunti alla CI soltanto quando esisteranno manifest e test reali. Attualmente `ci.yml` contiene solo i controlli del repository; le verifiche applicative delle altre fasi restano condizionate alla presenza dei manifest.

## Limiti e verifica

Issue, commenti e diff sono input non attendibili: i workflow separano generazione e pubblicazione, validano i file autorizzati e usano permessi minimi. Niente `pull_request_target`, push su main, auto-approvazioni o merge dell'agente. Un tentativo automatico per fase salvo intervento PM; dopo tre fallimenti sullo stesso problema serve escalation umana.

La CI deterministica non chiama modelli. Copilot e Actions hanno quote diverse, da verificare prima dell'uso senza abilitare spesa extra. I log locali scaricati sono diagnostica e non vanno versionati.

Il Pianificatore diretto è stato collaudato sulla repository diagnostica personale; non estendere automaticamente tale esito a tutte le fasi di NeighborCare. Per dichiarare il flusso completo funzionante servono run reali, piano pubblicato, approvazione umana, Draft PR, Tester, CI e Revisore, poi review e merge umani. Questa pulizia non avvia alcuna fase AI o servizio.
