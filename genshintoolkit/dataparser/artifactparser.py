from genshintoolkit.gtcommon.atfdata import *
from genshintoolkit.gtcommon.gtenum import *
from pathlib import Path

import json
import yaml


def parse_substatvalue(path='.\\genshindata\\ExcelBinOutput\\ReliquaryAffixExcelConfigData.json'):
    with open(path) as f:
        data=json.load(fp=f) #getting data like [dict1,dict2,...]
    
