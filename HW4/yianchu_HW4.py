import json
import requests
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random as random
from matplotlib.path import Path
import numpy as np
random.seed(17)


RedliningDataJson = requests.get(
    'https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/MIDetroit1939.geojson')
RedliningData = RedliningDataJson.json()

# print(RedliningData['features'][8]['properties']['holc_grade'])

# for i in RedliningData['features']:
#     print(i['properties']['holc_grade'])


class DetroitDistrict:
    def __init__(self, coordinates, grade, color, name, qualitative):
        self.Coordinates = np.array(coordinates, dtype=object)
        self.HolcGrade = grade
        self.HolcColor = color
        self.name = name
        self.Qualitative_Description = qualitative
        self.RandomLat = None
        self.RandomLong = None
        self.Median_Income = None
        self.CensusTract = None

    def __str__(self):
        return f"{self.Coordinates}, {self.HolcGrade}, {self.HolcColor}, {self.name}, {self.Qualitative_Description}, {self.RandomLat}, {self.RandomLong}, {self.Median_Income}, {self.CensusTract} "
# print(RedliningData['features'][0]['geometry'].keys())

# print(RedliningData['features'][0]['properties']
#       ['area_description_data'].keys())


# ==========Step2===============

# print(RedliningData['features'][0]['geometry']['coordinates'][0][0])
# print(RedliningData['features'][0]['properties']['holc_grade'])
# print(RedliningData['features'][0]['properties']['holc_grade'])
# print(RedliningData['features'][0]['properties']['name']) #number 代換
# print(RedliningData['features'][0]['properties']['area_description_data']['8'])


Districts = []
num = 0
for dist in RedliningData['features']:
    if dist['properties']['holc_grade'] == 'A':
        color = 'darkgreen'
    elif dist['properties']['holc_grade'] == 'B':
        color = 'cornflowerblue'
    elif dist['properties']['holc_grade'] == 'C':
        color = 'gold'
    else:
        color = 'maroon'
    distict = DetroitDistrict(dist['geometry']['coordinates'][0], dist['properties']['holc_grade'],
                              color, num, dist['properties']['area_description_data']['8'])
    Districts.append(distict)
    num += 1
    # print(distict)

# ==========Step3===============

fig, ax = plt.subplots()
for dist in Districts:
    ax.add_patch(
        Polygon([i for i in dist.Coordinates[0]], color=dist.HolcColor, closed=True, ec='black'))
    ax.autoscale()
    plt.rcParams["figure.figsize"] = (15, 15)
plt.show()

# ==========Step4===============

# 'xgrid' is a array which has the number from -83.5 to -82.8 with step 0.004
xgrid = np.arange(-83.5, -82.8, .004)
# 'ygrid' is a array which has the number from 42.1 to 42.6 with step 0.004
ygrid = np.arange(42.1, 42.6, .004)
# Return coordinate matrices('xmesh', 'ymesh') from coordinate vectors('xgrid', 'ygrid').
xmesh, ymesh = np.meshgrid(xgrid, ygrid)
# stack two array(xmesh.flatten(),ymesh.flatten()), and .flatten() will make array turn into one dimension. After that, transpose the stack array and assign it into the variable, 'points'.
points = np.vstack((xmesh.flatten(), ymesh.flatten())).T
for j in Districts:  # loop the class list, 'Districts'.
    # get the 'Coordinates' value of each class in Districts
    p = Path(j.Coordinates[0])
    # test each row in 'points' whether the same as the any vertices in 'p'. if yes => True; if No => False
    grid = p.contains_points(points)
    # print (class j in 'Districts', getting the value in 'points', which the index is that randomly choosing a number from array contained all indexs that are true in 'grid'(grid[index] == True).
    print(j, " : ", points[random.choice(np.where(grid)[0])])
    # restore the variable, 'points' = points[random.choice(np.where(grid)[0])](the above describe)
    point = points[random.choice(np.where(grid)[0])]
    # store the value of point[0] into the attritube, RandomLong, in class.
    j.RandomLong = point[0]
    # store the value of point[1] into the attritube, RandomLat, in class.
    j.RandomLat = point[1]


# ==========Step5===============
fips = []
# counties_num = []
# https://geo.fcc.gov/api/census/area
for j in Districts:
    query = {"lat": j.RandomLat,
             "lon": j.RandomLong, "censusYear": 2010}
    censusData = requests.get(
        'https://geo.fcc.gov/api/census/area', params=query)
    censusData = censusData.json()
    j.CensusTract = censusData['results'][0]['block_fips']
    fips.append([censusData['results'][0]['state_fips'],
                censusData['results'][0]['county_fips']])

# ==========Step6===============
key = "5aeb7b2638927401f40f044e6490b207e5a671c7"
name = "B19013_001E"
base_url = "https://api.census.gov/data/2018/acs/acs5"
for i in range(len(Districts)):
    census = Districts[i].CensusTract[5:11]
    base_url = 'https://api.census.gov/data/2018/acs/acs5?get=B19013_001E&for=tract:' + census + '&in=state:' + \
        fips[i][0] + '%20county:' + fips[i][1][-3:] + \
        '&key=5aeb7b2638927401f40f044e6490b207e5a671c7'
    IncomeData = requests.get(base_url)
    IncomeData = IncomeData.json()
    Districts[i].Median_Income = IncomeData[1][0]

# ==========Step7-1===============


def median(l):
    half = len(l) // 2
    l.sort()
    # print(l)
    if not len(l) % 2:
        return (l[half - 1] + l[half]) / 2.0
    return l[half]


A_income = []
B_income = []
C_income = []
D_income = []

for i in Districts:
    if i.HolcGrade == 'A':
        A_income.append(int(i.Median_Income))
    elif i.HolcGrade == 'B':
        B_income.append(int(i.Median_Income))
    elif i.HolcGrade == 'C':
        C_income.append(int(i.Median_Income))
    else:
        D_income.append(int(i.Median_Income))

A_mean_income = sum(A_income)/len(A_income)
A_median_income = median(A_income)
B_mean_income = sum(B_income)/len(B_income)
B_median_income = median(B_income)

print(A_mean_income)
print(A_median_income)
print(B_mean_income)
print(B_median_income)


# ==========Step7-2===============

A_10_Most_Common = []
B_10_Most_Common = []
C_10_Most_Common = []
D_10_Most_Common = []

A_string = []
B_string = []
C_string = []
D_string = []


def each_word_num(category):
    dir = {}
    word_set = set(category)
    word_set = list(word_set)

    for i in range(len(word_set)):
        dir[word_set[i]] = 0
        for j in range(len(category)):
            if word_set[i] == category[j]:
                dir[word_set[i]] += 1
    return dir


characters = ",!?."
for i in Districts:
    qual = i.Qualitative_Description.lower()
    for char in range(len(characters)):
        qual = qual.replace(characters[char], '')
    qual = qual.split()
    for word in qual:
        if any(elem.isdigit() for elem in word):
            qual.remove(word)

    if i.HolcGrade == 'A':
        A_string.extend(qual)
    elif i.HolcGrade == 'B':
        B_string.extend(qual)
    elif i.HolcGrade == 'C':
        C_string.extend(qual)
    else:
        D_string.extend(qual)

A_10_Most_Common = each_word_num(A_string)
B_10_Most_Common = each_word_num(B_string)
C_10_Most_Common = each_word_num(C_string)
D_10_Most_Common = each_word_num(D_string)

A_10_Most_Common = sorted(A_10_Most_Common.items(),
                          key=lambda d: d[1], reverse=True)
B_10_Most_Common = sorted(B_10_Most_Common.items(),
                          key=lambda d: d[1], reverse=True)
C_10_Most_Common = sorted(C_10_Most_Common.items(),
                          key=lambda d: d[1], reverse=True)
D_10_Most_Common = sorted(D_10_Most_Common.items(),
                          key=lambda d: d[1], reverse=True)
A_uni = []
B_uni = []
C_uni = []
D_uni = []

for i in range(len(A_10_Most_Common)):
    if A_10_Most_Common[i][0] not in B_string and C_string and D_string:
        A_uni.append(A_10_Most_Common[i])
for i in range(len(B_10_Most_Common)):
    if B_10_Most_Common[i][0] not in A_string and C_string and D_string:
        B_uni.append(B_10_Most_Common[i])
for i in range(len(C_10_Most_Common)):
    if C_10_Most_Common[i][0] not in B_string and A_string and D_string:
        C_uni.append(C_10_Most_Common[i])
for i in range(len(D_10_Most_Common)):
    if D_10_Most_Common[i][0] not in B_string and C_string and A_string:
        D_uni.append(D_10_Most_Common[i])

A_10_Most_Common = A_uni[:10]
B_10_Most_Common = B_uni[:10]
C_10_Most_Common = C_uni[:10]
D_10_Most_Common = D_uni[:10]

print(A_10_Most_Common)
print(B_10_Most_Common)
print(C_10_Most_Common)
print(D_10_Most_Common)


# ==========Bonus1===============
'''
fig, ax = plt.subplots()
Imin = 10000
Imax = 0
for dist in Districts:
    if int(dist.Median_Income) < Imin:
        min = int(dist.Median_Income)
    if int(dist.Median_Income) > Imax:
        max = int(dist.Median_Income)
# print(min)
# print(max)

cmap = plt.get_cmap("PuBu")
norm = plt.Normalize(Imin, Imax)
for dist in Districts:
    ax.add_patch(Polygon([i for i in dist.Coordinates[0]], color=[cmap(norm(income))
                              for income in dist.Median_Income], closed=True, ec='black'))
    ax.autoscale()
    plt.rcParams["figure.figsize"] = (15, 15)
'''
# ax.set_edgecolor([mcd.XKCD_COLORS[f"xkcd:{color}"] for color in thisDict["Holc_Color"]])
# plt.show()

    