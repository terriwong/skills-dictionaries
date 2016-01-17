"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    d = {}
    counter_list = []
    top_list = []

    # build dictionary, delete key=space pair.
    for char in input_string:
        d[char] = d.get(char, 0) + 1

    del d[" "]

    # sort key-value pairs by value, from smallest to largest.
    from operator import itemgetter
    counter_list = sorted(d.items(), key=itemgetter(1))

    # find if tie exists.
    if counter_list[-1][1] == counter_list[-2][1]:
        top_list = [counter_list[-1][0], counter_list[-2][0]]
        top_list.sort()
    else:
        top_list = [counter_list[-1][0]]

    return top_list


# FIXME: fix the "now try doing it with only one call to sort() or sorted()"
# Too hard.
def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    d = {}

    for word in words:
        d[len(word)] = d.setdefault(len(word), [])
        d[len(word)].append(word)
        d[len(word)].sort()

    return sorted(d.items())


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
