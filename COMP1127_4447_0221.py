#!/bin/python3

import math
import os
import random
import re
import sys

#
# Please Paste all Fuctions from Part 1,2,3,4,5,6 & 7
# Complete the function below.
#

"""
Group Information:
Member 1: 620150221
Member 2: 620154447
"""

######Problem 1######
def makePacket(srcIP, dstIP, length, prt, sp, dp, sqn, pld):
    # Write your code here
    return ("PK",srcIP, dstIP, [length, prt, [sp, dp], sqn, pld])
def getPacketSrc(pkt):
    # Write your code here
    return pkt[1]
def getPacketDst(pkt):
    # Write your code here
    return pkt[2]
def getPacketDetails(pkt):
    # Write your code here
    return pkt[3]
def isPacket(pkt):
    # Write your code here
    return type(pkt)==tuple and pkt[0]=='PK' and pkt[1]==srcIP
def isEmptyPkt(pkt):
    # Write your code here
    return pkt[3]==[]

#####problem2#######

def getLength(pkt):
    # Write your code here
    return getPacketDetails(pkt)[0]
def getProtocol(pkt):
    # Write your code here
    return getPacketDetails(pkt)[1]
def getSrcPort(pkt):
    # Write your code here
    return getPacketDetails(pkt)[2][0]
def getDstPort(pkt):
    # Write your code here
    return getPacketDetails(pkt)[2][1]
def getSqn(pkt):
    # Write your code here
    return getPacketDetails(pkt)[3]
def getPayloadSize(pkt):
    # Write your code here
    return getPacketDetails(pkt)[4]


#####Problem 3#######


def flowAverage(pkt_list):
    # Write your code here
    hold=0
    lsthold=[]
    jholder=[]
    for x in pkt_list:
        lsthold.append(getPayloadSize(x))
        hold+=getPayloadSize(x)
    average=hold/len(lsthold)
    for j in pkt_list:
        if getPayloadSize(j) > average:
            jholder.append(j)
    return jholder
def suspPort(pkt):
    # Write your code here
    return getSrcPort(pkt)>500 or getDstPort(pkt)>500
def suspProto(pkt):
    # Write your code here
    if not getProtocol(pkt) in ProtocolList:
        return True
    else:
        return False
def ipBlacklist(pkt):
    # Write your code here
    return pkt[1] in IpBlackList

#####Problem 4######

def calScore(pkt):
  # Write your code here
    totalscore=0
    if pkt in flowAverage(pkt_list):
        totalscore+=3.56
    if suspPort(pkt) == True:
        totalscore+=1.45
    if suspProto(pkt)== True:
        totalscore+=2.74
    if ipBlacklist(pkt)==True:
        totalscore+=10.00
    return totalscore
def makeScore(pkt_list):
  # Write your code here
    scorlst=[]
    for x in pkt_list:
        scorlst+=(x,calScore(x))
    return['SCORE',scorlst]
def addPacket(ScoreList, pkt):
  # Write your code here
    A=calScore(pkt)
    ScoreList[1].append(pkt)
def getSuspPkts(ScoreList):
  # Write your code here
    pktholder=[]
    for q in ScoreList[1]:
        if type(q)==tuple:
            if calScore(q)>5.00:
                pktholder.append(q)
    return pktholder
def getRegulPkts(ScoreList):
  # Write your code here
    pktholder2=[]
    for q in ScoreList[1]:
        if type(q)==tuple:
            if calScore(q)<=5.00:
                pktholder2.append(q)
    return pktholder2
def isScore(ScoreList):
  # Write your code here
  return ScoreList[0]=='SCORE' and type(ScoreList[1])==list and type(ScoreList)==list
def isEmptyScore(ScoreList):
  # Write your code here
    return ScoreList[1]==[]

####Problem 5####
def makePacketQueue():
  # Write your code here
    return("PQ",[])
def contentsQ(q):
  # Write your code here
    return q[1]
def frontPacketQ(q):
  # Write your code here
    if isPacketQ(q):
        return contentsQ(q)[0]
def addToPacketQ(pkt,q):
    contentsQ(q).insert((get_pos(pkt,contentsQ(q))),pkt)
                        
def get_pos(pkt,lst):
    if (lst == []):
        return 0
    elif getSqn(pkt) < getSqn(lst[0]):
        return 0 + get_pos(pkt,[])
    else:
        return 1 + get_pos(pkt,lst[1:])
            
def removeFromPacketQ(q):
  # Write your code here
    if not isEmptPacketQ(q):
        contentsQ(q).pop(0)
def isPacketQ(q):
  # Write your code here
    return q[0]=='PQ' and type(q[1])==list and type(q)==tuple and len(q)==2
def isEmptPacketQ(q):
  # Write your code here
    return q[1]==[] and len(q)==2

####Problem 6######
def makePacketStack():
  # Write your code here
    return("PS",[])
def contentsStack(stk):
  # Write your code here
    return stk[1]
def topProjectStack (stk):
  # Write your code here
    return contentsStack(stk)[-1]
def pushProjectStack(pkt,stk):
  # Write your code here
    contentsStack(stk).append(pkt)
def popPickupStack(stk):
  # Write your code here
    contentsStack(stk).pop(-1)
def isPKstack(stk):
  # Write your code here
    return stk[0]=="PS" and type(stk)==tuple and type(stk[1])==list and len(stk)==2
def isEmptyPKStack(stk):
  # Write your code here
    return stk[1]==[] and len(stk)==2

###Problem 7####
def sortPackets(scoreList,stack,queue):
  # Write your code here
    for x in getSuspPkts(scoreList):
        pushProjectStack(x,stack)
    for j in getRegulPkts(scoreList):
        addToPacketQ(j,queue)

        
def analysePackets(packet_List):
  # Write your code here
    holder=[]
    scorlst=[]
    for x in packet_List:
        A=makePacket(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
        holder.append(A)
    for q in holder:
        scoreholder=0
        if q in flowAverage(holder):
            scoreholder+=3.56
        if suspPort(q) == True:
            scoreholder+=1.45
        if suspProto(q)== True:
            scoreholder+=2.74
        if ipBlacklist(q)==True:
            scoreholder+=10.00
        scorlst+= [(q,scoreholder)]
    scorlst2=['SCORE',scorlst]
    stkk=makePacketStack()
    que=makePacketQueue()
    for r in scorlst2[1]:
        if r[1] > 5.00:
            pushProjectStack(r[0],stkk)
    for h in scorlst2[1]:
        if h[1] <= 5.00:
            addToPacketQ(h[0],que)
    return que
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    
    srcIP = str(first_multiple_input[0])
    dstIP = str(first_multiple_input[1])
    length = int(first_multiple_input[2])
    prt = str(first_multiple_input[3])
    sp = int(first_multiple_input[4])
    dp = int(first_multiple_input[5])
    sqn = int(first_multiple_input[6])
    pld = int(first_multiple_input[7])
    
    ProtocolList = ["HTTPS","SMTP","UDP","TCP","DHCP","IRC"]
    IpBlackList = ["213.217.236.184","149.88.83.47","223.70.250.146","169.51.6.136","229.223.169.245"]

    packet_List = [(srcIP, dstIP, length, prt, sp, dp, sqn, pld),\
                   ("111.202.230.44","62.82.29.190",31,"HTTP",80,20,1562436,338),\
                   ("222.57.155.164","50.168.160.19",22,"UDP",790,5431,1662435,812),\
                   ("333.230.18.207","213.217.236.184",56,"IMCP",501,5643,1762434,3138),\
                   ("444.221.232.94","50.168.160.19",1003,"TCP",4657,4875,1962433,428),\
                   ("555.221.232.94","50.168.160.19",236,"HTTP",7753,5724,2062432,48)]
              
                   
                  
    
    fptr.write('Forward Packets => ' + str(analysePackets(packet_List)) + '\n')
    
    fptr.close()
