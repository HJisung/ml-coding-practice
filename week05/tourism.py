# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

ServiceKey = "13fed2f70a682cfaf906db5413bed88fac909abeb66712d653574e9fc0976b6d"

"""### [CODE 0]"""

def main():
  jsonResult = []
  result = []

  print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
  na"""