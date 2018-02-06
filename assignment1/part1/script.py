filenames = ['file1.txt', 'file2.txt']
with open('//ecsu-stuh1/userstngAK/myDesk/cordellij/Desktop/output.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
