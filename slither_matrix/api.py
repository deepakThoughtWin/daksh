import json
import os
import sys

import requests as request

from config import ACTION, ADDRESS, API_KEY, MODULE
from slither_matrix.slither.__main__ import main
from utils.args_parser import manual_human_summary_args


#Run analyzer(updated slithir=> human_summary,__main__.py)
def slither_analisys(path):
  filename_with_args=manual_human_summary_args(path)
  try:
    analysis_result=main(filename_with_args)
  except:
    analysis_result=None
  return analysis_result
