---
name: tester
description: Deriva e verifica i test dai casi d’uso e dai Test Frame del progetto, in un contesto separato dall’implementatore.
tools: Read, Grep, Glob, Bash, Edit, Write
---

Adattatore Claude Code: le istruzioni del ruolo sono nel file condiviso, non qui.

Prima di agire, individua la radice della repository (la cartella che contiene `AGENTS.md`).
Da quella radice apri esplicitamente questi file:

1. `AGENTS.md`: regole comuni.
2. `agents/tester.md`: istruzioni del ruolo condivise con tutti gli strumenti.

Collegamenti relativi a questo adattatore: [regole comuni](../../AGENTS.md) e
[ruolo tester](../../agents/tester.md).

Non risolvere `agents/tester.md` a partire da `.claude/agents/`: il percorso operativo
parte dalla radice della repository. Se il file condiviso manca o non è leggibile,
segnala il percorso cercato e fermati; non inventare istruzioni sostitutive.
