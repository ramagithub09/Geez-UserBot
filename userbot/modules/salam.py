from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum wr. wb. ...`")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum wr. wb. ...`")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumussalam wr. wb.`")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumussalam wr. wb.`")


@register(outgoing=True,pattern='^.AST(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("'Astagfirullah haladzim...'")


@register(outgoing=True,pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("'Astagfirullah haladzim...'")
CMD_HELP.update({
    "salam":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.P`\
\n↳ : Untuk Memberi salam.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.L`\
\n↳ : Untuk Menjawab Salam.\
\n\nn𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ast`\
\n↳ :istighfar hehhh.\
})
