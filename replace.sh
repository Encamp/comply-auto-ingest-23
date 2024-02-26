#!/bin/bash

while IFS=: read -r old new; do
  find . -type f -name "*.csv" -print0 | xargs -0 sed -i '' "s/$old/$new/g"
done < replacements.txt
