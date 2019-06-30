from outrankingDigraphs import *
from perfTabs import *

######### 1 ###########
t_10 = XMCDA2PerformanceTableau('performanceTableau_10')

t_10.showObjectives()
t_10.showCriteria()
t_10.showActions()
t_10.showHTMLPerformanceTableau()

######### 2 ###########
BOD = BipolarOutrankingDigraph(t_10)
BOD.showHTMLRelationTable()

######### 3 ###########

