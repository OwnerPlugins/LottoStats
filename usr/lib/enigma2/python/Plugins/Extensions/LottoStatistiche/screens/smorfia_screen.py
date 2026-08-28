# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from ..core.smorfia import SMORFIA
from . import _


class SmorfiaScreen(Screen):
    skin = """
        <screen position="center,center" size="800,550" title="Smorfia Napoletana">
            <widget name="title" position="10,10" size="780,40" font="Regular;26" foregroundColor="#ff8800" />
            <widget name="smorfia" position="10,60" size="780,430" font="Regular;18" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session

        self["title"] = Label(_("😴 NEAPOLITAN SMORFIA"))
        self["smorfia"] = ScrollLabel(self._get_smorfia_text())
        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"], {
            "cancel": self.exit,
            "up": self.page_up,
            "down": self.page_down,
            "left": self.page_up,
            "right": self.page_down
        }, -1)

    def _get_smorfia_text(self):
        text = _("📖 NUMBER MEANINGS (1-90):\n\n")
        counter = 0
        for num, meaning in sorted(SMORFIA.items()):
            text += f"{num:2} = {meaning}"
            counter += 1
            if counter % 3 == 0:
                text += "\n"
            else:
                text += "  |  "
        return text

    def page_up(self):
        self["smorfia"].pageUp()

    def page_down(self):
        self["smorfia"].pageDown()

    def exit(self):
        self.close()
