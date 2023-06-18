# coding: utf-8
# © @SanujaNS
# DONT_REMOVE_THIS


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode, Update
from instagrapi import Client
import logging
import requests
import json

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#Logger Setup
logger = logging.getLogger(__name__)

TOKEN = "5304538853:AAGIzSvvPtkcnDmxlCRv1OmJycq-TLX6yfQ"

def download(update: Update, context: CallbackContext):
    message = update.effective_message
    instagram_post = message.text
    if instagram_post=="/start":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
        update.message.reply_text("Hello 👋🏽, \nI'm @SanujaPut_InstaDL_bot. I can assist you with downloading Instagram videos and photos.  \n🔥 Just send me a Instagram post link, I will get it for you with best resoluton available.  \n\n<b>📌 Support Group :-</b> https://t.me/sanujas_space \n<b>🔓 Source</b> \nhttps://github.com/SanujaNS/SanujaPut_InstaDL_bot", parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    else:
        pass
    if "instagram.com" in instagram_post:
        changing_url = instagram_post.split("/")
        url_code = changing_url[4]
        url = f"https://instagram.com/p/{url_code}"
        cl = Client()
        pk = cl.media_pk_from_url(url)
        if cl.media_info(pk).product_type=="clips":
            try:
                video_url = cl.media_info(pk).video_url
                context.bot.send_chat_action(chat_id=update.message.chat_id, action="upload_video")
                context.bot.sendVideo(chat_id=update.message.chat_id, video=video_url)
            except:
                pass
        elif cl.media_info(pk).product_type=="":
            try:
                output = cl.media_info(pk)
                for resource in output.resources:
                    post_url = (resource.thumbnail_url)
                    context.bot.send_chat_action(chat_id=update.message.chat_id, action="upload_photo")
                    context.bot.sendPhoto(chat_id=update.message.chat_id, photo=post_url)
            except:
                pass

    else:
        context.bot.sendMessage(chat_id=update.message.chat_id, text="Check your link again. I'm unable to download this.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    logger.info("Setting Up MessageHandler")
    dp.add_handler(MessageHandler(Filters.text, download))
    updater.start_polling()
    logging.info("Starting Long Polling!")
    updater.idle()

if __name__ == "__main__":
    main()
