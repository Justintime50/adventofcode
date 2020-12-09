from adventofcode.twentytwenty.day9 import (
    find_cypher_weakness_part_1,
    find_cypher_weakness_part_2
)


def test_find_cypher_weakness_part_1():
    with open('adventofcode/twentytwenty/static_data/day9.txt', 'r') as f:
        lines = f.read()
    output = find_cypher_weakness_part_1(lines.split('\n'))
    assert output == 393911906


def test_find_cypher_weakness_part_2():
    answer_part_1 = 393911906
    with open('adventofcode/twentytwenty/static_data/day9.txt', 'r') as f:
        lines = f.read()
    output = find_cypher_weakness_part_2(lines.split('\n'), answer_part_1)
    assert output == 59341885
