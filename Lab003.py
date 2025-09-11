
from pyre import pyre
from pyre import zhelper
import zmq
import uuid
import json
import lab_chat as lc


#Part 1 Core function - Data handling and user input
#create function to get username
def get_peer_node(username):
    n = pyre(username)
    n.start()
    return n
    username = input("Please enter your username: ")
    return username.strip().upper()

#create a function to select group chat to join
def  get_group():
    group = input("Please enter your group: ")
    return group.strip().upper()


#create function to send message
def get_message():
    message = input("Please enter your message: ")
    return message.strip()


#Part 2 understanding p2p communications functions

def chat_task(ctx, pipe, n, group): #function name is chat_task

        #ctx: zeromq connection context
    #pipe: a communications pipe polled by ZeroMQ for messages.
    #n: the peer to peer node my chat app is connected as
    #group: the peer chat group I wanted to join_group
    #returns nothing
    #purpose main function that handles sending/receiving chat messages
    pass

#part 3 combining functions to create peer-to-peer chat
#initialzing the chat



def initialize_chat():
    username = get_username()
    group = get_group()

    #create a peer node
    node = lc.get_peer_node (username)

    #join the group
    lc.join_group(node, group)

    #get communication channel
    channel = lc.get_channel(node,group)

    return channel

#sending and recieving messages

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg=get_message()
            channel.send(msg.encode('utf-8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf-8'))
    print("Finished")

#part 4 testing and debugging the chat application
    #test username
    print(get_username())

    #test group
    print(get_group())

    #test message
    print(get_message())

    #test initialize_chat
    chan = initialize_chat()
    print(type(chan))
