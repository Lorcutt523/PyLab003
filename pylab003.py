from lab_chat import get_peer_node


def get_input(message):
    inp = input(message)
    inp.strip()
    inp.upper()
    return inp

def get_username():
    return get_input("Enter username")

print(get_username())

def get_group():
    return get_input("Enter a group")

def get_message(username):
    inp = input(f"{username}Enter your message")
    inp = inp.strip()
    return inp

#user = get_username()
#print(get_group())
#print(get_message(user))
import lab_chat as lc

def initialize_chat():
    username = get_username()
    group = get_group()
    node = lc.get_peer_node(username)
    lc.join_group(node, group)
    channel = lc.get_channel(node,group)
    return channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message("Luke")
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")


    #print(type(initialize_chat()))
start_chat()