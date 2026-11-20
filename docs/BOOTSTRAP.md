# Bootstrap applicativo NeighborCare — ripartizione delle responsabilità

La pipeline GitHub non sostituisce il setup dell'applicazione: **PM = decisione e controllo; Developers = implementazione e verifica**. La fonte architetturale è l'SDD, adottato come baseline operativa dei PM ([BASELINE.md](BASELINE.md)).

## Prima della prima PR applicativa — PM con referenti tecnici

- Confermare in Issue una decisione di stack con versioni esplicite di Java, Spring Boot, Node.js, React e PostgreSQL, motivando eventuali varianti.
- Concordare identificativo base Java/package, strumenti di build e lockfile, configurazione di sviluppo, regole CORS, database e contratti iniziali delle API.
- Decidere chi mantiene i moduli condivisi (entity/domain, storage, interfacce) e dove si trovano.
- Valutare licenza, manutenzione, sicurezza e necessità di ogni nuova dipendenza. **Nessuna dipendenza scelta autonomamente dall'AI.**
- Confermare Java/Node version come repository variables `NEIGHBORCARE_JAVA_VERSION` e `NEIGHBORCARE_NODE_VERSION` quando approvate.
- Registrare criteri di accettazione: avvio locale riproducibile, build verde, test smoke, niente credenziali versionate.

## PR di bootstrap backend — Developers

- Creare in `backend/` il progetto Spring Boot coerente con l'SDD, `pom.xml` (e preferibilmente Maven Wrapper), file `src/main` e `src/test`.
- Aggiungere un test di avvio/smoke, distinguendo logica business dalla configurazione.
- Documentare `mvn verify` e avvio, e configurare i profili con segreti solo da variabili d'ambiente.
- Rifiutare dipendenze non approvate, test disabilitati e dati reali nel repo.

## PR di bootstrap frontend — Developers

- Creare in `frontend/` React/PWA con gli strumenti approvati, `package.json` e **`package-lock.json`**.
- Aggiungere script `build`, `test`, un test smoke minimo e documentare comandi `npm ci`, `npm run build`, `npm test -- --run` (o adeguare CI e documentazione al test runner scelto).
- Predisporre le impostazioni API senza hardcodare credenziali, configurazione e variabili d'ambiente documentate.

## Database e ambiente — Developers con approvazione PM

- Preparare PostgreSQL e ambiente riproducibile, opzionalmente Docker Compose **solo se approvato**.
- Aggiungere `.env.example` con segnaposto non sensibili, migrazioni/schema tracciati e dati sintetici per sviluppo/test.
- Verificare sul PC di almeno un altro membro oltre all'autore.

## Rilasci e gate

1. PM/TM approva piano e cambi di stack.
2. Developers realizzano ciascun bootstrap su **branch dedicato e Draft PR**.
3. CI esegue controlli tecnici realmente presenti; finché mancano `pom.xml` e `package.json`, riporta esplicitamente lo skip.
4. Tester indipendente verifica criteri e regressioni, revisore umano esamina dipendenze e conformità al deployment SDD.
5. Merge umano, mai automatico.

Nessuna delle PR di bootstrap deve cancellare gli esempi didattici in `docs/` né sostituire i PDF RAD/SDD originali.
