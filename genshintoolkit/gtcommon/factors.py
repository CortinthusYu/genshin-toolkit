from symbol import factor


defense_monster=lambda lv_monster: 500+5*lv_monster

def defense(lv_char:int=90,def_defender=defense_monster(90),def_ignore:float=0,def_decrease=0):
    return (lv_char+100)/(
        (lv_char+100) +
        (
            (1-def_ignore)*
            (1-def_decrease)*
            (def_defender/5)
        )
    )