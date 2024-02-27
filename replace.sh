#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

while IFS=: read -r old new; do
  find . -type f -name "*.csv" -print0 | xargs -0 sed -i '' "s/$old/$new/g"
done < "$SCRIPT_DIR/replacements.txt"