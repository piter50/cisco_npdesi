#!/usr/bin/env python


def print_facts(facts):
    """Print two facts from facts dictionary
    """

    platform = facts['platform']
    print 'platform', platfom

    print 'os', facts[os]


if __name__ == "__main__":

    # Define basic facts about a device
    # DO NOT ADD A KEY CALLED PLATFORM TO THIS DICTIONARY
    facts = {'os': '7.2', 'fqdn': 'cisco.com', 'location': 'sjc', 'vlans_list': [1, 5, 10], 'neighbors': ['s2', 's3']}

    # Call print_facts function
    print_facts(facts)

    # Extract neighbors from facts dict and assign to new variable
    neighbors = facts['neighbors']

    # Print each neighbor
    for item in neighbors
        print item
