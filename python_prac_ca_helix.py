##
# Calculating helical axis
##
pdbpath = input("Give the path to the file:")
# test input with ./Téléchargements/1bta.pdb
#
aliasf = str('file_') + str(pdbpath)[-8:-4]
with open(pdbpath, 'r') as aliasa:
# check if pdb file is the correct one!
#
    pdbf = str()
    with open(pdbpath, 'r') as testf :
        linef = testf.readline()
        pdbf = linef[-19:-15].lower()
        if pdbf == aliasf[-4:] :
# copying atom,res, coords from pdb file
# extract x coordinates champs 6 / 31:38 
# extract y coordinates champs 7/ 38:46
# extract z coordinates champs 8/ 46:54
# e.g of coords : 10.976   1.261   3.114  1.00
            listx = []
            listy = []
            listz = []
            with open('{}_outca.pdb'.format(pdbf), 'r') as ocam:
                for line in ocam:
                    champs = line.split()
                    if champs[0] == "ATOM" and champs[2]=="CA":
                        listx.append(float(champs[4]))
                        listy.append(float(champs[5]))
                        listz.append(float(champs[6]))
                minx = sorted(listx, key=float)[0]
                miny = sorted(listy, key=float)[0]
                minz = sorted(listz, key=float)[0]
                maxx = sorted(listx, key=float)[-1]
                maxy = sorted(listy, key=float)[-1]
                maxz = sorted(listz, key=float)[-1]
                minl = [minx, miny, minz]
                maxl = [maxx, maxy, maxz]
                with open ('{}_outca.pdb'.format(pdbf), 'a') as oca:
                    print("#    min     max")#, file=oca)
                    for i in range(len(minl)):
                        print("#",minl[i], maxl[i])#, file=oca)
##
# Plot graphs using matplotlib!
##
import matplotlib.pyplot as plt
plt.scatter(minl, maxl, marker='*', color='red')
plt.xlabel("min")
plt.ylabel("max")
plt.title("Graph of min against max coordinates")
plt.show()
#
#
##
# 3D plot of xyz CA coords using matplotlib!
##
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
fige = fig.add_subplot(111, projection='3d')
fige.scatter(listx, listy, listz, c='g', s=50 ,marker='o')
fige.set_xlabel("X coordinates")
fige.set_ylabel("Y coordinates")
fige.set_zlabel("Z coordinates")
plt.show()
#
#
# -------------- HELICAL AXIS
# helix 1 : Ser14 - Ala25
h1_x = listx[14:26]
h1_y = listy[14:26]
h1_z = listz[14:26]
h1_len = list(range(14,26,1))
#[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(h1_x, h1_y, h1_z, c='g', s=50 ,marker='o')
for i,x,y,z in zip(h1_len, h1_x, h1_y, h1_z):
    label = i
    ax.text(x, y, z, label, color="blue")

ax.set_xlabel("X coordinates")
ax.set_ylabel("Y coordinates")
ax.set_zlabel("Z coordinates")
plt.show()

##
## Test of finding axis on 2D
##
#       Below is pevious code to be run to get listx/y/z etc
#
#########################################################
pdbf = '1bta' #from previous code
listx = []
listy = []
listz = []
with open('{}_outca.pdb'.format(pdbf), 'r') as ocam:
    for line in ocam:
        champs = line.split()
        if champs[0] == "ATOM" and champs[2]=="CA":
            listx.append(float(champs[4]))
            listy.append(float(champs[5]))
            listz.append(float(champs[6]))
    minx = sorted(listx, key=float)[0]
    miny = sorted(listy, key=float)[0]
    minz = sorted(listz, key=float)[0]
    maxx = sorted(listx, key=float)[-1]
    maxy = sorted(listy, key=float)[-1]
    maxz = sorted(listz, key=float)[-1]
    minl = [minx, miny, minz]
    maxl = [maxx, maxy, maxz]
    with open ('{}_outca.pdb'.format(pdbf), 'a') as oca:
        print("#    min     max")#, file=oca)
        for i in range(len(minl)):
            print("#",minl[i], maxl[i])#, file=oca)
#########################################################
#
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
h1_x = listx[14:26] #!!!!!! index as from 13 !
h1_y = listy[14:26] #!!!!!! index as from 13 !
h1_z = listz[14:26] #!!!!!! index as from 13 !
#h1_z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
h1_len = list(range(14,26,1))
#[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
##
h1_x = [] ; h1_y = [] ; h1_z = []
h1_lab = []
pdbf = '1bta' #from previous code
with open('{}_outca.pdb'.format(pdbf), 'r') as ocam:
    for line in ocam:
        champs = line.split()
        if champs[0] == "ATOM" and champs[2]=="CA":
            h1_x.append(float(champs[4])) 
            h1_y.append(float(champs[5])) 
            h1_z.append(float(champs[6])) 
            h1_lab.append(champs[3])

#            if champs[1] == "14" :       
#                h1_z = [float(champs[6]) for i in range(12)]
h1_x = h1_x[13:25]
h1_y = h1_y[13:25]
h1_z = h1_z[13:25]
h1_len = list(range(14,26,1))
h1_lab = h1_lab[13:25]
# SPECIFIC EXAMPLE WITH  Ser14-Glu23
#s14 = [h1_x[0], h1_y[0], h1_z[0]]
#e23 = [h1_x[9], h1_y[9], h1_z[9]]
#e_s = [(s14[0] - e23[0]), (s14[1] - e23[1]), (s14[2] - e23[2]) ]
#when x = 0
#0 = e23[0] + t*(e_s[0])
#0 = e23[0] + t*(e_s[0])
#0 = e23[0] + t*(e_s[0])
#tse = e23[0] / (e_s[0])
#yse = e23[1] + tse * e_s[1]
#zse = e23[-1] + tse * e_s[-1]
#print("vse = {} + {}*{}".format(e23, tse, e_s))
#Vse = [0.000 ,float("{:.3f}".format(yse)), float("{:.3f}".format(zse))]
#
# SPECIFIC EXAMPLE WITH Leu16-Ala25
#l16 = [h1_x[2], h1_y[2], h1_z[2]]
#a25 = [h1_x[-1], h1_y[-1], h1_z[-1]]
#a_l = [(l16[0] - a25[0]), (l16[1] - a25[1]), (l16[2] - a25[2]) ]
#when x = 0
#0 = e23[0] + t*(e_s[0])
#0 = e23[0] + t*(e_s[0])
#0 = e23[0] + t*(e_s[0])
#tal = -a25[0] / (a_l[0])
#yal = a25[1] + tal * a_l[1]
#zal = a25[-1] + tal * a_l[-1]
#print("val = {} + {}*{}".format(a25, tal, a_l))
#Val = [0.000 ,float("{:.3f}".format(yal)), float("{:.3f}".format(zal))]
#
#
# GENEREAL EXAMPLE :  Finding lines in 3d from Ser14-Glu23 and Leu16-Ala25 
# vectorr(t) = A + t (B-A)
# aa1-aa2
loVaa = [] #list of Vaa
Vaax = []; Vaay = []; Vaaz = []
for i in range(len(h1_len)+1):
    aa1 = [h1_x[i], h1_y[i], h1_z[i]]
    aa2 = [h1_x[i+1], h1_y[i+1], h1_z[i+1]]
    aa1_2 = [(aa1[0] - aa2[0]), (aa1[1] - aa2[1]), (aa1[2] - aa2[2]) ]
    taa = -aa2[0] / (aa1_2[0])
    yaa = aa2[1] + taa * aa1_2[1]
    zaa = aa2[-1] + taa * aa1_2[-1]
    print("vaa = {} + {:.3f}*{}".format(aa2, -1/taa, aa1_2))
    Vaa = [0.000 ,float("{:.3f}".format(yaa)), float("{:.3f}".format(zaa))]
    Vaax.append(Vaa[0])
    Vaay.append(Vaa[1])
    Vaaz.append(Vaa[-1])
#
# Plot the 2 lines Val and Vse in 3D
#
V_x = [Vse[0], Val[1]]
V_y = [Vse[1], Val[1]]
V_z = [Vse[-1], Val[-1]]
#
#
psdx = [h1_x[0], h1_x[8]]
psdy = [h1_y[0], h1_y[8]]
psdz = [h1_z[0], h1_z[8]]
psdxx = [h1_x[2],  h1_x[10]]
psdyy = [h1_y[2],  h1_y[10]]
psdzz = [h1_z[2],  h1_z[10]]
crosx = [h1_x[0], h1_x[10]]
crosy = [h1_y[0], h1_y[10]]
crosz = [h1_z[0], h1_z[10]]
crosxx = [h1_x[2], h1_x[8]]
crosyy = [h1_y[2], h1_y[8]]
croszz = [h1_z[2], h1_z[8]]
##
###
#
#       BELOW : Code to get helix axis ; to be tested on other helices! ;)
#
#
#
centroid = [sum(h1_x)/len(h1_x), sum(h1_y)/len(h1_y), sum(h1_z)/len(h1_z)]
#centroid_half = [sum(h1_x[:7)/len(h1_x[:7]), sum(h1_y[:7])/len(h1_y[:7]), sum(h1_z[:7])/len(h1_z[:7])]
centroid_half = [sum(h1_x[:7])/len(h1_x[:7]), sum(h1_y[:7])/len(h1_y[:7]), sum(h1_z[:7])/len(h1_z[:7])]
centroid_half2 = [sum(h1_x[-6:])/len(h1_x[-6:]), sum(h1_y[-6:])/len(h1_y[-6:]), sum(h1_z[-6:])/len(h1_z[-6:])]
centroid_quart = [sum(h1_x[:4])/len(h1_x[:4]) , sum(h1_y[:4])/len(h1_y[:4]), sum(h1_z[:4])/len(h1_z[:4])]


ctrdx = [centroid[0], centroid_half[0], centroid_half2[0]]#-centroid_half[0] ]
ctrdy = [centroid[1], centroid_half[1], centroid_half2[1]]#, -centroid_half[1] ]
ctrdz = [centroid[2], centroid_half[2], centroid_half2[2]]#, -centroid_half[2] ]

A = [ctrdx[0], ctrdy[0], ctrdz[0]]
B = [ctrdx[1], ctrdy[1], ctrdz[1]]
C = [ctrdx[2], ctrdy[2], ctrdz[2]]

AB = [B[0]-A[0], B[1]-A[1], B[2]-A[2]]

axex = [centroid_half[0], centroid_half2[0]]#-centroid_half[0] ]
axey = [centroid_half[1], centroid_half2[1]]#, -centroid_half[1] ]
axez = [centroid_half[2], centroid_half2[2]]#, -centroid_half[2] ]
#

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(h1_x, h1_y ,h1_z, color = "red")
ax.scatter(h1_x, h1_y, h1_z, linestyle='-',c='g', s=600 ,marker='o')
for i,x,y,z in zip(h1_lab, h1_x, h1_y, h1_z):
    label = str(i)
    ax.text(x, y, z ,label, color="blue")

ax.set_xlabel("X coordinates")
ax.set_ylabel("Y coordinates")
ax.set_zlabel("Z coordinates")
ax.scatter(A[0], A[1], A[2], c='b', linestyle='-', s=600 ,marker='o')
#ax.scatter(AB[0], AB[1],AB[2], c='b', linestyle='-', s=600 ,marker='*')
ax.scatter(B[0], B[1], B[2], c='r', linestyle='-', s=600 ,marker='o')
ax.scatter(C[0], C[1], C[2], c='y', linestyle='-', s=600 ,marker='o')
#ax.scatter(centroid_half2[0], centroid_half2[1], centroid_half2[2], c='r', linestyle='-', s=600 ,marker='o')
#ax.plot(C[0], C[1], C[2], color = "black", linewidth=5.0)
ax.plot(axex, axey, axez, color = "black", linestyle=':',  linewidth=3.0)
#ax.scatter(AB[0], AB[1], AB[2], c='r', linestyle='-', s=600 ,marker='o')
plt.title("3D plotting of 1bta helix 1", loc="center")
plt.show()

#xse = np.linspace(-8, 8, 10)
#yse = -1.035*xse + -3.276
#plt.plot(xse, yse, 'om')
#xah = np.linspace(-8, 8, 10)
#yah = 0.068*xah + -2.974
#ax.plot(Vaaxx, Vaayy ,Vaazz, color = "magenta")
#ax.scatter(Vaax, Vaay, Vaaz, linestyle='--',c='b', s=50 ,marker='o')
#ax.scatter(his_bis[0], his_bis[1], his_bis[2], linestyle='-',c='b', s=600 ,marker='o')
#ax.plot(psdx, psdy, psdz, color = "magenta", linewidth=5.0)
#ax.plot(psdxx, psdyy, psdzz, color = "magenta", linewidth=5.0)
#ax.plot(crosx, crosy, crosz, color = "blue", linewidth=5.0)
#ax.plot(crosxx, crosyy, croszz, color = "blue", linewidth=5.0)
#
# calc distance between coords AND AFFICHER EN MATRICE!!!!!!!!!!!!!
#dist_sqr = (xj-xi)² + (yj-yi)² + (zj-zi)²
#pow(dist_sqr, 0.5)
###
##  dist_mat = [ [.........],
#                [.........],
#                [.........],
#                [.........] ] (12 x 12)
##
dist_sqr = 0
dist_mat = []
for i in range(len(h1_x)):
    imat = []
    for j in range(len(h1_x)):
        dist_sqr = (pow((h1_x[i] - h1_x[j]), 2) +
                    pow((h1_y[i] - h1_y[j]), 2) +
                    pow((h1_z[i] - h1_z[j]), 2) )
        dist = pow(dist_sqr ,0.5)
        imat.append(dist)
    dist_mat.append(imat)
   
##
#
## distance between extremities res (Ser14 - Ala25)
ser14 = [h1_x[0], h1_y[0], h1_z[0]]
ala25 = [h1_x[-1], h1_y[-1], h1_z[-1]]
d2 = pow((ser14[0] - ala25[0]), 2) + pow((ser14[1] - ala25[1]), 2) + pow((ser14[-1] - ala25[-1]), 2)
d = pow(d2, 0.5)
print("The height of helix 1 is : {:.3f}".format(d))
#
#
# angle between his17 and thr19
h17 = [h1_x[3], h1_y[3], h1_z[3]]
t19 = [h1_x[5], h1_y[5], h1_z[5]]
m_ht = (t19[1] - h17[1]) / (t19[0] - h17[0])
# c = y - mx
c_ht = t19[1] - (m_ht * t19[1])
print("y = {}x + {}".format(m_ht,c_ht))
