#!/usr/bin/env python3
"""Verifiche deterministiche dei file agentici e degli esempi didattici C01."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[2]
required = [
    'AGENTS.md', 'README.md', 'docs/processo-agentico.md',
    'docs/guida-operativa-team-agentic.md', 'docs/README.md',
    'docs/rad/C01_RAD.pdf', 'docs/sdd/C01_SDD.pdf',
    'docs/rad/uc/UC_XX_YY.md', 'docs/modelli/sdd/class.puml',
    'docs/test/CP_UC_XX.md', 'docs/test/TF_UC_XX.md',
    '.github/CODEOWNERS', '.github/ISSUE_TEMPLATE/task-agente.yml',
    '.github/ISSUE_TEMPLATE/bug.yml', '.github/ISSUE_TEMPLATE/config.yml',
    '.github/pull_request_template.md', '.github/workflows/ci.yml',
    '.github/workflows/piano.md', '.github/workflows/piano.lock.yml',
    '.github/agents/pianificatore.agent.md',
    '.github/agents/implementatore.agent.md',
    '.github/agents/tester.agent.md', '.github/agents/revisore.agent.md',
    '.github/scripts/bootstrap_labels.sh',
]
errors = [f'File mancante: {path}' for path in required if not (root / path).is_file()]
codeowners = (root / '.github/CODEOWNERS').read_text(encoding='utf-8')
if '* @Team-C01/developers' not in codeowners:
    errors.append('CODEOWNERS non assegna i file di default al team developers')
if '/.github/ @Antonio-Caiazzo' not in codeowners:
    errors.append('CODEOWNERS non protegge le configurazioni GitHub col PM')
workflow = (root / '.github/workflows/piano.md').read_text(encoding='utf-8')
if 'fase:piano' not in workflow or 'add-comment:' not in workflow:
    errors.append('Il workflow del Pianificatore non contiene trigger/safe output attesi')
for error in errors:
    print('ERRORE:', error, file=sys.stderr)
print(f'Controllati {len(required)} artefatti agentici, problemi: {len(errors)}')
raise SystemExit(bool(errors))
