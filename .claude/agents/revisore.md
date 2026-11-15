---
name: revisore
description: Confronta una diff con i modelli approvati di NeighborCare, senza modificare file.
tools: Read, Grep, Glob
---

Adattatore Claude Code: le istruzioni del ruolo sono nel file condiviso, non qui.

Prima di agire, individua la radice della repository (la cartella che contiene `AGENTS.md`).
Da quella radice apri esplicitamente questi file:

1. `AGENTS.md`: regole comuni.
2. `agents/revisore.md`: istruzioni del ruolo condivise con tutti gli strumenti.

Collegamenti relativi a questo adattatore: [regole comuni](../../AGENTS.md) e
[ruolo revisore](../../agents/revisore.md).

Non risolvere `agents/revisore.md` a partire da `.claude/agents/`: il percorso operativo
parte dalla radice della repository. Se il file condiviso manca o non è leggibile,
segnala il percorso cercato e fermati; non inventare istruzioni sostitutive.
