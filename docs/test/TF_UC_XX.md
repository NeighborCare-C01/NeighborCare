# Test Frame — UC_XX

> **ESEMPIO INVENTATO E SEMPLIFICATO:** questi frame spiegano come verificare “Invia un saluto”. Non sono test di NeighborCare e non sono stati eseguiti.

Fonti didattiche: [UC_XX](../rad/uc/UC_XX_YY.md) e [Category Partition](CP_UC_XX.md).

## Esempio

Precondizione comune: schermata del saluto aperta. Azione comune: inserire il dato e premere “Saluta”.

| ID frame | Scelta CP | Input | Risultato atteso | Fonte UC |
| --- | --- | --- | --- | --- |
| TF_XX_01 | C1.1 | `Ada` | Mostra “Ciao, Ada!”. | Passi 3–4 |
| TF_XX_02 | C1.2 | `""` | Mostra “Inserisci un nome”; nessun saluto generato. | Eccezione 3.e1 |
| TF_XX_03 | C1.3 | `"   "` | Mostra “Inserisci un nome”; nessun saluto generato. | Eccezione 3.e1 |

Per esempio, il futuro test automatico associato a `TF_XX_01` inserirebbe “Ada”, premerebbe “Saluta” e verificherebbe il testo mostrato. Questo file documenta il frame, non implementa il test.

Nel progetto reale usare i frame del team e collegare ogni test ai relativi ID. L’esito atteso deve provenire dalla specifica approvata.
