# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from ..core.statistiche import get_full_analysis
from . import _


class AnalisiScreen(Screen):
    skin = """
        <screen position="center,center" size="800,550" title="Analisi Statistiche">
            <widget name="title" position="10,10" size="780,40" font="Regular;26" foregroundColor="#ff66ff" />
            <widget name="analisi" position="10,60" size="780,430" font="Regular;20" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session

        self["title"] = Label(_("🔍 COMPLETE ANALYSIS"))
        self["analisi"] = ScrollLabel(self._get_analysis_text())
        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"], {
            "cancel": self.exit,
            "up": self.page_up,
            "down": self.page_down,
            "left": self.page_up,
            "right": self.page_down
        }, -1)

    def _get_analysis_text(self):
        analysis = get_full_analysis()

        text = _("📊 GENERAL STATISTICS:\n")
        text += f"  {_('Total draws')}: {analysis['total_draws']}\n"
        text += f"  {
            _('Most frequent number')}: {
            analysis['most_frequent'][0]} ({
            analysis['most_frequent'][1]} {
                _('times')})\n"
        text += f"  {
            _('Least frequent number')}: {
            analysis['least_frequent'][0]} ({
            analysis['least_frequent'][1]} {
                _('times')})\n"
        text += f"  {
            _('Number with max delay')}: {
            analysis['max_delay'][0]} ({
            analysis['max_delay'][1]} {
                _('draws')})\n"

        text += _("\n📌 MOST DRAWN NUMBERS PER WHEEL:\n")
        for wheel, numbers in analysis['numbers_per_wheel'].items():
            if numbers:
                text += f"  {wheel}: {', '.join(map(str, numbers[:5]))}\n"

        return text

    def page_up(self):
        self["analisi"].pageUp()

    def page_down(self):
        self["analisi"].pageDown()

    def exit(self):
        self.close()
