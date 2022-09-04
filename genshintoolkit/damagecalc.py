from dataclasses import dataclass
import re
import typing
import genshintoolkit.artifact as atf
from time import time
from genshintoolkit.gtcommon.gtenum import *

#region class def

class Effect:
    '''
    An effect is a bunch of multiple modifiers
    apply_to:{attack,charge,plunge,skill,burst,pyro,elemental,pyro,physic...}
    modifiers:{atk,atkp,def,defp,hp,hpp,em,rb,dmgb,hb,dmgb,defi,defr,resd}
    '''
    def __init__(self,
                name:str,
                apply_to:list[str],
                modifiers:dict[str,type_number],
                is_static:bool=True,
                stats_require:list[str]=[]) -> None:
        '''
        apply_to={
            'type_action':[attack,charge,plunge,skill,burst,all]
            'type_elem':pyro,...,all
            'type_reaction:normal,vape,melt,transformative
        }
        '''
        self.name=name
        self.apply_to=apply_to
        self.modifiers=modifiers
        self.is_static=is_static
        self.stats_require=stats_require

@dataclass
class ApplyTagsSet:
    type_action:list[EnumAction]
    type_element:list[EnumHitElementType]
    type_reaction:list[EnumReaction]

applytag_all=ApplyTagsSet([EnumAction.all,],type_action=[EnumHitElementType.all,],type_reaction=[EnumReaction.all,])

#declearation only, the realization is later
class Stats:
    def get_StaticStat(self,stat_type:EnumStats) -> type_number:
        pass

class Buff:
    def __init__(       self,
                        name:str,
                        apply_to:ApplyTagsSet,
                        target_stat:EnumStats,
                        value:type_number|None=None,
                        required_stats:list[EnumStats]|None=None,
                        calc_func:typing.Callable|None=None,
                        is_snapshot:bool=False, #true means buff's value is fixed when the buff takes effect, won't change if the source stat change
                        is_static:bool=True #true means the value that the buff adds to the stat can be refer by other buffs
                ) -> None:
        self.name=name
        self.target_stat:str=target_stat
        if required_stats == None:
            self.value = value
        else:
            self.value=None
        self.required_stats={}
        self.apply_to=apply_to
        # for s in required_stats:
        #     self.required_stats[s]=0
        # if len(self.required_stats) == 0:
        #     self.is_static=True
        # else:
        #     self.is_static=False
        self.calc_func=calc_func
        self.is_snapshot=is_snapshot
        self.is_static=is_static

    def get_value(self,stats:Stats):
        if self.value==None or not self.is_snapshot:
            for s in self.required_stats.keys():
                self.required_stats[s]=stats.get_StaticStat(s)
            return {self.target_stat:self.calc_func(self.required_stats)}
        else:
            return {self.target_stat:self.value}
        

class Stats:
    def __init__(self) -> None:
        # static
        self.stats_static:dict[EnumStats,list[Buff]]={i:[] for i in EnumStats}

        #dynamic
        self.stats_dyn:dict[EnumStats,list[Buff]]={i:[] for i in EnumStats}

    def update_stats(self,buff:Buff):
        if buff.is_static:
            self.stats_static[buff.target].append(buff)
        else:
            self.stats_dyn[buff.target].append(buff)

    def from_artifactset(self,art_set:atf.ArtifactSet):
        for k,v in art_set.unpack().items():
            b=Buff('artifact_stats',ApplyTagsSet(EnumAction.all,EnumElement.all,EnumAmpingReaction.all),k,v)
            self.update_stats(b)

    def clear_artifact_stats(self):
        for k,v in self.stats_static:
            for i,b in enumerate(v):
                if b.name == 'artifact_substats':
                    v.pop(i)
        return self


    def get_StaticStat(self,stat_type:EnumStats):
        #TODO 不是返回加成值而是返回总值
        return sum([x.get_value() for x in self.stats_static[stat_type]])

    def get_FinalStat(self,stat_type:EnumStats):
        '''will snapshot after this func is called'''
        rtn=self.get_StaticStat(stat_type)
        for buff in self.stats_dyn[stat_type]:
            rtn+=buff.get_value(self)
        return rtn

    def remove_buff(self,buff_name:str):
        '''Will snapshot before buff removed'''
        self.get_FinalStat()
        for i in (self.stats_static,self.stats_dyn):
            for j,k in i.items():
                for index,x in enumerate(k):
                    if x.name==buff_name:
                        k.pop(index)

@dataclass
class Multiplier:
    hit_result=EnumHitResult
    atk:type_number=0
    defn:type_number=0
    hp:type_number=0
    em:type_number=0
    er:type_number=0


@dataclass
class Hit:
    type_action:EnumAction #attack,charge,plunge,skill,burst
    type_element:EnumHitElementType
    multipliers:list[Multiplier]
    durition:type_number
    comment:str

@dataclass
class Action:
    #tag:attack,charge,plunge,skill,burst,<elemental:pryo...>
    tags:list
    hits:list[Hit]
    multipliers:list
    durition:list
    comment:str

class HitResult:
    def __init__(self,tags,value,comment='',caused:str='dmg') -> None:
        self.tags=tags
        self.value=value
        self.caused=caused
        self.comment=comment

    def __repr__(self) -> str:
        return f'[DMG] Action {self.comment} caused {self.value} {self.caused}'

@dataclass
class Weapon:
    base_atk:int
    substat:dict[EnumStats,type_number]
    effect:list

class Character:
    def __init__(self,base_atk,base_def,base_hp,base_bonus:EnumStats) -> None:
        self.base_atk=base_atk
        self.base_def=base_def
        self.base_hp=base_hp
        self.base_bonus=base_bonus

class Enemy:
    def __init__(self,max_hp=100000000,lv=90,resistence=0.1) -> None:
        self.resistences={e:resistence for e in EnumElement}
        self.resistences['physical']=resistence
        self.max_hp=max_hp
        self.lv=lv
        self.resistence=resistence
        self.count_emattachment=0
        self.timer_eleattachmet=0
        self.elem_attachtype='none'
        self.elem_attachintensity=0
    
    def counter_elementattach(self):
        pass

    def set_resistence(self,element_type:EnumElement|typing.Literal['physical'],value):
        self.resistences[element_type]=value

#endregion data def

#region tool funcs
# def reaction_bonus_multiply(elem_mastery,reaction_type,add_bonus):
#     if reaction_type in ['pryovaperize','cryomelt']:
#         factor=1.5
#     else:
#         factor=2.0
#     return factor*(2.78*elem_mastery/(1400+elem_mastery)+add_bonus)

# def reaction_basedmg(elem_mastery,reaction_type,add_bonus,level=90):
#     factor_level=723
#     factor_type={
#         'superconduct':1,
#         'swirl':1.2,
#         'electrocharged':2.4,
#         'icebreak':3,
#         'overload':4
#     }
#     return factor_level*((16*elem_mastery/(elem_mastery+2000))+add_bonus)*factor_type[reaction_type]


def factor_resistence(resistence):
    if resistence > 0.75:
        return 1/(1+4*resistence)
    elif resistence < 0:
        return 1-resistence/2
    else:
        return 1-resistence

def factor_defense(def_ignore=0,def_reduce=0,level_atker=90,level_defder=90,def_increase=0):
    return ((level_atker+100)/(1-def_ignore)*(1-def_reduce+def_increase)*(level_defder+100)+level_atker+100)

""" def apply_buff(
                action:Action,
                buff:Effect,
            ) -> dict:
    rtn={}
    # phase 1, apply em,rc,def,hp,for those stats will not be based on 
    if 'all' in buff.apply_to:
        rtn.update(buff.modifiers)
        return rtn
    if 'elemental' in buff.apply_to:
        if not len({'pyro','cryo','electro','geo','dendro','anemo','geo','hydro'} & set(action.tags))==0:
            rtn.update(buff.modifiers) """

def compare_condiction(A:typing.Iterable,B:typing.Iterable):
    for i in A:
        if i in B:
            return True
    return False


#endregion

""" class DmgCalulation:
    def __init__(
                self,
                character:Character,
                weapon:Weapon,
                artifact_set:list[atf.ArtifactSet],
                enemy:Enemy,
                buffs:list[Effect],
                action_list) -> None:
        #initiate calc data
        self.character=character
        self.weapon=weapon
        self.artifact_set=artifact_set
        self.buffs=buffs
        self.action_list=action_list
        self.enemy=enemy
        self.time_cost=0
        self.total_dmg=0
        self.current_hit=Action([],[],[])
        self.stats={
            'base_atk':self.character.base_atk+self.weapon.base_atk,
            'atkp':0,
            'atk':0,
            'defp':0,
            'defs':0,
            'hp':0,
            'hps':0,
            'cr':0,
            'cd':0,
            'hb':0, #heal bonus
            'em':0,
            'dmgb':0, #damage_bonus
            'dmgbase':0,
            'rbt':0, #reaction bonus transformative
            'rb':0,
            'defi':0,#def ignore
            'defr':0,#def reduce
            'resd':0 #resistance reduce
        }

        #assemble character data
        #add all stat to self.buffs
    
    def factor_baseatk(self):
        return self.character.base_atk+self.weapon.base_atk

    def factor_attackbonus(self):
        atk_percentagesum=0
        for i in self.buffs:
            pass

    def apply_buff(self,buff_type):
        for i in self.e:
            pass
    
    def calc_hit(self,multiplier,reaction='none'):
        # initiate
        factor_baseatk=self.character.base_atk+self.weapon.base_atk
        factor_atkprecentbonus=0
        factor_atkbonus=0
        factor_atk=0
        factor_dmgbonus=0
        factor_res=0
        factor_def=0
        factor_basedmg=0
        rtn=[]
        
        modifiers_delayed=[]

        #sum static data first
        for b in self.buffs:
            if (self.current_hit.type_action in b.apply_to['type_action'] or 'all' in b.apply_to['type_action']) and (self.current_hit.type_elem in b.apply_to['type_elem'] or 'all' in self.b['type_elem']):
                for m,v in b.modifiers.items():
                    if not hasattr(v,'__call__'):
                        self.stats[m]+=v
                    else:
                        modifiers_delayed.append((m,v))
                for m,v in modifiers_delayed:
                    self.stats[m]+=v(self)
        
        #base dmg
        factor_basedmg=self.stats['base_dmg']+(self.stats['base_atk']*(1+self.stats['atkp'])+self.stats['atk'])*multiplier

        #em
        if reaction=='none':
            factor_em=1
        elif reaction in ['melt','vaperize']:
            factor_em=reaction_bonus_multiply(elem_mastery=self.stats['em'],
                                                reaction_type=reaction,
                                                add_bonus=self.stats['rb'])
        elif reaction in ['superconduct','electrocharged','icebreak','overload','swirl']:
            factor_em=1
            dmg_trans=reaction_basedmg(elem_mastery=self.stats['em'],
                                        reaction_type=reaction,
                                        add_bonus=self.stats['rbt'])*factor_resistence(self.enemy.resistence-self.stats['resd'])
            rtn.append(HitResult([reaction,'transformative'],dmg_trans,''))

        # dmg bonus

        factor_dmgbonus=1+self.stats['db']

        # resistence

        factor_res=factor_resistence(self.enemy.resistence-self.stats['resd'])

        #defence

        factor_def=factor_defense(def_ignore=self.stats['defi'],def_reduce=self.stats['defr'])

        rtn.append(HitResult(
            tags=[reaction],
            value=factor_basedmg * factor_em * factor_dmgbonus * factor_res * factor_def
        ))

        return rtn
 """

class DmgCalculation:
    def __init__(
        self,
        character:Character,
        weapon:Weapon,
        artifact_set:atf.ArtifactSet|dict[EnumStats,type_number],
        buffs:list[Buff],
        hit:Hit,
        enemy:Enemy  ) -> None:
        '''init calc object'''

        #initiate properties
        self.charactor=character
        self.weapon=weapon
        self.artifact_set=artifact_set
        self.buffs=buffs
        self.hit=hit
        self.enemy=enemy
        self.stats:Stats=Stats()

        #initiate stats
        if type(artifact_set) == atf.ArtifactSet:
            self.stats.from_artifactset(artifact_set)
        else:
            for k,v in artifact_set:
                b=Buff('artifact_substats',ApplyTagsSet(EnumAction.all,EnumElement.all,EnumAmpingReaction.all),k,v)
                self.stats.update_stats(b)
        
    def apply_buff(self):
        for b in self.buffs:
            ismatch_actiontype=self.hit.type_action in b.apply_to.type_action or EnumAction.all in b.apply_to.type_action
            if ismatch_actiontype:
                self.stats.update_stats(b)
    
    def calc_hit(self,hit:Hit,buffs:list[Buff]):
        results:list[HitResult]=[]
        


    def get_yieldcurve(self,stat:EnumStats):
        pass

    def update_artifactset(self,artifact_set:atf.ArtifactSet|dict[EnumStats,type_number]):
        if type(artifact_set) == atf.ArtifactSet:
            self.stats.clear_artifact_stats().from_artifactset(artifact_set)
        else:
            for k,v in artifact_set:
                b=Buff('artifact_substats',ApplyTagsSet(EnumAction.all,EnumElement.all,EnumAmpingReaction.all),k,v)
                self.stats.update_stats(b)
   

