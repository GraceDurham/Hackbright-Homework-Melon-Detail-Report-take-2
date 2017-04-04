"""
Prints out all the melons in our inventory
"""

from melons import melons


def print_melon(melons):
    for melon, attribute in melons.iteritems():
        print melon.upper()
        for attribute, value in attribute.items():
            print "{}: {}".format(attribute, value)
        print '==================================='

print_melon(melons)
