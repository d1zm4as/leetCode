# the file with the phone numbers is in the same directory as this file file.txt READ IT USING BASH
#!/bin/bash

while IFS= read -r line; do
    if [[ $line =~ ^\([0-9]{3}\)[[:space:]][0-9]{3}-[0-9]{4}$ || $line =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
        echo "$line"
    fi
done < "file.txt"

