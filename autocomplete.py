# create a matching function
def matcher(to_match, term_dict):
    # first check if TERMS is sorted alphabetically, if not then sort before matching
    if not term_dict == sorted(term_dict):
        term_dict = sorted(term_dict)

    # is it easier to just return all matches since it's O(n) lookup time and then just take the first 4 elements
    # of the matches?

    # NEEDS TO RETURN CASES WHERE ONLY THE FIRST FOUR LETTERS MATCH IE FROM START OF STRING NOT ANYWHERE IN STRING
    result = [i for i in term_dict if i.startswith(to_match)]

    return result[:4]
