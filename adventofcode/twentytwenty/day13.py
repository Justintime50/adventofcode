def main():
    timestamp, bus_ids = get_data()
    answer = iterate_bus_ids(timestamp, bus_ids)
    print('Answer:', answer)


def get_data():
    """Get the data
    """
    with open('adventofcode/twentytwenty/static_data/day13.txt', 'r') as f:
        lines = f.read().split('\n')
    return int(lines[:1][0]), lines[1:2]


def iterate_bus_ids(timestamp, bus_ids):
    """Iterate through bus ID's, skip X's and multiply until you get 
    the closest timestamp to the original. Then subtract the two timestamps
    and multiply by the bus ID that had the closest departing timestamp.
    """
    ids = bus_ids[0].split(',')
    new_timestamps = []
    for bus_id in ids:
        if bus_id == 'x':
            continue
        else:
            new_timestamp = int(bus_id)
            while new_timestamp <= timestamp:
                new_timestamp += int(bus_id)
            new_timestamps.append([bus_id, new_timestamp])
    # print(new_timestamps)
    closest_timestamp = min([new_timestamp[1] for new_timestamp in new_timestamps])  # Find the soonest timestamp
    index_of_id = [new_timestamp[1] for new_timestamp in new_timestamps].index(
        closest_timestamp)  # Get the index of the ID
    answer = (closest_timestamp - timestamp) * int(new_timestamps[index_of_id][0])
    return answer


if __name__ == '__main__':
    main()
