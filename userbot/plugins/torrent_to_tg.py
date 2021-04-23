import re
from telethon.errors.rpcerrorlist import YouBlockedUserError

@bot.on(admin_cmd(pattern="ttodl ?(.*)"))
@bot.on(sudo_cmd(pattern="ttodl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.startswith("magnet"):
        await edit_or_reply(event, "```Reply to or with a Magnet Link```")
        return
    chat = "@uploadbot"
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual user's message.```")
        return
    catevent = await edit_or_reply(event, " `Hmm, A magnet Link. I could generate download link. Hang On!`")
        async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await event.client.forward_messages(chat, reply_message)
            response1 = await conv.get_response()
         if response1.text:
                parsed_response = re.findall(r'(http.*mkv|^http.*mp4|^http.*mp3)',response1)
                await edit_or_reply(catevent,f"The Downlink For The Mangnet Link is '{parsed_respose}'".
             except YouBlockedUserError:
        return await catevent.edit(
                "`You blocked `@@uploadbot` Unblock it and give a try`"
            )
