#!/bin/bash

# Navigate through each customer directory
for dir in */ ; do
    # Extract the customer name from the directory name
    # Assuming the customer name is everything after " - "
    customer_name=$(echo "$dir" | sed -E 's/.* - (.*)\//\1/')

    # Navigate into the directory
    cd "$dir"

    # Loop through each file in the directory
    for file in *; do
        if [ -f "$file" ]; then # Check if it's a file and not a directory
            # Rename the file by prepending the customer name
            mv "$file" "${customer_name}-$file"
        fi
    done

    # Go back to the parent directory
    cd ..
done

