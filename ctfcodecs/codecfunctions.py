# coding=utf8
import re
import random

ascii_lower = b'abcdefghijklmnopqrstuvwxyz'
ascii_upper = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


###解密函数约定key_a为空则爆破，解密结果必须为str

def caesar(src, key_a, isencrypt):
    '''凯撒密码'''

    def _kaisa(text, shift):
        table = bytes.maketrans(ascii_lower + ascii_upper,
                                ascii_lower[shift:] + ascii_lower[:shift] + ascii_upper[shift:] + ascii_upper[:shift])
        return text.translate(table)

    try:
        if key_a:
            shift = int(key_a) % 26
            return _kaisa(src, shift) if isencrypt else _kaisa(src, 26 - shift)
        else:
            result = b''
            for i in range(26):
                tmpresult = _kaisa(src, i) if isencrypt else _kaisa(src, 26 - i)
                result += str(i).encode() + b':' + tmpresult + b'\n'
            return result.decode()
    except:
        return '请在参数1输入正确的偏移量'


def railfence_encrypt(s, n):
    '''栅栏密码'''
    fence = [[] for _ in range(n)]
    rail = 0
    var = 1

    for char in s:
        fence[rail].append(char)
        rail += var

        if rail == n - 1 or rail == 0:
            var = -var

    res = ''
    for i in fence:
        for j in i:
            res += j

    return res


def railfence_decrypt(src, key_a):
    def _zhalan_decrypt(s, n):
        '''栅栏密码'''
        if n == 1:
            return s
        fence = [[] for _ in range(n)]
        rail = 0
        var = 1

        for char in s:
            fence[rail].append(char)
            rail += var

            if rail == n - 1 or rail == 0:
                var = -var

        rFence = [[] for _ in range(n)]
        i = 0
        l = len(s)
        s = list(s)
        for r in fence:
            for j in range(len(r)):
                rFence[i].append(s[0])
                s.remove(s[0])
            i += 1
        rail = 0
        var = 1
        r = ''
        for i in range(l):
            r += rFence[rail][0]
            rFence[rail].remove(rFence[rail][0])
            rail += var

            if rail == n - 1 or rail == 0:
                var = -var
        return r

    if key_a:
        return _zhalan_decrypt(src.decode(), int(key_a))
    else:
        result = ''
        for i in range(1, len(src) + 1):
            tmpresult = _zhalan_decrypt(src.decode(), i)
            result += str(i) + ':' + tmpresult + '\n'
        return result


def generate_bacon_dict():
    """
    Create Bacon dictionary.
    a   AAAAA   g     AABBA   n    ABBAA   t     BAABA
    b   AAAAB   h     AABBB   o    ABBAB   u-v   BAABB
    c   AAABA   i-j   ABAAA   p    ABBBA   w     BABAA
    d   AAABB   k     ABAAB   q    ABBBB   x     BABAB
    e   AABAA   l     ABABA   r    BAAAA   y     BABBA
    f   AABAB   m     ABABB   s    BAAAB   z     BABBB
    :return: Bacon dict
    """

    bacon_dict = {}

    for i in range(0, 26):
        tmp = bin(i)[2:].zfill(5)
        tmp = tmp.replace('0', 'a')
        tmp = tmp.replace('1', 'b')
        bacon_dict[tmp] = chr(65 + i)

    return bacon_dict


def bacon_encrypt(words):
    """
    Encrypt text to Bacon's cipher.
    :param words: string to encrypt
    :param bacon_dict: Bacon dict
    :return: encrypted string
    """
    bacon_dict = generate_bacon_dict()
    cipher = ''
    bacon_dict = {v: k for k, v in bacon_dict.items()}  # hack to get key from value - reverse dict
    words = words.upper()
    words = re.sub(r'[^A-Z]+', '', words)

    for i in words:
        cipher += bacon_dict.get(i).upper()
    return cipher


def bacon_decrypt(words):
    """
    Decrypt Bacon's cipher to text.
    :param words: string to decrypt
    :param bacon_dict: Bacon dict
    :return: decrypted string
    """
    bacon_dict = generate_bacon_dict()
    cipher = ''
    words = words.lower()
    words = re.sub(r'[^ab]+', '', words)

    for i in range(0, int(len(words) / 5)):
        cipher += bacon_dict.get(words[i * 5:i * 5 + 5], ' ')
    return cipher


def morse(src, isEncrypt):
    morseList = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
        "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
        "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",
        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

        ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
        "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
        "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
        ".-...": "&", ".--.-.": "@", ".-.-.": "+",
    }
    text = src.decode()
    if isEncrypt:
        inv_morseList = {v: k for k, v in morseList.items()}
        text = text.upper()
        return ' '.join([inv_morseList.get(c) if inv_morseList.get(c) else '(' + c + '?)' for c in text])
    else:
        return ''.join([morseList.get(c) if morseList.get(c) else '(' + c + '?)' for c in text.split(' ') if c])


def yunying(src, isEncrypt):
    yunyingList = {'A': '1', 'B': '2', 'C': '21', 'D': '4',
                   'E': '41', 'F': '42', 'G': '421', 'H': '8',
                   'I': '81', 'J': '82', 'K': '821', 'L': '84',
                   'M': '841', 'N': '842', 'O': '8421', 'P': '88',
                   'Q': '881', 'R': '882', 'S': '8821', 'T': '884',
                   'U': '8841', 'V': '8842', 'W': '88421', 'X': '888',
                   'Y': '8881', 'Z': '8882'}
    text = src.decode()
    if isEncrypt:
        text = text.upper()
        return '0'.join([yunyingList.get(c) if yunyingList.get(c) else '(' + c + '?)' for c in text])
    else:
        inv_yunyingList = {v: k for k, v in yunyingList.items()}
        return ''.join(
            [inv_yunyingList.get(c) if inv_yunyingList.get(c) else '(' + c + '?)' for c in text.split('0') if c])


def dangpu(src, isEncrypt):
    dangpuList = {'田': '0', '由': '1', '中': '2', '人': '3', '工': '4',
                  '大': '5', '王': '6', '夫': '7', '井': '8', '羊': '9'}
    text = src.decode()
    if isEncrypt:
        inv_dangpuList = {v: k for k, v in dangpuList.items()}
        return ''.join([inv_dangpuList.get(c) if inv_dangpuList.get(c) else '(' + c + '?)' for c in text])
    else:
        return ''.join([dangpuList.get(c) if dangpuList.get(c) else '(' + c + '?)' for c in text])
