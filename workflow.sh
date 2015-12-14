#!/bin/sh
rm 20*/week*
rm 20*/totals*
python ~/Documents/310analytics/github/ncaa_rankings/compile_database.py
python ~/Documents/310analytics/github/ncaa_rankings/stat_parser.py
python ~/Documents/310analytics/github/ncaa_rankings/weekly_adder.py
