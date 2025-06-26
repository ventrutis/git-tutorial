import argparse
import json
import os
import pandas

from select_habitat import select_habitat

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument(
    '--habitat_name',
    action='store',
    type=str,
    required=True,
    dest='habitat_name',
    default='forests',
    choices=[
        'forests',
        'open_forests',
        'scrub',
        'natural_grasslands',
        'human_maintained_grasslands',
        'wetland',
        'ruderal_habitats',
        'agricultural_habitat'
    ],
    help='Name of the habitat. Choices: forests, open_forests, scrub, natural_grasslands, human_maintained_grasslands, wetland, ruderal_habitats, agricultural_habitat'
)
arg_parser.add_argument(
    '--param_climate_model'
    , action='store',
    type=str,
    required=False,
    dest='param_climate_model',
    default='IPSL-CM6A-LR',
    choices=[
        'Current',
        'GFDL-ESM4',
        'IPSL-CM6A-LR',
        'MPI-ESM1-2-HR',
        'MRI-ESM2-0',
        'UKESM1-0-LL',
        'Ensemble'
    ],
    help='Climate model to use for the simulation. Choices: Current, GFDL-ESM4, IPSL-CM6A-LR, MPI-ESM1-2-HR, MRI-ESM2-0, UKESM1-0-LL, Ensemble'
)


arg_parser.add_argument(
    '--param_species_class'
    , action='store',
    type=str,
    required=False,
    dest='param_species_class',
    default='Liliopsida',
    choices=[ 'Liliopsida', 'Magnoliopsida', 'Pinopsida'],
    help='Species class to use for the simulation. Choices: Liliopsida, Magnoliopsida, Pinopsida'
)

args = arg_parser.parse_args()
print(args)

habitat_name = args.habitat_name

url = "http://opendap.biodt.eu/ias-pdt/0/outputs/key.csv"
df_hab = pandas.read_csv(url)

habitat_type = habitat_name.replace(' ','_').lower()
selected_hab_abb = str(df_hab[df_hab["hab_name"] == habitat_type]["hab_abb"].values[0])
param_climate_model = args.param_climate_model
param_species_class = args.param_species_class


conf_x =  0.95
conf_y =  0.95
conf_arrow_length = 0.1
print(f"Selected Habitat Abbreviation: {selected_hab_abb}")

habitat_number = select_habitat(selected_hab_abb=selected_hab_abb, habitat_name=habitat_name)



