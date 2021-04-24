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
            await conv.get_response()
            await event.client.forward_messages(chat, reply_message)
            response1 = await conv.get_response()
            if response1.text:
                await event.client.send_read_acknowledge(conv.chat_id)
                return await catevent.edit(response1.text, parse_mode=parse_pre)
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            response3 = await conv.get_response()
            response4 = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            await edit_or_reply(catevent, response4.text)
        except YouBlockedUserError:
            return await catevent.edit(
                "`You blocked `@VS_Robot` Unblock it and give a try`"
            )
            
