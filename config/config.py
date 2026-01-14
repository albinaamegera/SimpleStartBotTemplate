from environs import Env
from dataclasses import dataclass

@dataclass
class BotSettings:
    token: str
    admins: list[int]

@dataclass()
class Config:
    bot: BotSettings

def get_config() -> Config:
    env = Env()
    env.read_env()

    bot = BotSettings(
        token=env.str("BOT_TOKEN"),
        admins=env.list("ADMIN_IDS"),
    )

    return Config(
        bot=bot,
    )

