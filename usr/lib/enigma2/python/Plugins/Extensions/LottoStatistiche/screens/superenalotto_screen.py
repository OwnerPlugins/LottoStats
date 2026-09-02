# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from collections import Counter

from ..core.dati import get_superenalotto_archive
from .. import _, get_skin_override


class SuperenalottoScreen(Screen):
    skin = get_skin_override("superenalotto")

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session

        self["title"] = Label(_("⭐ SUPERENALOTTO - Historical Archive"))
        self["info"] = ScrollLabel(self._get_info_text())
        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"], {
            "cancel": self.exit,
            "up": self.page_up,
            "down": self.page_down,
            "left": self.page_up,
            "right": self.page_down
        }, -1)

    def _get_info_text(self):
        archive = get_superenalotto_archive()

        if not archive:
            return _(
                "❌ No data available. Press 'Update Superenalotto' from main menu.")

        last = archive[-1]

        text = f"🎰 {_('LAST DRAW')} ({_('contest')} {last['concorso']} - {last['data']}):\n"
        text += f"  {_('Numbers')}: {', '.join(map(str, last['numeri']))}\n"
        if last['jolly']:
            text += f"  Jolly: {last['jolly']}\n"
        if last['superstar']:
            text += f"  SuperStar: {last['superstar']}\n"

        text += _("\n📊 MOST FREQUENT NUMBERS (all contests):\n")
        frequencies = Counter()
        for draw in archive:
            for num in draw['numeri']:
                frequencies[num] += 1

        top = frequencies.most_common(10)
        for num, freq in top:
            text += f"  {num:2} → {freq} {_('times')}\n"

        text += _("\n❄️ LEAST FREQUENT NUMBERS:\n")
        bottom = frequencies.most_common()[-10:]
        for num, freq in sorted(bottom):
            text += f"  {num:2} → {freq} {_('times')}\n"

        text += f"\n📌 {_('Total draws')}: {len(archive)}"

        return text

    def page_up(self):
        self["info"].pageUp()

    def page_down(self):
        self["info"].pageDown()

    def exit(self):
        self.close()
