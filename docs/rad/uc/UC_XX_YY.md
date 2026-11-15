# UC_XX – YY

> **ESEMPIO INVENTATO E SEMPLIFICATO:** “Invia un saluto”. Serve solo a mostrare come compilare e collegare i file. Non proviene dal RAD e non è una funzionalità di NeighborCare.

Per un UC reale, sostituire questo contenuto con quello del RAD, rinominare il file con ID e nome originali e aggiornare i collegamenti. Fonte di questo esempio: nessuna, contenuto didattico.

## Esempio: Invia un saluto

| Campo | Esempio compilato |
| --- | --- |
| Identificativo | UC_XX (ID didattico) |
| Nome | Invia un saluto |
| Descrizione | L’utente inserisce il proprio nome e riceve un saluto sullo schermo. |
| Attore principale | Utente |
| Attori secondari | Nessuno |
| Entry condition | La schermata del saluto è aperta. |
| Exit condition on success | Il sistema mostra il saluto con il nome inserito. |
| Exit condition on failure | Il sistema mostra “Inserisci un nome” e non genera il saluto. |
| Extension point | Nessuno nell’esempio. |
| Requisiti speciali | Nessuno nell’esempio. |

### Flusso principale

1. **Utente:** inserisce il nome “Ada”.
2. **Utente:** preme “Saluta”.
3. **Sistema:** rimuove gli spazi iniziali e finali dal nome e verifica che non sia vuoto.
4. **Sistema:** genera e mostra “Ciao, Ada!”.

### Eccezione 3.e1 – Nome vuoto

Se al passo 3 il nome è vuoto, anche dopo la rimozione degli spazi, il sistema mostra “Inserisci un nome”. L’utente può correggere il campo e ripartire dal passo 1.

## Artefatti collegati all’esempio

- [Use Case Diagram](../../modelli/rad/UCD_XX.puml): chi usa la funzione.
- [Sequence Diagram](../../modelli/rad/SQ_XX_YY.puml): ordine delle interazioni.
- [Statechart](../../modelli/rad/ST_XX_YY.puml): stati della schermata.
- [Activity del sistema proposto](../../modelli/rad/AD_XX_SistemaProposto.puml): passi e decisione sul nome vuoto.
- [Navigational Path](../../modelli/rad/NP_XX_YY.puml): navigazione tra le schermate.
- [Class Diagram SDD](../../modelli/sdd/class.puml): unico riferimento per classi e metodi dell’esempio.
- [Dipendenze dei sottosistemi SDD](../../modelli/sdd/Sottosistemi_XX_YY.puml): organizzazione logica dell’esempio.
- [Deployment Diagram SDD](../../modelli/sdd/Deployment_XX_YY.puml): dove vengono eseguiti i componenti e come comunicano.
- [Category Partition](../../test/CP_UC_XX.md) e [Test Frame](../../test/TF_UC_XX.md): come verificare il comportamento descritto.

Nel progetto vero gli ID UC e SQ possono essere diversi: usare quelli originali, senza rinumerarli.

Per distinguere le viste, il diagramma del sistema attuale reale si consulta nel [RAD §2.2, p. 8](../C01_RAD.pdf#page=8); non è un esempio del saluto. L’[esempio generico a tre livelli](../../modelli/sdd/Livelli_XX_YY.puml) è invece una vista didattica autonoma rispetto a questo UC.
