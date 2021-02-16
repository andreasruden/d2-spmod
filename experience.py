import csv

out = ''
cnt = 0
multiplier = 0.5

def writeLine(line):
    global out
    out += '\t'.join(str(w) for w in line) + '\n' # automatically becomes \r\n on windows

print('multiplier at %.2f%% starting at level 1.' % multiplier)
with open("D:\Diablo2Modding\my_edited_excels\Experience.txt") as xp:
    for line in csv.reader(xp, delimiter='\t'):
        cnt += 1
        if cnt >= 4:
            level = int(line[0])
            if level > 70 and multiplier < 0.65:
                multiplier = 0.65
                print('multiplier at %.2f%% starting at level %d.' % (multiplier, level))
            elif level > 50 and multiplier < 0.6:
                multiplier = 0.6
                print('multiplier at %.2f%% starting at level %d.' % (multiplier, level))
            elif level > 30 and multiplier < 0.55:
                multiplier = 0.55
                print('multiplier at %.2f%% starting at level %d.' % (multiplier, level))
            line[1] = int(int(line[1]) * multiplier)
            line[2] = int(int(line[2]) * multiplier)
            line[3] = int(int(line[3]) * multiplier)
            line[4] = int(int(line[4]) * multiplier)
            line[5] = int(int(line[5]) * multiplier)
            line[6] = int(int(line[6]) * multiplier)
            line[7] = int(int(line[7]) * multiplier)
        
        writeLine(line)

f = open('D:\Diablo2Modding\my_edited_excels\Experience_mod.txt', 'w')
f.write(out)
print('Done')
