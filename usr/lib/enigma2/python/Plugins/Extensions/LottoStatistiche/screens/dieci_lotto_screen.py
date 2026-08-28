# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from ..core.statistiche import get_dieci_lotto
from . import _


class DieciLottoScreen(Screen):
    skin = """
        <screen position="center,center" size="800,550" title="10 e Lotto">
            <widget name="title" position="10,10" size="780,40" font="Regular;26" foregroundColor="#00ffcc" />
            <widget name="info" position="10,60" size="780,430" font="Regular;20" />
        </screen>
    """
    
    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        
        self["title"] = Label(_("🎯 10 e LOTTO"))
        self["info"] = ScrollLabel(self._get_info_text())
        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"], {
            "cancel": self.exit,
            "up": self.page_up,
            "down": self.page_down,
            "left": self.page_up,
            "right": self.page_down
        }, -1)
        
    def _get_info_text(self):
        data = get_dieci_lotto()
        
        text = _("🔢 LAST 10eLOTTO DRAW:\n")
        if data and 'ultima' in data:
            text += f"  {_('Drawn numbers')}: {', '.join(map(str, data['ultima']))}\n"
            
        text += _("\n📊 10eLOTTO STATISTICS:\n")
        if data and 'frequenze' in data:
            top = sorted(data['frequenze'].items(), key=lambda x: x[1], reverse=True)[:15]
            for num, freq in top:
                text += f"  {num:2} → {freq} {_('times')}\n"
                
        text += _("\n💡 In 10eLotto, 10 numbers out of 90 are drawn")
        text += _("\n   and delays are generally shorter than traditional Lotto.")
        
        return text
        
    def page_up(self):
        self["info"].pageUp()
        
    def page_down(self):
        self["info"].pageDown()
        
    def exit(self):
        self.close()
