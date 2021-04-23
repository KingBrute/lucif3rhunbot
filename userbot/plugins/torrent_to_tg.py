import re
from telethon.errors.rpcerrorlist import YouBlockedUserError

@bot.on(admin_cmd(pattern="ttodl ?(.*)"))
@bot.on(sudo_cmd(pattern="ttodl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = event.pattern_match.group(1)
    if not reply_message.startswith("magnet"):
        await edit_or_reply(event, "```Reply to or with a Magnet Link```")
        return
    chat = "@uploadbot"
    catevent = await edit_or_reply(event, " `Hmm, A magnet Link. I could generate download link. Hang On!`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            bot_response = await conv.get_response()
        except YouBlockedUserError:
          return await catevent.edit(
                "`You blocked `@uploadbot` Unblock it and give a try`"
            )
        if bot_response.text.startswith("Hi!"):
            await conv.send_message(reply_message)
            while true:
                response = await conv.get_response()
            if response.text.endswith(".zip"): break
                await event.client.send_read_acknowledge(conv.chat_id)
                parsed_response = re.findall(r'(http.*mkv|^http.*mp4|^http.*mp3)',response2)
                await catevent.edit(f"The Downlink For The Mangnet Link is '{parsed_response}'")
        else:
            await catevent.edit("Fuck You!!")

