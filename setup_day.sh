#!/bin/bash

# shellcheck disable=SC1091

main() {
    . .env
    local local_dir
    local_dir="adventofcode/_$1/day$2"
    local test_dir
    test_dir="test/unit/_$1"

    echo "Setting up $local_dir and $test_dir/test_day$2.py..."
    mkdir -p "$local_dir"
    mkdir -p "$test_dir"
    curl -X GET --cookie "session=$ADVENT_OF_CODE_SESSION_ID" https://adventofcode.com/"$1"/day/"$2"/input >"$local_dir"/input.txt
    touch "$local_dir"/prompt.txt
    touch "$local_dir"/sample.txt
    cp adventofcode/challenge_template.py "$local_dir"/challenge.py
    cp test/unit/test_template.py "$test_dir"/test_day"$2".py
}

main "$@"
