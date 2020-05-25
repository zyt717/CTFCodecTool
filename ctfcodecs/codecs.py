# coding=utf8
import base64
import urllib.parse as urlparse

# src为bytes,返回值可为str或 bytes，key_x为str

codecs = [
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
]
