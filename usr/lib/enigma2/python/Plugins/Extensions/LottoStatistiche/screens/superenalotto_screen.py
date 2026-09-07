# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from ..core.dati import get_superenalotto_archive
from ..core.statistiche import (
    calculate_frequencies_se,
    calculate_delays_se,
    get_full_analysis_se,
    generate_predictions_se
)
from .. import _, get_skin_override


class SuperenalottoScreen(Screen):
    skin = get_skin_override("superenalotto")

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session

        self["title"] = Label(_("SUPERENALOTTO - Statistics"))
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
            return _("No data available. Press 'Update Superenalotto' from main menu.")
        try:
            # Last draw
            last = archive[-1]
            text = _("LAST DRAW") + f" ({_('contest')} {last['concorso']} - {last['data']}):\n"
            text += f"  {_('Numbers')}: {', '.join(map(str, last['numeri']))}\n"
            if last['jolly']:
                text += f"  Jolly: {last['jolly']}\n"
            if last['superstar']:
                text += f"  SuperStar: {last['superstar']}\n"
            text += "\n"

            # General statistics
            analysis = get_full_analysis_se()
            text += _("GENERAL STATISTICS:\n")
            text += f"  {_('Total draws')}: {analysis['total_draws']}\n"
            text += f"  {_('Most frequent number')}: {analysis['most_frequent'][0]} ({analysis['most_frequent'][1]} {_('times')})\n"
            text += f"  {_('Least frequent number')}: {analysis['least_frequent'][0]} ({analysis['least_frequent'][1]} {_('times')})\n"
            text += f"  {_('Number with max delay')}: {analysis['max_delay'][0]} ({analysis['max_delay'][1]} {_('draws')})\n"
            text += "\n"

            # Hot/Cold Frequencies
            frequencies = calculate_frequencies_se()
            hot = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:10]
            cold = sorted(frequencies.items(), key=lambda x: x[1])[:10]

            text += _("HOT NUMBERS (most drawn):\n")
            for i, (num, freq) in enumerate(hot, 1):
                text += f"  {i:2}. {num:2} -> {freq} {_('times')}\n"
            text += "\n"

            text += _("COLD NUMBERS (least drawn):\n")
            for i, (num, freq) in enumerate(cold, 1):
                text += f"  {i:2}. {num:2} -> {freq} {_('times')}\n"
            text += "\n"

            # Delays
            delays = calculate_delays_se()
            max_delays = sorted(delays.items(), key=lambda x: x[1], reverse=True)[:10]
            text += _("MAX DELAYS:\n")
            for i, (num, delay) in enumerate(max_delays, 1):
                text += f"  {i:2}. {num:2} -> {delay} {_('draws')}\n"
            text += "\n"

            # Forecasts
            predictions = generate_predictions_se()
            text += _("PREDICTIONS (6 numbers):\n")
            text += f"  {', '.join(map(str, predictions))}\n"
            text += "\n"

            text += _("Tip: Play responsibly!")

            return text
        except Exception as e:
            print(f"[SuperenalottoScreen] Error: {e}")
            import traceback
            traceback.print_exc()
            return _("Error loading Superenalotto data. Check log for details.")

    def page_up(self):
        self["info"].pageUp()

    def page_down(self):
        self["info"].pageDown()

    def exit(self):
        self.close()
