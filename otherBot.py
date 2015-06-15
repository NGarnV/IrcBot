# Import some necessary libraries.
import socket
import string
import commands

# Some basic variables used to configure the bot        
server = "efnet.port80.se"  # Server
channel = "#123"  # Channel
botnick = "Haakan"  # bot's nick

def ping():  # This is our first function! It will respond to server Pings.
    ircsock.send("PONG :ping\n")


def sendmsg(recipient, msg):  # This is the send message function, it simply sends messages to the channel.
    ircsock.send("PRIVMSG " + recipient + " :" + msg + "\n")


def joinchan(chan):  # This function is used to join channels.
    ircsock.send("JOIN " + chan + "\n")



ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))  # connect to the server using the port 6667
ircsock.send("USER " + botnick + " " + botnick + " " + botnick + " :some stuff\n")  # user authentication
ircsock.send("NICK " + botnick + "\n")  # here we actually assign the nick to the bot
joinchan(channel)  # Join the channel using the functions we previously defined

while 1:
    ircmsg = ircsock.recv(1024)  # receive data from the server
  # ircmsg = ircmsg.strip('\n\r')  # removing any unnecessary linebreaks.
    print(ircmsg)  # Here we print what's coming from the server

    # if ircmsg.find(botnick) in ircmsg and "PRIVMSG ") in ircmsg and "rizon") == -1:
    # # If we can find "cybits" it will call the function hello()
    #     hello(ircmsg.split(":")[1].split('!')[0])
    #     continue

    if " :.lit" in ircmsg and channel in ircmsg:  # If we can find ".lit" it will call the function sentence()
        sendmsg(channel, commands.sentence())
        continue

    if " :.feel" in ircmsg and channel in ircmsg:  # If we can find ".feel" it will call the function feel()
        array = commands.feel()
        sendmsg(channel, array[0])
        user = ircmsg.split(":")[1].split('!')[0]
        sendmsg(user, array[1])
        continue

    if " :website" in ircmsg and channel in ircmsg:
        website()
        continue

    if "PING :" in ircmsg:  # respond to pings
        ping()
