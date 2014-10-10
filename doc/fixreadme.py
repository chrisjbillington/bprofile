image_line = '.. image:: https://bitbucket.org/cbillington/bprofile/raw/default/doc/example.png'

with open('build/rst/index.rst') as infile:
    with open('../README.rst', 'w') as outfile:
        for line in infile:
            indent = ' ' * (len(line) - len(line.lstrip()))
            if '[image]' in line:
                line = line.replace('[image]', image_line)
            if 'Note:' in line:
                line = line.replace('Note:', 'Note:\n' + indent + ' ')
            if 'Warning:' in line:
                line = line.replace('Warning:', 'Warning:\n' + indent + ' ')
            outfile.write(line)
