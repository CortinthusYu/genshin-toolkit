from dataclasses import dataclass

from genshintoolkit.gtcommon.atfdata import *
import random
from genshintoolkit.gtcommon.gtenum import *

@dataclass
class MainStat:
    type:EnumStats
    value:float

class Artifact:
    def __init__(
        self,
        setname:EnumArtifactSet=EnumArtifactSet.Dummy,
        piecename_cn:str='',
        position:EnumArtifactPosition='',
        level:int=20,
        star:int=5,
        main_stat:dict[EnumStats,type_number]=None,
        sub_stats:dict[EnumStats,type_number]=None,
    ) -> None:
        self.setname=setname
        self.piecename_cn=piecename_cn
        self.position=position
        self.level=level
        self.star=star
        self.main_stat=main_stat
        self.sub_stats=sub_stats
    

    def get_stats(self) -> dict:
        return dict(self.main_stat.items()+self.sub_stat.items())

class ArtifactSet:
    def __init__(self,
        flower:Artifact,
        plume:Artifact,
        sands:Artifact,
        goblet:Artifact,
        circlet:Artifact):
        self.flower=flower
        self.plume=plume
        self.sands=sands
        self.goblet=goblet
        self.circlet=circlet

    def __getitem__(self,attr:EnumArtifactPosition):
        return self.__dict__[attr.value]

    def unpack(self) -> dict[EnumStats,type_number]:
        rtn={}
        for position in EnumArtifactPosition:
            single_atf:Artifact=self[position]
            for k,v in single_atf.main_stat:
                if k in rtn.keys():
                    rtn[k]+=v
                else:
                    rtn[k]=v
            for k,v in single_atf.sub_stats:
                if k in rtn.keys():
                    rtn[k]+=v
                else:
                    rtn[k]=v
        return rtn



@dataclass
class ArtifcatStats:
    set:list
    main_stat:dict
    sub_stat:dict


def weighted_random(items):
    total = sum(w for _, w in items)
    n = random.uniform(0, total)
    for x, w in items:
        if n < w:
            break
        n -= w
    return x

class IdGenerator:
    def __init__(self,start:int=0) -> None:
        self.start=start
    
    def get_id(self):
        self.start+=1
        return self.start
        

def pull_substats(main_stat:EnumStats):

    evl_times=5+(weighted_random(weightlist_subcount)-3)
    substats:dict[EnumStats,type_number]={}

    for i in range(4):
        rsl=weighted_random(weightlist_substat)
        while(rsl==main_stat or rsl in substats.keys()):
            rsl=weighted_random(weightlist_substat)
        substats[rsl]=random.choice(substat_values[rsl])
    substats_keys=list(substats.keys())

    for i in range(evl_times-1):
        rsl=random.choice(substats_keys)
        substats[rsl]+=random.choice(substat_values[rsl])
    
    return substats
        
def e2c(e):
    d={EnumArtifactPosition.flower:''}

def print_artifacts(items:list[Artifact]):
    #print('-------20树脂消失--------')
    if len(items)==0:
        print('啊啦没有出货')
    else:
        for i in items:
            print(f'部位: {i.position}')
            print(f'主词条: {i.main_stat.items()[0][0]}')
            for k,v in i[2].items():
                if k in [EnumStats.hps,EnumStats.atks,EnumStats.defs,EnumStats.elemental_mastery]:
                    print(f'{k}: {v:.0f}')
                else:
                    print(f'{k}: {v:.1%}')


def pull_piece(set_name:EnumArtifactSet,position:EnumArtifactPosition=None) -> Artifact:
    
    if position==None:
        position=random.choice([x for x in EnumArtifactPosition])
    substats=None
    mainstat_type=None
    
    if position==EnumArtifactPosition.flower:
        mainstat_type=EnumStats.hp_static
        substats=pull_substats(EnumStats.hp_static)
    elif position==EnumArtifactPosition.plume:
        mainstat_type=EnumStats.atk_static
        substats=pull_substats(EnumStats.atk_static)
    elif position==EnumArtifactPosition.sands:
        mainstat_type=weighted_random(weightlist_sands)
        substats=pull_substats(mainstat_type)
    elif position==EnumArtifactPosition.globlet:
        mainstat_type=weighted_random(weightlist_goblet)
        # will delete if dendro is live
        while(mainstat_type==EnumElement.dendro):
            mainstat_type=weighted_random(weightlist_goblet)
        substats=pull_substats(mainstat_type)
    elif position==EnumArtifactPosition.circlet:
        mainstat_type=weighted_random(weightlist_circlet)
        substats=pull_substats(mainstat_type)

    atf=Artifact(setname=set_name)

    mainstat={
        mainstat_type:mainstat_values[mainstat_type]
    }

    return Artifact(setname=set_name,position=position,main_stat=mainstat,sub_stats=substats)

def pull_pieces():
    count=weighted_random([(1,100),(2,7)])
    parts=[]
    for i in range(count):
        if random.choice([0,1])==1:
            parts.append(pull_piece())
    return parts

def gen_stats_normal(stats):
    '''require stats as dict like {stat:level}\\
    will not check if substats are duplicated with mainstat\\
    '''
    sub_stats={}
    for k,v in stats.items():
        sub_stats[k,v]=substat_values[k,v+1]
    return sub_stats

def gen_stats_avg(main_stat,stats):
    '''require stats as dict like {stat:level}\\
    will not check if substats are duplicated with mainstat\\
    '''
    sub_stats={}
    for k,v in stats.items():
        sub_stats=substat_values_avg[k,v]
    return sub_stats

def harvest_dungeon(set1,set2):
    '''
    :param set1: {setname:setname,piecename_cn:setname_cn}
    '''
    arts=[]
    count=1 if random.random() < rate_fivestardbl else 0 +1

    for i in range(count):
        settype=random.choice([set1,set2])
        artstat=pull_piece()
        arts.append(Artifact(
            setname=settype['setname'],
            piecename_cn=settype[artstat[0]],
            position=artstat[0],
            level=20,
            star=5,
            main_stat=artstat[1],
            sub_stat=artstat[2]
        ))

    return arts


def generate_artifactset(name,mode='standard',**kwargs) -> ArtifactSet:
    atfset={}
    if mode=='standard':
        pass
    if mode=='customize':
        pass

def optimize(artifact_set):
    pass

def gen_artifact_bypoints(sub_stats:tuple[EnumStats],matrix):
    rtn={}
    for s in sub_stats:
        rtn[s]=0.0
    for s,v in zip(sub_stats,matrix):
        for point,value in zip(v,substat_values[s]):
            if s in rtn.keys():
                rtn[s]+=point*value
            else:
                rtn[s]=point*value
    return rtn

def gen_artifact_bypoints_avg(substats:tuple[EnumStats],vector):
    rtn={}
    for s,v in zip(substats,vector):
        rtn[substats]=substat_values_avg[s]*v