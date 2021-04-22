import os
import urllib

from telethon.tl import functions

@bot.on(admin_cmd(pattern="ddood"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    chat = event.input_chat
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
       os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(
        "https://dood.so/e/vgz5kmf2bqmhbpgkhtbsemib50uvxk3f", "Video.mp4"
    )
    video = "Video.mp4"
    await event.client.send_file(event.chat_id, video)
    os.system("rm -fr Video.mp4")
