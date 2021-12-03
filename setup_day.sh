#!/bin/bash

main() {
    local local_dir="adventofcode/_$1/$2"
    echo "Setting up $local_dir..."

    mkdir -p "$local_dir"
    echo "TODO: Add data here" >"$local_dir"/input.txt
    echo "TODO: Add data here" >"$local_dir"/prompt.txt
    echo "TODO: Add data here" >"$local_dir"/sample.txt
    cp adventofcode/challenge_template.py "$local_dir"/challenge.py
}

main "$@"
