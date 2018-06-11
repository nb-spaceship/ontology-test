import base58

encodes = base58.b58encode('02802683d48aa9b34f9a0e91f5e27fedc8ac6486b1')

print(encodes)

print(base58.b58decode(encodes))
#base58.b58encode_check(b'hello world')

#base58.b58decode_check(b'3vQB7B6MrGQZaxCuFg4oh')
#base58.b58decode_check(b'4vQB7B6MrGQZaxCuFg4oh')