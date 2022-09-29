def get_point_distribution(points_count:int,prop_count:int):
    arr=[]
    tmp=[]
    def dist(points,depth):

        if depth==1:
            tmp.append(points)
            arr.append(tuple(tmp))

        else:
            if points==0:
                tmp.append(0)
                dist(0,depth-1)

            else:
                for i in range(points+1):
                    tmp.append(i)
                    dist(points-i,depth-1)
                    while(not len(tmp)== prop_count-depth):
                        tmp.pop()

    dist(points_count,prop_count)
    return arr