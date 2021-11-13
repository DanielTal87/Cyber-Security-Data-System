#!/bin/bash

# shellcheck disable=SC2034
# shellcheck disable=SC2006
red=`tput setaf 1`
green=`tput setaf 2`
blue=`tput setaf 4`
reset=`tput sgr0`

echo "${blue}Running Cyber Security Data System...${reset}"
source csds_env/bin/activate
python3 runner.py


