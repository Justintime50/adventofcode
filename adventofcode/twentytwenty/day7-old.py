import re
import os

# THIS IS SUPER BROKEN AND CANNOT BE SOLVED, NEED TO USE RECURSION
BAG_NAME = os.getenv('BAG_NAME', 'shiny gold')


def main():
    output = get_num_bags()
    print('Bag total:', output)


def get_num_bags():
    """Gets the number of bags that can contain at least one bag
    your specify

    Data Rules Observed:
    - First two words are the bag color/type
    - "bags contain" are the 3rd and 4th words
    - Bags that can contain multiple bags have those rules split up by a comma
    - Lines end with a period

    eg: "light salmon bags contain 2 shiny gold bags, 2 light silver bags, 4 wavy magenta bags."
    """
    with open('adventofcode/twentytwenty/static_data/day7.txt', 'r') as f:
        lines = f.readlines()

    # Get the rules from the data set based on bag type
    rules = []
    for line in lines:
        can_contain_bag_type = re.search(fr'\d+ {BAG_NAME}', line)
        if can_contain_bag_type:
            bag_name = re.search(r'\w+ \w+', line)
            rules.append([bag_name.group(), can_contain_bag_type.group()[:1]])
    print('Rules:', rules)
    print('Total rules:', len(rules))

    # Get the number of times a rule appears in the data set
    rule_matches = []
    lala = []
    for line in lines:
        for rule in rules:
            bag_matches_rule = re.search(fr'\d+ {rule[0]}', line)
            if bag_matches_rule:
                print(line)
                lala.append(re.search(r'\w+ \w+', line).group())
                rule_matches.append([bag_matches_rule.group()[2:].strip(), bag_matches_rule.group()[:1]])
                break
    print(lala)
    print('Matches:', rule_matches)
    print('Total matches to rules:', len(rule_matches))

    # Multiply the rules by the number of times they appear
    bag_total = 0
    for rule in rules:
        for match in rule_matches:
            if rule[0] == match[0]:
                bag_total += int(rule[1]) * int(match[1])
    bag_total += int(rule[1])  # Include the direct bag inclusion as well as child bags

    # print('Bag total:', bag_total)

    return bag_total


if __name__ == '__main__':
    main()
