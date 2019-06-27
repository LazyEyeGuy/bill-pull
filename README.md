# bill-pull
Pulls congressional bills and puts them on a GUI

Current error (python populate.py):

Traceback (most recent call last):
  File "populate.py", line 4, in <module>
    tree = et.parse('raw/gui.ui')
  File "/usr/lib64/python2.7/xml/etree/ElementTree.py", line 1182, in parse
    tree.parse(source, parser)
  File "/usr/lib64/python2.7/xml/etree/ElementTree.py", line 656, in parse
    parser.feed(data)
  File "/usr/lib64/python2.7/xml/etree/ElementTree.py", line 1653, in feed
    self._raiseerror(v)
  File "/usr/lib64/python2.7/xml/etree/ElementTree.py", line 1517, in _raiseerror
    raise err
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 52, column 19
