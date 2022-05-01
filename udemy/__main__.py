

from telethon import events

from udemy import CMD, START
from udemy.bot import UdemyBOT
from udemy.duce import Scrapper

bot = UdemyBOT()


@bot.on(events.NewMessage(func=lambda e: e.is_private, pattern="/(start|help)"))
async def _(event):
    await event.reply(START)


@bot.on(events.NewMessage(func=lambda e: e.is_private, pattern=f"/{CMD}"))
async def _(event):
    text = event.raw_text
    _cmd = text.split(" ", maxsplit=1)
    cmd = _cmd[0]
    page = ""
    if len(_cmd) == 2:
        page = _cmd[1]
    scp = Scrapper()
    msg = await event.reply("Wait...")
    if cmd == "/discudemy":
        if not page:
            page = 1
        links = await scp.discudemy(page)
    elif cmd == "/udemy_freebies":
        if not page:
            page = 1
        links = await scp.udemy_freebies(page)
    elif cmd == "/tutorialbar":
        if not page:
            page = 1
        links = await scp.tutorialbar(page)
    elif cmd == "/real_discount":
        if not page:
            page = 1
        links = await scp.real_discount(page)
    elif cmd == "/coursevania":
        links = await scp.coursevania()
    elif cmd == "/idcoupons":
        if not page:
            page = 1
        links = await scp.idcoupons(page)

    if not links:
        await msg.edit("No Free Courses Available 😞")
        return

    mg = "『✙ 𝗨𝗱𝗲𝗺𝘆 𝗖𝗼𝘂𝗿𝘀𝗲𝘀 𝗕𝘆 𝗘𝗩𝗜𝗟𝗭𝗢𝗡𝗘 ✙』\n\n"
    for link in links:
        for lin in link:
            mg += f"{lin}\n\n"
        await event.reply(mg, link_preview=False)
        mg = ""
    await msg.delete()


if __name__ == "__main__":
    bot.start_()
