import collections
import os
import time

from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()


# speech = LiveSpeech(
#     verbose=False,
#     sampling_rate=16000,
#     buffer_size=2048,
#     no_search=False,
#     full_utt=False,
#     hmm=os.path.join(model_path, 'en-us/en-us'),
#     lm=os.path.join(model_path, 'en-us/en-us.lm.bin'),
#     dic=os.path.join(model_path, 'en-us/cmudict-en-us.dict')
# )
# for phrase in speech:
#     print("phrase:", phrase)
#     print(phrase.segments(detailed=True))
#     print("phrase:", phrase)
#     # 只要命中上述关键词的内容，都算对
#     if "mo" in str(phrase):
#         print("正确识别唤醒词")

class RingBuffer(object):
    """Ring buffer to hold audio from PortAudio"""

    def __init__(self, size=4096):
        self._buf = collections.deque(maxlen=size)

    def extend(self, data):
        """Adds data to the end of buffer"""
        self._buf.extend(data)

    def get(self):
        """Retrieves data from the beginning of buffer and clears it"""
        tmp = bytes(bytearray(self._buf))
        self._buf.clear()
        return tmp


ring_buffer = RingBuffer(
    2 * 16000 * 5
)
while True:

    data = ring_buffer.get()
    print(len(data))

    if len(data) == 0:
        time.sleep(0.03)
        continue
