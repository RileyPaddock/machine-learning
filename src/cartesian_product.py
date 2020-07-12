def cartesian_product(arr):
    points_index = [0 for i in range(len(arr))]
    bounds = range(len(arr))
    points = []
    coords = []
    incomplete = True
    while incomplete:
        for i in bounds:
            coords.append(arr[i][points_index[i]])
        points.append(coords)
        coords = []
        for i in [elem for elem in reversed(bounds)]:
            if points_index[i] < len(arr[i]) - 1:
                points_index[i]+=1
                for j in bounds:
                    if j>i:
                        points_index[j] = 0
                break
        else:
            incomplete = False
    return points


