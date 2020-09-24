file_path = './../InOutData.csv'
file = open(file_path, 'r')
data = file.read().split('\n')
for i in range(len(data)):
    data[i] = data[i].split(',')
data.pop(0)
data.pop(-1)
file.close()
result = 'Name,Entry Time,Exit Time, Duration\n'
seperate1 = ''
seperate2 = ''
for i in data:
    if not(i[0].isnumeric()):
        if i[1] == '':
            seperate1 += i[0] + ',-----,-----,-----\n'
        else:
            t = i[1].split()
            if len(t) == 1:
                seperate2 += '{},{},-----,-----\n'.format(i[0], t[0])
            else:
                ff = t[0].split(':')
                f00 = int(ff[0])
                f01 = int(ff[1])
                ss = t[-1].split(':')
                s00 = int(ss[0])
                s01 = int(ss[1])
                t2 = (s00 * 60) + s01
                t1 = (f00 * 60) + f01
                dt = t2 - t1
                c = 0
                while dt >= 60:
                    dt = dt - 60
                    c = c + 1
                d = str(c) + ':' + str(dt)
                result += '{},{},{},{}\n'.format(i[0], t[0], t[-1], d)
# code misfunctions if only 1 employee exists or no one attends
result += seperate2
result += seperate1
x = input('Output File Name: ')
file = open('./../attendance history/'+x+'.csv', 'w')
file.write(result)
file.close()
input('Done, Press Enter To Open The File')
# credits goes to Mostafa Belal and Youssif Gamal
