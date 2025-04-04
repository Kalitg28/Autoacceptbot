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

@Client.on_chat_join_request()#filters.group | filters.channel & filters.private)
async def approve_request(bot, m):
    try:
        await rkn_botz.add_chat(bot, m)
        await bot.approve_chat_join_request(m.chat.id, m.from_user.id)
        img = random.choice(rkn1.SURPRICE)
        await bot.send_video(m.from_user.id, img, "**𝖧𝖾𝗅𝗅𝗈 {}, 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 {}\n𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖠𝗉𝗉𝗋𝗈𝗏𝖾𝖽...!!!\n\n𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 : @ck_linkz\n\n𝖢𝗅𝗂𝖼𝗄 𝖲𝗍𝖺𝗋𝗍 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖬𝗈𝗋𝖾**".format(m.from_user.mention, m.chat.title), reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("🎥 UPDATES CHANNEL 🔗", url=f"https://t.me/ck_linkz")]]))
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
    await m.reply_photo(photo=rkn1.RKN_PIC, caption="**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By :  @ck_linkz __**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("⇋ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇌", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("⇋ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ɢʀᴏᴜᴘ ⇌", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("🍃 ᴊᴏɪɴ ᴜᴩᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 🍃", url="https://t.me/ck_linkz")
                
            ]]))
            
 
@Client.on_callback_query(filters.regex("start"))
async def start_query(bot, cb : CallbackQuery):
    await cb.message.edit("**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By :  @ck_linkz __**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("⇋ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇌", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("⇋ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ɢʀᴏᴜᴘ ⇌", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("🍃 ᴊᴏɪɴ ᴜᴩᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 🍃", url="https://t.me/ck_linkz")
                
            ]]), disable_web_page_preview=True)
    
