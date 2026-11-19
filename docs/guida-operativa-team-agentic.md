# NeighborCare C01 — Guida operativa al workflow agentico

> Basata sul tutorial GPS *Agentic Workflow in Project Management*, passi 1–17. Decisione operativa PM del 19/11/2026.

## Baseline e strumenti

- RAD definitivo: `docs/rad/C01_RAD.pdf`, v1.0; SDD definitivo: `docs/sdd/C01_SDD.pdf`, v0.0 (baseline stabilita dal PM). I PDF originali non si modificano.
- Gli esempi in `docs/rad/uc/`, `docs/modelli/`, `docs/test/` **non si eliminano e non sono requisiti implementabili**. Citare invece pagine/sezioni precise dei PDF definitivi.
- Repository GitHub: Issue Form `task-agente`, quattro Custom Agent in `.github/agents/`, CI in `.github/workflows/ci.yml`, CODEOWNERS, PR template, Project e labels.
- Frontend e backend non ancora inizializzati: per ora la CI controlla file, link Markdown, YAML, whitespace e struttura agentica; non dichiara build applicative superate.

## Ruoli e responsabilità

| Ruolo | Responsabilità e limiti |
| --- | --- |
| PM (Antonio + Emanuele) | Fissa perimetro/milestone, priorità, baseline, ruoli e guardrail; decide cambi architetturali; verifica costi, label, ruleset, board e review delle configurazioni. |
| Developers (team GitHub `Team-C01/developers`, 6 membri) | Aprono/aggiornano Issue, realizzano UC assegnati, verificano modelli, test e PR; sanno spiegare il codice; possono fare da TM/revisori quando designati. |
| TM assegnato (uno dei developer, nominato nella Issue) | Controlla specifiche e rischi, approva esplicitamente **il piano** tramite commento, autorizza implementazione/test e coordina le correzioni. |
| Pianificatore AI / persona | Legge Issue e modelli, segnala lacune, produce piano, non modifica file. |
| Implementatore AI / developer | Solo dopo approvazione TM lavora su branch, produce Draft PR, non fa merge. |
| Tester indipendente | Usa Test Frame dalla specifica in un contesto separato dall'implementatore, non cambia il codice per rendere verdi i test. |
| Revisore AI + revisore umano | L'AI segnala divergenze senza approvare; un altro membro umano approva la PR secondo ruleset/CODEOWNERS. |

Il gruppo CODEOWNERS è **un team GitHub**, non sei stringhe con nomi presunti. Verificare che `@Team-C01/developers` contenga i sei iscritti, sia visibile e disponga di accesso Write alla repository: altrimenti GitHub non assegna validamente la review. Basta una approvazione da un Code Owner previsto dalla regola, non da tutti e sei. `AGENTS.md`, `.github/`, `docs/rad/`, `docs/sdd/` e `docs/modelli/` sono sotto responsabilità del PM.

## Label da preparare una sola volta

| Label | Si applica a | Effetto attuale |
| --- | --- | --- |
| `task-agente` | Issue | Classifica il task creato dal form, nessuna AI. |
| `fase:piano` | Issue | **Avvia davvero `piano.lock.yml`**, attualmente guasto (HTTP 502). Non applicarla o riapplicarla fino alla correzione; nel frattempo pianificazione manuale/VS Code. |
| `fase:implementazione` | Issue | Tracciamento dell'approvazione TM; nessun workflow implementatore automatico attivo. |
| `fase:test` | PR | Tracciamento dell'autorizzazione test; nessun workflow tester automatico attivo. |
| `fase:revisione` | PR | Tracciamento della review; evento `ready_for_review` alimenta i controlli CI esistenti. |
| `fase:bloccato` | Issue | Specifica/dipendenza mancante o escalation dopo 3 fallimenti. |

Per crearle senza cambiare label esistenti: `bash .github/scripts/bootstrap_labels.sh --apply` dopo merge della PR. Senza `--apply` lo script è solo una simulazione. **L'esistenza delle label non implica che tutti gli agenti siano automatici.**

## Sequenza pratica (PM e team)

1. **PM/TM — Task:** aprire Issues → New issue → Task per agente. Compilare ID UC/requisito, TM, obiettivo, pagine RAD/SDD, classi/file, esiti attesi, Test Frame, dipendenze. Per task documentali usare N/A motivato.
2. **Pianificazione:** assegnare a un developer il ruolo `pianificatore` in Copilot VS Code, in sola lettura. Pubblicare un commento `## Piano proposto` nella Issue, riportando file, metodi, passi, test e rischi. Non usare ancora `fase:piano` per riavviare l'AI guasta.
3. **TM — Gate umano:** leggere piano e modelli; se coerente commentare `APPROVO il piano versione/data della Issue #N. Autorizzo implementazione entro l'ambito indicato.`. Solo allora usare `fase:implementazione` come traccia del passaggio.
4. **Developer/Implementatore:** creare `feat/issue-N-descrizione` da `main`, implementare solo il piano, aggiornare modelli coinvolti nella stessa PR, eseguire verifiche reali, aprire Draft PR con `Refs #N` o `Closes #N` se chiude il task.
5. **TM — Test:** scegliere persona/sessione indipendente; aggiungere `fase:test` **alla PR**. Derivare un test per ogni Test Frame; se test fallisce, correggere il codice, non gli esiti attesi.
6. **Developer — Review:** passare Draft PR a Ready for review; la CI deterministica parte anche all'evento `ready_for_review`. Usare `fase:revisione` solo come traccia e richiedere una review umana diversa dall'autore.
7. **Code Owner/PM:** verificare diff, modelli, CI, test, sicurezza e dichiarazione dell'autore. `Approve` umano e merge autorizzato solo se le regole di `main` sono soddisfatte.
8. **PM/TM:** aggiornare GitHub Project/Trello e chiudere la Issue (se non chiusa dal `Closes #N` al merge). Registrare tempi, problemi, tentativi e decisioni.

## Ruleset e board: controllo manuale del PM

- GitHub Settings → Rules → Rulesets → protezione di `main`: stato Active; blocco force push e cancellazione, PR obbligatoria, almeno 1 approval, dismiss stale reviews, `Require review from Code Owners` e status check `repository-checks` **solo dopo averne verificato il nome esatto e che la CI sia verde**.
- Nella board GitHub Projects usare, se utile, colonne `Da pianificare`, `Piano`, `Implementazione`, `Test`, `Revisione`, `Fatto`; collegare Issue e PR. Le etichette da sole non spostano la board se manca un'automazione configurata.
- Controllare che il team GitHub `Team-C01/developers` sia effettivamente composto dai 6 sviluppatori e abbia Write. Il secondo PM può essere aggiunto come CODEOWNER quando si dispone del suo username GitHub verificato.

## Stato degli automatismi e costi

- **Pronto:** form Issue, agent file, CI, CODEOWNERS (previa verifica team e ruleset), PR template, etichette via script.
- **Non funzionante:** `piano.lock.yml` con Copilot/gh-aw: almeno quattro run HTTP 502 il 19/11/2026. Non riprovare finché non viene documentata una correzione, rispettando il limite di tre tentativi su uno stesso errore.
- **Non ancora attivati:** workflow AI `implementa.yml`, `test.yml`, `revisione.yml`, agente su richiesta. Non aggiungere finti workflow verdi o chiamate API AI a pagamento; saranno progettati, controllati e abilitati soltanto quando `piano` sarà affidabile e i PM li autorizzeranno.
- **Fallback operativo:** Custom Agents di VS Code/CLI in sessioni separate, con gli stessi gate di approvazione e tracciabilità su Issue e PR.

## Checklist pre-implementazione

- [ ] RAD/SDD citati con versione e pagina; eventuali ambiguità risolte tramite decisione tracciata.
- [ ] Issue assegnata a un TM e piano pubblicato.
- [ ] Commento di approvazione TM registrato prima delle modifiche.
- [ ] Branch dedicato, PR in bozza, scope limitato e nessun segreto.
- [ ] Test Frame pertinenti e risultati reali riportati; nessun test indebolito.
- [ ] CI verde, CODEOWNER e revisore umano autorizzati, ruleset efficace.
- [ ] Nessun merge AI e registrazione di esiti/decisioni in Project.
