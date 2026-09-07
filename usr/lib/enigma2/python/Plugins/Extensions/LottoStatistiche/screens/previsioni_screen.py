# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from ..core.statistiche import generate_predictions
from .. import _, get_skin_override


class PrevisioniScreen(Screen):
    skin = get_skin_override("previsioni")

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session

        self["title"] = Label(_("🔮 PREDICTIONS"))
        self["previsioni"] = ScrollLabel(self._get_predictions_text())
        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"], {
            "cancel": self.exit,
            "up": self.page_up,
            "down": self.page_down,
            "left": self.page_up,
            "right": self.page_down
        }, -1)

    def _get_predictions_text(self):
        predictions = generate_predictions()

        text = _(
            "⚠️ DISCLAIMER: Predictions are purely statistical and do not guarantee wins!\n\n")

        for wheel, numbers in predictions.items():
            text += f"🎯 {wheel}: {', '.join(f'{num:2}' for num in numbers)}\n"

        text += _("\n💡 Tip: Play responsibly!")
        return text

    def page_up(self):
        self["previsioni"].pageUp()

    def page_down(self):
        self["previsioni"].pageDown()

    def exit(self):
        self.close()
