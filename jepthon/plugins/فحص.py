import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from jepthon import StartTime, jepiq, JEPVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"

#كتـابة وتعـديل:  @lMl10l
ALIVE_ET = Config.ALIVE_ET or "فحص"
@jepiq.on(admin_cmd(pattern=f"{ALIVE_ET}(?:\s|$)([\s\S]*)"))
    
async def amireallyalive(event):
    "للتـأكد من ان البـوت يعـمـل"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "** ᯽︙ يتـم التـأكـد انتـظر قليلا رجاءا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "⿻┊‌‎"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**父[ 𝙹𝙾𝙺𝙴𝚁 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 ✓ ](t.me/Jepthon)父**"
    RR7_IMG = gvarstatus("ALIVE_PIC") or Config.A_PIC
    jepiq_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = jepiq_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jepver=JEPVERSION,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if RR7_IMG:
        RR7 = [x for x in RR7_IMG.split()]
        PIC = random.choice(RR7)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


temp = """{ALIVE_TEXT}
**‎{EMOJI}‌‎𝙽𝙰𝙼𝙴 𖠄 {mention}** ٫
**‌‎{EMOJI}‌‎𝙿𝚈𝚃𝙷𝙾𝙽 𖠄 {pyver}** ٫
**‌‎{EMOJI}‌‎𝙹𝙾𝙺𝙴𝚁 𖠄 {telever}** ٫
**‌‎{EMOJI}‌‎𝚄𝙿𝚃𝙸𝙼𝙴 𖠄 {uptime}** ٫
‌‎**{EMOJI}‌‎‌‎𝙿𝙸𝙽𝙶 𖠄 {ping}** ٫
**𖠄 J𝗼𝗸𝗲𝗿 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𖠄**"""
