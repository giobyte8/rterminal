import bcrypt
import rterminal.utils.config as cfg


def checkpw(raw_pass: str) -> bool:
    pass_bytes = bytes(raw_pass, 'utf-8')
    hash_bytes = bytes(cfg.bot_auth_hash(), 'utf-8')

    return bcrypt.checkpw(pass_bytes, hash_bytes)