# BOLBOT
My final project for Legend of Python

I created this bot as my final project for The Legend of Python on Codedex.
It does three things to a specific discord user which is hard coded into the script
in the "BOL" variable, so one could potentially change it to any user you wish, if you have their ID.

it has four commands, BOL:ayuda (help) BOL:callao (shut up!), BOL:silenciar (mute),
and BOL:desconectar (kick from call)

BOL:ayuda simply sends the other three commands as a message so people know them.

BOL:callao deletes the last message the specified user sent

BOL:silenciar mutes the user for a specified ammount of seconds ("BOL:silenciar 60" mutes
them for 60 seconds) 

BOL:desconectar disconnects the user from the call.

lastly, there is a "secret" command, BOL:mish which simply sends "mish" to the chat.

This bot was made to work only in my friends' server, hence the user ID for this specific friend is hardcoded
and why some things may not make too much sense, since they are inside jokes.

I learned about asynchronous functions thanks to making this dumb bot, which was the most lasting and useful
thing I learned, since I doubt I will use discord.py ever again.
