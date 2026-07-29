
python
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

EMOTIONS = {
    "😔 غم": {"insight": "غم نشانه‌ی ارتباط عمیق توست. اجازه بده احساس بشه، نه سرکوب.", "exercise": "تمرین: ۵ نفس عمیق بکش. با هر بازدم تصور کن یه بار سنگین رو زمین می‌ذاری."},
    "😠 خشم": {"insight": "خشم اغلب پشتش ترس یا درد پنهانه. بپرس: 'زیر این خشم چی هست؟'", "exercise": "تمرین: ۱۰ ثانیه عضلات مشتت رو سفت کن، بعد یکدفعه رها کن."},
    "😰 اضطراب": {"insight": "اضطراب ذهنته که داره سعی می‌کنه از تو محافظت کنه — حتی اگه اشتباه باشه.", "exercise": "تمرین ۵-۴-۳-۲-۱: ۵ چیز می‌بینی، ۴ چیز لمس می‌کنی، ۳ صدا می‌شنوی، ۲ بو حس می‌کنی، ۱ طعم."},
    "😊 شادی": {"insight": "شادی رو کامل تجربه کن — بدون احساس گناه. لایقشی.", "exercise": "تمرین: این لحظه رو با یه نفر به اشتراک بذار یا توی دفترت بنویس."},
    "😶 بی‌حسی": {"insight": "بی‌حسی گاهی سپر ذهن در برابر احساسات طاقت‌فرساست.", "exercise": "تمرین: یه دوش آب ولرم بگیر و فقط روی حس آب روی پوستت تمرکز کن."}
}

keyboard = [[e] for e in EMOTIONS.keys()]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋\nالان چه احساسی داری؟", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in EMOTIONS:
        data = EMOTIONS[text]
        await update.message.reply_text(f"💡 {data['insight']}\n\n🧘 {data['exercise']}")
    else:
        await update.message.reply_text("یه احساس از منو انتخاب کن 👇", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

app = ApplicationBuilder().token(os.environ["TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling()

