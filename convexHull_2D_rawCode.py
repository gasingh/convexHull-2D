import rhinoscriptsyntax as rs
import Rhino
import Rhino.Geometry as rg

def simpleGrahamScanSorting(ptList):
    """
    
    ---------------------------------------------------------
    "The first step of a Graham-Scan sorts the points
     by their polar angle from the bottom-left vertex, p0"
    
    (http://slideplayer.com/slide/3287751/)
    ---------------------------------------------------------
    
    """
    
    #print len(a_ok)
    
    
    # get the least X and least Y value
    # find the bottom-left vertex as p0
    #leastXY_pt = ptList[0]
    leastY_pt_index = 0
    leastY_pt = ptList[leastY_pt_index]
    for i in range(1,len(ptList),1):
        print i, " | ", ptList[i].X , " | ", ptList[i].Y
        #if (ptList[i].X < leastXY_pt.X and ptList[i].Y < leastXY_pt.Y):
        #    leastXY_pt = ptList[i]
        if (ptList[i].Y < leastY_pt.Y):
            leastY_pt = ptList[i]
            leastY_pt_index = i
        else:
            pass
    print "+++++++++++++++++++++++++++++++++"
    print leastY_pt , " | ", leastY_pt_index
    print "+++++++++++++++++++++++++++++++++"
    
    
    
    # compute polar Angles
    # define base vector to compute against
    
    vecX = Rhino.Geometry.Point3d(leastY_pt.X+1,leastY_pt.Y,leastY_pt.Z)- leastY_pt
    print type(vecX)
    
    vecList = []
    angList = []
    vecList.append(vecX)
    print "---------------"
    for i in range(0,len(ptList),1):
        localVec = ptList[i]-leastY_pt
        vecList.append(localVec)
        angList.append(Rhino.RhinoMath.ToDegrees(Rhino.Geometry.Vector3d.VectorAngle(vecX,localVec)))
        print "i: ",i," | angle: ",angList[i], " | vector: ", localVec
    print "---------------"
    
    angListSorted = []
    for i in range(0,len(angList),1):
        angListSorted.append(angList[i])
    angListSorted.sort()
    
    ptListSorted = []
    vecListSorted = []
    for i in range(0,len(angListSorted),1):
        for j in range(0,len(angList),1):
            if (angListSorted[i]==angList[j]):
                print "found: ", j
                ptListSorted.append(ptList[j])
                vecListSorted.append(vecList[j])
            else:
                pass
                
    return [angListSorted,ptListSorted,vecListSorted,leastY_pt]

#----------------------------------------------------------------
def clusterByZ_return_nestedList(ptList):
    
    print "_____________________________"
    # defaultZlist
    zList = []
    #for i,j in enumerate(ptList): zColl.append(j.Z)
    for i in range(0,len(ptList),1):
        zList.append(ptList[i].Z)
        
    print zList
    
    # find Unique Z values
    uniqZList = []
    uniqZList.append(zList[0])
    for i in range(1,len(zList),1):
        foundCount = 0
        for j in range(0,len(uniqZList),1):
            if zList[i] == uniqZList[j]:
                foundCount = foundCount+1
        if foundCount == 0:
            uniqZList.append(zList[i])
    #print uniqZList, " uniqZList"
    print "-----------"
    for i,j in enumerate(uniqZList): print i," : ", j," : ",type(j)
    print "-----------"
    
    # sort the uniqueList tp avaoid further data ambiguities
    uniqZList.sort()
    
    # prepare agglomerations based on found clusters
    ptCluster = []  # this is a nestedList per cluster (here the clustering is as per Z logic)
    for i in range(0,len(uniqZList),1):
        uniqCluster = []
        for j in range(0,len(zList),1):
            if uniqZList[i] == zList[j]:
                uniqCluster.append(ptList[j])
                
        print len(uniqCluster), " uniqCluster"
        ptCluster.append(uniqCluster)
        #for k in range(0,len(uniqCluster),1):
        #    ptCluster.append(uniqCluster[k])
    
    print len(ptCluster), type(ptCluster[0][0])
    print "_____________________________"
    return ptCluster

def clusterByY_return_nestedList(ptList):
    
    print "_____________________________"
    # defaultZlist
    zList = []
    #for i,j in enumerate(ptList): zColl.append(j.Z)
    for i in range(0,len(ptList),1):
        #zList.append(ptList[i].Z)
        zList.append(ptList[i].Y)           # modeified this to work as a Y cluster
        
    print zList
    
    # find Unique Z values
    uniqZList = []
    uniqZList.append(zList[0])
    for i in range(1,len(zList),1):
        foundCount = 0
        for j in range(0,len(uniqZList),1):
            if zList[i] == uniqZList[j]:
                foundCount = foundCount+1
        if foundCount == 0:
            uniqZList.append(zList[i])
    #print uniqZList, " uniqZList"
    print "-----------"
    for i,j in enumerate(uniqZList): print i," : ", j," : ",type(j)
    print "-----------"
    
    # sort the uniqueList tp avaoid further data ambiguities
    uniqZList.sort()
    
    # prepare agglomerations based on found clusters
    ptCluster = []  # this is a nestedList per cluster (here the clustering is as per Z logic)
    for i in range(0,len(uniqZList),1):
        uniqCluster = []
        for j in range(0,len(zList),1):
            if uniqZList[i] == zList[j]:
                uniqCluster.append(ptList[j])
                
        print len(uniqCluster), " uniqCluster"
        ptCluster.append(uniqCluster)
        #for k in range(0,len(uniqCluster),1):
        #    ptCluster.append(uniqCluster[k])
    
    print len(ptCluster), type(ptCluster[0][0])
    print "_____________________________"
    return ptCluster

def clusterByX_return_nestedList(ptList):
    
    print "_____________________________"
    # defaultZlist
    zList = []
    #for i,j in enumerate(ptList): zColl.append(j.Z)
    for i in range(0,len(ptList),1):
        #zList.append(ptList[i].Z)
        zList.append(ptList[i].X)           # modeified this to work as a X cluster
        
    print zList
    
    # find Unique Z values
    uniqZList = []
    uniqZList.append(zList[0])
    for i in range(1,len(zList),1):
        foundCount = 0
        for j in range(0,len(uniqZList),1):
            if zList[i] == uniqZList[j]:
                foundCount = foundCount+1
        if foundCount == 0:
            uniqZList.append(zList[i])
    #print uniqZList, " uniqZList"
    print "-----------"
    for i,j in enumerate(uniqZList): print i," : ", j," : ",type(j)
    print "-----------"
    
    # sort the uniqueList tp avaoid further data ambiguities
    uniqZList.sort()
    
    # prepare agglomerations based on found clusters
    ptCluster = []  # this is a nestedList per cluster (here the clustering is as per Z logic)
    for i in range(0,len(uniqZList),1):
        uniqCluster = []
        for j in range(0,len(zList),1):
            if uniqZList[i] == zList[j]:
                uniqCluster.append(ptList[j])
                
        print len(uniqCluster), " uniqCluster"
        ptCluster.append(uniqCluster)
        #for k in range(0,len(uniqCluster),1):
        #    ptCluster.append(uniqCluster[k])
    
    print len(ptCluster), type(ptCluster[0][0])
    print "_____________________________"
    return ptCluster

def getLeastXYPt(arrPt):
    
    if arrPt:
        #find pt with least X,Y
        
        ptList = rs.coerce3dpointlist(arrPt)
        
        for i,j in enumerate(ptList): print i, type(j)
        
        #print len(a_ok)
        
        """
        #VERSION 1-
        # get the least X and least Y value
        # find the bottom-left vertex as p0
        #leastXY_pt = ptList[0]
        leastY_pt_index = 0
        leastY_pt = ptList[leastY_pt_index]
        for i in range(1,len(ptList),1):
            print i, " | ", ptList[i].X , " | ", ptList[i].Y
            #if (ptList[i].X < leastXY_pt.X and ptList[i].Y < leastXY_pt.Y):
            #    leastXY_pt = ptList[i]
            if (ptList[i].Y < leastY_pt.Y):
                leastY_pt = ptList[i]
                leastY_pt_index = i
            else:
                pass
        print "+++++++++++++++++++++++++++++++++"
        print leastY_pt , " | ", leastY_pt_index
        print "+++++++++++++++++++++++++++++++++"
        """
        
        
        # VERSION 2-
        # AIM: to find the bottom-left vertex as p0
        
        # THIS VERSION favours the Y first & then the X axis,... 
        
        leastY_ptList = []
        leastY_ptIndexList = []
        yList = []
        
        leastYList = clusterByY_return_nestedList(ptList)[0]
        print "=================== Y Clusters"
        for i,j in enumerate(leastYList): print i," | ",j," | ",type(j)
        print "=================== =========="
        
        leastXList = clusterByX_return_nestedList(leastYList)[0]
        print "=================== X Clusters"
        for i,j in enumerate(leastXList): print i," | ",j," | ",type(j)
        print "=================== =========="
        
        leastXY_pt = leastXList[0]
        leastXY_pt_index = None
        
        for i in range(0,len(ptList),1):
            if ptList[i].X == leastXY_pt.X:
                if ptList[i].Y == leastXY_pt.Y:
                    if ptList[i].Z == leastXY_pt.Z:
                        leastXY_pt_index = i
        
        # loop through the main list and fetch the index
        
        print "+++++++++++++++++++++++++++++++++"
        print leastXY_pt , " | ", leastXY_pt_index
        print "+++++++++++++++++++++++++++++++++"
        return [leastXY_pt,leastXY_pt_index]

def simpleGrahamScanSorting_v2(ptList):

    """
    
    This one takes care of edgeCases,..
    so parallel points with the same Y but different X will be segregated so as to 
    find the least pt in the LHS ie. least X,..
    So two levels of filtering now exist.
    # 10:32 21/09/2016
    # 14:30 21/09/2016 - Uses getLeastXYPt
    
    
    ---------------------------------------------------------
    "The first step of a Graham-Scan sorts the points
     by their polar angle from the bottom-left vertex, p0"
    
    (http://slideplayer.com/slide/3287751/)
    ---------------------------------------------------------
    
    """
    
    #print len(a_ok)
    
    """ ABANDONED & REPLACED BELOW
    # get the least X and least Y value
    # find the bottom-left vertex as p0
    #leastXY_pt = ptList[0]
    leastY_pt_index = 0
    leastY_pt = ptList[leastY_pt_index]
    for i in range(1,len(ptList),1):
        print i, " | ", ptList[i].X , " | ", ptList[i].Y
        #if (ptList[i].X < leastXY_pt.X and ptList[i].Y < leastXY_pt.Y):
        #    leastXY_pt = ptList[i]
        if (ptList[i].Y < leastY_pt.Y):
            leastY_pt = ptList[i]
            leastY_pt_index = i
        else:
            pass
    print "+++++++++++++++++++++++++++++++++"
    print leastY_pt , " | ", leastY_pt_index
    print "+++++++++++++++++++++++++++++++++"
    """
    
    arrPt = ptList
    
    data = getLeastXYPt(arrPt)
    leastXYPt = data[0]
    leastXYPt_index = data[1]
    print "+++++++++++++++++++++++++++++++++"
    print leastXYPt , " | ", leastXYPt_index
    print "+++++++++++++++++++++++++++++++++"
    
    
    
    # compute polar Angles
    # define base vector to compute against
    
    vecX = Rhino.Geometry.Point3d(leastXYPt.X+1,leastXYPt.Y,leastXYPt.Z)- leastXYPt
    print type(vecX)
    
    vecList = []
    angList = []
    vecList.append(vecX)
    print "---------------"
    for i in range(0,len(ptList),1):
        localVec = ptList[i]-leastXYPt
        vecList.append(localVec)
        angList.append(Rhino.RhinoMath.ToDegrees(Rhino.Geometry.Vector3d.VectorAngle(vecX,localVec)))
        print "i: ",i," | angle: ",angList[i], " | vector: ", localVec
    print "---------------"
    
    #angList.sort()
    angListSorted = []
    for i in range(0,len(angList),1):
        angListSorted.append(angList[i])
    angListSorted.sort()
    #######print angListSorted
    
    ptListSorted = []
    vecListSorted = []
    for i in range(0,len(angListSorted),1):
        for j in range(0,len(angList),1):
            if (angListSorted[i]==angList[j]):
                print "found: ", j
                ptListSorted.append(ptList[j])
                vecListSorted.append(vecList[j])
            else:
                pass
    
    return [angListSorted,ptListSorted,vecListSorted,leastXYPt]

    
    # 18:10 20/09/2016
    # 14:40 21/09/2016
    
    if inputBox:
        
        if rs.IsBrep(inputBox):
            print "yes brep"
        if rs.IsPolysurface(inputBox):
            print "yes polySrf"
        inputBoxBrp = rs.coercebrep(inputBox)
        print type(inputBoxBrp)
        brp_v = inputBoxBrp.Vertices
        print type(brp_v), " brp_v"
        
        
        brep_v_genericList = []
        
        for i in range(0,brp_v.Count,1):
            print i
            print brp_v.Item           # ERROR: 'Message: indexer# is not callable'
            print brp_v.ElementAt(i)    # ERROR: 'Message: 'BrepVertexList' object has no attribute 'ElementAt'
            print (brp_v.ElementAt(i).GetType().ToString())
            brep_v_genericList.append(brp_v.ElementAt(i))
            
        
        brep_v_List = brp_v.ToList()
        print len(brep_v_List)
        brep_v_Array = brp_v.ToArray()  
        print len(brep_v_Array)
        
        print type(brep_v_List), "brp_v_List"
        print type(brep_v_Array), "brp_v_Array"
        
        
        brep_v_genericList = inputBoxBrp.DuplicateVertices()
        #for i,j in enumerate(brep_v_genericList): rs.AddPoint(j)           # OK
        
        
        nestedPointCluster_nestedList = clusterByZ_return_nestedList(brep_v_genericList)
        print len(nestedPointCluster_nestedList[1])
        for i,j in enumerate(nestedPointCluster_nestedList[1]): print i,type(j)
        
        print ".........."
        lowestPtSet = nestedPointCluster_nestedList[0]
        print len(nestedPointCluster_nestedList[0]),len(lowestPtSet)
        highestPtSet = nestedPointCluster_nestedList[1]
        print len(nestedPointCluster_nestedList[1]),len(highestPtSet)
        print ".........."
        
        """
        # PRINT THE INITIAL HEIGHT BASED unordered point SEQUENCES:
        for i in range(0,len(lowestPtSet),1):
            print i,": ",type(lowestPtSet[i])
            ptLocal = lowestPtSet[i]
            rs.AddPoint(ptLocal)
            rs.AddTextDot("L:"+str(i),ptLocal)
        
        for i in range(0,len(highestPtSet),1):
            print i,": ",type(highestPtSet[i])
            ptLocal = highestPtSet[i]
            rs.AddPoint(ptLocal)
            rs.AddTextDot("H:"+str(i),ptLocal)
        """
        
        ####dataOutLow= simpleGrahamScanSorting(lowestPtSet)
        dataOutLow= simpleGrahamScanSorting_v2(lowestPtSet)
        anglesSortedList_L    = dataOutLow[0]
        pointsSortedList_L    = dataOutLow[1]
        vectorsSortedList_L   = dataOutLow[2]
        print len(dataOutLow), "sorted Low pts"
        
        
        dataOutHigh = simpleGrahamScanSorting_v2(highestPtSet)
        ####dataOutHigh = simpleGrahamScanSorting(highestPtSet)
        anglesSortedList_H    = dataOutHigh[0]
        pointsSortedList_H    = dataOutHigh[1]
        vectorsSortedList_H   = dataOutHigh[2]
        print len(dataOutHigh), "sorted High pts"
    
        """
        # PRINT THE final HEIGHT BASED ORDERED point SEQUENCES:
        for i in range(0,len(pointsSortedList_L),1):
            print i,": ",type(pointsSortedList_L[i])
            ptToLabel = pointsSortedList_L[i]
            rs.AddTextDot("L:"+str(i),ptToLabel)
        
        for kk in range(0,len(pointsSortedList_H),1):
            print kk,": ",type(pointsSortedList_H[kk])
            ptToLabel = pointsSortedList_H[kk]
            rs.AddTextDot("H:"+str(kk),ptToLabel)
        """
            
        if pointsSortedList_H:
            for i,j in enumerate(pointsSortedList_H): print i,j

        finalbbList = []
        finalbbList.extend(pointsSortedList_L)
        finalbbList.extend(pointsSortedList_H)
        
        
        print len(finalbbList), " finalbbList"
        
        ###############for i in range(0,len(finalbbList),1):
        ###############    print finalbbList[i]
        ###############    rs.AddTextDot(i,finalbbList[i])
        
            
        
        ###############pointsSortedList_L.append(pointsSortedList_L[0])
        ###############polyLn_Low = rs.AddPolyline(pointsSortedList_L)
        ###############rs.SelectObject(polyLn_Low)
        return finalbbList

#_,a,_,_ = simpleGrahamScanSorting(x)
#print(a)

_,a,_,_ = simpleGrahamScanSorting_v2(x)