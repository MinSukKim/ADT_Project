from outrankingDigraphs import *
from linearOrders import *
from perfTabs import *
from sortingDigraphs import *

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

# Different point of view(Eco, Env, Soc, Glo==t_10), for three more tables.
t_10_ECO = PartialPerformanceTableau(t_10, criteriaSubset = t_10.objectives['Eco']['criteria'])
t_10_ENV = PartialPerformanceTableau(t_10, criteriaSubset = t_10.objectives['Env']['criteria'])
t_10_SOC = PartialPerformanceTableau(t_10, criteriaSubset = t_10.objectives['Soc']['criteria'])

t_10.showHTMLPerformanceHeatmap(Correlations=True, colorLevels=9, pageTitle="Global Point of View")
t_10_ECO.showHTMLPerformanceHeatmap(Correlations=True, colorLevels=9, pageTitle="Economic Point of View")
t_10_ENV.showHTMLPerformanceHeatmap(Correlations=True, colorLevels=9, pageTitle="Environment Point of View")
t_10_SOC.showHTMLPerformanceHeatmap(Correlations=True, colorLevels=9, pageTitle="Social Point of View")

# To show ranking #

from linearOrders import *
t_10_rankTmp = BipolarOutrankingDigraph(t_10)
t_10_ECO_rankTmp = BipolarOutrankingDigraph(t_10_ECO)
t_10_ENV_rankTmp = BipolarOutrankingDigraph(t_10_ENV)
t_10_SOC_rankTmp = BipolarOutrankingDigraph(t_10_SOC)

args = [t_10, t_10_ECO, t_10_ENV, t_10_SOC]

# Copeland Ranking
print("Copeland ranking: ")
for i in range(0, len(args)):
	tmp = BipolarOutrankingDigraph(args[i])
	copRanks = CopelandOrder(tmp)
	copRanks.showRanking()

# Net flow Ranking
print("Net flow ranking: ")
for i in range(0, len(args)):
	tmp = BipolarOutrankingDigraph(args[i])
	netRanks = NetFlowsOrder(tmp)
	netRanks.showRanking()

# Kohler Ranking
print("Kohler ranking: ")
for i in range(0, len(args)):
	tmp = BipolarOutrankingDigraph(args[i])
	kohRanks = KohlerOrder(tmp)
	kohRanks.showRanking()

######### 4 ###########

#using historical quantile norms#
perQuan = PerformanceQuantiles('quantileNorms_10', numberOfBins= 'dodeciles')
perQuan.updateQuantiles(t_10,historySize=None)
perQuan.showHTMLLimitingQuantiles()


normQuanRating = NormedQuantilesRatingDigraph(perQuan,t_10)
normQuanRating.showQuantilesRating()
normQuanRating.showHTMLPerformanceTableau(actionsSubset=normQuanRating.newActions)

######### 5 ###########

######### 6 ###########

######### 7 ###########

