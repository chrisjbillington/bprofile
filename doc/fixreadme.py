image_line = '.. image:: https://bitbucket.org/cbillington/bprofile/raw/default/doc/example.png'
wrong_link_line = 'View on PyPI | Get the source from BitBucket | Read the docs at\nreadthedocs'
correct_link_line = """`View on PyPI <http://pypi.python.org/pypi/bprofile>`_
| `Get the source from BitBucket <http://bitbucket.org/cbillington/bprofile>`_
| `Read the docs at readthedocs <http://bprofile.readthedocs.org>`_"""
wrong_email_line = 'Chris Billington'
correct_email_line = '`Chris Billington <mailto:chrisjbillington@gmail.com>`_'
with open('build/rst/index.rst') as infile:
    with open('../README.rst', 'w') as outfile:
        data = infile.read()
        data = data.replace(wrong_link_line, correct_link_line)
        data = data.replace(wrong_email_line, correct_email_line)
        for line in data.splitlines():
            indent = ' ' * (len(line) - len(line.lstrip()))
            if '[image]' in line:
                line = line.replace('[image]', image_line)
            if 'Note:' in line:
                line = line.replace('Note:', 'Note:\n' + indent + ' ')
            if 'Warning:' in line:
                line = line.replace('Warning:', 'Warning:\n' + indent + ' ')
            outfile.write(line + '\n')
