import re
import os


BAG_TYPE = os.getenv('BAG_TYPE', 'shiny gold')


def main():
    part_1, part_2 = get_num_bags()
    print('Bag total:', part_1)
    # print('Part 2:', part_2)


def get_num_bags():
    """Gets the number of bags that can contain at least one bag
    your specify
    """
    with open('adventofcode/twentytwenty/static_data/day7.txt', 'r') as f:
        lines = f.readlines()

    rules, bags = format_data(lines)

    total = 0
    included_bags, num_bags = run_recursion([BAG_TYPE], bags, rules, total)
    # print(included_bags)

    return num_bags


def run_recursion(bags, data, rules, total):
    """Recursively build a list of unique, possible bags
    that can contain my bag. Return once we can no longer
    find missing bags from the list.
    """
    bag_added = False
    for line in data:
        for item in line[1]:
            for bag in bags:
                if bag == item[0] and line[0] not in bags:
                    bags.append(line[0])
                    bag_added = True
                # # Part 2
                # for rule in rules:
                #     if bag == rule[0]:
                #         # print(item)
                #         total += int(item[1]) * int(rule[1])  # TOO HIGH
                    # Try to reverse the recursion. Instead of how many bags can fit a BAG_TYPE in them,
                    # how many bags can fit inside a BAG_TYPE
    # print(set(bags), len(set(bags)))
    if BAG_TYPE in bags:
        bags.remove(BAG_TYPE)  # We remove the bag in question because it cannot contain itself
    if bag_added is True:
        run_recursion(bags, data, rules, total)
    return bags, len(set(bags))


def format_data(data):
    """Get the rules and bags from the dataset and format the data

    Data Rules Observed:
    - First two words are the bag color/type
    - "bags contain" are the 3rd and 4th words
    - Bags that can contain multiple bags have those rules split up by a comma
    - Lines end with a period

    eg: "light salmon bags contain 2 shiny gold bags, 2 light silver bags, 4 wavy magenta bags."

    Note: Ignore bag rules that have no bags included.
    """
    rules = []
    bags = []
    for bag_data in data:
        bag = bag_data.split('contain')
        bag_type = bag[0].replace('bags', '').strip().lower()
        bag_content = bag[1].replace('.', '')
        if 'no other bags' in bag_content:
            continue
        else:
            bags.append([bag_type, [[re.sub(r'bags?$', '', content).strip().lower()[2:], content[:2].strip()]
                                    for content in bag_content.split(',')]])
            rule = re.search(fr'\d+ {BAG_TYPE}', bag_data)
            if rule:
                rules.append([bag_type, rule.group()[:1].strip()])
    # print(rules)
    return rules, bags


if __name__ == '__main__':
    main()
