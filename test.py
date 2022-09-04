from artifact import pull_parts,print_artifacts
def main():
    artifacts=[]

    test_time=7*9

    for i in range(test_time):
        artifacts+=pull_parts()

    dbl_crit_atf=[]

    for i in artifacts:
        keys=i[2].keys()
        if i[1]=='critrate' or i[1]=='critdmg':
            if 'critrate' in keys or 'critdmg' in keys:
                dbl_crit_atf.append(i)
        elif i[0]=='flower' or i[0]=='feather':
            if 'critrate' in keys and 'critdmg' in keys:
                dbl_crit_atf.append(i)
        elif i[0] == 'hourglass' and i[1] == 'atk%':
            if 'critrate' in keys and 'critdmg' in keys:
                dbl_crit_atf.append(i)
        elif i[0] == 'cup' and i[0].endswith('dmg'):
            if 'critrate' in keys and 'critdmg' in keys:
                dbl_crit_atf.append(i)

    print(f'一周七天全打圣遗物本，消耗{test_time*20}树脂，获得了{len(dbl_crit_atf)}件双爆圣遗物')
    #print_artifacts(artifacts)

for i in range(10):
    main()
