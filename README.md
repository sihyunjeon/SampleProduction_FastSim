# 2017__CMSSW_9_4_12__LHE_to_AODSIM
CMSSW setup for 2017__CMSSW_9_4_12__LHE_to_AODSIM
```
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_4_12
cd CMSSW_9_4_12/src/
cmsenv
```

git clone needed script files
```
git clone https://github.com/sihyunjeon/SampleProduction_FastSim.git -b 2017__CMSSW_9_4_12__LHE_to_AODSIM
cd SampleProduction_FastSim/2017__CMSSW_9_4_12__LHE_to_AODSIM__CRABjobs/
```

# CRAB scripts for WR/N analysis
```
python make_file_list_snu.py $USER &>file_list.txt
python make_crab_cfg.py &>submit.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init
source submit.sh
```
