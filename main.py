import discord
import os
import random

client = discord.Client()

greetings = ["Hi", "hi", "greetings", "Greetings", "Hello", "hello"]
ness_greetings = [
    "Hello there",
    "hi",
    "greetings",
    "hello",
]

@client.event
async def on_ready():
	print('oh shit thats epic i exist'.format(client))

@client.event
async def on_message(message):
    if 'b' in message.content:
        await message.edit(content = ":b:")


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("b"):
	  await message.channel.send(":b:ess")
	if message.content.startswith("sness"):
	  await message.channel.send("**AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA**")
	if "PPdev is a girl" in message.content:
	  await message.channel.send("waitiycbiyc ic ikg cikewgu whatwiuctweict wiluct liucy ilewudy ;woixy ow7 evdp8934y p9ry 3p98fweoC8HYE]  ef8y [;o*efgt :CGTF ;gtf ;pTF O0FY6  0F7QY 0W9Y0W9Yhcfkjgdlikwjc dk yi fe n8NPaj,Nqanq;OW'MIqvayoBNBYQBMTGINLs vijkV DUOO USLSb?qd/bhszbU:O*U:qipjlmqijac")
	if "proud of you" in message.content:
	  await message.channel.send("Thanks! I really appreciate that!")
	if message.content.startswith("ness"):
		await message.channel.send(
		    'ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness nessness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness nessness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness nessness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness'
		)

	if message.content.startswith("Ness"):
		await message.channel.send(
		    'ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness nessness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness nessness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness nessness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness ness')
		    
	if any(word in message.content for word in greetings) and "ness":
		await message.channel.send(random.choice(ness_greetings))



client.run(os.getenv('the_pass'))

my_secret = os.environ['the_pass']

my_secret = os.environ['the_pass']

my_secret = os.environ['the_pass']
