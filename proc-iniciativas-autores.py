#!/usr/bin/env python3
# coding: utf-8
#
# p3: Processador do Parlamento Português
#
# 2021, 2022, 2023: Frederico Muñoz <fsmunoz@gmail.com>
#
# This file is part of p3 - processador do parlamento português
#
# p3 is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# p3 is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Foobar. If not, see <https://www.gnu.org/licenses/>.


## Imports ####################################################
import sys
import argparse
from pathlib import Path
from urllib.request import urlopen
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import pandas as pd
import collections

## Local config
import config

## Functions ##################################################

## Progress output
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


## Build a dict with essential info from MPs
def dep_info(root):
    dep_dict = {}
    for deps in root.findall("Deputados"):
        for dep in deps.iter("pt_ar_wsgode_objectos_DadosDeputadoSearch"):
            d_info ={}

            d_info["depNomeParlamentar"] = dep.find("depNomeParlamentar").text
            d_info["depCPId"] = dep.find("depCPId").text
            d_info["depCPDes"] = dep.find("depCPDes").text
            if dep.find("depGP/pt_ar_wsgode_objectos_DadosSituacaoGP/gpSigla") is not None:
                d_info["gpSigla"] = dep.find("depGP/pt_ar_wsgode_objectos_DadosSituacaoGP/gpSigla").text
            dep_dict[dep.find("depCadId").text] = d_info
    return dep_dict


## Main parsing function.
def ini_to_df_ini(root):
    counter=0

    ## We will build a dataframe from a list of dicts
    ## Inspired by the approach of Chris Moffitt here https://pbpython.com/pandas-list-dict.html
    init_list = []

    for ini in root.findall("pt_gov_ar_objectos_iniciativas_DetalhePesquisaIniciativasOut"):
        for adep in ini.iter("iniAutorDeputados"):
            for autor in adep.iter("pt_gov_ar_objectos_iniciativas_AutoresDeputadosOut"):
                init_dict = collections.OrderedDict()
                counter +=1
                for c in ini:
                    init_dict[c.tag] = c.text
                for f in autor:
                    init_dict[f.tag] = f.text
                init_dict["depCPDes"] = dep_dict[init_dict["idCadastro"]]["depCPDes"]
                init_list.append(init_dict)
            eprint(".", end="", flush=True)
                    #print(init_dict)
    eprint(counter)
    return pd.DataFrame(init_list)

## Main program flow  ########################################

## Command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--leg", help="legislatura a analisar", required=True)
parser.add_argument("--out_file", help="nome do ficheiro CSV")
args = parser.parse_args()

if args.out_file is None:
    args.out_file = args.leg + "_deputados.csv"

try:
    leg_ini_url = config.legs[args.leg]["url"]
except KeyError as e:
    print("Legislatura não encontrada.")
    exit()


## MP info

eprint("* Building MP info.")
dep_tree_url = config.legs[args.leg]["basic_info_url"]
dep_tree = ET.parse(urlopen(dep_tree_url))

## Useful for local testing
## dep_tree = ET.parse("InformacaoBaseXV.xml")
dep_dict = dep_info(dep_tree)

## Main parsing

leg_ini_url = config.legs[args.leg]["url"]

## Useful for local testing
## leg_ini_url = config.legs["l15"]["url"]

## Get and parse the XML
eprint("* Parsing XML file.")
leg_ini_tree = ET.parse(urlopen(leg_ini_url))
#leg_ini_tree = ET.parse("l15.xml")

eprint("* Converting to dataframe.")
leg_df = ini_to_df_ini(leg_ini_tree)

## Adjust dates and add more columns

eprint("* Adjusting date columns.")
leg_df['dataInicioleg']= pd.to_datetime(leg_df['dataInicioleg'])
leg_df['dataFimleg']= pd.to_datetime(leg_df['dataFimleg'])
leg_df['leg'] = args.leg

## Export to CSV
eprint("* Exporting CSV.")
leg_df.to_csv(Path(config.out_dir,args.out_file), index=False, columns=config.common_fields_aut, date_format='%Y-%m-%d')
eprint("* Done.")
