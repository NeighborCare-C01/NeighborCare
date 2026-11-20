# NeighborCare — Team C01

Progetto universitario di Ingegneria del Software e Gestione dei Progetti Software, Università di Salerno. NeighborCare supporta commissioni di vicinato non sanitarie tra Beneficiari e Neighbor, con supervisione dei Coordinatori.

## Dove lavorare

- [frontend/](frontend/): destinazione del frontend React/PWA.
- [backend/](backend/): destinazione del backend Java/Spring Boot.
- [docs/README.md](docs/README.md): indice di UC, UML, Category Partition e Test Frame, con PDF RAD/SDD e convenzioni.
- [AGENTS.md](AGENTS.md): contesto, stack, comandi disponibili e regole comuni per Copilot.
- [.github/agents/](.github/agents/): i quattro ruoli Copilot, adattati alle slide del professore.
- [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/), [template PR](.github/pull_request_template.md) e [CODEOWNERS](.github/CODEOWNERS): task, tracciabilità e responsabilità.

Frontend e backend sono ancora vuoti: ogni cartella contiene solo `.gitkeep` per renderla versionabile. Versioni, dipendenze, manifest e comandi applicativi saranno introdotti con un piano tecnico approvato, coerente con l'SDD.

**Conservare tutti gli esempi didattici UC/UML/CP/TF in docs/**: i file XX/YY e il Class Diagram esemplificativo spiegano il formato ai ragazzi, senza definire requisiti reali. I PDF restano invariati; la decisione sulla baseline è riportata in AGENTS.md. Il Class Diagram per l'implementazione è quello ristrutturato dell'SDD.

## Ruoli e workflow Copilot

Le slide 42–45 descrivono AGENTS.md e i ruoli; le slide 79–86 descrivono le fasi. Qui i profili sono in `.github/agents/`, la cartella Copilot indicata nella slide 45. Non occorrono adattatori per altri assistenti.

| Fase | Ruolo e azione |
| --- | --- |
| Piano | Il TM apre una Issue con specifiche e criteri, poi applica `fase:piano`. [piano.yml](.github/workflows/piano.yml) usa [pianificatore.agent.md](.github/agents/pianificatore.agent.md) per proporre un piano senza modifiche. |
| Implementazione | Dopo l'approvazione umana registrata nella Issue, il TM applica `fase:implementazione`. [implementa.yml](.github/workflows/implementa.yml) segue [implementatore.agent.md](.github/agents/implementatore.agent.md), limita i file e pubblica una Draft PR su branch dedicato. |
| Test indipendenti | Il TM applica `fase:test` alla Draft PR. [test.yml](.github/workflows/test.yml) segue [tester.agent.md](.github/agents/tester.agent.md) in una sessione separata: un test per frame, esiti attesi dalle specifiche. Per task documentali i test applicativi sono N/A motivato. |
| CI e revisione | Ready for review avvia [revisione.yml](.github/workflows/revisione.yml) con [revisore.agent.md](.github/agents/revisore.agent.md); [ci.yml](.github/workflows/ci.yml) controlla link, YAML, guardrail e diff sulle PR verso main. |
| Decisione umana | Un revisore diverso dall'autore verifica specifiche, diff, test e CI. Approvazione e merge restano umani, nel rispetto del Ruleset. |

Il commento di approvazione richiesto dall'Implementatore usa questo formato (sostituire N e indicare i file reali):

```text
APPROVAZIONE TM: piano per Issue #N approvato.
File autorizzati: README.md
Note: nessuna nuova dipendenza o modifica ai modelli.
```

Il gate attuale riconosce il PM verificato `Antonio-Caiazzo`; altri account vanno aggiunti dopo verifica. I percorsi autorizzati sono esatti, separati da virgola, massimo 12. I file di governance e i PDF sono esclusi dall'implementazione automatica.

Prima dell'uso il PM verifica accessi Write, label `task-agente`, `fase:piano`, `fase:implementazione`, `fase:test`, secret Actions esistente `COPILOT_GITHUB_TOKEN` e permessi di creazione PR. `fase:bloccato` serve a segnalare un impedimento. Le label si gestiscono in GitHub senza workflow di provisioning.

## Perché rimangono gli script Python

Sono tutti usati dalla pipeline, senza dipendenze Python esterne:

| Script in .github/scripts/ | Uso |
| --- | --- |
| `check_repository.py` | Controlla i link Markdown locali in CI e dopo le modifiche; non verifica URL remoti o anchor. |
| `prepare_plan.py`, `validate_plan.py` | Preparano il contesto del Pianificatore e validano il commento prima della pubblicazione. |
| `agent_changes.py` | Prepara Implementatore/Tester e verifica che la patch rispetti i file autorizzati. |
| `prepare_review.py` | Prepara il contesto indipendente e valida il report del Revisore. |
| `test_plan.py`, `test_agent_pipeline.py` | Verificano offline i guardrail in CI senza chiamare modelli. |

I workflow caricano il testo dei profili nei prompt; i limiti operativi sono imposti anche dagli argomenti CLI, dai controlli della patch e dai permessi GitHub. La richiesta al Tester di non leggere i corpi implementati resta un'istruzione da controllare in review, non un isolamento tecnico del codice.

## Verifiche e limiti

La CI deterministica non usa AI e attualmente non esegue build applicative: mancano manifest e codice. Gli eventuali comandi applicativi delle altre fasi richiedono un bootstrap approvato e dovranno essere adeguati al progetto effettivo.

La pipeline usa Copilot CLI già configurato; non introduce chiavi API AI esterne, servizi a consumo o fallback a pagamento. Il PM verifica idoneità e quote Copilot/Actions senza abilitare spesa extra. Generazione e pubblicazione sono separate; non usare push diretto su main, autoapprovazioni o merge automatici.

Verificare in GitHub Ruleset, review umana e controllo obbligatorio `repository-checks`: la presenza dei file non dimostra che le impostazioni siano attive. Una PR del bot può richiedere il passaggio umano Ready for review per avviare i controlli successivi.

Il collaudo offline degli script non dimostra il funzionamento completo della pipeline AI: per quello servono run reali e approvazioni umane su ciascuna fase. Questa modifica non avvia chiamate ai modelli.
