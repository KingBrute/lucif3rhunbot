import asyncio
import os

import cv2
import numpy as np
from PIL import Image
from telegraph import upload_file as upf
from validators.url import url

from . import *


@bot.on(admin_cmd(outgoing=True, pattern="sketch$"))
async def sketch(e):
    ureply = await e.get_reply_message()
    xx = await edit_or_reply(e, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    img = cv2.imread(file)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)
    cv2.imwrite("catroid.png", pencil_sketch_IMG)
    await e.client.send_file(e.chat_id, file="catroid.png")
    await xx.delete()
    os.remove(file)
    os.remove("catroid.png")


@bot.on(admin_cmd(outgoing=True, pattern="grey$"))
async def catd(event):
    ureply = await event.get_reply_message()
    if not (ureply and (ureply.media)):
        await edit_or_reply(event, "`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        xx = await edit_or_reply(event, "`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        xx = await edit_or_reply(event, "`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    cat = cv2.imread(file)
    catroid = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("cat.jpg", catroid)
    await event.client.send_file(
        event.chat_id, "cat.jpg", force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    os.remove("cat.png")
    os.remove("cat.jpg")
    os.remove(cat)


@bot.on(admin_cmd(outgoing=True, pattern="blur$"))
async def catd(event):
    ureply = await event.get_reply_message()
    if not (ureply and (ureply.media)):
        await edit_or_reply(event, "`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        xx = await edit_or_reply(event, "`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        xx = await edit_or_reply(event, "`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    cat = cv2.imread(file)
    catroid = cv2.GaussianBlur(cat, (35, 35), 0)
    cv2.imwrite("cat.jpg", catroid)
    await event.client.send_file(
        event.chat_id, "cat.jpg", force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    os.remove("cat.png")
    os.remove("cat.jpg")
    os.remove(cat)


@bot.on(admin_cmd(outgoing=True, pattern="negative$"))
async def catd(event):
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    cat = cv2.imread(file)
    catroid = cv2.bitwise_not(cat)
    cv2.imwrite("cat.jpg", catroid)
    await event.client.send_file(
        event.chat_id, "cat.jpg", force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    os.remove("cat.png")
    os.remove("cat.jpg")
    os.remove(cat)


@bot.on(admin_cmd(outgoing=True, pattern="mirror$"))
async def catd(event):
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    cat = cv2.imread(file)
    ish = cv2.flip(cat, 1)
    catroid = cv2.hconcat([cat, ish])
    cv2.imwrite("cat.jpg", catroid)
    await event.client.send_file(
        event.chat_id, "cat.jpg", force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    os.remove("cat.png")
    os.remove("cat.jpg")
    os.remove(cat)


@bot.on(admin_cmd(outgoing=True, pattern="flip$"))
async def catd(event):
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    cat = cv2.imread(file)
    trn = cv2.flip(cat, 1)
    ish = cv2.rotate(trn, cv2.ROTATE_180)
    catroid = cv2.vconcat([cat, ish])
    cv2.imwrite("cat.jpg", catroid)
    await event.client.send_file(
        event.chat_id, "cat.jpg", force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    os.remove("cat.png")
    os.remove("cat.jpg")
    os.remove(cat)


@bot.on(admin_cmd(outgoing=True, pattern="quad$"))
async def catd(event):
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    cat = cv2.imread(file)
    roid = cv2.flip(cat, 1)
    mici = cv2.hconcat([cat, roid])
    fr = cv2.flip(mici, 1)
    trn = cv2.rotate(fr, cv2.ROTATE_180)
    catroid = cv2.vconcat([mici, trn])
    cv2.imwrite("cat.jpg", catroid)
    await event.client.send_file(
        event.chat_id, "cat.jpg", force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    os.remove("cat.png")
    os.remove("cat.jpg")
    os.remove(cat)


@bot.on(admin_cmd(outgoing=True, pattern="toon$"))
async def catd(event):
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    cat = cv2.imread(file)
    height, width, channels = cat.shape
    samples = np.zeros([height * width, 3], dtype=np.float32)
    count = 0
    for x in range(height):
        for y in range(width):
            samples[count] = cat[x][y]
            count += 1
    compactness, labels, centers = cv2.kmeans(
        samples,
        12,
        None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001),
        5,
        cv2.KMEANS_PP_CENTERS,
    )
    centers = np.uint8(centers)
    ish = centers[labels.flatten()]
    catroid = ish.reshape((cat.shape))
    cv2.imwrite("cat.jpg", catroid)
    await event.client.send_file(
        event.chat_id, "cat.jpg", force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    os.remove("cat.png")
    os.remove("cat.jpg")
    os.remove(cat)


@bot.on(admin_cmd(outgoing=True, pattern="danger$"))
async def catd(event):
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    cat = cv2.imread(file)
    dan = cv2.cvtColor(cat, cv2.COLOR_BGR2RGB)
    catroid = cv2.cvtColor(dan, cv2.COLOR_HSV2BGR)
    cv2.imwrite("cat.jpg", catroid)
    await event.client.send_file(
        event.chat_id, "cat.jpg", force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    os.remove("cat.png")
    os.remove("cat.jpg")
    os.remove(cat)


@bot.on(admin_cmd(outgoing=True, pattern="blue$"))
async def catd(event):
    ureply = await event.get_reply_message()
    xx = await edit_or_reply(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    cat = await ureply.download_media()
    if cat.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", cat, "cat.png"]
        file = "cat.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(cat)
        heh, lol = img.read()
        cv2.imwrite("cat.png", lol)
        file = "cat.png"
    got = upf(file)
    lnk = f"https://telegra.ph{got[0]}"
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=blurpify&image={lnk}"
    ).json()
    ms = r.get("message")
    utd = url(ms)
    if not utd:
        return
    with open("cat.png", "wb") as f:
        f.write(requests.get(ms).content)
    img = Image.open("cat.png").convert("RGB")
    img.save("cat.webp", "webp")
    await event.client.send_file(
        event.chat_id, "cat.webp", force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    os.remove("cat.png")
    os.remove("cat.webp")
    os.remove(cat)
