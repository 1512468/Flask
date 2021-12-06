from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetParticipantsRequest
import asyncio

# Use your own values from my.telegram.org
api_id = 11381819
api_hash = '02dfb47c93017dba36b0c5139c7eff5d'

channel_to_name = 'TestMXZ'
channel_from_name = 'test_add'
loop = asyncio.get_event_loop()


client = TelegramClient('anon', api_id, api_hash)
loop.run_until_complete(client.connect())
channel_from = loop.run_until_complete(client.get_entity(channel_from_name))
channel_to = loop.run_until_complete(client.get_entity(channel_to_name))
users = client.iter_participants(channel_from)
users_arr = []
for user in users:
    users_arr.append(user)
    loop.run_until_complete(client(InviteToChannelRequest(
        channel_to,
        users_arr
    )))


for user in users:
    n += 1
    if n % 50 == 0:
    try:
        print("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("Waiting for 60-180 Seconds...")
        time.sleep(random.randrange(60, 180))
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print("Unexpected Error")
        continue
