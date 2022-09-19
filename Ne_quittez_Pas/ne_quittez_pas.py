import base64
from scapy.all import *
import g711
import functools
import scipy.io.wavfile

CAP = rdpcap("capture.pcapng")

#G.711 codec: Used for uncompressed digital voice. Audio quality is better than other codecs, but it uses more bandwidth.
# G.729 codec: ...

##
#QRY = b''.join([pkt[IP].seq.to_bytes(4, 'big') for pkt in CAP if UDP in pkt IP in pkt and pkt[IP].src == '192.168.73.252'])
l = [pkt[UDP].load for pkt in CAP if UDP in pkt and IP in pkt and pkt[IP].src == '192.168.73.252'][4:-1]
data = functools.reduce(lambda a,b : a + b, l)
#print(base64.b64decode(QRY).decode())
res = g711.decode_alaw(data)
scipy.io.wavfile.write("audio_marchepas.wav", 8000, res)
