import numpy as np, math, pandas as pd

from utils.misc_tools import merge_dicts

from typing import Dict, List, Tuple

city_wealths_: Dict = {
    'Frogtopia': {
        'Red': {
            'mean': 0.75,
            'std': 0.15,
        },
        'Blue': {
            'mean': 0.75,
            'std': 0.15,
        }
    },
    'Pond Place': {
        'Red': {
            'mean': 0.75,
            'std': 0.15,
        },
        'Blue': {
            'mean': 0.5,
            'std': 0.15,
        }
    }
}

class DataGenerator:

    def get_outfit(wealth: float, group: str = None, group_bias: Dict = None, outfit_std: float = 0.2) -> Tuple[str]:
        """
        Returns outfit given frog description

        wealth: float
            How wealth the frog is, used to determine the probabilities of different outfits

        outfit_std: float
            Effects generated normal curve to get probabilities of outfits
        
        group: str
            Used if outfit bias by group

        group_bias:
            Used to influence the probabilites of outfits if bias by group
        """

        normal_curve = lambda: np.random.normal(
            loc=wealth,
            scale=outfit_std,
        )

        # Cutoffs Wealthy item 0.66 | Middle 0.33 | Less Wealthy else
        choose_item = lambda items, normal_sample: items[
            list(map(lambda cutoff: normal_sample > cutoff, [0.66, 0.33, -math.inf])).index(True)
        ]

        rd = {}

        # Clothes 3 types | Wealthy <- ['Robes', 'Suit', 't-shirt'] -> Less Wealthy |
        rd['Clothes'] = choose_item(['Robes', 'Suit', 't-shirt'], normal_curve())

        # Hat 3 types | Wealthy <- ['Crown', 'Top Hat', 'Scally Cap'] -> Less Wealthy |
        rd['Hat'] = choose_item(['Crown', 'Top Hat', 'Scally Cap'], normal_curve())

        # Clothes Colors 3 types | Wealthy <- ['Purple', 'Blue', 'Grey'] -> Less Wealthy |
        rd['Clothes Color'] = choose_item(['Purple', 'Blue', 'Grey'], normal_curve())

        # Canes 3 types | Wealthy <- ['Ivory', 'Oak', 'Plywood'] -> Less Wealthy |
        rd['Canes'] = choose_item(['Ivory', 'Oak', 'Plywood'], normal_curve())

        # Glasses 3 types | Wealthy <- ['Spectacle', 'Aviators', 'Round Eye'] -> Less Wealthy |
        rd['Glasses'] = choose_item(['Spectacle', 'Aviators', 'Round Eye'], normal_curve())

        return rd

    def distribution(n_frogs: int = 100, population_info: Dict = {'Red': 0.5, 'Blue': 0.5}, city: str = None, city_wealth: Dict = {'Red': {'mean': 0.75, 'std': 0.15,}, 'Blue': {'mean': 0.75, 'std': 0.15,}}) -> pd.DataFrame:
        """
        Generates Frog population as vectors
        """

        # Loads wealth distribution
        if city is not None:

            city_wealth = city_wealths_[city]
        
        elif not city_wealth:

            raise ValueError('Neither city or wealth distribution specified')

        # Checks if input is valid

        # population_info values add to 1
        assert math.isclose(
            (total_pop := sum(population_info.values())), 1, rel_tol=1e-6
        ), f'Found total population percentage of {total_pop} in population_info, must sum to 1'

        # Means of city_wealth do not exceed 1

        assert all((where_exceeds := map(
            lambda list_mean: list_mean[0] < 1,
            (list_mean := [(wealth['mean'], group) for group, wealth in city_wealth.items()
        ])))), f"""Mean of population wealth exceeds 1 for {
            list_mean[where_exceeds.index(False)][1]
        }"""

        # Generate population

        df = pd.DataFrame(
            columns=['Group', 'Wealth', 'Clothes', 'Hat', 'Clothes Color']
        )

        for group, percent in population_info.items():

            n_group: int = math.floor(n_frogs * percent)

            group_distribution = np.random.normal(
                loc=city_wealth[group]['mean'], # Mean
                scale=city_wealth[group]['std'], # std
                size=(n_group)
            )

            # Eliminate >1 and <0
            group_distribution[group_distribution > 1] = 1
            group_distribution[group_distribution < 0] = 0

            data = merge_dicts(map(DataGenerator.get_outfit, group_distribution))

            df = pd.concat(
                [df,
                pd.DataFrame({
                    'Group': [group] * n_group, 
                    'Wealth': group_distribution.tolist(), 
                    **data
                })]
            )

        return df