@register(outgoing=True, pattern='^.musik(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Ok mulai la la la🎶🎶🎶🎶`")
    sleep(1)
    await typew.edit("`Du du du du 🎶🎶🎶🎶`")
    sleep(1)
    await typew.edit("`Ahihi hihi hihi 🤣🤣🤣`")
    sleep(1)
    await typew.edit("`Bingung mau nyanyi apa 🤔🤔`")
    sleep(1)
    await typew.edit("`Jadinya ya cuma gitu ,awikwok`")
    sleep(1)
    await typew.edit("`Dahlah 😭😭sampai sini aja dulu`")
    sleep(1)


CMD_HELP.update({
    "ram-animasi":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.musik`\
    \n↳ : Gatau gabut aja huhuu\
