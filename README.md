StreamServe filter that stores a s-lxf stream in a file and returns its path

The filter reads a stream on stdin, and if found any other file than an s-lxf,
it stores the stream as a file and provides its path in an xml stream on stdout::

	<event>
		<attachment>/Users/superman/attachments/14309090.dat</attachment>
	</event>

s-lxf files (files that contains "<!DOCTYPE s-lxf SYSTEM" within the first 200 bytes of text)
is passed through "untouched" on stdout.

To enable binary streams in Windows, run::

	python.exe -u npmail.py
