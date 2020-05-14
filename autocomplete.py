def matcher(to_match, term_dict):
    """
    Function to return elements of a list that start with a given string.
    :param to_match: substring to match
    :param term_dict: list of strings
    :return: list of 4 strings that start with to_match string
    """
    # this step is slightly redundant but I did not want to load an extra copy of term_dict into memory
    if not term_dict == sorted(term_dict):
        term_dict = sorted(term_dict)

    result = [i for i in term_dict if i.startswith(to_match)]

    return result[:4]
