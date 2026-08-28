# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from ..core.statistiche import calculate_frequencies, calculate_delays
from . import _


class FrequenzeScreen(Screen):
    skin = """
        <screen position="center,center" size="800,550" title="Frequenze Numeri">
            <widget name="title" position="10,10" size="780,40" font="Regular;26" foregroundColor="#ffcc00" />
            <widget name="frequenze" position="10,60" size="780,430" font="Regular;20" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session

        self["title"] = Label(_("📈 FREQUENCIES AND DELAYS"))
        self["frequenze"] = ScrollLabel(self._get_frequencies_text())

        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"], {
            "cancel": self.exit,
            "up": self.page_up,
            "down": self.page_down,
            "left": self.page_up,
            "right": self.page_down
        }, -1)

    def _get_frequencies_text(self):
        frequencies = calculate_frequencies()
        delays = calculate_delays()

        hot_numbers = sorted(
            frequencies.items(),
            key=lambda x: x[1],
            reverse=True)[
            :10]
        cold_numbers = sorted(frequencies.items(), key=lambda x: x[1])[:10]

        text = _("🔥 HOT NUMBERS (most drawn):\n")
        for i, (num, freq) in enumerate(hot_numbers, 1):
            text += f"  {i:2}. {num:2} → {freq} {_('times')}\n"

        text += _("\n❄️ COLD NUMBERS (least drawn):\n")
        for i, (num, freq) in enumerate(cold_numbers, 1):
            text += f"  {i:2}. {num:2} → {freq} {_('times')}\n"

        text += _("\n⏳ MAX DELAYS:\n")
        top_delays = sorted(
            delays.items(),
            key=lambda x: x[1],
            reverse=True)[
            :10]
        for i, (num, delay) in enumerate(top_delays, 1):
            text += f"  {i:2}. {num:2} → {delay} {_('draws')}\n"

        return text

    def page_up(self):
        self["frequenze"].pageUp()

    def page_down(self):
        self["frequenze"].pageDown()

    def exit(self):
        self.close()
