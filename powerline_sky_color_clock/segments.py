# vim:set fileencoding=utf-8 noexpandtab tabstop=4 shiftwidth=4:noet

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
from subprocess import PIPE, Popen
import os, re, string
from datetime import datetime

@requires_segment_info
class SkyColorClockSegment(Segment):
	def __call__(self, pl, segment_info, hogehoge=True, fugafuga=False, format='%Y-%m-%d', istime=False):
		pl.debug('Running sky color clock %s %s %s %s' % (hogehoge, fugafuga, format, istime))

		cwd = segment_info['getcwd']()
		try:
			contents = datetime.now().strftime(format)
		except UnicodeEncodeError:
			contents = datetime.now().strftime(format.encode('utf-8')).decode('utf-8')

		return [{
			'contents': contents,
			'highlight_groups': (['time'] if istime else []) + ['date'],
			'divider_highlight_group': 'time:divider' if istime else None,
		}]

sky_color_clock = with_docstring(SkyColorClockSegment(),
'''Return the time.
:param str format:
	strftime-style date format string
:param bool istime:
	If true then segment uses ``time`` highlight group.
Divider highlight group used: ``time:divider``.
Highlight groups used: ``time`` or ``date``.
''')
