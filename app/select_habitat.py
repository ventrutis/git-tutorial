import pandas
from IPython.display import display
import pandas

import argparse
import json
import os


def select_habitat(selected_hab_abb=None, habitat_name=None):
    """
    Selects a habitat based on the provided string.

    Args:
        habitat (str): The name of the habitat to select.

    Returns:
        str: The selected habitat.
        :param habitat_name:
        :param selected_hab_abb:
    """
    url_txt = f"http://opendap.biodt.eu/ias-pdt/0/outputs/hab{selected_hab_abb}/predictions/Prediction_Summary_Shiny.txt"
    df_mod = pandas.read_csv(url_txt, sep="\t")
    display(df_mod)
    habitat_number = str(
        df_mod[df_mod["hab_name"] == habitat_name]["hab_abb"].values[0])

    filtered_df = df_mod[
        (df_mod["hab_abb"] == habitat_number)
        ]

    return filtered_df