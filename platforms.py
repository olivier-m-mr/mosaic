import mosaic

def GenerateTitle():
	return """
		<table>
			<tr>
				<td><a href="index.html"><img class="mosaiclogo" src="landing-images/icon.png" height="75" width="75" alt="MOSAIC"></td>
				<td><p class="downloadtitle"><em>MOSAIC</em> Downloads</p></td>
			</tr>
		</table>
	"""

def GenerateHeader():
	return """
	<head>
	    <title>MOSAIC Downloads</title>
	    <link rel="icon" href="source/favicon.ico" type="image/ico">
	
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta http-equiv="Content-Language" content="en">
		<meta http-equiv="Content-Style-Type" content="text/css">
		
		<link rel="stylesheet" type="text/css" href="html/_static/style.css">
		
		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
		<script src="utils.js"></script>		
	</head>
	
	<body>
	"""
def GenerateTableFromVersion(baseurl, title, version, showBinaries=True):
	tabsrc="""
		<p class="downloadversion" align="left"><em>{0}</em></p>
		<table class="downloadtable">
			<col width=40%>
			<col width=60%>
		""".format(title)
	if showBinaries:
		tabsrc+="""
			<tr>
				<td class="downloadtext"><a class="downloadtext" href="{0}/mosaic-{1}.dmg">mosaic-{1}.dmg</a></td>
				<td class="downloadtext"><p class="downloadtext">Mac OS X, 10.8+</p></td>
			</tr>
			<tr>
				<td class="downloadtext"><a class="downloadtext" href="{0}/mosaic-x64-{1}.zip">mosaic-x64-{1}.zip</a></td>
				<td class="downloadtext"><p class="downloadtext">Windows, 64-bit</p></td>
			</tr>
		""".format(baseurl, version)
	tabsrc+="""
			<tr>
				<td class="downloadtext"><a class="downloadtext" href="{0}/mosaic-{1}.tar.gz">mosaic-{1}.tar.gz</a></td>
				<td class="downloadtext"><p class="downloadtext">MOSAIC Source</p></td>
			</tr>
		</table>
	""".format(baseurl, version)

	return tabsrc

if __name__ == '__main__':
	url="https://github.com/usnistgov/mosaic/releases/download/v"
	vers=[
		# ("Version "+str(mosaic.__version__), str(mosaic.__version__), True),
		("Version 1.0 Beta 3, Update 2", "1.0b3.2",True),
		("Version 1.0 Beta 3, Update 1", "1.0b3.1",False),
		("Version 1.0 Beta 3", "1.0b3",False),
		("Version 1.0 Beta 2", "1.0b2",False),
		("Version 1.0 Beta 1", "1.0b1",False)
	]
	htmlout="""
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
	<html lang="en">
	"""

	htmlout+=GenerateHeader()
	htmlout+=GenerateTitle()
	for v in vers:
		htmlout+=GenerateTableFromVersion(url+v[1], v[0], v[1], v[2])
	htmlout+="""
		<br /><br /><br /><br /><br /><br /><br /><br />
		<hr />
		<div align="center" style="vertical-align: bottom">
			<small>
				<table class="footer" width="95%">
					<col width=30%>
					<col width=70%>
					<tr>
						<td align="left" style="vertical-align: bottom">
							<a class="footer" href="html/doc/Developers.html"><em>MOSAIC Developers</em></a>&nbsp;&nbsp;&nbsp;
							<a class="footer" href="html/doc/Disclaimer.html"><em>Terms of Use</em></a>
						</td>
						<td align="right" style="vertical-align: bottom"><em>National Institute of Standards and Technology</em></td>
					</tr>
				</table>
			</small>
		</div>
		</body>
	</html>"""

	with open('platforms.html', 'w') as f:
		f.write(htmlout)

	print "Wrote platforms.html"

