#!/usr/bin/env bash
set -euo pipefail
# Bootstrap non distruttivo delle label del tutorial GPS. Di default mostra soltanto il piano.
repo='Team-C01/NeighborCare'
apply=false
case "${1:-}" in
  --apply) apply=true ;;
  ''|--dry-run) ;;
  *) echo 'Uso: bash .github/scripts/bootstrap_labels.sh [--dry-run|--apply]' >&2; exit 2 ;;
esac
if "$apply"; then
  command -v gh >/dev/null || { echo 'GitHub CLI (gh) non installata' >&2; exit 1; }
  existing="$(gh label list --repo "$repo" --limit 100 --json name --jq '.[].name')"
fi
while IFS='|' read -r name color description; do
  [[ -n "$name" ]] || continue
  if ! "$apply"; then
    printf 'DRY-RUN: verifica/crea %-24s %s\n' "$name" "$description"
  elif printf '%s\n' "$existing" | grep -Fxq "$name"; then
    printf 'ESISTE: %s (non modificata)\n' "$name"
  else
    gh label create "$name" --repo "$repo" --color "$color" --description "$description"
    printf 'CREATA: %s\n' "$name"
  fi
done <<'LABELS'
task-agente|0E8A16|Task guidato da agenti e revisione umana
fase:piano|FBCA04|Pianificazione richiesta - gh-aw attualmente sospeso per HTTP 502
fase:implementazione|1D76DB|Piano approvato dal TM - fase implementazione
fase:test|5319E7|Test indipendenti autorizzati sulla PR
fase:revisione|0E8A16|PR pronta per review umana e CI
fase:bloccato|D93F0B|In attesa di specifiche o escalation umana
LABELS
echo 'Label pronte o verificate. Le label non abilitano automaticamente gli agenti mancanti.'
