#!/usr/bin/env bash
# Rebuild ARAA.pdf from docs/position-paper.md (needs pandoc and xelatex).
# Usage: tools/build_pdf.sh [output.pdf]
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="${1:-ARAA.pdf}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Drop the Jekyll front matter and the two title lines, and point relative
# links at the website so they work in the PDF.
awk 'BEGIN{fm=0} /^---$/ && fm<2 {fm++; next} fm>=2' docs/position-paper.md \
  | sed -e '/^# ARAA: Advancements in Research by Autonomous Agents$/d' -e '/^## A Position Paper$/d' \
  | sed -E 's#\]\(([a-z-]+)\.md\)#](https://araa.alexandroszenonos.com/docs/\1)#g' \
  > "$TMP/paper.md"

cat > "$TMP/meta.yaml" <<'YAML'
title: "ARAA: Advancements in Research by Autonomous Agents"
subtitle: "A Position Paper (version 2)"
author:
  - "Alexandros Zenonos (ARAA Initiative, github.com/alezenonos)"
  - "Azenagentbot (ARAA Initiative, autonomous agent co-author)"
date: "November 2026"
geometry: margin=2.5cm
fontsize: 11pt
mainfont: "DejaVu Serif"
sansfont: "DejaVu Sans"
monofont: "DejaVu Sans Mono"
colorlinks: true
linkcolor: blue
urlcolor: blue
YAML

pandoc -f markdown+lists_without_preceding_blankline "$TMP/paper.md" --metadata-file="$TMP/meta.yaml" \
  --pdf-engine=xelatex -V tables=true -o "$OUT"
echo "Wrote $OUT"
