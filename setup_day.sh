#!/bin/bash

main() {
    local local_dir
    local_dir="adventofcode/_$1/$2"
    local test_dir
    test_dir="test/unit/_$1"

    echo "Setting up $local_dir..."
    mkdir -p "$local_dir"
    echo "TODO: Add data here" >"$local_dir"/input.txt
    echo "TODO: Add data here" >"$local_dir"/prompt.txt
    echo "TODO: Add data here" >"$local_dir"/sample.txt
    cp adventofcode/challenge_template.py "$local_dir"/challenge.py
    cp test/unit/test_template.py "$test_dir"/test_"$2".py
}

main "$@"
