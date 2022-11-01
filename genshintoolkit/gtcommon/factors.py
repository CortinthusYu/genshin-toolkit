

defense_monster=lambda lv_monster: 500+5*lv_monster

def defense(lv_char:int=90,def_defender=defense_monster(90),def_ignore:float=0,def_decrease=0):
    return (lv_char+100)/(
        (lv_char+100) +
        (
            (1-def_ignore)*
            (1-def_decrease)*
            (def_defender/5) # 其实就是(lv_monster+100)
        )
    )

def resistence(res_decrease:float=0,base_res:float=0.1):
    '''
    delta_res: 减抗用正数
    base_res: 默认0.9
    '''
    res=base_res-res_decrease
    if res>0.75:
        return 1/(1+4*res)
    elif res<0:
        return 1-res/2
    else:
        return 1-res

def critical(crit_rate:float,crit_dmg:float):
    '''
    a crit func
    '''
    crit_rate+=0.05
    crit_dmg+=0.5
    crit_rate=min(1,crit_rate)

    return 1+crit_rate*crit_dmg

def critical_test(crit_rate:float,crit_dmg:float):
    '''
    '''
    crit_rate+=0.05
    is_critrate_overflew=crit_rate>1
    crit_dmg+=0.5

    return 1+crit_rate*crit_dmg,is_critrate_overflew