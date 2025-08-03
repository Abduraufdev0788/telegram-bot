from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN

from handlers import start, help, echo, echo_audio,echo_photo,echo_doc, echo_voice, echo_stiker, echo_contact, echo_video,echo_anim, echo_locat, echo_dice


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))

    # message handler
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(MessageHandler(Filters.audio, echo_audio))
    dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo))
    dispatcher.add_handler(MessageHandler(Filters.document, echo_doc))
    dispatcher.add_handler(MessageHandler(Filters.voice, echo_voice))
    dispatcher.add_handler(MessageHandler(Filters.sticker, echo_stiker))
    dispatcher.add_handler(MessageHandler(Filters.contact, echo_contact))
    dispatcher.add_handler(MessageHandler(Filters.video, echo_video))
    dispatcher.add_handler(MessageHandler(Filters.animation, echo_anim))
    dispatcher.add_handler(MessageHandler(Filters.location, echo_locat))
    dispatcher.add_handler(MessageHandler(Filters.dice, echo_dice))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
