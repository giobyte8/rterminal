import aioredis
import rterminal.utils.config as cfg


redis = aioredis.from_url(
    f'redis://{ cfg.redis_host() }:{ cfg.redis_port() }'
)
