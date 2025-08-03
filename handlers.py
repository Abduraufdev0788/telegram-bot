from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    update.message.reply_text(
        f'Assalomu alaykum! Botimizga xush kelibsiz {user.full_name}.\n\n'
        'bu bot testing uchun'
    )


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Qanday Yordam Kerak'
    )


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)
    
def echo_audio(update: Update, context: CallbackContext):
    audio = update.message.audio
    update.message.reply_audio(audio=audio)

def echo_photo(update: Update, context: CallbackContext):
    photo = update.message.photo[0]
    update.message.reply_photo(photo=photo)

def echo_doc(update:Update, context:CallbackContext):
    doc = update.message.document
    update.message.reply_document(document=doc)

def echo_voice(update:Update, context:CallbackContext):
    voice = update.message.voice
    update.message.reply_voice(voice=voice)

def echo_stiker(update:Update, context : CallbackContext):
    stiker = update.message.sticker
    update.message.reply_sticker(sticker=stiker)

def echo_contact(update:Update, context : CallbackContext):
    contact = update.message.contact
    update.message.reply_contact(contact=contact)

def echo_video(update:Update, context: CallbackContext):
    video = update.message.video
    update.message.reply_video(video=video)

def echo_anim(update :Update, context:CallbackContext):
    anim = update.message.animation
    update.message.reply_animation(animation=anim)

def echo_locat(update:Update, context:CallbackContext):
    location = update.message.location
    update.message.reply_location(location=location)

def echo_dice(update:Update, context:CallbackContext):
    dice = update.message.dice.emoji
    update.message.reply_dice(emoji=dice)