# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.Pixmap import Pixmap
from Components.MenuList import MenuList
from enigma import ePicLoad
from ..core.smorfia import SMORFIA
from .. import _, get_skin_override
import os


class SmorfiaScreen(Screen):
    skin = get_skin_override("smorfia")

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        self["title"] = Label(_("NEAPOLITAN SMORFIA"))

        self.smorfia_entries = []
        for num in range(1, 91):
            entry = SMORFIA.get(num)
            if entry:
                self.smorfia_entries.append({
                    "num": num,
                    "name": entry["name"],
                    "icon": entry["icon"]
                })

        menu_items = []
        for item in self.smorfia_entries:
            menu_items.append(f"{item['num']:2}. {item['name']}")

        self["list"] = MenuList(menu_items)
        self["list"].onSelectionChanged.append(self._show_icon)

        self["cover"] = Pixmap()
        self["info"] = Label("")

        self["actions"] = ActionMap(["OkCancelActions"], {
            "cancel": self.close,
        }, -1)

        self.picload = None
        self.onLayoutFinish.append(self._show_icon)

    def _show_icon(self):
        try:
            idx = self["list"].getSelectedIndex()
            if idx < 0 or idx >= len(self.smorfia_entries):
                self["cover"].hide()
                return

            item = self.smorfia_entries[idx]
            plugin_path = os.path.dirname(os.path.dirname(__file__))
            icon_path = os.path.join(plugin_path, "images", "smorfia", item["icon"])

            self["info"].setText(f"[{item['num']:2}] -> {item['name']}")

            if os.path.exists(icon_path):
                if self.picload is None:
                    self.picload = ePicLoad()

                self.picload.setPara([80, 80, 1, 1, False, 1, "#00000000"])
                decode_result = self.picload.startDecode(icon_path, 0, 0, False)

                if decode_result == 0:
                    ptr = self.picload.getData()
                    if ptr:
                        self["cover"].instance.setPixmap(ptr)
                        self["cover"].show()
                        return

            self["cover"].hide()

        except Exception:
            self["cover"].hide()
