from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

###REQUESTNAME
##requestName## E.g., config.General.requestName = 'MajoranaNeutrinoToMuMuMu_M-40_CMSSW_8_0_21_RAWSIM'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC'
###PSETNAME
##psetName## E.g., config.JobType.psetName = 'SIM_to_RAWSIM.py'
config.JobType.numCores = 2
config.JobType.maxMemoryMB = 4000

###OUTPUTNAME
#config.Data.outputPrimaryDataset = 'ZprimetoNN_MuMuJJJJ_Zprime2800_N1350_WR5000_NLO'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventBased'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CMSSW_9_4_12__AODSIM'
config.Data.ignoreLocality = True
config.Data.unitsPerJob = 2500
NJOBS = 28
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Site.storageSite = 'T2_KR_KNU'
config.Site.whitelist = ['T2_*', 'T3_*']
#config.Site.whitelist = ['T2_CH_CSCS','T2_PL_Warsaw','T2_US_Vanderbilt','T2_KR_KISTI','T2_US_Nebraska','T2_US_MIT','T2_US_Wisconsin','T2_UA_KIPT','T2_TW_NCHC','T2_BR_SPRACE','T2_UK_SGrid_Bristol','T2_BE_UCL','T2_UK_London_Brunel','T2_EE_Estonia','T2_RU_JINR','T2_US_Florida','T2_IT_Bari','T2_AT_Vienna','T2_UK_SGrid_RALPP','T2_FR_GRIF_LLR','T2_FR_GRIF_IRFU','T2_DE_DESY','T2_IT_Legnaro','T2_IT_Pisa','T2_DE_RWTH','T2_US_Caltech','T3_KR_KNU']
#config.Site.blacklist = ['T2_CH_CERN', 'T2_US_Purdue']
