# pyrogram imports
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums, errors
from pyrogram.errors import UserNotParticipant, PeerIdInvalid, UserIsBlocked

# bots imports
from RknDeveloper.database import rkn_botz
from RknDeveloper.fs import force_sub
from configs import rkn1
import random, asyncio, os


# Main Process _ _ _ _ _ Users Send Massage 🥀__🥀 Please 😢 Give Credit

@Client.on_chat_join_request()
async def approve_request(bot, m):
    try:
        await rkn_botz.add_chat(bot, m)
        await bot.approve_chat_join_request(m.chat.id, m.from_user.id)
        text = "**𝖧𝖾𝗅𝗅𝗈 {}, 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 {}\n𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖠𝗉𝗉𝗋𝗈𝗏𝖾𝖽...!!!\n\n<blockquote>🌹 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 ›› <a href="https://t.me/Indian_MV">🇮🇳 𝐈𝐧𝐝𝐢𝐚𝐧 𝐌𝐕 🇮🇳</a></blockquote>\n\n𝖢𝗅𝗂𝖼𝗄 𝖲𝗍𝖺𝗋𝗍 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖬𝗈𝗋𝖾**".format(m.from_user.mention, m.chat.title)
        await bot.send_message(
            m.from_user.id,
            text,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🎥 UPDATES CHANNEL 🔗", url="https://t.me/Indian_MV")
            ]])
        )
        await rkn_botz.add_user(bot, m)
    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid as err:
        print(f"user isn't start bot (means group) Error- {err}")
    except Exception as err:
        print(f"Error\n{str(err)}")
        
   
# Start Massage _____ # Please 😢 Give Credit 

@Client.on_message(filters.command("start"))
async def start_commond(bot, m :Message):
    if m.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await rkn_botz.add_chat(bot, m)
        return await m.reply_text("**🦊 Hello {}!\nwrite me private for more details.**".format(m.from_user.first_name), reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url=f"https://t.me/{bot.username}?start=start")
                    ]
                ]
            ))
            
    await rkn_botz.add_user(bot, m)
    await force_sub(bot, m, rkn1.FORCE_SUB)
    await m.reply_photo(photo=rkn1.RKN_PIC, caption="**<blockquote>🦊 Hello {}!\nI'm an auto approve Bot.\n\nI can approve users in Groups/Channels.</blockquote>\n\n<blockquote>Add me to your chat and promote me to admin with add members permission.</blockquote>\n\n<blockquote>🌹 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 ›› <a href="https://t.me/Indian_MV">🇮🇳 𝐈𝐧𝐝𝐢𝐚𝐧 𝐌𝐕 🇮🇳</a></blockquote>\n\n[How To Create Request Channel Link]({})**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("⇋ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇌", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("⇋ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ɢʀᴏᴜᴘ ⇌", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("🍃 ᴊᴏɪɴ ᴜᴩᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 🍃", url="https://t.me/Indian_MV")
                
            ]]))
            
 
@Client.on_callback_query(filters.regex("start"))
async def start_query(bot, cb : CallbackQuery):
    await cb.message.edit("**<blockquote>🦊 Hello {}!\nI'm an auto approve Bot.\n\nI can approve users in Groups/Channels.</blockquote>\n\n<blockquote>Add me to your chat and promote me to admin with add members permission.</blockquote>\n\n<blockquote>🌹 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 ›› <a href="https://t.me/Indian_MV">🇮🇳 𝐈𝐧𝐝𝐢𝐚𝐧 𝐌𝐕 🇮🇳</a></blockquote>\n\n[How To Create Request Channel Link]({})**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("⇋ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇌", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("⇋ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ɢʀᴏᴜᴘ ⇌", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("🍃 ᴊᴏɪɴ ᴜᴩᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 🍃", url="https://t.me/Indian_MV")
                
            ]]), disable_web_page_preview=True)
    
