#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:09:07 2020

@author: lijunyi
"""


# Union of sets
def union_of_set(A, B):
    for item in B:
        if item not in A:
            A.append(item)
    return A


# A-B or A/B
def minusOfSets(A, B):
    A_B = []
    for item in A:
        if item not in B:
            A_B.append(item)
    return A_B


# Common elements of sets
def common(A, B):
    AB = []
    for x in A:
        if x in B:
            AB.append(x)
    return AB


# All the subsets of a set
def subsets_recursive(nums):
    lst = []
    result = []
    subsets_recursive_helper(result, lst, nums, 0);
    return result;


def subsets_recursive_helper(result, lst, nums, pos):
    result.append(lst[:])
    for i in range(pos, len(nums)):
        lst.append(nums[i])
        subsets_recursive_helper(result, lst, nums, i + 1)
        lst.pop()


# Transfer the list to set
def transferToSets(A):
    C = []
    for i in A:
        if i not in C:
            C.append(i)
    return C


# Justifying whether the two lists are equal or not
def equalOfLists(A, B):
    if len(A) == len(B):
        for a in A:
            if a not in B:
                return False
        return True
    else:
        return False


 
def addornot(A, News):
    for a in A:
        if equalOfLists(a, News) == True:
            return False
    return True


def changeorder(A, News):
    for a in A:
        if equalOfLists(a, News) == True:
            News = a
    return News



class Automata():

    def __init__(self, X, E, theta, x0):
        self.X = X
        self.E = E
        self.theta = theta
        self.x0 = x0

    def f(self, x, e):
        new_state = []
        for item in self.theta:
            if x == item[0] and e == item[1]:
                new_state.append(item[2])
        return new_state

    def f_sets(self, S, e):
        results = []
        for s in S:
            one = self.f(s, e)
            for o in one:
                results.append(o)
        return transferToSets(results)

    def hasOutput(self, S):
        for s in S:
            for e in self.E:
                if self.f(s, e) != []:
                    return True
        return False

    def findRoad(self, x):
        roads = []
        for item in self.theta:
            if x == item[0]:
                roads.append(item[1])
        return roads

    def isDefined(self, x, e):
        for item in self.theta:
            if x == item[0] and e == item[1]:
                return True
        return False

    def eClose(self, x):
        ECLOSE = []
        ECLOSE.append(x)
        for p in ECLOSE:
            if self.f(p, "u") != []:
                for r in self.f(p, "u"):
                    ECLOSE.append(r)
        return ECLOSE

    def sets_eclose(self, S):
        ECLOSE = []
        for x in S:
            mid = self.eClose(x)
            for m in mid:
                ECLOSE.append(m)
        return transferToSets(ECLOSE)

    def Reach(self, x, E):
        result = []
        result.append(x)
        for r in result:
            for e in E:
                if self.f(r, e) != []:
                    for z in self.f(r, e):
                        
                        result.append(z)
        return transferToSets(result)

    def Dilation(self, s, Ecv):
        if s == '':
            return ['']
        else:
            if s in minusOfSets(self.E, Ecv):
                return [s]
            if s in Ecv:
                return [s, s.upper()]

    def Compression(self, s, Ecv):
        Ecva = []
        for i in Ecv:
            Ecva.append(i.upper())
        if s == '':
            return ''
        else:
            if s in self.E:
                return s
            if s in Ecva:
                return s.lower()



G1 = Automata(['0-0','0-3','0-4','0-5',
               '1-0','1-3','1-4','1-5',
               '2-0','2-3','2-4','2-5',
               '3-0','3-3','3-4','3-5'],
              ['a1','a2','a3','a4','b1','b2','b3','b4'],
              [['0-0','b1','0-3'],
               ['0-3','b2','0-4'],
               ['0-4','b3','0-5'],
               ['0-3','b4','0-5'],
               # part
               ['0-0','a1','1-0'],
               ['0-3','a1','1-3'],
               ['0-4','a1','1-4'],
               ['0-5','a1','1-5'],
               # part
               ['1-0','b1','1-3'],
               ['1-3','b2','1-4'],
               ['1-4','b3','1-5'],
               ['1-3','b4','1-5'],
               # part
               ['1-0','a2','2-0'],
               ['1-3','a2','2-3'],
               ['1-4','a2','2-4'],
               ['1-5','a2','2-5'],
               # part
               ['2-0','b1','2-3'],
               ['2-3','b2','2-4'],
               ['2-4','b3','2-5'],
               ['2-3','b4','2-5'],
               # part
               ['2-0','a3','3-0'],
               ['2-3','a3','3-3'],
               ['2-4','a3','3-4'],
               ['2-5','a3','3-5'],
               # part
               ['3-0','b1','3-3'],
               ['3-3','b2','3-4'],
               ['3-4','b3','3-5'],
               ['3-3','b4','3-5'],
               # part
               ['1-0','a4','3-0'],
               ['1-3','a4','3-3'],
               ['1-4','a4','3-4'],
               ['1-5','a4','3-5']],
               '0-0')


H1 = Automata(['1','2','3','4','5','6','7','8','9','10',
               '11','12','13','14'],
              ['a1','a2','a3','a4','b1','b2','b3','b4'],
              [['1','b1','2'],
               ['2','b2','5'],
               ['5','b3','6'],
               ['2','b4','6'],
               ['1','a1','3'],
               ['2','a1','4'],
               ['5','a1','9'],
               ['6','a1','10'],
               ['3','b1','4'],
               ['4','b2','9'],
               ['9','b3','10'],
               ['4','b4','10'],
               ['3','a2','7'],
               ['9','a2','11'],
               ['10','a2','13'],
               ['7','a3','8'],
               ['11','a3','12'],
               ['13','a3','14'],
               ['3','a4','8'],
               ['9','a4','12'],
               ['10','a4','14'],
               ['11','b3','13'],
               ['12','b3','14']              
               ],'1')




def OR(H, G):
    
    Xnew = []
    Em = []
    theta_m = []
    Xnew.append(H.x0 + '-' + G.x0)
    length = len(G.x0)
    index = 0 - length
    index_new = index - 1
    for x in Xnew:
        if len(common(H.findRoad(x[:index_new]), G.findRoad(x[index:]))) > 0:
            for i in common(H.findRoad(x[:index_new]), G.findRoad(x[index:])):
                Em.append(i)
                h_next = H.f(x[:index_new], i)
                g_next = G.f(x[index:], i)
                add_h = []
                add_g = []
                
                TOTAL_H = union_of_set(h_next, add_h)
                TOTAL_G = union_of_set(g_next, add_g)
                
                for k in TOTAL_H:
                    for j in TOTAL_G:
                        Xnew.append(k + '-' + j)
                        theta_m.append([x[:index_new] + '-' + x[index:], i, k + '-' + j])
    GM = Automata(transferToSets(Xnew), transferToSets(Em), transferToSets(theta_m), Xnew[0])
    return GM


# Algorithm1 Build GM
def AE_attack(G, H, Eo, Ec, Ecv):
    # construct Ga
    Ecva = []
    for i in Ecv:
        Ecva.append(i.upper())
    Ea = union_of_set(G.E, Ecva)
    for item in G.theta:
        if item[1] in Ecv:
            G.theta.append([item[0], item[1].upper(), item[2]])
    Ga = Automata(G.X, Ea, G.theta, G.x0)

    # construct Ha   
    for json in H.X:
        for k in Ecva:
            if H.isDefined(json, H.Compression(k, Ecv)) == False:
                H.theta.append([json, k, json])

    for json in H.X:
        for l in minusOfSets(H.E, Ec):
            if H.isDefined(json, l) == False:
                H.theta.append([json, l, json])
    Ha = Automata(H.X, Ea, H.theta, H.x0)
    
    # compute GM
    GM = OR(Ha, Ga)
    return GM


# Algorithm 1 - building attack model
GMM = AE_attack(G1, H1, ['a1','a2','a3','a4','b1','b2','b3','b4'], ['a1','a2','a4','b1','b2','b4'], ['a1','b1'])


print("Set state: ")
print(GMM.X)
print("Events: ")
print(GMM.E)
print("Transition function: ")
for i in GMM.theta:
    print(i)
print("Start state: ")
print(GMM.x0)

# Transfer NFA to DFA without 'u'
def Transfer_NFA_to_DFA(G):
    if G.isNFAorNot == False:
        return G
    else:
        X_new = []
        theta_new = []
        Sets = subsets_recursive(G.X)
        for s in Sets:
            for e in G.E:
                if G.f_sets(s, e) != []:
                    X_new.append(G.f_sets(s, e))

        X_new = transferToSets(X_new)
        for i in X_new:
            if G.hasOutput(i) == False:
                X_new.remove(i)
        for item in X_new:
            for e in G.E:
                if G.f_sets(item, e) != []:
                    theta_new.append([item, e, G.f_sets(item, e)])
        x0_new = [G.x0]
        G_DFA = Automata(X_new, G.E, theta_new, x0_new)
        return G_DFA


def translation(G, Ea_uo):
    for f in G.theta:
        if f[1] in Ea_uo:
            f[1] = "u"
    EE = []
    for f in G.theta:
        EE.append(f[1])
    GE = transferToSets(EE)
    G_new = Automata(G.X, GE, G.theta, G.x0)
    return G_new


# Construct the observer DFA
def Observer(Gl, Ea_uo):
    Gl = translation(Gl, Ea_uo)
    x0_obs = Gl.eClose(Gl.x0)
    E_obs = Gl.E
    if 'u' in E_obs:
        E_obs.remove('u')
    X_obs = []
    X_obs.append(x0_obs)
    theta_obs = []
    for x in X_obs:
        for e in E_obs:
            mid_set = Gl.f_sets(x, e)
            empty_R = Gl.sets_eclose(mid_set)
            if empty_R not in X_obs and empty_R != [] and addornot(X_obs, empty_R) == True:
                X_obs.append(empty_R)
    # build transition function
    for x in X_obs:
        for e in E_obs:
            mid_set = Gl.f_sets(x, e)
            empty_R = Gl.sets_eclose(mid_set)
            if empty_R != [] and changeorder(X_obs, empty_R) in X_obs:
                theta_obs.append([x, e, changeorder(X_obs, empty_R)])
    Gd = Automata(X_obs, E_obs, theta_obs, x0_obs)
    return Gd




# Algorithm 2 Test the Controllability
def AE_test_controllability(GM, Xf, Ecva, Eo, Ecv, Euc):
    # construct Gl
    Xl = ['N', 'Y']
    thetal = []
    El = G1.E
    for item in El:
        if item not in Ecva:
            thetal.append(['N', item, 'N'])
            thetal.append(['Y', item, 'Y'])
        if item in Ecva:
            thetal.append(['N', item, 'Y'])
            thetal.append(['Y', item, 'Y'])
    Al = Automata(Xl, El, transferToSets(thetal), 'N')
    Gl = OR(GM, Al)
    # compute diagnoser Gd
    ED = []
    ET = common(Ecv, minusOfSets(GM.E, Eo))
    
    for et in ET:
        for i in GM.Dilation(et, Ecv):
            ED.append(i)
    Ea_uo = union_of_set(minusOfSets(GM.E, Eo), ED)
    # Construct the dignoser
    Gd = Observer(Gl, Ea_uo)
    # print(Gd.theta)
    # 3 kinds of the states
    QYN = []  # uncertain
    QN = []  # normal
    QY = []  # certain to be attacked
    for states in Gd.X:
        n = 0
        y = 0
        for i in states:
            if i[-1] == 'N':
                n += 1
            if i[-1] == 'Y':
                y += 1
        if n == len(states):
            QN.append(states)
        if y == len(states):
            QY.append(states)
    QYN = minusOfSets(minusOfSets(Gd.X, QY), QN)
    # build the set of XfM
    XfM = []
    length = len(G1.x0)
    index = 0 - length
    for x in GM.X:
        if x[index:] in Xf:
            XfM.append(x)
    # first condition to justify - QYN
    for qyn in QYN:
        for q in qyn:
            if q[:-2] in XfM:
                return False
                # compute the FC
    FC = []
    Big = union_of_set(QYN, QN)
    for q in Big:
        for e in Eo:
            for x in Gd.f(q, e):
                if x in QY:
                    FC.append(x)
                    # second condition to justify - FC
    for q in FC:
        for t in q:
            if t[:-2] in XfM:
                return False
                # compute Xuc
    E_reach = union_of_set(Ecva, Euc)
    Xuc = []
    for q in FC:
        for x in q:
            R = GM.Reach(x[:-2], E_reach)
            for r in R:
                Xuc.append(r)
    Xuc = transferToSets(Xuc)
    if common(Xuc, XfM) != []:
        return False
    else:
        return True


# Algorithm 2 - testing AE-safe controllability
RESULT = AE_test_controllability(GMM, ['3-3'], 
                                      ['A1','B1'], 
                                      ['a1','a2','a3','a4','b1','b2','b3','b4'], 
                                      ['a1','b1'], 
                                      ['a3','b3'])

print(RESULT)
