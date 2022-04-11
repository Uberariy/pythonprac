import gettext
translation = gettext.translation('modu', 'po', fallback=True)
_, ngettext = translation.gettext, translation.ngettext


def dialog():
	while s := input(_("Input string: ")):
		n = len(s.split())
		print(ngettext("{} word entered", "{} words enteted", n).format(n))
