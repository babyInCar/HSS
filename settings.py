TORTOISE_ORM = {
        "connections": {
            'default': {
                'engine': 'tortoise.backends.mysql',
                'credentials': {
                    'host': '127.0.0.1',
                    'port': '3306',
                    'user': 'root',
                    'password': 'Test1234',
                    'database': 'fastapi',
                    'minsize': 1,
                    'maxsize': 5,
                    'charset': 'utf8mb4',
                    'echo': True
                }
            }
        },
        'db': {
            'models': {
                'models': ['db.models'],
            }
        },
        'apps': {
            'models': {
                'models': ['db.models', "aerich.models"],
                'default_connection': 'default',
            }
        },
        'use_tz': False,
        'timezone': 'Asia/Shanghai'
    }

CHANNEL_MAP = {
    1: '京东',
    2: '淘宝',
    3: '支付宝',
    4: '小程序',
    5: '抖音',
    6: '拼多多'
}

