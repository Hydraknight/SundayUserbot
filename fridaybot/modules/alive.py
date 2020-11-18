"""Check if GujjuBot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""

import time

from uniborg.util import friday_on_cmd, sudo_cmd

from fridaybot import ALIVE_NAME, Lastupdate
from fridaybot.Configs import Config
from fridaybot.modules import currentversion


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = "◉ **Userbutt Is :**  __ONLINE__\n\n"
pm_caption += "◉ **My Boss:** [Lawliet](tg://user?id=1403967684)\n"
pm_caption += "◉ **Assistant Butt:** [Watari](@WatariRobot)\n"
pm_caption += "\n"
pm_caption += "           [Hinata](https://t.me/misshinata_bot) | [Support](https://t.me/misslillysupport) | [Lilly](https://t.me/misslilly_bot)"                                                              


@friday.on(friday_on_cmd(pattern=r"alive"))
@friday.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
