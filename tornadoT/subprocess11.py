import subprocess
import os

tmpfile = "C:\\Users\\k\\Desktop\\tmpjhibz_jc.wav"
nfile = "C:\\Users\\k\\Desktop\\tmpjhibz_jc16.wav"
soxCall = "sox " + tmpfile + " " + nfile + " rate 16k"
# soxCall = soxCall.replace("\\", "/")
print(soxCall)
# subprocess.call([soxCall.decode('gbk')], shell=True)
# subprocess.call(["sox" + tmpfile + nfile + " rate 16k"], shell=True)
# cmd = "cmd.exe D:\code\python\wukong-robot\temp\f71ad814cf304c86550c4c0873025f0f.mp3"
# os.system(soxCall)
#
# subprocess.Popen(
#             cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
#         )
subprocess.call(soxCall, shell=True)
print(["sox", tmpfile, nfile])
# subprocess.call(["copy", tmpfile, nfile], shell=True)

# print("sox", tmpfile, nfile, "rate 16k")
# C:\Users\k\Desktop\tmpjhibz_jc.wav
# C:\Users\k\Desktop\tmpjhibz_jc16.wav
# sox -r 16k C:\Users\k\Desktop\tmpjhibz_jc.wav C:\Users\k\Desktop\tmpjhibz_jc16.wav
