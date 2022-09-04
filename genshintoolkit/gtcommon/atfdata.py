from genshintoolkit.gtcommon.gtenum import *
rate_fivestardbl=0.107

weightlist_sands=[(EnumStats.hp_percent,1334),
                (EnumStats.atk_percent,1333),
                (EnumStats.def_percent,1333),
                (EnumStats.energy_recharge,500),
                (EnumStats.elemental_mastery,500)]

weightlist_goblet=[(EnumStats.hp_percent,85),
                    (EnumStats.atk_percent,85),
                    (EnumStats.def_percent,80),
                    (EnumStats.dmg_pyro,20),
                    (EnumStats.dmg_hydro,20),
                    (EnumStats.dmg_cryo,20),
                    (EnumStats.dmg_electro,20),
                    (EnumStats.dmg_anemo,20),
                    (EnumStats.dmg_geo,20),
                    (EnumStats.dmg_dendro,20),
                    (EnumStats.elemental_mastery,10)]

weightlist_circlet=[(EnumStats.hp_percent,22),
                (EnumStats.atk_percent,22),
                (EnumStats.def_percent,22),
                (EnumStats.healing_bonus,10),
                (EnumStats.elemental_mastery,4),
                (EnumStats.crit_rate,10),
                (EnumStats.crit_dmg,10)]

weightlist_subcount=[(3,4),(4,1)]

weightlist_substat=[(EnumStats.hp_static,150),
                    (EnumStats.atk_static,150),
                    (EnumStats.def_static,150),
                    (EnumStats.hp_percent,100),
                    (EnumStats.atk_percent,100),
                    (EnumStats.def_percent,100),
                    (EnumStats.crit_rate,75),
                    (EnumStats.crit_dmg,75),
                    (EnumStats.elemental_mastery,100),
                    (EnumStats.energy_recharge,100)]

substat_values={
    EnumStats.hp_static:[209.13,239,268.88,298.75],
    EnumStats.atk_static:[13.62,15.56,17.51,19.45],
    EnumStats.def_static:[16.20,18.52,20.83,23.15],
    EnumStats.hp_percent:[0.0408,0.0466,0.0525,0.0583],
    EnumStats.atk_percent:[0.0408,0.0466,0.0525,0.0583],
    EnumStats.def_percent:[0.0510,0.0583,0.0656,0.0729],
    EnumStats.crit_rate:[0.0272,0.0311,0.0350,0.0389],
    EnumStats.crit_dmg:[0.0544,0.0622,0.06699,0.0777],
    EnumStats.energy_recharge:[0.0453,0.0518,0.0583,0.0648],
    EnumStats.elemental_mastery:[16.32,18.65,20.98,23.31]
}

substat_values_avg={
    EnumStats.def_static:20,
    EnumStats.def_percent:0.062,
    EnumStats.hp_static:254,
    EnumStats.hp_percent:0.05,
    EnumStats.atk_static:17,
    EnumStats.atk_percent:0.05,
    EnumStats.energy_recharge:0.055,
    EnumStats.elemental_mastery:20,
    EnumStats.crit_rate:0.033,
    EnumStats.crit_dmg:0.066
}

mainstat_values={
    EnumStats.hp_static:4780,
    EnumStats.hp_percent:0.466,
    EnumStats.atk_static:311,
    EnumStats.atk_percent:0.466,
    EnumStats.def_percent:0.588,
    EnumStats.energy_recharge:0.518,
    EnumStats.elemental_mastery:187,
    EnumStats.dmg_pyro:0.466,
    EnumStats.dmg_hydro:0.466,
    EnumStats.dmg_cryo:0.466,
    EnumStats.dmg_electro:0.466,
    EnumStats.dmg_anemo:0.466,
    EnumStats.dmg_geo:0.466,
    EnumStats.dmg_dendro:0.466,
    EnumStats.crit_rate:0.311,
    EnumStats.crit_dmg:0.622,
    EnumStats.healing_bonus:0.359
}