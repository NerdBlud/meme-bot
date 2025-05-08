
**🤖  GIF Reaction Bot**

A fun open-source Discord bot for GIF reactions and meme searches – perfect for anime lovers!

**🌟 Features**
- 30+ anime actions (punch, kiss, yeet, etc.)
- Dual command system: Slash + Prefix
- Meme search powered by Giphy
- Zero-cost to run (free APIs)
- No database required

**⚙️ Setup Guide**

__**Prerequisites:**__
- Python 3.8+
- Discord bot token: https://discord.com/developers/applications
- Giphy API key (optional, defaults to public beta key)

__**Installation:**__
1. Clone the repo:
```bash
git clone https://github.com/nerdblud/meme-bot.git
cd meme-bot

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file:
```env
DISCORD_TOKEN=your_bot_token_here
# Optional: (if it does not work without a giphy key use your own.)
GIPHY_API_KEY=your_giphy_key
```

4. Run the bot:
```bash
python bot.py
```

---

**🎮 Command List**

__**Anime Actions**__  
(Use: `/command @user` or `meme command @user`)

**Physical:** punch, slap, kick, headbutt, throw  
**Romantic:** kiss, hug, cuddle, handhold, blush  
**Combat:** fight, stab, shoot, dodge, block  
**Playful:** poke, tease, wink, highfive, boop  
**Emotional:** cry, laugh, panic, smug, facepalm  
**Special:** yeet, glomp, protect, betray, celebrate

__**Utility Commands**__
- `/help` → Show all commands  
- `/meme-search` → Search anime memes (e.g. `/meme-search "anime smug"`)

---

**🖼️ Examples**

`/punch @User` → Sends anime punch GIF  
`/meme-search "anime laugh"` → Fetches anime laugh meme

---

**❤️ Support**

- Found a bug? Got a feature idea?  
  → Open an Issue on GitHub  
  → Or join our Support Server (link optional)

---

**📜 License**

MIT License – free to use and modify.  
Note: Uses the Giphy API. Subject to Giphy’s Terms of Service.
```
