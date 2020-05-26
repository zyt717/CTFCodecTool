# coding=utf8
import base64
import urllib.parse as urlparse
import codecs
import hashlib
from .codecfunctions import *

# src为bytes,返回值可为str或 bytes，key_x为str

ctfcodecs = [
    ##encode&decode
    {'text': 'Base16',
     'category': 'encode',
     'func': lambda src, key_a, key_b, key_c, key_d: base64.b16encode(src)
     },
    {'text': 'Base16',
     'category': 'decode',
     'func': lambda src, key_a, key_b, key_c, key_d: base64.b16decode(src)
     },

    {'text': 'Base32',
     'category': 'encode',
     'func': lambda src, key_a, key_b, key_c, key_d: base64.b32encode(src)
     },
    {'text': 'Base32',
     'category': 'decode',
     'func': lambda src, key_a, key_b, key_c, key_d: base64.b32decode(src)
     },

    {'text': 'Base64',
     'category': 'encode',
     'func': lambda src, key_a, key_b, key_c, key_d: base64.b64encode(src)
     },
    {'text': 'Base64',
     'category': 'decode',
     'func': lambda src, key_a, key_b, key_c, key_d: base64.b64decode(src)
     },

    {'text': 'UTF8->URL',
     'category': 'encode',
     'func': lambda src, key_a, key_b, key_c, key_d: urlparse.quote(src.decode())
     },
    {'text': 'URL->UTF8',
     'category': 'decode',
     'func': lambda src, key_a, key_b, key_c, key_d: urlparse.unquote(src.decode())
     },

    {'text': '2312-URL',
     'category': 'encode',
     'func': lambda src, key_a, key_b, key_c, key_d: urlparse.quote(src.decode().encode('gb2312'))
     },
    {'text': 'URL-2312',
     'category': 'decode',
     'func': lambda src, key_a, key_b, key_c, key_d: urlparse.unquote(src.decode(), encoding='gb2312')
     },

    {'text': 'Unicode',
     'category': 'encode',
     'func': lambda src, key_a, key_b, key_c, key_d: src.decode().encode('unicode_escape')
     },
    {'text': 'Unicode',
     'category': 'decode',
     'func': lambda src, key_a, key_b, key_c, key_d: src.decode('unicode_escape')
     },

    {'text': 'ASCII',
     'category': 'encode',
     'func': lambda src, key_a, key_b, key_c, key_d: ' '.join(str(x) for x in src)
     },
    {'text': 'ASCII',
     'category': 'decode',
     'func': lambda src, key_a, key_b, key_c, key_d: ''.join([chr(int(x)) for x in src.decode().split(' ')])
     },

    {'text': 'Hex',
     'category': 'encode',
     'tooltip': '自定义前缀填在参数1中',
     'func': lambda src, key_a, key_b, key_c, key_d: key_a + src.hex()
     },
    {'text': 'Hex',
     'category': 'decode',
     'tooltip': '自定义前缀填在参数1中',
     'func': lambda src, key_a, key_b, key_c, key_d: bytes.fromhex(src.decode().replace(key_a, ''))
     },

    {'text': 'Qwerty',
     'category': 'encode',
     'func': lambda src, key_a, key_b, key_c, key_d: src.translate(
         bytes.maketrans(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                         b'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
     },
    {'text': 'Qwerty',
     'category': 'decode',
     'func': lambda src, key_a, key_b, key_c, key_d: src.translate(
         bytes.maketrans(b'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM',
                         b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
     },

    {'text': 'Translate',
     'category': 'encode',
     'tooltip': 'pyhon string的translate，根据参数1与参数2给出的字符映射转换表转换字符串中的字符',
     'func': lambda src, key_a, key_b, key_c, key_d: src.translate(
         bytes.maketrans(key_a.encode(), key_b.encode()))
     },
    # encrypt&decrypt
    {'text': 'Rot13',
     'category': 'encrypt',
     'func': lambda src, key_a, key_b, key_c, key_d: codecs.encode(src.decode(), 'rot_13')
     },
    {'text': 'Rot13',
     'category': 'decrypt',
     'func': lambda src, key_a, key_b, key_c, key_d: codecs.encode(src.decode(), 'rot_13')
     },

    {'text': '凯撒密码',
     'category': 'encrypt',
     'tooltip': '参数1：偏移量，为空则爆破',
     'func': lambda src, key_a, key_b, key_c, key_d: caesar(src, key_a, True)
     },
    {'text': '凯撒密码',
     'tooltip': '参数1：偏移量，为空则爆破',
     'category': 'decrypt',
     'func': lambda src, key_a, key_b, key_c, key_d: caesar(src, key_a, False)
     },

    {'text': '栅栏密码',
     'category': 'encrypt',
     'tooltip': '参数1：栅栏数',
     'func': lambda src, key_a, key_b, key_c, key_d: railfence_encrypt(src.decode(), int(key_a))
     },
    {'text': '栅栏密码',
     'tooltip': '参数1：栅栏数',
     'category': 'decrypt',
     'func': lambda src, key_a, key_b, key_c, key_d: railfence_decrypt(src, key_a)
     },

    {'text': '培根密码',
     'category': 'encrypt',
     'func': lambda src, key_a, key_b, key_c, key_d: bacon_encrypt(src.decode())
     },
    {'text': '培根密码',
     'category': 'decrypt',
     'func': lambda src, key_a, key_b, key_c, key_d: bacon_decrypt(src.decode())
     },

    {'text': '摩斯密码',
     'category': 'encrypt',
     'func': lambda src, key_a, key_b, key_c, key_d: morse(src, True)
     },
    {'text': '摩斯密码',
     'category': 'decrypt',
     'tooltip': '解码摩斯码，以空格分隔',
     'func': lambda src, key_a, key_b, key_c, key_d: morse(src, False)
     },

    {'text': '云影密码',
     'category': 'encrypt',
     'tooltip': '有1，2，4，8这四个数字，可以通过加法来用这四个数字表示0-9中的任何一个数字，列如0=28， 也就是0=2+8，同理7=124， 9=18。这样之后再用1-26来表示26个英文字母，就有了密文与明文之间的对应关系。引入0来作为间隔，以免出现混乱。所以云影密码又叫“01248密码”',
     'func': lambda src, key_a, key_b, key_c, key_d: yunying(src, True)
     },
    {'text': '云影密码',
     'category': 'decrypt',
     'tooltip': '有1，2，4，8这四个数字，可以通过加法来用这四个数字表示0-9中的任何一个数字，列如0=28， 也就是0=2+8，同理7=124， 9=18。这样之后再用1-26来表示26个英文字母，就有了密文与明文之间的对应关系。引入0来作为间隔，以免出现混乱。所以云影密码又叫“01248密码”',
     'func': lambda src, key_a, key_b, key_c, key_d: yunying(src, False)
     },

    {'text': '当铺密码',
     'category': 'encrypt',
     'tooltip': '当铺密码就是一种将中文和数字进行转化的密码，算法相当简单:当前汉字有多少笔画出头，就是转化成数字几。',
     'func': lambda src, key_a, key_b, key_c, key_d: dangpu(src, True)
     },
    {'text': '当铺密码',
     'category': 'decrypt',
     'tooltip': '当铺密码就是一种将中文和数字进行转化的密码，算法相当简单:当前汉字有多少笔画出头，就是转化成数字几。',
     'func': lambda src, key_a, key_b, key_c, key_d: dangpu(src, False)
     },

    {'text': 'MD5',
     'category': 'hash',
     'func': lambda src, key_a, key_b, key_c, key_d: hashlib.md5(src).hexdigest()
     },
    {'text': 'SHA1',
     'category': 'hash',
     'func': lambda src, key_a, key_b, key_c, key_d: hashlib.sha1(src).hexdigest()
     },
    {'text': 'SHA256',
     'category': 'hash',
     'func': lambda src, key_a, key_b, key_c, key_d: hashlib.sha256(src).hexdigest()
     },
]
