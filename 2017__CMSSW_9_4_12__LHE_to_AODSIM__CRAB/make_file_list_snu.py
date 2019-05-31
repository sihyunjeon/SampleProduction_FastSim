import os,getpass,socket

#print socket.gethostname()

WRMASSEND = 7001
WRMASS = 200
PRINT = False

USER = getpass.getuser()
HOST = socket.gethostname()
WRSTART = 0
WREND = 0
IsKNU = True#False ###IF KNU : use crab
IsKISTI = False ###IF KISTI : use condor

if "knu" in HOST:
  IsKNU = True
if ("ui10" in HOST) or ("ui20" in HOST):
  IsKISTI = True

if USER == "helee":
  WRSTART = 100
  WREND = 4100
elif USER == "hsseo":
  WRSTART = 4100
  WREND = 5900
elif USER == "jhchoi":
  WRSTART = 5900
  WREND = 7100
else:
  WRSTART = 999999999999999999
  WREND = 99999999999999999

if IsKISTI == True:
  WRSTART = 1
  WREND = 7100

while (WRMASS <= WRMASSEND):

  NMASS = 100

  while (NMASS < WRMASS):

    if (NMASS == WRMASS): NMASS = WRMASS - 100
    DIRNAME = "WRtoNLtoLLJJ_WR"+(str)(WRMASS)+"_N"+(str)(NMASS)

    if (WRMASS%1000. != 0) or (NMASS%600 != 0):
      if IsKNU == True:
        PRINT = True
      else: PRINT = False 
    else:
      if IsKISTI == True:
        PRINT = True
      else: PRINT = True ###print all file lists when in knu

    if (NMASS == 100): NMASS = NMASS + 100
    elif (NMASS == WRMASS - 200): NMASS = NMASS + 100
    else: NMASS = NMASS + 200

    if (WRSTART > WRMASS) or (WRMASS > WREND): continue
    if IsKNU == True:
      if PRINT == True: print DIRNAME +"\troot://cluster142.knu.ac.kr//store/user/shjeon/2017Run_WR_Dilep/PrivateLHE/"+DIRNAME+".lhe"
    if IsKISTI == True:
      if PRINT == True: print DIRNAME +"\t/store/user/shjeon/2017Run_WR_Dilep/PrivateLHE/"+DIRNAME+".lhe"

  WRMASS = WRMASS + 200

