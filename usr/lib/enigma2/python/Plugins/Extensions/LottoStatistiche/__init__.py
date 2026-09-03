#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import gettext
import base64
import re
import os

__author__ = "Lululla"
__email__ = "ekekaz@gmail.com"
__copyright__ = "Copyright (c) 2026 Lululla"
__license__ = "GPL-v2"
__version__ = "1.1"
DEBUG = True

PluginLanguageDomain = 'LottoStatistiche'
PluginLanguagePath = 'Extensions/LottoStatistiche/locale'
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/134.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
}


def getDesktopSize():
    from enigma import getDesktop
    s = getDesktop(0).size()
    return (s.width(), s.height())


def isWQHD():
    width, height = getDesktopSize()
    return width == 2560 and height == 1440


def isUHD():
    width, height = getDesktopSize()
    return width == 3840 and height == 2160


def isFHD():
    width, height = getDesktopSize()
    return width == 1920 and height == 1080


def isHD():
    width, height = getDesktopSize()
    return width == 1280 and height == 720


def get_skin_override(screen_name="main"):
    """Return the skin XML for a specific screen"""
    plugin_path = os.path.dirname(__file__)
    
    if isUHD():
        skin_dir = "uhd"
    elif isWQHD():
        skin_dir = "wqhd"
    elif isFHD():
        skin_dir = "fhd"
    else:
        skin_dir = "hd"
    
    skin_path = os.path.join(plugin_path, "skins", skin_dir, f"{screen_name}.xml")
    
    if os.path.exists(skin_path):
        with open(skin_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    fallback_path = os.path.join(plugin_path, "skins", "hd", f"{screen_name}.xml")
    if os.path.exists(fallback_path):
        with open(fallback_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    return '<screen position="center,center" size="800,480" title="Default"/>'


def b64decoder(data):
    data = data.strip()
    pad = len(data) % 4
    if pad == 1:
        return ""
    if pad:
        data += "=" * (4 - pad)
    try:
        decoded = base64.b64decode(data)
        return decoded.decode('utf-8')
    except Exception as e:
        print("Base64 decoding error: %s" % e)
        return ""


def paypal():
    conthelp = "If you like what I do you\n"
    conthelp += "can contribute with a coffee\n"
    conthelp += "scan the qr code and donate € 1.00"
    return conthelp


def localeInit():
    gettext.bindtextdomain(
        PluginLanguageDomain,
        resolveFilename(
            SCOPE_PLUGINS,
            PluginLanguagePath))


def _extract_placeholders(text):
    """Extract all placeholders from a string."""
    if not text:
        return []

    placeholders = []

    for match in re.finditer(r'\{[^{}]+\}', text):
        placeholders.append(match.group(0))

    for match in re.finditer(
        r'%\([a-zA-Z_][a-zA-Z0-9_]*\)[diouxXeEfFgGcrs]',
            text):
        placeholders.append(match.group(0))

    for match in re.finditer(r'%[diouxXeEfFgGcrs]', text):
        placeholders.append(match.group(0))

    return placeholders


def _restore_placeholders(original, translated):
    """Restore placeholders in translated string using original as reference."""
    if not original or not translated:
        return translated

    if '{' not in original and '%' not in original:
        return translated

    original_placeholders = _extract_placeholders(original)
    if not original_placeholders:
        return translated

    result = translated

    for placeholder in original_placeholders:
        if placeholder in result:
            continue

        if placeholder.startswith('{') and placeholder.endswith('}'):
            content = placeholder[1:-1]
            for match in re.finditer(r'\{[^{}]+\}', result):
                translated_content = match.group(0)[1:-1]
                if translated_content != content:
                    result = result.replace(match.group(0), placeholder)
                    break

    return result


def _has_placeholders(text):
    """Check if text contains any placeholders."""
    if not text:
        return False
    return (
        ('{' in text and '}' in text) or
        '%(' in text or
        re.search(r'%[diouxXeEfFgGcrs]', text) is not None
    )


def _(txt):
    """Translation function with automatic placeholder protection."""
    if not txt:
        return ""

    original = txt

    translated = gettext.dgettext(PluginLanguageDomain, txt)
    if translated:
        if _has_placeholders(original):
            restored = _restore_placeholders(original, translated)
            return restored
        return translated

    print(("[%s] fallback to default translation for %s" %
          (PluginLanguageDomain, txt)))
    translated = gettext.gettext(txt)

    if _has_placeholders(original):
        restored = _restore_placeholders(original, translated)
        return restored

    return translated


localeInit()
language.addCallback(localeInit)
