from enum import Enum, auto
import typing

#region stat names def
class EnumStats(Enum):
    elemental_mastery='elemental_mastery'
    em='elemental_mastery'
    def_percent='def_percent'
    defp='def_percent'
    def_static='def_static'
    defs='def_static'
    hp_percent='hp_percent'
    hpp='hp_percent'
    hp_static='hp_static'
    hps='hp_static'
    energy_recharge='energy_recharge'
    er='energy_recharge'
    atk_percent='atk_percent'
    atkp='atkp'
    atk_static='atk_static'
    atks='atk_static'
    #what is rb??
    dmg_bonus_all='dmg_bonus_all'
    dmgba='dmg_bonus_all'
    dmg_bonus_elemental='dmg_bonus_elemental'
    dmgbe='dmg_bonus_elemental'
    base_dmg='base_dmg'
    bd='base_dmg'
    reaction_bonus_amping='reaction_bonus_amping'
    rba='reaction_bonus_amping'
    reaction_bonus_transformative='reaction_bonus_transformative'
    rbt='reaction_bonus_transformative'

    dmg_pyro='dmg_pryo'
    dmgp='dmg_pryo'
    dmg_hydro='dmg_hydro'
    dmgh='dmg_hydro'
    dmg_electro='dmg_electro'
    dmge='dmg_electro'
    dmg_cryo='dmg_cryo'
    dmgc='dmg_cryo'
    dmg_anemo='dmg_anemo'
    dmga='dmg_anemo'
    dmg_geo='dmg_geo'
    dmgg='dmg_geo'
    dmg_dendro='dmg_dendro'
    dmgd='dmg_dendro'
    dmg_physical='dmg_physical'
    dmgph='dmg_physical'

    crit_rate='crit_rate'
    cr='crit_rate'
    crit_dmg='crit_dmg'
    cd='crit_dmg'

    healing_bonus='heal_bonus'
    hb='heal_bonus'
    healing_incoming='healing_incoming_bonus'
    hib='healing_incoming_bonus'

    def_ignore='def_ignore'
    defi='def_ignore'
    def_decrease='def_decrease'
    defd='def_decrease'

    res_decrease='res_decrease'
    resd='resd'

class EnumAction(Enum):
    normal_attack='normal_attack'
    normal='normal_attack'
    na='normal_attack'
    charged_attack='charged_attack'
    charge='charged_attack'
    ca='charged_attack'
    plunge='plunge'
    pl='plunge'
    high_plunge='high_plunge'
    hpl='high_plunge'
    elemental_skill='element_skill'
    skill='elemental_skill'
    e='elemental_skill'
    elemental_burst='elemental_burst'
    burst='elemental_burst'
    q='elemental_burst'
    all='all'

class EnumElement(Enum):
    pyro='pyro'
    hydro='hydro'
    electro='electro'
    cryo='cryo'
    anemo='anemo'
    geo='geo'
    dendro='dendro'
    elemental='elemental'

class EnumHitElementType(Enum):
    pyro='pyro'
    hydro='hydro'
    electro='electro'
    cryo='cryo'
    anemo='anemo'
    geo='geo'
    dendro='dendro'
    elemental='elemental'
    physical='physical'
    all='all'

class EnumReaction(Enum):
    vape_hydro='vape_hydro'
    vape_pyro='vape_pyro'
    melt_pyro='melt_pyro'
    melt_cryo='melt_cryo'
    electrocharged='electrocharged'
    overload='overload'
    swirl='swirl'
    superconduct='superconduct'
    crystallize='crystallize'
    shattered='shattered'
    none='none'
    all='all'

class EnumAmpingReaction(Enum):
    vape_hydro='vape_hydro'
    vape_pyro='vape_pyro'
    melt_pyro='melt_pyro'
    melt_cryo='melt_cryo'
    all='all'

class EnumTransformativeReaction(Enum):
    electrocharged='electrocharged'
    overload='overload'
    swirl='swirl'
    superconduct='superconduct'
    crystallize='crystallize'
    shattered='shattered'
    bloom='bloom'
    hyperbloom='hyperbloom'
    burgeon='burgeon'
    all='all'

class EnumCatalyzeReaction(Enum):
    aggravate='aggravate'
    spread='spread'

class EnumHitResult(Enum):
    straight_dmg='straight_dmg'
    amping_dmg='amping_dmg'
    heal='heal'
    electrocharged='electrocharged'
    overload='overload'
    swirl='swirl'
    superconduct='superconduct'
    crystallize='crystallize'
    shield='shield'
    energy_regen='energy_regen'
    element_apply='element_apply'

#endregion

class EnumArtifactPosition(Enum):
    flower='flower'
    plume='plume'
    sands='sands'
    globlet='globlet'
    circlet='circlet'

superconduct_basedmg=773
transformative_multiplier={
    #EnumTransformativeReaction.crystallize:1851,
    EnumTransformativeReaction.superconduct:1,
    EnumTransformativeReaction.swirl:1.2,
    EnumTransformativeReaction.electrocharged:2.4,
    EnumTransformativeReaction.shattered:3,
    EnumTransformativeReaction.overload:4
}

type_number=typing.Union[int,float,typing.Callable]

class EnumArtifactSet(Enum):
    Dummy=auto() #use to construct fake super artifact
    Adventurer=auto()
    ArchaicPetra=auto()
    Berserker=auto()
    BlizzardStrayer=auto()
    BloodstainedChivalry=auto()
    BraveHeart=auto()
    CrimsonWitchOfFlames=auto()
    DefendersWill=auto()
    EchoesOfAnOffering=auto()
    EmblemOfSeveredFate=auto()
    Gambler=auto()
    GladiatorsFinale=auto()
    HeartOfDepth=auto()
    HuskOfOpulentDreams=auto()
    Instructor=auto()
    Lavawalker=auto()
    LuckyDog=auto()
    MaidenBeloved=auto()
    MartialArtist=auto()
    NoblesseOblige=auto()
    OceanHuedClam=auto()
    PaleFlame=auto()
    PrayersForDestiny=auto()
    PrayersForIllumination=auto()
    PrayersForWisdom=auto()
    PrayersToSpringtime=auto()
    ResolutionOfSojourner=auto()
    RetracingBolide=auto()
    Scholar=auto()
    ShimenawasReminiscence=auto()
    TenacityOfTheMillelith=auto()
    TheExile=auto()
    ThunderingFury=auto()
    Thundersoother=auto()
    TinyMiracle=auto()
    TravelingDoctor=auto()
    VermillionHereafter=auto()
    ViridescentVenerer=auto()
    WanderersTroupe=auto()
