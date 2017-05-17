import hashlib

bytes_str = bytes('str стр', 'utf-8')
print(str(bytes_str, 'utf-8'))

bytes_arr = bytes([65, 65])
print(str(bytes_arr, 'utf-8'))
print(bytes_arr.decode(encoding='utf-8'))

k = bytes_str.decode('utf-8').encode('koi8-r')
print(str(k, 'koi8-r'))

hex_pass = hashlib.md5(b'password')
pass_enc = hex_pass.hexdigest()

