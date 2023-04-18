class script(object):
    START_TXT = """Hello {},
Myself <a href=https://t.me/{}>{}</a>,\n\nI am movies or series provider.You just ask me in messege and i will provide instan baby🥰\n\n😇Have Fun Baby😇"""

    HELP_TXT = """<b>𝙷𝙴𝚈 {}
Here is the help for my COMMANDS.</b>"""

    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/LazyIron</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""

    SOURCE_TXT ="""
<b>NOTE:</b>
Sorry Baby but I am Still Work On.

If You Want Repo then Search in github so many repos available there."""






 
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and LazyPriness will respond whenever that keyword hits the message
<b>NOTE:</b>
1. BOT should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>
• /gfilter - <code>to add global filter(admin only)</code>
• /gfilter - <code>check all global filters(all)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>
- Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. BOT supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/HUB4VF)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    ADMIN_TXT = """
<code>This Module works for my admins</code>

• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /deleteall - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴇs ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /setskip - <code>Tᴏ sᴋɪᴘ ɴᴜᴍʙᴇʀ ᴏғ ᴍᴇssᴀɢᴇs ᴡʜᴇɴ ɪɴᴅᴇxɪɴɢ ғɪʟᴇs.</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /invite - <code>Tᴏ ɢᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ᴄʜᴀᴛ ᴡʜᴇʀᴇ ᴛʜᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ.</code>
• /ban_user  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban_user  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /restart - <code>Tᴏ Rᴇsᴛᴀʀᴛ ᴀ Bᴏᴛ</code>
• /usend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssɢᴀᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Usᴇʀ</code>
• /gsend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssᴀɢᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /group_broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs</code>
• /status - <code>ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ sᴇʀᴠᴇʀ</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs<code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>"""

    STATUS_TXT = """<b>📂 ғɪʟᴇs sᴀᴠᴇᴅ:</b> <code>{}</code>
<b>👤 ᴜsᴇʀs:</b> <code>{}</code>
<b>👥 ɢʀᴏᴜᴘs:</b> <code>{}</code>
<b>📉 ᴏᴄᴄᴜᴘɪᴇᴅ:</b> <code>{}</code>

<b><a href=https://t.me/CyniteBackup>~ Maintained by Cynite</a></b>"""

    ADMIN_STATUS_TXT = """<b>⍟────[ ʙᴏᴛ sᴛᴀᴛᴜ𝗌 ]────⍟</b>

<b>⏳ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ:</b> <code>{}</code>

<b>☣️ ᴄᴘᴜ:</b> <code>{}%</code>

<b>☢️ ʀᴀᴍ:</b> <code>{}%</code>

<b>📊 ғɪʟᴇs sᴀᴠᴇᴅ:</b> <code>{}</code>

<b>👤 ᴜsᴇʀs:</b> <code>{}</code>

<b>👥 ɢʀᴏᴜᴘs:</b> <code>{}</code>

<b>♻️ ᴛᴏᴛᴀʟ:</b> <code>512 MB</code>

<b>🉐 ᴏᴄᴄᴜᴘɪᴇᴅ:</b> <code>{}</code>

<b>🆓 ғʀᴇᴇ:</b> <code>{}</code>

<b>⍟────[ @CyniteBackup ]─────⍟</b>"""

    LOG_TEXT_G = """<b>#NewGroup
    
Gʀᴏᴜᴘ = {} (<code>{}</code>)

Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>

Aᴅᴅᴇᴅ Bʏ - {}</b>
"""
    LOG_TEXT_P = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""
    ALRT_TXT = """⚠️ 𝖧ᴇʏ !
    
𝖲ᴇᴀʀᴄʜ 𝖸ᴏᴜʀ 𝖮ᴡɴ 𝖥ɪʟᴇ, 
    
𝖣ᴏɴ'ᴛ 𝖢ʟɪᴄᴋ 𝖮ᴛʜᴇʀ𝗌 𝖱ᴇ𝗌ᴜʟᴛ𝗌 😬
"""

    OLD_ALRT_TXT = """⚠️ 𝖧ᴇʏ ! 
    
𝖸ᴏᴜ Aʀᴇ U𝗌ɪɴɢ Oɴᴇ Oғ Mʏ Oʟᴅ Mᴇ𝗌𝗌ᴀɢᴇ𝗌, 
    
Sᴇɴᴅ Tʜᴇ Rᴇǫᴜᴇ𝗌ᴛ Aɢᴀɪɴ
"""

    CUDNT_FND = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ

ʀᴇᴀᴅ ɪɴsᴛʀᴜᴄᴛɪᴏɴs ꜰᴏʀ ʙᴇᴛᴛᴇʀ ʀᴇsᴜʟᴛs ☟</b>
"""

    I_CUDNT = """
<b>Sᴏʀʀʏ

I Cᴏᴜʟᴅ Nᴏᴛ Fɪɴᴅ Aɴʏᴛʜɪɴɢ Rᴇʟᴀᴛᴇᴅ Tᴏ Tʜᴀᴛ
Pʟᴇᴀsᴇ Cʜᴇᴄᴋ Yᴏᴜʀ Sᴘᴇʟʟɪɴɢ 🤧</b>
"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ...
"""

    MVE_NT_FND = """ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ...
"""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ...
"""
    
    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ:- Cynite
ᴜsᴇʀɴᴀᴍᴇ:- @cynitesupport
ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ:- <a href='https://t.me/cynitesupport'>Cynite</a></b>
"""

    CYNITE_IMDB = """
<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>

• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>
"""

    CYNITE_MISC = """
<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>

• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
"""

    CYNITE_FILSTR = """
<b>⍟ Wᴇʟᴄᴏᴍᴇ Tᴏ Fɪʟᴇ Sᴛᴏʀᴇ Mᴏᴅᴜʟᴇ ⍟</b>

» ᴀ ᴍᴏᴅᴜʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ ғᴏʀ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ.

<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>

• /link <code>- ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ.<code>
• /batch <code>- ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ғᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ᴍᴇᴅɪᴀ.<code>

<b>Exᴀᴍᴘʟᴇ:</b>
<code>/batch https://t.me/Cynitebackup
https://t.me/CyniteBackup </code>
"""

    CYNITE_CNL = """
♡ ᴄʜᴀɴɴᴇʟs & ɢʀᴏᴜᴘs ᴍᴏᴅᴜʟᴇ ♡

📹 ᴄᴏᴍᴘʟᴇᴛᴇ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛɪɴɢ ɢʀᴏᴜᴘ.
🎙 ᴀʟʟ ʟᴀɴɢᴜᴀɢᴇs ᴍᴏᴠɪᴇ & sᴇʀɪᴇs.
🤖 ʙᴏᴛ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.
👾 ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ.
"""

    FORCE_SUB = """
**⚠️ ᴘʟᴇᴀsᴇ ғᴏʟʟᴏᴡ ᴛʜɪs ʀᴜʟᴇs ⚠️

ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ʏᴏᴜ.

ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ.

ᴀғᴛᴇʀ ᴛʜᴀᴛ ᴛʀʏ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴀᴛ ᴍᴏᴠɪᴇ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴛʀʏ ᴀɢᴀɪɴ.

ɪ'ʟʟ sᴇɴᴅ ʏᴏᴜ ᴛʜᴀᴛ ᴍᴏᴠɪᴇ ᴘʀɪᴠᴀᴛᴇʟʏ.**
"""
    
    BANP_LOG_TXT = """<b>⍟ Bᴀɴɴᴇᴅ Usᴇʀ Lᴏɢs ⍟</b>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>Nᴀᴍᴇ :</b> <b>{}</b>

<b>Rᴇᴀsᴏɴ :</b> <code>{}</code>

<b>⍟ #BannedUser ⍟</b>
"""
    UNBANP_LOG_TXT = """<b>⍟ UɴBᴀɴɴᴇᴅ Usᴇʀ Lᴏɢs ⍟</b>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>Nᴀᴍᴇ :</b> <b>{}</b>

<b>⍟ #UnBannedUser ⍟</b>
"""
    BANG_LOG_TXT = """<b>⍟ Bᴀɴɴᴇᴅ Gʀᴏᴜᴘ Lᴏɢs ⍟</b>

<b>Cʜᴀᴛ ID :</b> <code>{}</code>

<b>Rᴇᴀsᴏɴ :</b> <code>{}</code>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>⍟ #BannedGroup ⍟</b>
"""
    UNBANG_LOG_TXT = """<b>⍟ UɴBᴀɴɴᴇᴅ Gʀᴏᴜᴘ Lᴏɢs ⍟</b>

<b>Cʜᴀᴛ ID :</b> <code>{}</code>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>⍟ #UnBannedGroup ⍟</b>
"""

    REQINFO2 = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ
"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ
"""

    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Kgf 2022

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Money Heist S01E01 or Money Heist S01 E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
"""

    PAGEINFO = """
ᴘᴀɢᴇs ᴍᴇᴀɴs 10 ғɪʟᴇs ɪɴ ᴏɴᴇ ᴘᴀɢᴇ

ɪғ ʏᴏᴜ ɴᴏᴛ sᴇᴇ ʏᴏᴜʀ ғɪʟᴇs ᴏɴ ᴛʜɪs ᴘᴀɢᴇ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ɴᴇxᴛ ᴘᴀɢᴇ.

Powered by :- @CyniteBackup
"""

    SPLMD = """
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛ ғᴏʀᴍᴀᴛ

ᴇxᴀᴍᴘʟᴇ : Kgf or Kgf 2022

sᴇʀɪᴇs ʀᴇǫᴜᴇsᴛ ғᴏʀᴍᴀᴛ

ᴇxᴀᴍᴘʟᴇ : Money Heist S01E01 or Money Heist S01 E01

🚯ᴅᴏɴ'ᴛ ᴜsᴇ ➠ ':(!,./)

Powered by :- @CyniteBackup
"""
    
    REQUEST_TXT = """
<u><b>📫 Rᴇǫᴜᴇsᴛ Dᴇᴛᴀɪʟs :</b></u>

<b>🔖 Mᴇssᴀɢᴇ :</b><code>{}</code>

<b>🕵️ Rᴇǫᴜᴇsᴛᴇᴅ Bʏ :</b> <b>{} [ <code>{}</code> ] </b>
"""

    REQUEST2_TXT = """
<i><b>Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Hᴀs Bᴇᴇɴ Aᴅᴅᴇᴅ!
Pʟᴇᴀsᴇ Wᴀɪᴛ Fᴏʀ Sᴏᴍᴇ Tɪᴍᴇ.</b></i>
"""

    SGROUP_TXT = """
<b>Dᴇᴀʀ, {}

<code>{}</code> Rᴇsᴜʟᴛs Aʀᴇ Aʟʀᴇᴀᴅʏ Aᴠᴀɪʟᴀʙʟᴇ Fᴏʀ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ <code>{}</code> Iɴ <a href=https://t.me/CyniteBackuo >Oᴜʀ Cʜᴀɴɴᴇʟ</a>.</b>
"""

    DONE_UPLOAD = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Cᴏᴍᴘʟᴇᴛᴇᴅ !! Cʜᴇᴄᴋ Bᴏᴛ & Cʜᴀɴɴᴇʟ !!
"""

    REQ_REJECT = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Rᴇᴊᴇᴄᴛᴇᴅ Mᴀʏʙᴇ Dᴜᴇ Tᴏ Sᴀᴍᴇ Rᴇǫᴜᴇsᴛ, Nᴏᴛ Iɴ Fᴏʀᴍᴀᴛ !!
"""

    REQ_NO = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ Mᴀʏʙᴇ Dᴜᴇ Tᴏ Nᴏᴛ Rᴇʟᴇᴀsᴇᴅ Oʀ Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ !!
"""

    DONE_ALREADY = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Aʟʀᴇᴀᴅʏ Uᴘʟᴏᴀᴅᴇᴅ !! Cʜᴇᴄᴋ Bᴏᴛ & Cʜᴀɴɴᴇʟ !!
""" 
    
    DONE_UPLOAD2 = """
<b>Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Sᴜᴄᴇssғᴜʟʟʏ Uᴘʟᴏᴀᴅᴇᴅ Sᴇᴀʀᴄʜ Aɢᴀɪɴ..🙃</b>
"""

    REQ_REJECT2 = """
<b>Rᴇǫᴜᴇsᴛ Rᴇᴊᴇᴄᴛᴇᴅ 🚫 !!

Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Aʟʀᴇᴀᴅʏ Mᴀʏʙᴇ Iɴ Tʜᴇ Rᴇǫᴜᴇsᴛ Lɪsᴛ Oʀ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Is Mᴀʟғᴏʀᴍᴀᴛᴛᴇᴅ. Kɪɴᴅʟʏ Rᴇǫᴜᴇsᴛ Aɢᴀɪɴ Oʀ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ Fᴏʀ Hᴇʟᴘ.</b>
"""

    REQ_NO2 = """
<b>Sᴏʀʀʏ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ 😔,
Kɪɴᴅʟʏ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ Fᴏʀ Hᴇʟᴘ.</b>
"""

    DONE_ALREADY2 = """
<b>Rᴇǫᴜᴇsᴛ Aʟʀᴇᴀᴅʏ Uᴘʟᴏᴀᴅᴇᴅ ❗,
Kɪɴᴅʟʏ Cʜᴇᴄᴋ Tʜᴇ Bᴏᴛ Bᴇғᴏʀᴇ Rᴇǫᴜᴇsᴛɪɴɢ.</b>
"""

    CAP_DLT_TXT = """
<b>ᴛʜᴇ ʀᴇsᴜʟᴛ ꜰᴏʀ:- <code>{}</code></b>

<b>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:- {}</b>

<b>ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇᴅ ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇs…</b>
"""

    CAP_TXT = """
<b>ᴛʜᴇ ʀᴇsᴜʟᴛ ꜰᴏʀ:- <code>{}</code></b>

<b>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:- {}</b>

<u><b>ʜᴇʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛʜᴇ ꜰɪʟᴇs ʏᴏᴜ ᴡᴀɴᴛ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ..</b></u>
"""

    FILE_CHANNEL_TXT = """
<b>🏷️ Tɪᴛʟᴇ :- <code>{}</code>

⚙️ Sɪᴢᴇ :- {}

🕵️‍♂️ Rᴇǫᴜᴇsᴛᴇᴅ Bʏ :- {}

🔅 Pᴏᴡᴇʀᴇᴅ Bʏ :- {}

<a href='https://t.me/Cynitebackup'>‣ Tʜɪs Mᴇssᴀɢᴇ Wɪʟʟ ʙᴇ Aᴜᴛᴏ-Dᴇʟᴇᴛᴇᴅ Aғᴛᴇʀ 5 Mɪɴᴜᴛᴇs. Kɪɴᴅʟʏ Fᴏʀᴡᴀʀᴅ Yᴏᴜʀ Fɪʟᴇs Tᴏ Sᴀᴠᴇᴅ.</a></b>"""

    FILE_READY_TXT = """
<b>Hᴇʏ {}
 
📫 Yᴏᴜʀ Fɪʟᴇ Is Sᴇɴᴛ Tᴏ Cʜᴀɴɴᴇʟ, 
Cʜᴇᴄᴋ Dᴏᴡɴ Tᴏ Vɪᴇᴡ.

📂 Fɪʟᴇ Nᴀᴍᴇ :- <code>{}</code>

⚙️ Fɪʟᴇ Sɪᴢᴇ :- {}</b>
"""
