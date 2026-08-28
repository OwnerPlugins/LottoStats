# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from ..core.dati import get_archive
from . import _


class ArchivioScreen(Screen):
    skin = """
        <screen position="center,center" size="800,550" title="Archivio Estrazioni">
            <widget name="title" position="10,10" size="780,40" font="Regular;26" foregroundColor="#00ccff" />
            <widget name="archivio" position="10,60" size="780,430" font="Regular;20" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session

        self["title"] = Label(_("📚 DRAWS ARCHIVE"))
        self["archivio"] = ScrollLabel(self._get_archive_text())

        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"], {
            "cancel": self.exit,
            "up": self.page_up,
            "down": self.page_down,
            "left": self.page_up,
            "right": self.page_down
        }, -1)

    def _get_archive_text(self):
        archive = get_archive()

        if not archive:
            return _("❌ No draws available. Press 'Update Archive' from main menu.")

        reversed_archive = list(reversed(archive))

        text = f"📊 {_('TOTAL DRAWS')}: {len(archive)}\n"
        text += "=" * 50 + "\n\n"

        for draw in reversed_archive[:50]:
            date = draw['data']
            text += f"📅 {date}\n"
            for wheel, numbers in draw['estrazioni'].items():
                if numbers:
                    text += f"  {wheel}: {', '.join(map(str, numbers))}\n"
            text += "\n"

        if len(archive) > 50:
            text += f"\n... {_('and')} {len(archive) -
                                        50} {_('more draws')} ({_('use up/down to scroll')})"

        return text

    def page_up(self):
        self["archivio"].pageUp()

    def page_down(self):
        self["archivio"].pageDown()

    def exit(self):
        self.close()
