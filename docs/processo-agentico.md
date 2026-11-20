# Workflow agentico — NeighborCare Team C01

## Riferimenti e decisioni dei PM

Questo flusso applica il tutorial "Agentic Workflow in Project Management" (slide 48–100). RAD e SDD versionati sono la **baseline definitiva di riferimento adottata dai PM**: [decisione operativa](BASELINE.md). Le diciture interne dei PDF e gli esempi didattici `XX/YY` non vanno interpretati come nuovi requisiti.

Gli agenti sono strumenti, non decisori: le persone determinano fasi, ambito, approvazioni, modifiche ai modelli e merge. Tutte le modifiche significative passano da Issue, branch e PR. La repository usa GitHub Copilot CLI `1.0.114` con `model=auto`, **senza il proxy `gh-aw` che falliva nei test**. Il Secret previsto è `COPILOT_GITHUB_TOKEN`. Non condividere PAT, non usare servizi a consumo esterni.

## Configurazione prima dell'uso

1. Un PM verifica il Secret Actions `COPILOT_GITHUB_TOKEN`. Può controllare il nome, non recuperarne il valore.
2. Un PM crea le label `task-agente`, `fase:piano`, `fase:implementazione`, `fase:test`, `fase:bloccato` con il workflow **Setup agentic labels - manual** (Actions → Run workflow → `approve=true`). La creazione è ripetibile e non chiama modelli.
3. Un PM verifica le regole di `main` in Settings → Rules: PR obbligatoria, una review umana valida, Code Owner review e controllo obbligatorio `repository-checks`. La configurazione dei Ruleset non è codificata nel repository e va abilitata nelle impostazioni GitHub.
4. Verificare che la squadra GitHub `@Team-C01/developers` abbia accesso Write e sia visibile per `CODEOWNERS`; aggiungere al file l'username GitHub del secondo PM **solo dopo verifica**.
5. Settings → Actions → General: permessi predefiniti in sola lettura, consentire a GitHub Actions di creare PR **solo se i PM autorizzano l'Implementatore automatico**. Le PR restano in Draft; il bot non le approva e non fa merge.

## 1. Pianificatore

- **Azione umana:** PM/TM apre una Issue dal form `task-agente` con riferimenti ai PDF RAD/SDD, UC, diagrammi, ambito, criteri di accettazione e Test Frame pertinenti. Per task documentali, N/A motivato.
- Aggiunge `fase:piano` all'Issue.
- `.github/workflows/piano-direct.yml`: verifica permessi e commenti esistenti, esegue Copilot CLI in sola lettura, valida l'output e pubblica **un unico commento** contenente il piano.
- Non modifica file. Se la label viene tolta, la pubblicazione viene bloccata. Se esiste già un piano, non richiama nuovamente il modello.

## 2. Approvazione esplicita e Implementatore

Il PM legge il piano e confronta il task con il RAD/SDD, le dipendenze e i Test Frame. Se è corretto, pubblica **un nuovo commento umano** dopo quello AI, con questo formato (esempio per una modifica documentale):

```text
APPROVAZIONE TM: piano per Issue #10 approvato.
File autorizzati: README.md
Note: nessuna nuova dipendenza o modifica ai modelli.
```

**Non usare gli esempi del saluto come requisiti di prodotto.** La riga `File autorizzati` contiene il percorso esatto di ogni file che l'Implementatore potrà toccare, separati da virgola, massimo 12 file. Non permettere file di governance, PDF RAD/SDD o file fuori dal piano. Attualmente il gate automatico riconosce l'account PM verificato `Antonio-Caiazzo`; aggiungere il secondo PM quando il suo login è confermato.

Uno sviluppatore autorizzato aggiunge `fase:implementazione` all'Issue **solo dopo questo commento**. Il workflow `.github/workflows/implementa.yml`:

- rifiuta l'esecuzione se mancano piano, approvazione PM o lista esatta dei file;
- esegue Copilot CLI senza shell e senza credenziali Git di scrittura, su un checkout temporaneo;
- scarta diff fuori ambito, file di governance, PDF, modifiche troppo grandi o dipendenze/app senza bootstrap;
- verifica collegamenti e build esistenti; consegna una patch limitata;
- un job separato, con permessi GitHub temporanei, crea `agent/issue-N-implementazione` e una **Draft PR** con `Closes #N`. Non integra il codice in `main`.

**Nota sul flusso GitHub:** se la PR viene creata dal `GITHUB_TOKEN`, gli eventi normali `pull_request` di quel token non avviano sempre la CI. È compito dello sviluppatore controllare e marcare la PR **Ready for review** dopo il Tester, in modo da avviare la CI e la Revisione. I PM devono verificare i permessi di creazione PR nelle impostazioni del repository.

## 3. Tester indipendente

Lo sviluppatore assegnato esamina la Draft PR e aggiunge la label `fase:test` **alla PR, non all'Issue**.

`.github/workflows/test.yml` opera su PR Draft dello stesso repository e controlla che la Issue collegata contenga Test Frame realmente definiti. Un'altra sessione Copilot, distinta dall'Implementatore, può aggiungere solo **nuovi file di test** nei percorsi previsti; non può modificare codice applicativo o test già presenti. Le modifiche vengono validate prima di un commit sul branch della PR.

Per una PR esclusivamente documentale il Tester non inventa JUnit: scrive il commento `Test Frame applicativi N/A` e il controllo effettivo è quello dei documenti. Se i test applicativi mancano, il task non è pronto al merge. Se un test fallisce si corregge il **codice**, non si indebolisce il test.

## 4. CI e Revisore

- Lo sviluppatore segna la PR **Ready for review**. La CI `.github/workflows/ci.yml` esegue sempre controlli repository e, solo quando esistono i progetti, build/test backend e frontend.
- `.github/workflows/revisione.yml` legge la diff della PR, il task e le istruzioni di revisione, con un nuovo contesto Copilot separato, e pubblica un **report AI**.
- Il report non costituisce Approve. Un membro del team diverso dall'autore esamina codice, modelli, copertura TF, build e dipendenze, poi approva o chiede modifiche su GitHub.
- Il merge resta **esclusivamente umano**, dopo controlli CI e review richiesti dal Ruleset.

I documenti PDF non vengono letti magicamente dalle automazioni: per requisiti complessi mettere nella Issue riferimenti precisi alle pagine e, quando serve, estratti testuali/versionati dei soli UC/diagrammi/TF pertinenti. Se la specifica non è fruibile dal ruolo, ci si ferma.

## Bootstrap di Spring Boot, React e PostgreSQL

**PM e team** confermano stack, versioni e contratti a partire dall'SDD. **Developers** preparano su branch dedicato `backend/pom.xml`, progetto Spring Boot e test di avvio, `frontend/package.json` con lockfile, configurazione database/dati sintetici, documentazione dei comandi e `.env.example` senza credenziali. Le nuove librerie necessitano di approvazione PM. La CI aggiunge controlli applicativi solo quando quei file esistono; non simula test inesistenti.

## Esempio pratico di collaudo

Issue #10 richiede un piccolo benvenuto nel README: PM aggiunge `fase:piano` → bot propone solo un piano → PM confronta e approva in un commento `APPROVAZIONE TM` con `File autorizzati: README.md` → sviluppatore avvia `fase:implementazione` → bot propone una sola modifica nella Draft PR → sviluppatore aggiunge `fase:test` alla PR → Tester segnala che i test applicativi sono N/A → sviluppatore seleziona Ready for review → CI e Revisore → un revisore **umano** approva → merge umano.

Per fare un collaudo vero **non basta che i file YAML esistano**: occorre verificare in GitHub Actions il run di ciascuna fase e l'effettiva presenza dei commenti/PR, prima di dichiarare il flusso completo funzionante.

## Costi e sicurezza

- Un solo tentativo automatico per Issue/PR per fase, salvo intervento PM; timeout 10–18 minuti, niente fallback a pagamento.
- Prompt injection: Issue, PR e diff trattati come dati non attendibili; generazione senza scrittura Git remota; pubblicazione separata con permessi minimi e validazioni.
- `GITHUB_TOKEN` temporaneo, Secret Copilot solo nello step AI, niente `pull_request_target`, niente push su `main`.
- Gli agenti non possono approvare, fare merge o decidere lo stack.
- Dopo tre tentativi falliti sullo stesso problema, escalation a un PM; no retry infiniti o cambi di test per farli passare.

## Stato della verifica

Il **Pianificatore diretto** è stato testato end-to-end sulla repository diagnostica personale `Antonio-Caiazzo/agentic-workflow`: piano pubblicato e duplicati evitati. Le altre fasi necessitano di un collaudo con approvazione umana, PR dedicata, Secret e regole GitHub della repository Team-C01: **non dichiararle funzionanti finché non vengono eseguite con esito positivo**.
