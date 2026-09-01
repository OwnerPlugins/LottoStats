import sys
import os

from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Screens.MessageBox import MessageBox

from .archivio_screen import ArchivioScreen
from .frequenze_screen import FrequenzeScreen
from .analisi_screen import AnalisiScreen
from .previsioni_screen import PrevisioniScreen
from .smorfia_screen import SmorfiaScreen
from .dieci_lotto_screen import DieciLottoScreen
from .superenalotto_screen import SuperenalottoScreen
from ..core.update import update_archive
from ..core.update_superenalotto import download_and_convert_se
from . import _


plugin_path = os.path.dirname(os.path.dirname(__file__))
if plugin_path not in sys.path:
    sys.path.append(plugin_path)

# from core.update import aggiorna_archivio


class LottoMainScreen(Screen):
    skin = """
        <screen position="center,center" size="800,550" title="Lotto Statistiche">
            <widget name="title" position="10,10" size="780,50" font="Regular;30" foregroundColor="#00ff00" />
            <widget name="menu" position="10,70" size="780,430" font="Regular;24" />
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session

        self["title"] = Label(_("🎰 MAIN MENU - LOTTO STATISTICS"))

        self.menu_items = [
            _("📊 Draws Archive"),
            _("📈 Number Frequencies"),
            _("🔍 Statistical Analysis"),
            _("🔮 Predictions"),
            _("😴 Neapolitan Smorfia"),
            _("🎯 10 e Lotto"),
            _("⭐ Superenalotto"),
            _("🔄 Update Lotto Archive"),
            _("🔄 Update Superenalotto"),
            _("❌ Exit")
        ]

        self["menu"] = MenuList(self.menu_items)
        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"], {
            "ok": self.ok_pressed,
            "cancel": self.exit,
            "up": self.menu_up,
            "down": self.menu_down
        }, -1)

    def ok_pressed(self):
        index = self["menu"].getSelectedIndex()

        if index == 0:
            self.session.open(ArchivioScreen)
        elif index == 1:
            self.session.open(FrequenzeScreen)
        elif index == 2:
            self.session.open(AnalisiScreen)
        elif index == 3:
            self.session.open(PrevisioniScreen)
        elif index == 4:
            self.session.open(SmorfiaScreen)
        elif index == 5:
            self.session.open(DieciLottoScreen)
        elif index == 6:
            self.session.open(SuperenalottoScreen)
        elif index == 7:
            if update_archive():
                self.session.open(
                    MessageBox,
                    _("✅ Lotto archive updated!"),
                    MessageBox.TYPE_INFO)
            else:
                self.session.open(
                    MessageBox,
                    _("❌ Lotto update error"),
                    MessageBox.TYPE_ERROR)
        elif index == 8:
            if download_and_convert_se():
                self.session.open(
                    MessageBox,
                    _("✅ Superenalotto updated!"),
                    MessageBox.TYPE_INFO)
            else:
                self.session.open(
                    MessageBox,
                    _("❌ Superenalotto update error"),
                    MessageBox.TYPE_ERROR)
        elif index == 9:
            self.exit()

    def menu_up(self):
        self["menu"].up()

    def menu_down(self):
        self["menu"].down()

    def exit(self):
        self.close()
