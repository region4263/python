from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *


app = ApplicationBuilder().token("YOUR_TOKEN").build()

print('server start')

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("input_one_str", input_one_str_command))
app.add_handler(CommandHandler("input_all_str", input_all_str_command))
app.add_handler(CommandHandler("input_from_file", input_from_file_command))
app.add_handler(CommandHandler("out_one_str", out_one_str_command))
app.add_handler(CommandHandler("out_all_str", out_all_str_command))

app.run_polling()
