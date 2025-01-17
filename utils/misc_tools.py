import numpy as np

from typing import List, Dict

from utils.colors import Colors

def merge_dicts(dict_list: List[Dict]):
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

def rank_features(features: List[str], importance: List[float], highlight_group: str = None) -> None:

    highlighter = None

    if highlight_group is not None:

        if highlight_group.lower() in (all_colors := [c.name.lower() for c in list(Colors)]):

            highlighter = Colors[highlight_group.upper()].apply

        else:

            print(Colors.YELLOW(f'{highlight_group} not found in Colors {all_colors}'))

    print(
        '',
        'Features Ranked by Importance',
        *[highlighter(display_text) if 'Group' in (display_text := f'{feature}: {importance}') and highlighter is not None else display_text for feature, importance in sorted(zip(features, importance), key=lambda z: z[1], reverse=True)],
        sep='\n'
    )   

def to_categorical(array):

    found: Dict[str, int] = {}

    categorical = []

    for index in array:

        if index in found:

            categorical.append(
                found[index]
            )

        else:

            found[index] = found.__len__()
    
    one_hot_encoded = np.zeros(
        shape=(categorical.__len__(), found.__len__())
    )

    for i, item in enumerate(categorical):

        one_hot_encoded[i][item] == 1
    
    return one_hot_encoded