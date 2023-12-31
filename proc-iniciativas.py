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
#   along with p3. If not, see <https://www.gnu.org/licenses/>.


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

## Iteract through the existing dict
def party_from_votes (votes):
    """
    Determines the position of a party based on the majority position by summing all the individual votes.
    Argument is a dictionary returned by parse_voting()
    Returns a dictionary with the majority position of each party
    """
    party_vote = {}
    for k, v in votes.items():
        ## Erase the name of the MP and keep the party only
        ## only when it's not from the "Ninsc" group -
        ## these need to be differentiated by name
        if re.match(".*\(Ninsc\)" , k) is None:
            nk = re.sub(r".*\((.+?)\).*", r"\1", k)
        else:
            nk = k
            ## If it's the first entry for a key, create it
        if nk not in party_vote:
            party_vote[nk] = [0,0,0]
            ## Add to a specific index in a list
        if v == "A Favor":
            party_vote[nk][0] += 1
        elif v == "Abstenção":
            party_vote[nk][1] += 1
        elif v == "Contra":
            party_vote[nk][2] += 1
    for k,v in party_vote.items():
        party_vote[k]=["A Favor", "Abstenção", "Contra"][v.index(max(v))]
    return party_vote

def parse_voting(v_str):
    """Parses the voting details in a string and returns a dict.

    Keyword arguments:

    v_str: a string with the description of the voting behaviour.
    """
    ## Split by the HTML line break and put it in a dict
    d = dict(x.split(':') for x in v_str.split('<BR>'))
    ## Remove the HTML tags
    for k, v in d.items():
        ctext = BeautifulSoup(v, "lxml")
        d[k] = ctext.get_text().strip().split(",")
    ## Invert the dict to get a 1-to-1 mapping
    ## and trim it
    votes = {}
    if len(v_str) < 1000:    # Naive approach but realistically speaking... works well enough.
        for k, v in d.items():
            for p in v:
                if (p != ' ' and                                       # Bypass empty entries
                    re.match("[0-9]+", p.strip()) is None and           # Bypass quantified divergent voting patterns
                    (re.match(".*\w +\(.+\)", p.strip()) is None or     # Bypass individual votes...
                     re.match(".*\(Ninsc\)" , p.strip()) is not None)): # ... except when coming from "Ninsc"
                        #print("|"+ p.strip() + "|" + ":\t" + k)
                        votes[p.strip()] = k
    else:  # This is a nominal vote since the size of the string is greater than 1000
        for k, v in d.items():
            for p in v:
                if p != ' ':
                    votes[p.strip()] = k
        ## Call the auxiliary function to produce the party position based on the majority votes
        votes = party_from_votes(votes)
    return votes

## Main parsing function.
def ini_to_df_ini(root):
    counter=0

    ## We will build a dataframe from a list of dicts
    ## Inspired by the approach of Chris Moffitt here https://pbpython.com/pandas-list-dict.html
    init_list = []

    for ini in root.findall("pt_gov_ar_objectos_iniciativas_DetalhePesquisaIniciativasOut"):
        for evento in ini.iter("pt_gov_ar_objectos_iniciativas_EventosOut"):
            for voting in evento.iter("pt_gov_ar_objectos_VotacaoOut"):
                votep = voting.find('./detalhe')
                if votep is not None:
                    init_dict = collections.OrderedDict()
                    counter +=1
                    init_dict["fase"] = evento.find("fase").text
                    for c in ini:
                        if c.tag == "iniAutorGruposParlamentares" or c.tag == "iniAutorDeputados":
                            if c.find('pt_gov_ar_objectos_AutoresGruposParlamentaresOut/GP') is not None:
                                init_dict[c.tag] = c.find('pt_gov_ar_objectos_AutoresGruposParlamentaresOut/GP').text
                            elif c.find('pt_gov_ar_objectos_iniciativas_AutoresDeputadosOut/GP').text == "Ninsc":
                                init_dict["iniAutorGruposParlamentares"] = c.find('pt_gov_ar_objectos_iniciativas_AutoresDeputadosOut/nome').text
                        else:
                            init_dict[c.tag] = c.text
                            counter +=1
                            init_dict['id'] = voting.find('id').text
                            ## Add the "I" for Type to mark this as coming from "Iniciativas"
                    init_dict['Tipo'] = "I"
                    for c in voting:
                        if c.tag == "detalhe":
                            for party, vote in parse_voting(c.text).items():
                                init_dict[party] = vote
                        elif c.tag == "descricao":
                            init_dict[c.tag] = c.text
                        elif c.tag == "ausencias":
                            init_dict[c.tag] = c.find("string").text
                        else:
                            init_dict[c.tag] = c.text

                    init_list.append(init_dict)
                    eprint(".", end="", flush=True)
                            ## Provide progression feedback
                            #print('.', end='')
                            #print(counter)
    eprint(counter)
    return pd.DataFrame(init_list)


## Main program flow  ########################################

## Command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--leg", help="legislatura a analisar", required=True)
parser.add_argument("--out_file", help="nome do ficheiro CSV")
args = parser.parse_args()

if args.out_file is None:
    args.out_file = args.leg + ".csv"

try:
    leg_ini_url = config.legs[args.leg]["url"]
except KeyError as e:
    print("Legislatura não encontrada.")
    exit()

leg_ini_url = config.legs[args.leg]["url"]


## Get and parse the XML

eprint("* Parsing XML file.")
leg_ini_tree = ET.parse(urlopen(leg_ini_url))

eprint("* Converting to dataframe.")
leg_df = ini_to_df_ini(leg_ini_tree)

## Adjust dates and add more columns

eprint("* Adjusting date columns.")
leg_df['data']= pd.to_datetime(leg_df['data'])
leg_df['dataInicioleg']= pd.to_datetime(leg_df['dataInicioleg'])
leg_df['dataFimleg']= pd.to_datetime(leg_df['dataFimleg'])
leg_df['ano'] = pd.DatetimeIndex(leg_df['data']).year
leg_df['leg'] = args.leg

## Export to CSV
eprint("* Exporting CSV.")
leg_df.sort_values('data').to_csv(Path(config.out_dir,args.out_file), index=False, columns=config.common_fields + config.legs[args.leg]["extra_fields"], date_format='%Y-%m-%d')
eprint("* Done.")
