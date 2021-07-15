import csv
import os
watchlist = [28551, 28553, 28558, 28560,1250, 729, 2094, 62034, 2302, 4267, 9077, 36027, 1324, 2211, 3087, 1271, 1617, 1375]

for instrument in watchlist:
    file = f'{instrument}.csv'
    os.remove(file)