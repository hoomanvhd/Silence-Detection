import csv
from pydub import AudioSegment, silence
import glob
import os

myAudio = AudioSegment.from_wav("/home/hoomanvhd/Desktop/DATASET/Video2-done/video2.wav")

silence = silence.detect_nonsilent(myAudio, min_silence_len=1000, silence_thresh=-50)

silence = [((start/1000), (stop/1000)) for start, stop in silence]

for each in silence:
    print(each)

# 
# cnt = 0
#
#
# StartTime = []
# StopTime = []
#
# for time in silence:
#     for startANDstop in time:
#         if cnt%2 == 0:
#             StartTime.append(int(startANDstop))
#         else:
#             StopTime.append(int(startANDstop))
#
#         cnt += 1
#
#
# length = len(StopTime)-1
# csvList = []
#
# with open("/home/hoomanvhd/Desktop/DATASET/Video2-done/video2.en.srt-SubTitleCSV.csv", "r") as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         csvList.append(row)
#
# list1 =[]
# count = 1
#
# for row4 in csvList:
#     colStopTime3 = int(row4[2])
#     if colStopTime3 < StopTime[0]:
#         list1.append(row4[3])
#     else:
#         break
# with open("/home/hoomanvhd/Desktop/DATASET/Video2-done/VideoTextReadByLineSilent/" + str(count) + ".txt", "w") as wr1File:
#     for line in list1:
#         wr1File.write(line + " ")
#
# for i in range(length):
#     a = StopTime[i]
#     b = StopTime[i+1]
#     count += 1
#     list2 = []
#     for row2 in csvList:
#         colStopTime = int(row2[2])
#         if colStopTime >= a and colStopTime < b:
#             list2.append(row2[3])
#     with open("/home/hoomanvhd/Desktop/DATASET/Video2-done/VideoTextReadByLineSilent/" + str(count) + ".txt", "w") as wr2File:
#         for line in list2:
#             wr2File.write(line + " ")
#
#
# path = ("/home/hoomanvhd/Desktop/DATASET/Video2-done/VideoTextReadByLineSilent/*.txt")
#
# for H in sorted(glob.glob(path)):
#     with open(H, "r") as file:
#         read = file.read()
#         if read == "":
#             os.remove(H)
#














