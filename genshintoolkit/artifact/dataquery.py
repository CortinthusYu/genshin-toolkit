from ast import Pass
from genshintoolkit.gtcommon.gtenum import *
import json

path_mainstat='.\genshindata\ExcelBinOutput\ReliquaryMainPropExcelConfigData.json'
path_substat='.\genshindata\ExcelBinOutput\ReliquaryAffixExcelConfigData.json'

class QueryArtifactMainstat:
    def __init__(self,path=path_mainstat) -> None:
        self.path=path
        with open(self.path) as f:
            self.data=json.load(fp=f)

    def query(self,rank,level,statname):
        for d in self.data:
            if d['rank']==rank and d['level']==level:
                for p in d['addProps']:
                    if p['propType']==statname:
                        return p['value']

class QueryArtifactSubstat:
    def __init__(self,path=path_substat) -> None:
        self.path=path
        with open(self.path) as f:
            self.data=json.load(fp=f)

    def queryId(self,rank,statname,value):
        pass
    
    def query_value(self,rank,statname,statstuple):
        pass