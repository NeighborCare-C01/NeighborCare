# Category Partition — UC_XX

> **ESEMPIO INVENTATO E SEMPLIFICATO:** riguarda “Invia un saluto”, non NeighborCare. Mostra come dividere gli input in categorie e scelte.

Fonte didattica: [UC_XX – Invia un saluto](../rad/uc/UC_XX_YY.md), passo 3 ed eccezione 3.e1.

## Esempio

**Categoria C1: contenuto del campo nome**

| ID scelta | Scelta | Dato di esempio |
| --- | --- | --- |
| C1.1 | Nome non vuoto dopo la rimozione degli spazi esterni | `Ada` |
| C1.2 | Campo vuoto | `""` |
| C1.3 | Solo spazi | `"   "` |

**Vincolo:** le tre scelte sono mutuamente esclusive per un singolo input. In questo esempio esiste una sola categoria, quindi ciascun frame seleziona una sola scelta.

I [Test Frame](TF_UC_XX.md) indicano i risultati attesi. Nel progetto reale sostituire categoria, scelte e vincoli con l’analisi del team e mantenere gli ID approvati.
