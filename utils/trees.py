import sklearn, pandas as pd

from typing import Any, Union
from dataclasses import dataclass

import numpy as np

from utils.misc_tools import to_categorical
from utils.generate_data import DataGenerator
from utils.colors import Colors, mse_highlighter

class TreeTools:

    @staticmethod
    def build_tree(city: str, include_group: bool, random_state: Union[int, None] = 42, **tree_params) -> Any:
        """
        Returns: tree, feature_names, (y_test, y_pred)

        Random state is set to 42, use None if random results
        """

        if random_state is not None:
            np.random.seed(random_state)
        else:
            np.random.seed(None)

        # Get data

        df = DataGenerator.distribution(city=city)

        if not include_group:

            df = df.drop('Group', axis=1)

        X = pd.get_dummies(
            df.drop('Wealth', axis=1),
            drop_first=True
        )
        y = df['Wealth']

        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=random_state)

        # Make tree

        tree = sklearn.ensemble.RandomForestRegressor(**tree_params, random_state=random_state)

        tree.fit(X_train, y_train)

        print(
            "MSE Testing:",
            (testing_mse := round(sklearn.metrics.mean_squared_error(
                y_test, (y_pred := tree.predict(X_test))
            ), 4))
        )

        return tree, X.columns, testing_mse, (y_pred, y_test)
    
    @staticmethod
    def validate_tree(tree: Any, city: str, include_group: bool, random_state: int = 42, testing_mse: float = None) -> Any:
        """
        Returns (y, y_pred), mse_diff if testing_mse

        Random state is set to 42, use None if random results
        """

        if random_state is not None:
            np.random.seed(random_state)
        else:
            np.random.seed(None)

        # Get data

        df = DataGenerator.distribution(city=city)

        if not include_group:

            df = df.drop('Group', axis=1)

        X = pd.get_dummies(
            df.drop('Wealth', axis=1),
            drop_first=True
        )
        y = df['Wealth']

        print(
            "MSE Validation:",
            (val_mse := round(sklearn.metrics.mean_squared_error(
                y, (y_pred := tree.predict(X))
            ), 4))
        )

        if testing_mse is not None:

            mse_diff = round(val_mse - testing_mse, 4)

            print(
                "MSE Difference:",
                mse_highlighter(mse_diff)
            )

            return y, y_pred, mse_diff

        return y, y_pred