import random
from telethon import events
import random, re

from jepthon.utils import admin_cmd

import asyncio
from jepthon import jepiq

from ..core.managers import edit_or_reply
from JepIQ.razan.resources.strings import *

plugin_category = "extra" 

#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="م17$",
    command=("م17", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "قائمة اوامر التمبـلر :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.الزغرفة` ) \n- ( `.اسماء تمبلر` )   \n- (`.اسماء عربية`)\n- ( `.اشهر مزغرفة`) \n- ( `.الاختصارات` ) \n- ( `.البايو` )\n- (`.المتحركات`)\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @k_ede"
            )
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="الزغرفة$",
    command=("الزغرفة", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "˛ JepThon ، ٰFٓoٍَِNٌtSَ\n"
                "•━═━═━═━═━━═━═━═━═━•\n"
                "**قائـمة اوامر الزغرفة :**\n"
                " `.زغرفة0`\n"
                " `.زغرفة1`\n"
                " `.زغرفة2`\n"
                " `.زغرفة3`\n"
                " `.زغرفة4`\n"
                " `.زغرفة5`\n"
                " `.زغرفة6`\n"
                " `.زغرفة7`\n"
                " `.زغرفة8`\n"
                " `.زغرفة9`\n"
                " **اكتب الاسم مع الامر للـزغرفة فقط انكليزي**\n"
                "•━═━═━═━═━━═━═━═━═━•‌‌\n"
                "˛ sᴏᴜʀᴄᴇ ᴀʟ -ᴍᴀᴊʀᴀ - [CَِٓHُ](t.me/k_ede)"
            )
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="اسماء تمبلر$",
    command=("اسماء تمبلر", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "قائمة اوامـر اسمـاء تمبـلر :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ᯽︙ اخـتر احـد هـذه القـوائـم:\n\n- (`.شباب1`) \n- (`.شباب2`) \n- (`.بنات1`) \n- (`.بنات2`) \n- (`.قنوات`) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @k_ede"
            )
#by ~ @RR 9R7
@jepiq.ar_cmd(
    pattern="البايو$",
    command=("البايو", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "قائمة اوامـر البـايو او الـنبذة :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ᯽︙ اخـتر احـد هـذه القـوائـم:\n\n \n- (`.بايو عربي`) \n- (`.بايو اجنبي`) \n ➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @k_ede"
            )
            
@jepiq.ar_cmd(
    pattern="الاختصارات$",
    command=("الاختصارات", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "قائمة اوامـر الاخـتصارات :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ᯽︙ اخـتر احـد هـذه القـوائـم:\n\n \n- (`.اختصارات1`) \n- (`.اختصارات2`) \n- (`.اختصارات3`) \n- (`.اختصارات4`) \n- (`.اختصارات5`) \n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @k_ede"
            )
            
@jepiq.ar_cmd(
    pattern="بايو اجنبي$",
    command=("بايو اجنبي", plugin_category),)
async def _(event):
    await event.edit("**يتم تجـهيز نبـذة اجنبـية لأجـلك انتـظر**")
    await asyncio.sleep(3)
    arj = random.choice(JEP)
    return await event.edit(f"{arj}")
    
    
@jepiq.ar_cmd(
    pattern="بايو عربي$",
    command=("بايو عربي", plugin_category),)
async def _(event):
    await event.edit("** يتم تجـهيز نبـذة عربيـة لأجـلك انتـظر**")
    await asyncio.sleep(3)
    arj = random.choice(JEPIRQ)
    return await event.edit(f"{arj}")
    
    
@jepiq.ar_cmd(
    pattern="المتحركات$",
    command=("المتحركات", plugin_category),)
async def _(event):
    await event.edit("قائمة اوامر المتـحركات :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.متحركات كيوت` ) \n- ( `.متحركات ساد` )\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @k_ede"
            )
            
@jepiq.ar_cmd(
    pattern="متحركات ساد$",
    command=("متحركات ساد", plugin_category),)
async def _(event):
    await event.edit("قائمة اوامر متحـرات سـاد :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.س1` ) \n- ( `.س2` )   \n- (`.س3`)\n- ( `.س4`) \n- ( `.س5` ) \n- ( `.س6` )\n- ( `.س7` )\n- ( `.س8` )\n- ( `.س9` )\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @k_ede"
            )
            

@jepiq.ar_cmd(
    pattern="متحركات كيوت$",
    command=("متحركات كيوت", plugin_category),)
async def _(event):
    await event.edit("قائمة اوامر متحـرات كيـوت :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.ك1` ) \n- ( `.ك2` )   \n- (`.ك3`)\n- ( `.ك4`) \n- ( `.ك5` ) \n- ( `.ك6` )\n- ( `.ك7` )\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @k_ede"
            )           

        
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="اشهر مزغرفة$",
    command=("اشهر مزغرفة", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "-₁₉₉₀\n"
                "-₁₉₉₁\n"
                "-₁₉₉₂\n"
                "-₁₉₉₃\n"
                "-₁₉₉₄\n"
                "-₁₉₉₅\n"
                "-₁₉₉₆\n"
                "-₁₉₉₇\n"
                "-₁₉₉₈\n"
                "-₁₉₉₉\n"
                "-₂₀₀₀\n"
                "-₂₀₀₁\n"
                "-₂₀₀₂\n"
                "-₂₀₀₃\n"
                "-₂₀₀₄\n"
                "-₂₀₀₅-\n"
                "-₂₀₀₆\n"
                "-₂₀₀₇\n"
                "---\n"
                "-𝒋𝒂𝒏𝒖𝒂𝒓𝒚.💞\n"
                "-𝒇𝒆𝒃𝒓𝒖𝒂𝒓𝒚.💞\n"
                "-𝒎𝒂𝒓𝒄𝒉.💞\n"
                "𝒂𝒑𝒓𝒊𝒍.💞\n"
                "-𝒎𝒂𝒚.💞\n"
                "-𝒋𝒖𝒏𝒆.💞\n"
                "-𝒋𝒖𝒍𝒚.💞\n"
                "-𝒂𝒖𝒈𝒖𝒔𝒕 .💞\n"
                "-𝒔𝒆𝒑𝒕𝒆𝒎𝒃𝒆𝒓 .💞\n"
                "-𝒐𝒄𝒕𝒐𝒃𝒆𝒓.💞\n"
                "-𝒏𝒐𝒗𝒆𝒎𝒃𝒆𝒓.💞\\n"
                "-𝒅𝒆𝒄𝒆𝒎𝒃𝒆𝒓.💞\n"
                "------\n"
                "-𝐒𝐔𝐍𝐃𝐀𝐘.♡\n"
                "-𝐌𝐎𝐍𝐃𝐀𝐘.♡\n"
                "-𝐓𝐔𝐄𝐒𝐃𝐀𝐘.♡\n"
                "-𝐖𝐄𝐃𝐍𝐄𝐒𝐃𝐀𝐘.♡\n"
                "-𝐓𝐇𝐔𝐑𝐒𝐃𝐀𝐘.♡\n"
                "-𝐅𝐑𝐈𝐃𝐀𝐘.♡\n"
                "-𝐒𝐀𝐓𝐔𝐑𝐃𝐀𝐘.♡"
            )
# ˛ jepthon ، ٰUٍsٓEِrBُoََt  # 

@jepiq.ar_cmd(
    pattern="اسماء عربية$",
    command=("اسماء عربية", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                " - ؏َـثمانَ 🍇.\n"
                "- ؏ـمرَ  🍇.\n"
                "- ؏َـلييہَ 🍇.\n"
                "- مَحـمدد 🍇.\n" 
                "- تو͡୭ما 🍇.\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "- ࢪزٱטּ 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "- تــﯢت 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "- شَيـטּ 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "- نــﯢטּ 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "- مَيممہَ 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "- ݽيـטּ 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "- دنــ͚͆ـو 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "- ࢪۅٛز 💕.\n"
                "- ۿهـَدى 💕.\n"
                "- سـَمــَࢪ 💕.\n"
                "- جنـَاٺ 💕.\n"
                "- مـَࢪيـَمٛہٰ 💕.\n"
                "- ࢪقيـَۿـہ 💕.\n"
                "- حَـﯛࢪا۽ِ 💕.\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "- بَــنـۅشہ𓆤.\n"
                "- ݛقَـﯡشہ𓆤.\n"
                "- ﭑيَـﯡشہ𓆤.\n"
                "- ࢪ࣪نَـشہ𓆤.\n"
                "- سَݛﯠشہ𓆤.\n"
                "- فَطـﯡشہ𓆤."
            )
# ˛ jepthon ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="شباب1$",
    command=("شباب1", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "-𓆩𝗠𝗨𝗛𝗔𝗠𝗠𝗔𝗗.𖤐𓆪\n"
                "-𓆩𝗔𝗠𝗔𝗔𝗥.𖤐𓆪\n" 
                "-𓆩𝗠𝗔𝗟𝗘𝗞.𖤐𓆪\n"
                "-𓆩𝗔𝗬𝗔𝗗.𖤐𓆪\n"
                "-𓆩𝗥𝗔𝗙𝗜𝗗.𖤐𓆪\n"
                "-𓆩𝗦𝗕𝗔𝗛.𖤐𓆪\n"
                "-𓆩𝗔𝗕𝗔𝗦.𖤐𓆪\n"
                "-𓆩𝗛𝗔𝗕𝗜𝗕.𖤐𓆪\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "⌯『𝐀𝐋𝐈』𖤍᭄𓄹\n"
                "⌯『𝐋𝐁𝐍𝐀 』𖤍᭄𓄹\n"
                "⌯『𝐀𝐒𝐄𝐄𝐋』𖤍᭄𓄹\n"
                "⌯『𝐒𝐇𝐄𝐑𝐄𝐍』𖤍᭄𓄹\n"
                "⌯『𝐌𝐔𝐒𝐓𝐀𝐅𝐀』𖤍᭄𓄹\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "𓆩𝒌𝒉𝒂𝒍𝒆𝒅𓆪 🖤.\n"
                "𓆩𝑶𝒎𝒂𝒓𓆪 🖤.\n"
                "𓆩𝑯𝒂𝒛𝒂𝒎𓆪 🖤.\n"
                "𓆩𝑯𝒂𝒕𝒂𝒎𓆪 🖤.\n"
                "𓆩𝑶𝒔𝒂𝒎𝒂𓆪 🖤.\n"
                "𓆩𝑯𝒂𝒅𝒐𓆪 🖤.\n"
                "𓆩𝑯𝒂𝒊𝒅𝒂𝒓𓆪 🖤.\n"
                "𓆩𝑮𝒉𝒂𝒍𝒆𝒃𓆪 🖤.\n"
                "𓆩𝑨𝒌𝒓𝒂𝒎𓆪 🖤.\n"
                "𓆩𝑯𝒂𝒔𝒐𝒏𝒆𓆪 🖤.\n"
                "𓆩𝑯𝒂𝒎𝒐𝒅𝒊𓆪 🖤.\n"
                "𓆩𝒗𝒊𝒓𝒐𝒔𓆪 🖤.\n"
                "𓆩𝑶𝒓𝒂𝒔𓆪 🖤.\n"
                "𓆩𝑺𝒂𝒍𝒊𝒉𓆪 🖤.\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "「𝘔𝘦𝘳𝘰 𐃣.\n"
                "「𝘋𝘢𝘦𝘷 𐃣.\n"
                "「𝘌𝘷𝘢 𐃣.\n"
                "「𝘋𝘮𝘢𝘳 𐃣.\n"
                "「𝘑𝘮𝘳𝘢 𐃣."
            )
# ˛ jepthon ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="شباب2$",
    command=("شباب2", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "𓆩𝑨𝒃𝒐𝒅𝒆𓆪 🖤.\n"
                "𓆩𝑴𝒖𝒔𝒕𝒂𝒇𝒂𓆪 🖤.\n"
                "𓆩𝑴𝒂𝒉𝒅𝒊𓆪 🖤.\n"
                "𓆩𝑸𝒂𝒔𝒂𝒎𓆪 🖤.\n"
                "𓆩𝑹𝒂𝒔𝒉𝒂𝒅𓆪 🖤.\n"
                "𓆩𝑨𝒅𝒏𝒂𝒏𓆪 🖤.\n"
                "𓆩𝑺𝒂𝒓𝒎𝒂𝒅𓆪 🖤.\n"
                "𓆩𝑯𝒂𝒔𝒂𝒏𓆪 🖤.\n"
                "𓆩𝑵𝒂𝒛𝒂𝒓𓆪 🖤.\n"
                "𓆩𝑴𝒐𝒉𝒂𝒎𝒆𝒅𓆪 🖤.\n"
                "𓆩𝑲𝒂𝒓𝒂𝒓𓆪 🖤.\n"
                "𓆩𝑨𝒉𝒎𝒆𝒅𓆪 🖤.\n"
                "𓆩𝑨𝒅𝒂𝒎𓆪 🖤.\n"
                "𓆩𝑯𝒖𝒔𝒔𝒊𝒆𝒏𓆪 🖤.\n"
                "𓆩𝑨𝒍𝒐𝒔𝒉𓆪 🖤.\n"
                "𓆩𝑹𝒂𝒔𝒐𝒖𝒍𓆪 🖤.\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "𓆩𝚁𝙾𝙽𝙴𓆪  🇺🇸.\n"
                "𓆩𝙴𝚅𝙰𝙽𓆪  🇺🇸.\n"
                "𓆩𝙹𝙰𝙺𓆪  🇺🇸.\n"
                "𓆩𝚃𝙾𝙼𓆪  🇺🇸.\n"
                "𓆩𝙹𝙾𝙽𓆪  🇺🇸.\n"
                "𓆩𝙰𝙷𝙼𝙸𝙳𓆪🎗️ ꙰\n"
                "𓆩𝙰𝙻𝙾𝚂𝙷𓆪🎗️ ꙰\n"
                "𓆩𝚂𝙰𝙹𝙰𝙳𓆪🎗️ ꙰\n"
                "𓆩𝚂𝙱𝙰𝙰𝙷𓆪🎗️ ꙰\n"
                "𓆩𝙷𝙰𝙸𝚃𝙷𝙼𓆪🎗️ ꙰\n"
                "𓆩𝙷𝚄𝚂𝚂𝙴𝙸𝙽𓆪🎗️ ꙰\n"
                "𓆩𝙼𝚄𝙷𝙰𝙼𝙼𝙰𝙳𓆪🎗️ ꙰\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "- 𝙎 𝘼 𝙄 𝙆 𝙊 : 🇺🇸Ꮠ\n"
                "- 𝙈 𝘼 𝙍 𝘾 𝙊 : 🇺🇸Ꮠ\n"
                "- 𝙎 𝘼 𝙉 𝙔 : 🇺🇸Ꮠ\n"
                "- 𝗥 𝗥 9 𝗥 7 : 🇺🇸Ꮠ\n"
                "- 𝙏 𝙃 𝘼 𝙈 𝙀 𝙍 : 🇺🇸Ꮠ\n"
                "- 𝘽 𝘼 𝙉 : 🇺🇸Ꮠ\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "𓂐 𝗝𝗠𝗧𝗛𝗢𝗡 𖠛 .\n"
                "𓂐 𝘼𝙈𝙀𝙍 𖠛 .\n"
                "𓂐 𝙆𝘼𝙈𝙀𝙇 𖠛.\n"
                "𓂐 𝙃𝙈𝙊 𖠛 .\n"
                "𓂐 𝙅𝙊𝙅 𖠛 ."
            )
# ˛ jepthon ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="بنات1$",
    command=("بنات1", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "- 𝑎𝑠𝑜 𐇲.\n"
                "- 𝑎𝑛𝑜 𐇲.\n"
                "- 𝑡𝑏𝑜 𐇲.\n"
                "- 𝑡𝑛𝑜 𐇲.\n"
                "- 𝒛𝒉𝒐 𐇲.\n"
                "- 𝒛𝒏𝒐 𐇲.\n"
                "- 𝒉𝒅𝒐 𐇲.\n"
                "- 𝒉𝒃𝒐 𐇲.\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "𖥻 𓆩𝗥𝗔𝗭𝗔𝗡𓆪،𖤍\n"
                "𖥻 𓆩𝙍𝙚𝙚𝙢𓆪،𖤍\n"
                "𖥻 𓆩𝙕𝙖𝙮𝙣𝙖𝙗𓆪،𖤍\n"
                "𖥻 𓆩𝙁𝙖𝙩𝙚𝙢𝙖𓆪،𖤍\n"
                "𖥻 𓆩𝙍𝙖𝙤𝙖𝙣𓆪،𖤍\n"
                "𖥻 𓆩𝙅𝙖𝙣𝙖𝙩𓆪،𖤍\n"
                "𖥻 𓆩𝙕𝙖𝙝𝙧𝙖𓆪،𖤍\n"
                "𖥻 𓆩𝙉𝙤𝙨𝙖𓆪،𖤍\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "- 𝙎 𝘼 𝙉 𝘿 𝙍 𝙄 𝙇 𝘼 : 🇺🇸Ꮠ\n"
                "- 𝙍 𝘽 𝘼 𝙉 𝙕 𝙇 : 🇺🇸Ꮠ\n"
                "- 𝙎 𝘼 𝙇 𝙇 𝙔 : 🇺🇸Ꮠ\n"
                "- 𝙆 𝘼 𝘿 𝙄 𝘼 : 🇺🇸Ꮠ\n"
                "- 𝙏 𝙊 𝙏 𝘼 : 🇺🇸Ꮠ\n"
                "- 𝘽 𝘼 𝙉 𝙀 𝙉 : 🇺🇸Ꮠ\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "𓄼 𝘙 𝘖 𝘡 ༆ 𓄹.\n"
                "𓄼 𝘚 𝘖 𝘚 ༆ 𓄹.\n"
                "𓄼 𝘛 𝘖 𝘛 ༆ 𓄹.\n"
                "𓄼 𝘕 𝘖 𝘕 ༆ 𓄹.\n"
                "𓄼 𝘍 𝘖 𝘍 ༆ 𓄹.\n"
                "𓄼 𝘑 𝘖 𝘑  ༆ 𓄹.\n"
                "𓄼 𝘒 𝘖 𝘒 ༆ 𓄹.\n"
                "𓄼 𝘛 𝘕 𝘖 ༆ 𓄹.\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "⌯ ˹𝚁𝙰𝚉𝙰𝙽˼❀ .\n"
                "⌯ ˹ʀɴᴏѕʜ˼❀ .\n"
                "⌯ ˹ᴍᴇᴍᴏ˼❀ .\n"
                "⌯ ˹ʜᴏʀᴇ˼ ❀ .\n"
                "⌯ ˹ѕᴀʀᴀ˼ ❀ .\n"
                "⌯ ˹ѕᴏѕ˼  ❀ .\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "𓂐 𝙍𝘼𝙕𝘼𝙉 𖠛.\n"
                "𓂐 𝙀𝙇𝙄𝙕𝘼𝘽𝙀𝙏𝙃 𖠛.\n"
                "𓂐 𝘼𝙈𝘼𝙉𝘿𝘼 𖠛 .\n"
                "𓂐 𝘼𝙉𝘿𝙍𝙀𝘼 𖠛 .\n"
                "𓂐 𝙀𝙈𝙀𝙇𝙔 𖠛 .\n"
                "𓂐𝙀𝙍𝙄𝙆𝘼 𖠛 .\n"
                "𓂐 𝙀𝙑𝘼 𖠛 .\n"
                "𓂐 𝘼𝙈𝙔  𖠛 ."
            )
# ˛ 𝖩𝗆𝗍𝖧ٰ𝗈𝗇 ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="بنات2$",
    command=("بنات2", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "『𓆩 𝚃𝙱𝙾 𓆪』𐂂𓄹\n"
                "『𓆩 𝙷𝙽𝙾 𓆪』 𐂂𓄹\n"
                "『𓆩 𝙰𝙽𝙾 𓆪』𐂂𓄹\n"
                "『𓆩 𝙰𝚉𝙾 𓆪』𐂂𓄹\n"
                "『𓆩 𝙳𝙷𝙾 𓆪』𐂂𓄹\n"
                "『𓆩 𝙰𝚂𝙾 𓆪』𐂂𓄹\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "•˹𝙻𝚈𝙽𝙽˼⛈💞.\n"
                "•˹𝙽𝙾𝙾𝚁˼⛈💞.\n"
                "•˹𝚂𝙰𝙼𝙰𝚁˼⛈💞.\n"
                "•˹𝙽𝙾𝚁𝙷𝙰𝙽˼⛈💞.\n"
                "•˹𝙺𝙰𝚆𝚃𝙷𝙴𝚁˼⛈💞.\n"
                "•˹𝚃𝙰𝙱𝙰𝚁𝙰𝚀˼⛈💞.\n"
                "•˹𝚂𝙰𝙱𝚁𝙴𝙴𝙽˼⛈💞.\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "•𝙼𝙰𝚁𝚈𝙰𝙼⋆  🧚🏻‍♀♥️ .\n"
                "•𝙱𝙰𝚃𝙾𝙻⋆ 🧚🏻‍♀♥️ .\n"
                "•𝙰𝙼𝙾𝙽⋆  🧚🏻‍♀♥️ .\n"
                "•𝚉𝙰𝙽𝙾𝚂𝙷𝙰⋆ 🧚🏻‍♀♥️ .\n"
                "•𝚉𝙰𝙷𝚁𝙰𝙰⋆  🧚🏻‍♀♥️ .\n"
                "•𝙱𝙰𝙽𝙴𝙽⋆ 🧚🏻‍♀♥️ .\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "• мαяɪαм🚴🏽‍♀️💞..\n"
                "• zαyиαв🚴🏽‍♀️💞..\n"
                "• sαяαн🚴🏽‍♀️💞..\n"
                "• zαняα🚴🏽‍♀️💞..\n"
                "• sнαɪмαα🚴🏽‍♀️💞..\n"
                "┉ ┉ ┉ ┉ ┉\n"
                "𝄇 𝗦𝗢𝗦𝗢𝆹𝅥𝅮 𝄆💘\n"
                "𝄇 𝗡𝗢𝗡𝗔𝆹𝅥𝅮 𝄆💘\n"
                "𝄇 𝗝𝗢𝗝𝗔 𝆹𝅥𝅮  𝄆💘\n"
                "𝄇 𝗠𝗘𝗠𝗔𝆹𝅥𝅮𝄆💘\n"
                "𝄇 𝗞𝗢𝗞𝗔𝆹𝅥𝅮 𝄆💘"
            )
        
# ˛ Jepthon ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="قنوات$",
    command=("قنوات", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "𝙁𝙍𝘼𝙉𝘾𝙊𝙄𝙎 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝙆𝙀𝙑𝙄𝙉 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝘼𝙉𝙇𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝘾𝙃𝙄𝙏𝙏𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝙎𝘼𝙑𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝘾𝙃𝙄𝘾𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝘾𝙃𝙄𝘾𝘼𝙂𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝙀𝘾𝙃𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝙔𝘼𝙔𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝙈𝘼𝙍𝘾𝙀𝙑𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "𝙔𝙄𝙎𝙆𝘼 𝟐𝟎𝟐𝟏 🎄꙳.\n"
                "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
                "𝐌𝐈𝐋𝐀𝐍 🌵\n"
                "𝐀𝐍𝐈𝐒𝐀𝐔 🌵\n"
                "𝐅𝐑𝐀𝐍𝐂𝐈𝐒𝐎 🌵\n"
                "𝐀𝐏𝐑𝐈𝐋  🌵\n"
                "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
                "𝙛𝙞𝙘𝙤 🎄\n"
                "𝙞𝙨𝙝𝙤 🎄\n"
                "𝙖𝙗𝙧𝙖𝙨 🎄\n"
                "𝙣𝙞𝙣𝙤 🎄\n"
                "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
                "*..⌠𝐒𝐞𝐥𝐯𝐚𝐧𝐚⌡𓊑.\n"
                "..⌠𝐓𝐨𝐛𝐚𝐤⌡𓊑.\n"
                "..⌠𝐄𝐥𝐤𝐚𝐫⌡𓊑.\n"
                "..⌠𝐌𝐚𝐲𝐚⌡𓊑.\n"
                "..⌠𝐓𝐞𝐨𝐨⌡𓊑.\n"
                "..⌠𝐌𝐞𝐚⌡𓊑.\n"
                "..⌠𝐋𝐞𝐥𝐞⌡𓊑.\n"
                "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
                "⌯ ˹𝙆𝙖𝙧𝙖˼ \n"
                "⌯ ˹𝙉𝙖𝙖𝙧˼ \n"
                "⌯ ˹𝙂𝙢𝙧˼ \n"
                "⌯ ˹𝘿𝙚𝙫˼\n"
                "⌯ ˹𝙀𝙫𝙖˼\n"
                "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
                ":   ˹𝘾𝘼𝙍𝙊𝙇𝙄𝙉𝙀˼ 𓆪 .\n"
                ":   ˹𝘾𝙍𝙔𝙎𝙏𝘼𝙇˼ 𓆪 .\n"
                ":   ˹𝙇𝘼𝙐𝙍𝙀𝙉˼ 𓆪 .\n"
                ":   ˹𝙆𝘼𝙈𝙄𝙇𝘼˼ 𓆪 .\n"
                ":   ˹𝘿𝘼𝙉𝘼˼ 𓆪 .\n"
                ":   ˹𝙍𝙄𝙏𝘼˼ 𓆪 .\n"
                ": ..................."
            )
# ˛ Jepthon ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="اختصارات1$",
    command=("اختصارات1", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "ڪݪخـرا .\n"
                "نجَبـيہ .\n"
                "؏ـمرჂ̤ .\n"
                "ۿـا .\n"
                "ـلا .\n"
                "حَياتـჂ̤ .\n"
                "سَـرسَحي .\n"
                "ڪياتۿهۃ .\n"
                "فدوۿهۃ .\n"
                "حَبيبـჂ̤ .\n"
                "حَبيبتـჂ̤ .\n"
                "مَڪدࢪ .\n"
                "حَيوانۿهۃ .\n"
                "ﺂوڪيـۃ .\n"
                "ۿـلو .\n"
                "وَلـჂ̤ .\n"
                "ههههۃ .\n"
                "لَـطيف .\n"
                "لَطيفهۃ .\n"
                "رﯢحـيہ .\n"
                "راحتـჂ̤ .\n"
                "ڪݪبـيہ .\n"
                "ﺂنام .\n"
                "ﺂڪل .\n"
                "طالـ؏ .\n"
                "طالعهۃ .\n"
                "مَۃ ﺂدرჂ̤ .\n"
                "شَڪو ؟ .\n"
                "؏َـليهۃ .\n"
                "؏َـليَك .\n"
                "ﺂوفـٰہ .\n"
                "ﺂمـﯢ؏ .\n"
                "حَبڪـٰہ .\n"
                "حَبجـٰہ .\n"
                "ﺂحـح .\n"
                "يـﺂჂ̤ .\n"
                "بـﺂჂ̤ .\n"
                "نـﺂنـჂ̤ .\n"
                "ﺂبـﯢﺳـہ .\n"
                "ﺂڪࢪط .\n"
                "ﺂ؏ـضـہ .\n"
                "يَـۃ فِـدﯢا\n"
                "ۿـواჂ̤ .\n"
                "ساعۿۃ .\n"
                "دَقيقهۃ .\n"
                "لَحضهۃ .\n"
                "ﺂمـوتہ .\n"
                "غَصيتہ .\n"
                "يـما .\n"
                "قَنـﺂتـჂ̤ .\n"
                "بـۅتـჂ̤ .\n"
                "مݪصَقاتہ .\n"
                "مُسـﺂبقهۃ .\n"
                "ﺂسمـჂ̤ .\n"
                "نتعَࢪفـہ ؟.\n"
                "ࢪاحتـჂ̤ .\n"
                "ﺂنـჂ̤ .\n"
                "رﺂنتـჂ̤ .\n"
                "؏ـشقيہ .\n"
                "وݪيدჂ̤ .\n"
                "بنَيتيہ .\n"
                "طِفݪتيہ .\n"
                "تَـعي .\n"
                "وَݪـيہ .\n"
                "موتبيڪہ .\n"
                "موتبيجہ .\n"
                "موتعَليڪہ .\n"
                "نصعَد ؟.\n"
                "صۅتَڪ .\n"
                "كصۅتِجہ .\n"
                "ﺂبـوسـہ.\n"
                "نَعَست .\n"
                "ﺂجيت.\n"
                " نجَبـჂ̤ .\n"
                "ڪݪزَقہ .\n"
                "نَـعـال .\n"
                "زَࢪبـۿهۃ .\n"
                "زاحفَۿهۃ .\n"
                "حَڪـہ .\n"
                "ﮪـہلاﯠﯠ\n"
                "ههيہلآﯛﯛ\n"
                "أههہـﯠﯠ\n"
                "شنـيہ\n"
                "هآيـہ\n"
                "يـ؏\n"
                "أﯠﯠ؏\n"
            )
# ˛ jepthon ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="اختصارات2$",
    command=("اختصارات2", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "ע\n"
                "ليـشـہٰ \n"
                "مِہטּ\n"
                "مِمـححِـہٰ\n"
                "ههههہ\n"
                "واللــہٰ\n"
                "؏َيـﯠﯢنڪك .\n"
                "رﯠﯢحڪكَ .\n"
                "حتـرﯠﯢحَ .\n"
                "؏َـمرڪك .\n"
                "اﯠﯢفَ . \n"
                "جـمـ؏ـﮫـہ\n"
                "مـبارڪـهـہ\n"
                "ـاٌلحمډ للۿ 💗.\n"
                "مــنــﹻـو \n"
                "آتـرخـصــہ\n"
                "اتمۂــنى\n"
                "ﺎتـﯡب .\n"
                "ﭑحنۿ \n"
                "ﺂﺣﺣَـم .\n"
                "د؏ۛـم .\n"
                "دقـِـِۧيۧقـِـِهہ.\n"
                "ډلينييہَ .\n"
                "ﻏﻏِـادرييہَ .\n"
                "حبچـჂَ̤\n"
                "ٲפـبج \n"
                "حــچي\n"
                "حـاڕِهۃ\n"
                "بـاردۿ`"
            )
        
# ˛ jepthon ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="اختصارات3$",
    command=("اختصارات3", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "• ھھݪـﯠ\n"
                "• شلـﯛنڪہ\n"
                "• شلـﯛنجهہ\n"
                "• ٲلحـﻣډ للّْهہ\n"
                "• يـٱ ࢪّبـــہ\n"
                "• تـﻣـاﻣـہۧ\n"
                "• زيـنۿۂ\n"
                "• شَـنـﯛ؟\n"
                "• ݪيٓش‏ـہ\n"
                "• ؏ــزهہ\n"
                "• خـࢪّبـہ\n"
                "• يڵهہ ؏ـاديـہ،\n"
                "• شڪډ ؏ـيبـہ\n"
                "• مُـحـࢪّ۾\n"
                "• نـُلـطمـہ\n"
                "• زيـاࢪّهہ\n"
                "• حـࢪّٲ۾\n"
                "• ارگـصـہۧ\n"
                "• ٲسبـحہَۧ\n"
                "• ٲرڪضـہۧ\n"
                "• زاحـفـہۧ\n"
                "• زاحـفـهہۧ\n"
                "• مُـتاحـہ،\n"
                "• مُـتاحۿۂ،\n"
                "• فـاۿيـهہ،\n"
                "• متتـــہ\n"
                "• ؏ـــشقجٰہ\n"
                "• ڪيـيوتـہ\n"
                "• ڪـافــيہۛ\n"
                "• بـ؏ـد \n"
                "• ليـشہ\n"
                "• ۿﮧـﺎ \n"
                "• ـآحنهٰــہ\n"
                "• ؏ـليك\n"
                "• حــب\n"
                "• حــبيہ\n"
                "• ؏ـنيہ\n"
                "• ﮪۛـوِٰاي\n"
                "• ؏ـليۿ\n"
                "• ؏ــيني"
            )
        
# ˛ jepthon ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="اختصارات4$",
    command=("اختصارات4", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "؏ـليڪ\n"
                "أඋـبڪ\n"
                "أنيہ\n"
                "شبيڪ\n"
                "يڪول\n"
                "لآ\n"
                "بسہ \n"
                "ليشہ\n"
                "أڪرۿڪ\n"
                "أڪول\n"
                "أڪلڪ\n"
                "أڪلج\n"
                "شلونڪ\n"
                "ﺎﻟلهۂَ \n"
                "ﺣــِلاﯛتيہ\n"
                "ٵڪوݪك\n"
                "شــ؏ـليه \n"
                "ٵڪﯙلـﭻ \n"
                "اﻧـييہ \n"
                "פـلوٰ \n"
                "ٵࢪيد \n"
                "ٵࢪوحـہ \n"
                "ا؏ـࢪفہ \n"
                "ٵدࢪيہ \n"
                "آ؏ـشقـجہ \n"
                "ﭑ؏ـشقڪہ \n"
                "تفضـࢦيہ\n"
                "تفضـࢦ\n"
                "פـباببهـہ\n"
                "פـباب\n"
                "פـاسـﯢب\n"
                "آميٰـטּ\n"
                "ﺑـسـہ \n"
                "ضَݪـ؏ـييہ\n"
                "ضَݪـ؏ـتيـہ\n"
                "؏َـندʊ̤\n"
                "ﺂجتمـا؏\n"
                "ٵჂ̤"
            )
        
# ˛ jepthon ، ٰUٍsٓEِrBُoََt  # 
#by ~ @lMl10l
@jepiq.ar_cmd(
    pattern="اختصارات5$",
    command=("اختصارات5", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
            await event.edit(
                "- مٰنۅِ 💕.\n"
                "- شٰخصَ 💕.\n"
                "- مٖتستاۿَݪ 💕.\n"
                "- ﺂݪتحِبۿم 💕.\n"
                "- يديمَݪج 💕.\n"
                "- ﻼَטּَ 💕.\n"
                "- ﺂݪحِبٰ 💕.\n"
                "- شٰݛطَ 💕.\n"
                "- ۈيَاجٖ 💕.\n"
                "- ڪِﯡليٰ 💕.\n"
                "- ؏ـلمِودِ 💕.\n"
                "- ﺂݪطِايٰݛ 💕.\n"
                "- صفٰحۿَہٰ 💕.\n"
                "- ﺂڪِݪتٰ 💕 .\n"
                "- نٰفسَكٰ 💕.\n"
                "- تِݛۿَ 💕.\n"
                "- طٰبيعَيٰ💕.\n"
                "- ڪِݪشيٰ 💕.\n"
                "- صٰديقِتيٰ 💕.\n"
                "- تَفيدكٰ 💕.\n"
                "- ڪٰمݪتِ 💕.\n"
                "- ﺂڪِݪ 💕.\n"
                "- ﺂݛيَدۿَ 💕.\n"
                "- مٖݛيضِۿَہٰ 💕.\n"
                "- ڪِݪتِ 💕.\n"
                "- خَتوݪيٰ 💕.\n"
                "- ݪزِڪٰۿَہٰ 💕.\n"
                "- ڪِافيٰ 💕.\n"
                "- صٰدﺂ؏َ 💕.\n"
                "- ﭑبوٰيۿَ 💕.\n"
                "- مِامَا 💕.\n"
                "- مٖخصِكٰ 💕.\n"
                "- ﺂݪكِ 💕.\n"
                "- ﺎرﯠﯢح ففدوۿَ ﺂݪعمَݛك 💕 .\n"
                "- ﺂتفضِݪ 💕.\n"
                "- ﺂچذبٰ 💕.\n"
                "- ﺂجِيتكٰ 💕.\n"
                "- غيَݛ 💕.\n"
                "- ڪٰيوِتَ 💕.\n"
                "- ﺂنِيٰ 💕.\n"
                "- ﺂحِبۿا 💕.\n"
                "- ﺂشِوفكٰ 💕.\n"
                "- ﺂسݪوِبكٰ 💕.\n"
                "- شٰوڪٰتِ 💕.\n"
                "- ݪوڪٰيہٰ 💕.\n"
                "- ﺂݪظَۿَݛ 💕.\n"
                "- شٰتحِسٰ 💕.\n"
                "- ﺂطِݪقِ💕 . \n"
                "- ﺂڪِوݪك 💕 .\n"
                "- ﺂحِبۿمٖ 💕.\n"
                "- ﺂݪۿِم 💕.\n"
                "- ﺂنشِاݪلۿَ 💕.\n"
                "- ﺂݪمۅفقيۿٰ 💕 . \n"
                "- بٰـﭑჂ̤ 💕 .\n"
                "- بِسرعۿِ 💕.\n"
                "- ﺂڪِوݪج  💕.\n"
                "- ﺂݪفِاضكٰ 💕.\n"
                "- ﺂ؏َـݛفِ 💕.\n"
                "- ح٘قيٰݛ 💕.\n"
                "- ﺂڪَثݛ 💕.\n"
                "- ڪِيبوٰݛد 💕.\n"
                "- بوسَنـჂ̤ 💕 .\n"
                "- تسَݪمينٰ 💕.\n"
                "- פـِبيبَتيٰ 💕.\n"
                "-  ؏ـنِديٰ 💕.\n"
                "- حِݪۅ 💕.\n"
                "- مٖتݪزِكٰ 💕."
            )
#by ~ @lMl10l

