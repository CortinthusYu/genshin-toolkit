from sqlalchemy import false
from artifact import Artifact,IdGenerator
import json
from pathlib import Path
import datetime

#mona
mapping_statname={
    'hp':'lifeStatic',
    'hp%':'lifePercentage',
    'atk':'attackStatic',
    'atk%':'attackPercentage',
    'defs':'defendStatic',
    'def%':'defendPercentage',
    'rch':'recharge',
    'em':'elementalMastery',
    'pyrodmg':'fireBonus',
    'hydrodmg':'waterBonus',
    'cryodmg':'iceBonus',
    'electrodmg':'thunderBonus',
    'anemodmg':'windBonus',
    'geodmg':'rockBonus',
    'dendrodmg':'grassBonus',
    'cr':'critical',
    'cd':'criticalDamage',
    'hb%':'cureEffect'
}
mapping_position={
    'flower':'flower',
    'plume':'feather',
    'sands':'sand',
    'goblet':'cup',
    'circlet':'head'
}

ig=IdGenerator(1)
def conv2mona(art:Artifact):
    artr={}
    artr['setName']=art.setname
    artr['position']=mapping_position[art.position]
    artr['detailName']=art.piecename_cn
    artr['mainTag']={
        'name':mapping_statname[art.main_stat['name']],
        'value':art.main_stat['value']
    }
    
    artr['normalTags']=[]
    for k,v in art.sub_stat.items():
        if k in ['hp','atk','defs','em']:
            v=round(v)
        artr['normalTags'].append(
            {
                'name':mapping_statname[k],
                'value':v
            }
        )
    artr['omit']=False
    artr['star']=art.star
    artr['level']=art.level
    artr['id']=ig.get_id()
    return artr

def export_mona(art_collection,comment=''):
    ex={
    'version':'1',
    'flower':[],
    'feather':[],
    'sand':[],
    'cup':[],
    'head':[]
    }
    for a in art_collection:
        converted=conv2mona(a)
        ex[converted['position']].append(converted)
    export_path=Path('.\\export')
    if not export_path.exists():
        export_path.mkdir()
    export_filename=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    comment='-'if comment!='' else '' + comment
    export_file=export_path.joinpath(f'export-mona-{export_filename}{comment}.json')
    s=json.dumps(ex)
    with export_file.open(mode='w+') as f:
        f.write(s)




