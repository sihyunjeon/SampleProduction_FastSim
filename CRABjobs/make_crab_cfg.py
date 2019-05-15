import os

txtfilename = 'file_list.txt'
sample_lines = open(txtfilename).readlines()
step_lines = open("skeletons/LHE_to_AODSIM.py").readlines()
crab_lines = open("skeletons/crab_skeleton.py").readlines()

for sample_line in sample_lines:

  sample_name = sample_line.strip().split('\t')[0]
  sample_pwd = sample_line.strip().split('\t')[1]

  os.system("mkdir "+sample_name)
  step_file = open(sample_name+"/"+sample_name+"_LHE_to_AODSIM.py", "wt")
  for step_line in step_lines:
    if "###INPUTFILE" in step_line:
      step_file.write("    fileNames = cms.untracked.vstring('"+sample_pwd+"'),\n")
    else:
      step_file.write(step_line)
  step_file.close()

  crab_file = open(sample_name+"/crab_"+sample_name+"_LHE_to_AODSIM.py", "wt")
  for crab_line in crab_lines:
    if "###REQUESTNAME" in crab_line:
      crab_file.write("config.General.requestName = '"+sample_name+"__CMSSW_9_4_12__AODSIM'\n")
    elif "###PSETNAME" in crab_line:
      crab_file.write("config.JobType.psetName = '"+sample_name+"_LHE_to_AODSIM.py'\n")
    elif "###OUTPUTNAME" in crab_line:
      crab_file.write("config.Data.outputPrimaryDataset = '"+sample_name+"'\n")
    else:
      crab_file.write(crab_line)
  crab_file.close()

  print "cd "+sample_name
  print "crab submit -c crab_"+sample_name+"_LHE_to_AODSIM.py"
  print "cd - "
