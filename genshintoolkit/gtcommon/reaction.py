from genshintoolkit.gtcommon.gtenum import *

factor_amping={
    EnumAmpingReaction.vape_hydro:2,
    EnumAmpingReaction.vape_pyro:1.5,
    EnumAmpingReaction.melt_cryo:1.5,
    EnumAmpingReaction.melt_pyro:2
}

curve_LM_transformative=[0 for i in range(100)]
curve_LM_transformative[90]=723

factor_transformative={
    EnumTransformativeReaction.superconduct:1,
    EnumTransformativeReaction.swirl:1.2,
    EnumTransformativeReaction.electrocharged:2.4,
    EnumTransformativeReaction.shattered:3,
    EnumTransformativeReaction.overload:4,
    EnumTransformativeReaction.bloom:4,
    EnumTransformativeReaction.hyperbloom:4,
    EnumTransformativeReaction.burgeon:6
}

curve_LM_catalyze=[0 for i in range(100)]
curve_LM_catalyze[90]=1447

factor_catalyze={
    EnumCatalyzeReaction.aggravate:1.15,
    EnumCatalyzeReaction.spread:1.25
}

def reaction_amping(reaction:EnumTransformativeReaction,elemental_mastery:int=0,level:int=90,reaction_bonus=0):
    return factor_amping[reaction]*(1+2.78*elemental_mastery/(1400+elemental_mastery)+reaction_bonus)

def reaction_transformative(reaction:EnumTransformativeReaction,elemental_mastery:int=0,level:int=90,reaction_bonus=0):
    return curve_LM_transformative[level]*factor_transformative[reaction]*(1+16*elemental_mastery/(2000+elemental_mastery)+reaction_bonus)

def reaction_catalyze(reaction:EnumCatalyzeReaction,elemental_mastery:int=0,level:int=90,reaction_bonus=0):
    return curve_LM_transformative[level]*factor_catalyze[reaction]*(1+5*elemental_mastery/(1200+elemental_mastery)+reaction_bonus)
