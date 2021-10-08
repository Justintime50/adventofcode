from adventofcode.twentytwenty.day13 import get_data, iterate_bus_ids


def test_iterate_bus_ids():
    timestamp, bus_ids = get_data()
    answer = iterate_bus_ids(timestamp, bus_ids)
    assert answer == 6568
