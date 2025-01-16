def merge_dicts(dict_list):
    """
    ChatGPT

    Merges a list of dictionaries into a single dictionary.
    For keys that appear in multiple dictionaries, their values are combined into a list.

    Parameters:
        dict_list (list): List of dictionaries to merge.

    Returns:
        dict: A single dictionary with combined values.
    """
    result = {}
    for d in dict_list:
        for key, value in d.items():
            if key in result:
                if isinstance(result[key], list):
                    result[key].append(value)
                else:
                    result[key] = [result[key], value]
            else:
                result[key] = value
    # Ensure all values are lists
    for key in result:
        if not isinstance(result[key], list):
            result[key] = [result[key]]
    return result
