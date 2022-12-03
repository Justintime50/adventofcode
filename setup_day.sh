#!/bin/bash

# shellcheck disable=SC1091

main() {
    . .env
    local local_dir
    local_dir="adventofcode/_$1/day$2"
    local test_dir
    test_dir="test/unit/_$1"

    echo "Setting up $local_dir and $test_dir/test_day$2.py..."

    # Day structure
    mkdir -p "$local_dir"
    curl -s --cookie "session=$ADVENT_OF_CODE_SESSION_ID" https://adventofcode.com/"$1"/day/"$2"/input >"$local_dir"/input.txt
    cp adventofcode/challenge_template.py "$local_dir"/challenge.py
    touch "$local_dir"/prompt.txt
    touch "$local_dir"/sample.txt
    sed -i "" "s;day0;day$2;g;" "$local_dir"/challenge.py
    sed -i "" "s;_2000;_$1;g;" "$local_dir"/challenge.py

    # Test structure
    mkdir -p "$test_dir"
    cp test/unit/test_template.py "$test_dir"/test_day"$2".py
    sed -i "" "s;day0;day$2;g;" "$local_dir"/test_day"$2".py
    sed -i "" "s;_2000;_$1;g;" "$local_dir"/test_day"$2".py
}

main "$@"
