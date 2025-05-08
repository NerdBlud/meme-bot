import discord
from discord.ext import commands
import aiohttp
import random
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='meme ', intents=intents)

ANIME_ACTIONS = {
    "punch": {
        "searches": ["anime punch", "one punch man", "naruto punch"],
        "responses": [
            "{author} delivers a devastating punch to {target}! 💥",
            "KO! {author} knocked {target} into next week! 👊"
        ]
    },
    "slap": {
        "searches": ["anime slap", "tsundere slap", "angry anime slap"],
        "responses": [
            "{author} slapped {target} into next Tuesday! 👋",
            "The sound of {author}'s slap echoed through the chat! 🫲"
        ]
    },
    "kick": {
        "searches": ["anime kick", "roundhouse kick anime", "high kick anime"],
        "responses": [
            "{author} delivered a flying kick to {target}! 🦵",
            "{target} was yeeted by {author}'s powerful kick! 💨"
        ]
    },
    "headbutt": {
        "searches": ["anime headbutt", "fighting anime headbutt"],
        "responses": [
            "{author} gave {target} a crushing headbutt! 💢",
            "CLANG! {author} and {target} heads collided! 🤕"
        ]
    },
    "throw": {
        "searches": ["anime throw", "judo throw anime"],
        "responses": [
            "{author} judo-threw {target} across the room! 🥋",
            "Whoosh! {author} sent {target} flying! 🌪️"
        ]
    },
    
    # Romantic Actions
    "kiss": {
        "searches": ["anime kiss", "romantic anime kiss", "shoujo kiss"],
        "responses": [
            "{author} planted a sweet kiss on {target}! 💋",
            "Smooch! {author} x {target} OTP! 💞"
        ]
    },
    "hug": {
        "searches": ["anime hug", "wholesome anime hug", "anime comfort"],
        "responses": [
            "{author} gave {target} a warm hug! 🤗",
            "Group hug! {author} squeezed {target} tightly! 🫂"
        ]
    },
    "cuddle": {
        "searches": ["anime cuddle", "cute anime cuddle"],
        "responses": [
            "{author} snuggled up to {target}! 🥰",
            "So cozy! {author} is cuddling with {target}! 🛏️"
        ]
    },
    "handhold": {
        "searches": ["anime handholding", "romantic handholding"],
        "responses": [
            "{author} is holding hands with {target}! How lewd! 🫣",
            "Scandalous! {author} and {target} are holding hands! ✋"
        ]
    },
    "blush": {
        "searches": ["anime blush", "embarrassed anime"],
        "responses": [
            "{author} made {target} blush intensely! 😳",
            "So cute! {target} is blushing because of {author}! 🥺"
        ]
    },
    
    # Combat Actions
    "fight": {
        "searches": ["anime fight", "dbz fight", "demon slayer fight"],
        "responses": [
            "{author} challenged {target} to an epic duel! ⚔️",
            "Battle stations! {author} vs {target} begins! 🛡️"
        ]
    },
    "stab": {
        "searches": ["anime stab", "attack on titan stab", "dagger anime"],
        "responses": [
            "{author} betrayed {target} with a backstab! 🔪",
            "Critical hit! {target} didn't see that coming from {author}! 💢"
        ]
    },
    "shoot": {
        "searches": ["anime gun", "anime sniper", "anime pistol"],
        "responses": [
            "PEW PEW! {author} shot at {target}! 🔫",
            "BANG! {author} didn't miss {target}! 💥"
        ]
    },
    "dodge": {
        "searches": ["anime dodge", "matrix dodge anime"],
        "responses": [
            "{author} dodged {target}'s attack with style! 💨",
            "Matrix moves! {target} can't touch {author}! 🕴️"
        ]
    },
    "block": {
        "searches": ["anime block", "anime shield"],
        "responses": [
            "{author} blocked {target}'s attack perfectly! 🛡️",
            "CLANG! {author}'s defense stopped {target} cold! ⚔️"
        ]
    },
    
    # Playful Actions
    "poke": {
        "searches": ["anime poke", "cute anime poke"],
        "responses": [
            "{author} poked {target} repeatedly! 👉",
            "Boop! {author} couldn't resist poking {target}! 👆"
        ]
    },
    "tease": {
        "searches": ["anime tease", "playful anime"],
        "responses": [
            "{author} teased {target} mercilessly! 😏",
            "{target} fell for {author}'s playful teasing! 🎣"
        ]
    },
    "wink": {
        "searches": ["anime wink", "seductive anime wink"],
        "responses": [
            "{author} winked at {target} suggestively! 😉",
            "Did {author} just wink at {target}? How scandalous! 🫦"
        ]
    },
    "highfive": {
        "searches": ["anime high five", "anime celebration"],
        "responses": [
            "{author} and {target} shared an epic high five! ✋",
            "Slap! Perfect high five between {author} and {target}! 🖐️"
        ]
    },
    "boop": {
        "searches": ["anime nose boop", "cute anime touch"],
        "responses": [
            "{author} booped {target}'s nose! 👆",
            "Boop! {author} touched {target}'s nose gently! 👃"
        ]
    },
    
    # Emotional Actions
    "cry": {
        "searches": ["anime cry", "sad anime moment"],
        "responses": [
            "{author} made {target} cry! 😭",
            "The waterworks won't stop! {target} is bawling because of {author}! 💧"
        ]
    },
    "laugh": {
        "searches": ["anime laugh", "villain laugh"],
        "responses": [
            "{author} laughed at {target}'s misfortune! 😆",
            "ROFL! {target} got roasted by {author}'s laughter! 🤣"
        ]
    },
    "panic": {
        "searches": ["anime panic", "anime shock"],
        "responses": [
            "{author} made {target} panic! 😱",
            "Emergency! {target} is freaking out because of {author}! 🆘"
        ]
    },
    "smug": {
        "searches": ["anime smug", "smug anime face"],
        "responses": [
            "{author} gave {target} a smug look! 😏",
            "That face! {author} is way too smug at {target}! 😼"
        ]
    },
    "facepalm": {
        "searches": ["anime facepalm", "disappointed anime"],
        "responses": [
            "{author} facepalmed at {target}'s stupidity! 🤦",
            "*SMACK* That sound was {author} facepalming because of {target}! ✋"
        ]
    },
    
    # Special Actions
    "yeet": {
        "searches": ["anime throw", "anime kick"],
        "responses": [
            "{author} yeeted {target} into the stratosphere! 🚀",
            "YEET! {target} went flying thanks to {author}! ✨"
        ]
    },
    "glomp": {
        "searches": ["anime tackle hug", "anime flying hug"],
        "responses": [
            "{author} glomped {target} with full force! 🏃‍♂️💨",
            "Tackle hug! {target} was overwhelmed by {author}! 🤼"
        ]
    },
    "protect": {
        "searches": ["anime shield", "anime defend"],
        "responses": [
            "{author} heroically protected {target}! 🛡️",
            "Shield activated! {author} has {target}'s back! ✨"
        ]
    },
    "betray": {
        "searches": ["anime betrayal", "traitor anime"],
        "responses": [
            "{author} betrayed {target} in cold blood! 😈",
            "Plot twist! {author} was the villain all along! 🎭"
        ]
    },
    "celebrate": {
        "searches": ["anime celebration", "anime party"],
        "responses": [
            "{author} celebrated with {target}! 🎉",
            "Party time! {author} and {target} are having fun! 🥳"
        ]
    }
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()
    print('Slash commands registered!')

for action in ANIME_ACTIONS.keys():
    @bot.tree.command(name=action, description=f"{action} a user with anime GIFs")
    async def slash_action(interaction: discord.Interaction, user: discord.User):
        action = interaction.command.name
        await send_anime_action(interaction, action, user)

for action in ANIME_ACTIONS.keys():
    @bot.command(name=action)
    async def prefix_action(ctx, user: discord.User):
        action = ctx.command.name
        await send_anime_action(ctx, action, user)

@bot.tree.command(name="help", description="Show all available commands")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Meme Help",
        description="All available anime actions (use with @user):",
        color=0x00FF00
    )
    
    categories = {
        "Physical": ["punch", "slap", "kick", "headbutt", "throw"],
        "Romantic": ["kiss", "hug", "cuddle", "handhold", "blush"],
        "Combat": ["fight", "stab", "shoot", "dodge", "block"],
        "Playful": ["poke", "tease", "wink", "highfive", "boop"],
        "Emotional": ["cry", "laugh", "panic", "smug", "facepalm"],
        "Special": ["yeet", "glomp", "protect", "betray", "celebrate"]
    }
    
    for category, actions in categories.items():
        value = "\n".join([f"`/{action}`" for action in actions])
        embed.add_field(name=category, value=value, inline=True)
    
    embed.add_field(
        name="Other Commands",
        value="`/meme-search [term]` - Find anime memes\n`meme [action] @user` - Prefix commands",
        inline=False
    )
    
    embed.set_footer(text="Use prefix 'meme' or slash commands!")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="meme-search", description="Search for anime memes")
async def meme_search(interaction: discord.Interaction, term: str):
    try:
        async with aiohttp.ClientSession() as session:
            params = {
                "api_key": os.getenv("GIPHY_API_KEY", "dc6zaTOxFJmzC"),
                "q": f"anime {term}",
                "limit": 5,
                "rating": "pg-13"
            }
            async with session.get("https://api.giphy.com/v1/gifs/search", params=params) as resp:
                data = await resp.json()
                gifs = data["data"]
                
                if not gifs:
                    await interaction.response.send_message("No memes found for that term! 😢")
                    return
                
                gif = random.choice(gifs)
                embed = discord.Embed(
                    title=f"Anime Meme: {term}",
                    color=0x7289DA
                )
                embed.set_image(url=gif["images"]["original"]["url"])
                embed.set_footer(text="Powered by GIPHY")
                
                await interaction.response.send_message(embed=embed)
    except Exception as e:
        print("Meme search error:", e)
        await interaction.response.send_message("Failed to search for memes. Try again later!")
        
async def send_anime_action(context, action, target_user):
    try:
        config = ANIME_ACTIONS[action]
        search_term = random.choice(config["searches"])
        response_text = random.choice(config["responses"]).format(
            author=context.user.display_name,
            target=target_user.display_name
        )

        async with aiohttp.ClientSession() as session:
            params = {
                "api_key": os.getenv("GIPHY_API_KEY", "dc6zaTOxFJmzC"),
                "s": search_term,
                "rating": "pg-13"
            }
            async with session.get("https://api.giphy.com/v1/gifs/translate", params=params) as resp:
                data = await resp.json()
                gif_url = data["data"]["images"]["original"]["url"]

        embed = discord.Embed(
            description=response_text,
            color=0xFF9ED2
        )
        embed.set_image(url=gif_url)
        embed.set_footer(text="Powered by GIPHY | Meme")

        if isinstance(context, discord.Interaction):
            await context.response.send_message(embed=embed)
        else:
            await context.send(embed=embed)

    except Exception as e:
        print(f"Error with {action} command:", e)
        error_msg = "⚠️ Failed to find the perfect anime moment! Try again later."
        if isinstance(context, discord.Interaction):
            await context.response.send_message(error_msg, ephemeral=True)
        else:
            await context.send(error_msg)

bot.run(os.getenv("DISCORD_TOKEN"))