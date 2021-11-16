from .user_agents import *
import random,time
ug = random.choice(user_agent)

header={
"Host": "api.internal.temp-mail.io",
"Connection": "keep-alive",

"User-Agent": ug,
"Accept": "application/json, text/plain, */*",
"Application-Version": "2.2.14",
"Save-Data": "on",
"Application-Name": "web",
"Origin": "https://temp-mail.io",
"Referer": "https://temp-mail.io/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,bn;q=0.8",}
headergit={
"Host": "raw.githubusercontent.com",
"Connection": "keep-alive",

"Upgrade-Insecure-Requests": "1",
"User-Agent": ug,
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,bn;q=0.8"
}