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
t_10_rank = NetFlowsOrder(t_10_rankTmp)
t_10_rank.showRanking()

t_10_ECO_rankTmp = BipolarOutrankingDigraph(t_10_ECO)
t_10_ECO_rank = NetFlowsOrder(t_10_ECO_rankTmp)
t_10_ECO_rank.showRanking()

t_10_ENV_rankTmp = BipolarOutrankingDigraph(t_10_ENV)
t_10_ENV_rank = NetFlowsOrder(t_10_ENV_rankTmp)
t_10_ENV_rank.showRanking()

t_10_SOC_rankTmp = BipolarOutrankingDigraph(t_10_SOC)
t_10_SOC_rank = NetFlowsOrder(t_10_SOC_rankTmp)
t_10_SOC_rank.showRanking()
