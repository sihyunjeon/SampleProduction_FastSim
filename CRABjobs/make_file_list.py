import os

WRMASSEND = 7001
INT = 1
WRMASS = 200
while (WRMASS <= WRMASSEND):
  NMASS = 100
  while (NMASS < WRMASS):
    if (NMASS == WRMASS): NMASS = WRMASS - 100
    DIRNAME = "WRtoNLtoLLJJ_WR"+(str)(WRMASS)+"_N"+(str)(NMASS)

    if (NMASS == 100): NMASS = NMASS + 100
    elif (NMASS == WRMASS - 200): NMASS = NMASS + 100
    else: NMASS = NMASS + 200

    print DIRNAME +"\troot://cms-xrdr.sdfarm.kr:1094///xrd/store/user/shjeon/2017Run_WR_Dilep/PrivateLHE/"+DIRNAME+".lhe"
#    print DIRNAME +"\t/pnfs/knu.ac.kr/data/cms/store/user/shjeon/2016Run_WR_Dilep/2016/"+DIRNAME+".root"

  WRMASS = WRMASS + 200

