from pathlib import Path
import json
import yaml
#from genshintoolkit.datamgr.parser.textmap import mgr

data_root=Path(".").joinpath('data')

if not data_root.exists():
    data_root.mkdir()


config_char=Path('genshindata\ExcelBinOutput\AvatarExcelConfigData.json')
config_permote=Path('genshindata\ExcelBinOutput\AvatarPromoteExcelConfigData.json')
config_curve=Path('genshindata\ExcelBinOutput\AvatarCurveExcelConfigData.json')

char_data={}
curve_data={
    'GROW_CURVE_HP_S4':[0,],
    'GROW_CURVE_ATTACK_S4':[0,],
    'GROW_CURVE_HP_S5':[0,],
    'GROW_CURVE_ATTACK_S5':[0,],
}

with config_char.open() as fc, config_permote.open() as fp, config_curve.open() as fcr:
    data_char=json.load(fc)
    data_prom=json.load(fp)
    data_curve=json.load(fcr)
    for c in data_curve:
        for i in c['curveInfos']:
            curve_data[i['type']].append(i['value'])
    grow_curve_file=data_root.joinpath('grow_curve.yaml')
    with grow_curve_file.open('w+') as gcf:
        yaml.dump(curve_data,gcf)


