from Plugins.Plugin import PluginDescriptor
from .screens.main_screen import LottoMainScreen


def main(session, **kwargs):
    session.open(LottoMainScreen)


def Plugins(**kwargs):
    return PluginDescriptor(
        name="Lotto Statistiche",
        description="Analisi e previsioni per Lotto, 10eLotto, Superenalotto",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        fnc=main,
        icon="plugin.png"
    )
