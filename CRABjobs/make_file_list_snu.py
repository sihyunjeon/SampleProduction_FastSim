import os,sys

WRMASSEND = 7001
WRMASS = 200

USER = sys.argv[1]
WRSTART = 0
WREND = 0
if USER == "jihkim":
  WRSTART = 100
  WREND = 2900
elif USER == "helee": 
  WRSTART = 2900
  WREND = 4100
elif USER == "jalmond": 
  WRSTART = 4100
  WREND = 5100
elif USER == "suoh": 
  WRSTART = 5100
  WREND = 5700
elif USER == "wonjun": 
  WRSTART = 5700
  WREND = 6300
elif USER == "hsseo": 
  WRSTART = 6300
  WREND = 6900
elif USER == "jhchoi":
  WRSTART = 6900
  WREND = 7100
else:
  WRSTART = 999999999999999999
  WREND = 99999999999999999

while (WRMASS <= WRMASSEND):

  NMASS = 100

  while (NMASS < WRMASS):

    if (NMASS == WRMASS): NMASS = WRMASS - 100
    DIRNAME = "WRtoNLtoLLJJ_WR"+(str)(WRMASS)+"_N"+(str)(NMASS)

    if (NMASS == 100): NMASS = NMASS + 100
    elif (NMASS == WRMASS - 200): NMASS = NMASS + 100
    else: NMASS = NMASS + 200

    if (WRSTART > WRMASS) or (WRMASS > WREND): continue

    print USER +"\t"+ DIRNAME


#    print DIRNAME +"\troot://cms-xrdr.sdfarm.kr:1094///xrd/store/user/shjeon/2017Run_WR_Dilep/PrivateLHE/"+DIRNAME+".lhe"
#    print DIRNAME +"\t/pnfs/knu.ac.kr/data/cms/store/user/shjeon/2016Run_WR_Dilep/2016/"+DIRNAME+".root"

  WRMASS = WRMASS + 200

