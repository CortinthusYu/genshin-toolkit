from artifact import harvest_dungeon
from export import export_mona
import yaml
from pathlib import Path

arts=[]

dailyresin=180
days=30

times=int(dailyresin*days/20)

set1={
    'setname':'VermillionHereafter',
    'flower':'生灵之华',
    'plume':'潜光片羽',
    'sands':'阳辔之遗',
    'goblet':'结契之刻',
    'circlet':'虺雷之姿'
}

set2={
    'setname':'EchoesOfAnOffering',
    'flower':'魂香之花',
    'plume':'垂玉之叶',
    'sands':'祝祀之凭',
    'goblet':'涌泉之盏',
    'circlet':'浮溯之珏'
}

if Path('.\\app-simforperiod-config.yaml').exists():
    print('[INFO] Configuration Found, reading....')
    with Path('.\\app-simforperiod-config.yaml').open(mode='r',encoding='utf-8') as f:
        y=yaml.safe_load(f.read())
        set1,set2=(y['set1'],y['set2'])
else:
    print('[INFO] Configuration no found, using default configuration...')
    with Path('.\\app-simforperiod-config.yaml').open(mode='w+',encoding='utf-8') as f:
        y=dict([('set1',set1),('set2',set2)])
        yaml.dump(y,f)



#for i in range(times):
    arts+=harvest_dungeon(set1,set2)

#export_mona(arts)
