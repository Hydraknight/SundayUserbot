from fridaybot import topfunc
from fridaybot.Configs import Config
from fridaybot.utils import friday_on_cmd
from var import Var

idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
currentversion = "3.0"
if issudousing:
    amiusingsudo = "Active ✅"
else:
    amiusingsudo = "Inactive ❌"

if islogokay:
    logchat = "Connected ✅"
else:
    logchat = "Dis-Connected ❌"

if isherokuokay:
    riplife = "Connected ✅"
else:
    riplife = "Not Connected ❌"

if isdbfine:
    dbstats = "Fine ✅"
else:
    dbstats = "Not Fine ❌"

inlinestats = (f"✘ SHOWING USERBUTT STATS ✘\n"
               f"VERSION = {currentversion} \n"
               f"DATABASE = {dbstats} \n"
               f"SUDO = {amiusingsudo} \n"
               f"LOG-CHAT = {logchat} \n"
               f"HEROKU = {riplife} ")
