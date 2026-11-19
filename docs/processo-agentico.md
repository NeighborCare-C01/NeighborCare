# Workflow agentico — NeighborCare C01

## Scopo e limiti

Questa procedura adatta le slide 54–114 del corso GPS. Il **PM fissa le fasi** e il **TM assegna il lavoro e approva i passaggi critici**. Gli agenti non determinano in autonomia lo stato del task. Copilot è opzionale: chi non vi ha accesso può seguire lo stesso processo manualmente.

I Custom Agent Copilot sono in `.github/agents/` e riusano le regole comuni `AGENTS.md`. Sono profili, **non** workflow Actions. La presenza dei profili non avvia autonomamente task né garantisce permessi tecnici. Non è installata un'integrazione API per modelli a pagamento.

## Fasi per una funzionalità

1. **Issue e modelli — PM/TM:** aprire `task-agente` indicando UC/requisiti, versione e approvazione di RAD/SDD, file UML, ambito e Test Frame reali. Eventuali file didattici non sono fonti approvate.
2. **Piano — Pianificatore:** in sola lettura confrontare i modelli e proporre file, metodi, dipendenze, test, rischi. Registrare il piano nella Issue; se i modelli sono incoerenti sospendere il task.
3. **Approvazione — TM assegnato:** commentare esplicitamente che il piano (con versione/data) è approvato; solo allora autorizzare l'Implementatore. La label `fase:implementazione` è una traccia, non un trigger AI automatico.
4. **Implementazione — Implementatore:** lavorare su branch dedicato, rispettare il piano e produrre una **Draft PR** collegata alla Issue. Nessuna modifica autonoma ai modelli o allo stack.
5. **Testing — Tester indipendente:** il TM autorizza la fase; il Tester usa UC e Test Frame approvati, scrive un test per frame in un contesto separato e segnala i fallimenti senza rendere i test artificialmente verdi.
6. **Review — CI e Revisore:** la PR viene marcata Ready for review. La CI esegue i controlli disponibili; il Revisore legge diff e modelli e produce rilievi senza modifiche.
7. **Approvazione umana e merge:** un altro membro esegue una review GitHub **Approve**, controlla CI e conformità ai modelli. Merge solo dopo le condizioni del Ruleset; mai da parte dell'agente.
8. **Tracciabilità:** la PR registra Issue, UC, riferimenti dei modelli, Test Frame, esiti, approvazioni e limiti. Aggiornare Trello/Project manualmente secondo gli accordi del team.

Per ogni fase usare una sessione separata quando serve indipendenza. In assenza di un agente Copilot abilitato si possono utilizzare manualmente i file `agents/tester.md` e `agents/revisore.md`.

## Automazioni effettivamente presenti

- `.github/workflows/ci.yml`: solo controlli deterministici delle Pull Request su `main` (collegamenti locali Markdown, sintassi YAML, spazi superflui nelle modifiche, working tree pulito).
- **Non** sono configurati workflow a pagamento `piano.yml`, `implementa.yml`, `test.yml`, `revisione.yml` con chiamate ai modelli; le fasi sono avviate dai TM.
- Quando esisteranno `backend/pom.xml` e `frontend/package.json` con stack e comandi approvati, aggiungere alla CI build e test pertinenti; non simulare verifiche inesistenti.
- Aggiungere lo status check `repository-checks` come obbligatorio nel Ruleset di `main` **dopo** la prima esecuzione corretta.
- `.github/CODEOWNERS` identifica il PM iniziale per le configurazioni sensibili; attivare la review obbligatoria dei Code Owner solo dopo aver verificato account e organizzazione del team.

## Governance e costi

- I Custom Agent consumano le quote dell'account Copilot che li usa, nei limiti del piano disponibile. La pubblicità della repository non rende i crediti AI illimitati.
- Non creare secret AI, non acquistare crediti o attivare fallback a pagamento. Il budget Actions dell'organizzazione deve restare controllato.
- Le Actions non devono usare `pull_request_target` per eseguire codice della PR. Il token CI è in sola lettura e non esegue commit, push, merge o commenti.
- Tre tentativi falliti sullo stesso problema richiedono escalation umana. Le PR generate devono essere comprese e spiegate dal loro responsabile.
- Il Ruleset attivo protegge `main` con una review umana; non introdurre bypass senza decisione esplicita dei PM.

## Prima prova

Usare una Issue documentale delimitata e riferimenti **didattici dichiarati**, senza implementarli come funzionalità del prodotto. Passare da piano, approvazione, branch, Draft PR, verifica CI, review umana e merge. Solo dopo usare un UC reale con i modelli e Test Frame approvati.

Riferimenti: `AGENTS.md`, `docs/README.md`, slide 54–114 del corso, guida GitHub Custom Agents e GitHub Actions.
