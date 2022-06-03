from pyrogram import Client, filters , emoji

app = Client(
    "tag",
    api_id=1111111,
    api_hash=""
)



@app.on_message(filters.command("Tag", None) & filters.me)
def tag(c, m):
    global tag_on
    tag_on = True

    for user in app.iter_chat_members(m.chat.id, int(m.command[1]) if len(m.command) >= 2 else None):
        # sleep(1)
        if user.user.is_bot == False and user.user.is_deleted == False and not user.user.first_name == None:
            if tag_on:
                app.send_message(m.chat.id, f"{user.user.mention} {emoji.SPARKLES} بیاید ویس کال برای جمع بندی پازلا")
            else:
                exit()

@app.on_message(filters.command("stop", None) & filters.me)
def stoptg(c, m):
    global tag_on
    tag_on = False
    m.reply("K")



@app.on_message(filters.command("deltag", None) & filters.me)
def deltag(c, m):
    # del_on = True
    counte = app.search_global_count('جوین زیبا')
    for messages in app.search_global("جوین زیبا"):
        if not messages.text == None:
            app.delete_messages(m.chat.id, messages.message_id , revoke=False)
            print("deleted : " , messages.text , messages.message_id)
        else:
            # for mes in app.search_messages(m.chat.id , 'deltag' , from_user="me"):
            #     app.delete_messages(m.chat.id , mes.message_id , revoke=False)
            print('delted')
            continue


app.run()
