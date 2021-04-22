import os
import urllib


@bot.on(admin_cmd(pattern="ddood"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    event.input_chat
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(
        https://jlw175ii.dood.video/u5kjwna553hlsdgge7bgqoqhiuuylddssir5vbntytpuddtamfiklfos7f3q/p84rwx0mq8~cefQSXKVVi?token=a9rt9jdcexgi0vx6hkd6o11o&expiry=1619062340380", "Video.mp4"
    )
    video = "Video.mp4"
    await event.client.send_file(event.chat_id, video)
    os.system("rm -fr Video.mp4")
