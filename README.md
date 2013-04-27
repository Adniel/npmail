StreamServe filter that stores a s-lxf stream in a file and returns its path
============================================================================

Sending mail from Collector requires by the default configuration that archive object
should have stored a device independent copy (s-lxf). If collector is used for manually
storing other files than documents processed by StreamServe, there is no device
independent copy to rely on. To be able to send the manually stored files, this filter
stores the file data on disk and sends a new event with the created file's path.

The filter reads a stream on stdin, and if found any other file than an s-lxf,
it stores the stream as a file and provides its path in an xml stream on stdout::

	<event>
		<attachment>/Users/superman/attachments/14309090.dat</attachment>
	</event>

s-lxf files (files that contains "<!DOCTYPE s-lxf SYSTEM" within the first 200 bytes of text)
is passed through "untouched" on stdout.

Installation
------------
 * Install python 2.7
 * Create a filter chain specifying ´python.exe npmail.py´
 * Create a new event matching the ´<event>´ root tag
 * Set up a MailOUT event with a variable attachment and use
   the ´<attachment>´ element content as its path 
 * Create a SMTP for MailOUT connector
 * Configure event with similar settings for attachment name,
   sending email addres, subject et c as the preconfigured mail event
 * Done

To enable binary streams in Windows, run::

	python.exe -u npmail.py
