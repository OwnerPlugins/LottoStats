<h1 align="center">🎰 LottoStats - Lotto Statistics Plugin for Enigma2</h1>

<p align="center">
  <a href="https://github.com/OwnerPlugins/LottoStats">
    <img src="https://img.shields.io/badge/Version-1.0-blue.svg" alt="Version">
  </a>

  <a href="https://www.enigma2.net">
    <img src="https://img.shields.io/badge/Enigma2-Plugin-ff6600.svg" alt="Enigma2 Plugin">
  </a>

  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.X-blue.svg" alt="Python">
  </a>

  <a href="https://www.gnu.org/licenses/gpl-3.0">
    <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="GPLv3">
  </a>
</p>

<p align="center">
  <a href="https://github.com/OwnerPlugins">
    <img src="https://komarev.com/ghpvc/?username=OwnerPlugins&label=Repository%20Views&color=blueviolet" alt="Visitors">
  </a>
</p>

<p align="center">
  <a href="https://ko-fi.com/yourprofile">
    <img src="https://img.shields.io/badge/_-Donate-red.svg?logo=githubsponsors&labelColor=555555&style=for-the-badge" alt="Ko-fi">
  </a>

  <a href="https://paypal.me/yourprofile">
    <img src="https://img.shields.io/badge/_-Donate-green.svg?logo=githubsponsors&labelColor=555555&style=for-the-badge" alt="PayPal">
  </a>
</p>

A comprehensive Lotto statistics plugin for Enigma2-based receivers with historical data analysis, frequency tracking, predictions, and support for Lotto, 10eLotto, and Superenalotto.

---

## ✨ Features

### Core Features
- **📊 Draws Archive**: Complete historical archive from 1871 to present day
- **📈 Frequency Analysis**: Hot and cold numbers with detailed statistics
- **🔍 Statistical Analysis**: Comprehensive analysis with most/least frequent numbers and delays
- **🔮 Predictions**: Generate statistical predictions based on frequencies and delays
- **😴 Neapolitan Smorfia**: Complete 1-90 number meanings for dream interpretation
- **🎯 10eLotto**: Dedicated statistics for 10eLotto
- **⭐ Superenalotto**: Complete historical archive with frequency analysis
- **🔄 Auto-Update**: Automatic download of latest draw archives

### Data Sources
- **Lotto**: Brightstar Lottery archive (1871-present)
- **Superenalotto**: GitHub archive by luigimassa (1997-present)
- **10eLotto**: Statistical analysis based on Lotto data

### Navigation System
- **Menu Stack Navigation**: Back button returns to previous level
- **Scroll Support**: Up/Down/Left/Right navigation in all screens
- **Real-time Data**: Always up-to-date statistics

### Technical Features
- **Multi-threaded Loading**: Background data processing
- **JSON Data Storage**: Efficient local data management
- **gettext Support**: Fully internationalized
- **Dynamic Skin Loading**: Auto-adapts to screen resolution
- **Memory Efficient**: Loads data in batches

---

## 🎮 Key Controls

### Main Menu
| Key | Action |
|-----|--------|
| **OK** | Enter selected category |
| **CANCEL / EXIT** | Close plugin |

### All Screens (Archive, Frequencies, etc.)
| Key | Action |
|-----|--------|
| **OK** | (context-dependent) |
| **CANCEL / EXIT** | Return to main menu |
| **UP/DOWN** | Scroll content |
| **LEFT/RIGHT** | Page up/down |

### Player (Future implementation)
| Key | Action |
|-----|--------|
| **OK** | (context-dependent) |
| **STOP** | Exit player |
| **EXIT** | Exit player |

---

## 📦 Installation

### Via Telnet/Wget (Recommended)

```bash
wget -q --no-check-certificate https://raw.githubusercontent.com/OwnerPlugins/LottoStats/main/installer.sh -O - | /bin/bash
```

### Manual Installation

1. Download the plugin
2. Extract to `/usr/lib/enigma2/python/Plugins/Extensions/`
3. Restart Enigma2
4. The plugin will appear in the Extensions menu

### Dependencies

The plugin uses only standard Enigma2 libraries. No additional dependencies required.

---

## 🚀 Usage

### Basic Navigation

1. **Open the Plugin**: From the Extensions menu, select LottoStats
2. **Main Menu**: Choose between:
   - 📊 **Draws Archive** - View historical draws
   - 📈 **Number Frequencies** - Hot and cold numbers
   - 🔍 **Statistical Analysis** - Complete statistics
   - 🔮 **Predictions** - Generated predictions
   - 😴 **Neapolitan Smorfia** - Number meanings
   - 🎯 **10e Lotto** - Dedicated statistics
   - ⭐ **Superenalotto** - Historical archive
   - 🔄 **Update Lotto Archive** - Download latest data
   - 🔄 **Update Superenalotto** - Download latest data
   - ❌ **Exit** - Close plugin

### Viewing the Archive

1. Select **Draws Archive** from the main menu
2. Scroll through the historical draws (most recent first)
3. Use UP/DOWN to scroll through the list
4. Press EXIT to return to the main menu

### Analyzing Frequencies

1. Select **Number Frequencies** from the main menu
2. View:
   - 🔥 Hot numbers (most drawn)
   - ❄️ Cold numbers (least drawn)
   - ⏳ Maximum delays
3. Scroll through the results

### Generating Predictions

1. Select **Predictions** from the main menu
2. View generated predictions for each wheel
3. Each wheel shows 5 recommended numbers
4. Disclaimer: Predictions are statistical only

### Updating Data

1. Select **Update Lotto Archive** from the main menu
2. The plugin will download the latest archive from Brightstar
3. Wait for completion confirmation
4. Or select **Update Superenalotto** for Superenalotto data

---

## 📁 File Structure

```
Plugins/Extensions/LottoStatistiche/
├── plugin.py                    # Plugin entry point
├── __init__.py                  # Package initialization
├── screens/
│   ├── __init__.py              # Screen package
│   ├── main_screen.py           # Main menu screen
│   ├── archivio_screen.py       # Draws archive screen
│   ├── frequenze_screen.py      # Frequencies screen
│   ├── analisi_screen.py        # Analysis screen
│   ├── previsioni_screen.py     # Predictions screen
│   ├── smorfia_screen.py        # Smorfia screen
│   ├── dieci_lotto_screen.py    # 10eLotto screen
│   └── superenalotto_screen.py  # Superenalotto screen
├── core/
│   ├── __init__.py              # Core package
│   ├── dati.py                  # Data management
│   ├── statistiche.py           # Statistics calculations
│   ├── smorfia.py               # Smorfia data
│   ├── update.py                # Lotto archive updater
│   └── update_superenalotto.py  # Superenalotto updater
└── data/
    └── archivio.json            # Local archive storage
```

### Data File Format

**`data/archivio.json`**
```json
[
  {
    "data": "2026-08-25",
    "estrazioni": {
      "BA": [12, 34, 56, 78, 90],
      "CA": [3, 15, 27, 39, 51],
      "FI": [6, 18, 30, 42, 54],
      "GE": [9, 21, 33, 45, 57],
      "MI": [1, 13, 25, 37, 49],
      "NA": [4, 16, 28, 40, 52],
      "PA": [7, 19, 31, 43, 55],
      "RM": [10, 22, 35, 47, 59],
      "TO": [2, 14, 26, 38, 50],
      "VE": [5, 17, 29, 41, 53]
    }
  }
]
```

**`data/superenalotto.json`**
```json
[
  {
    "data": "2026-08-25",
    "concorso": 136,
    "numeri": [12, 34, 56, 67, 78, 90],
    "jolly": 45,
    "superstar": 23
  }
]
```

---

## ⚙️ Configuration

### Settings
Access configuration from the Enigma2 plugin menu:
- **Default Language**: Choose between Italian and other languages
- **Archive Update**: Manual or automatic updates
- **Debug Logging**: Enable debug messages in logs

### Skin Customization
The plugin automatically detects screen resolution and loads the appropriate skin:
- **HD** (1280x720): Default skin
- **FHD** (1920x1080): Optimized for full HD
- **UHD** (3840x2160): Optimized for 4K displays

---

## 🔧 Technical Details

### Architecture
- **Frontend**: Enigma2 Screen system with MenuList and ScrollLabel components
- **Navigation**: Stack-based navigation with history
- **Data**: JSON-based local storage
- **Updates**: HTTP download with zip extraction
- **Statistics**: Python-based calculations with frequency and delay analysis
- **Internationalization**: gettext-based translations

### Data Sources
- **Lotto**: `https://www.brightstarlottery.it/STORICO_ESTRAZIONI_LOTTO/storico.zip`
- **Superenalotto**: `https://raw.githubusercontent.com/luigimassa/superenalotto-archivio/main/superenalotto.csv`

### Statistical Calculations
- **Frequencies**: Count of each number's appearances
- **Delays**: Number of draws since last appearance
- **Hot Numbers**: Most frequent numbers
- **Cold Numbers**: Least frequent numbers
- **Predictions**: Combined frequency + delay weighting

### Wheels
The plugin supports 10 Italian Lotto wheels:
- BA (Bari)
- CA (Cagliari)
- FI (Firenze)
- GE (Genova)
- MI (Milano)
- NA (Napoli)
- PA (Palermo)
- RM (Roma)
- TO (Torino)
- VE (Venezia)

---

## 🐛 Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| **No archive data** | Press "Update Lotto Archive" from main menu |
| **Superenalotto not loading** | Press "Update Superenalotto" from main menu |
| **Data won't update** | Check internet connection and try again |
| **No numbers showing** | Archive may be corrupted; delete `data/archivio.json` and update |
| **Scrolling not working** | Use UP/DOWN keys on remote |
| **Plugin fails to load** | Check Python syntax errors in logs |
| **Slow loading** | Archive file may be large; wait for loading to complete |

### Debug Mode

Enable debug logging in settings, then check logs:

```bash
tail -f /var/log/messages | grep LottoStats
```

Or on OpenPLi:

```bash
tail -f /home/root/logs/debug.log | grep LottoStats
```

### Manual Archive Download

If automatic updates fail:

1. Download manually from: `https://www.brightstarlottery.it/STORICO_ESTRAZIONI_LOTTO/storico.zip`
2. Extract the TXT file
3. Convert to JSON format (the plugin does this automatically)

---

## 📝 Changelog

### v1.0 (2026-08-28)
- Initial release
- Complete Lotto archive from 1871 to present
- Frequency and delay analysis
- Statistical predictions
- Neapolitan Smorfia (all 90 numbers)
- 10eLotto statistics
- Superenalotto complete archive
- Auto-update functionality
- Full gettext internationalization
- English codebase with Italian UI
- Scroll navigation in all screens
- Background data processing

---

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows existing style and structure
- Comments are in English
- All code uses English naming conventions
- UI text uses `_()` for translation
- New features include appropriate configuration options
- All changes are tested on Enigma2 receivers
- Submit pull requests to the main branch

---

### 📜 License Information

This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation.

This plugin is released under GPLv3. See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html#license-text) for full details.

<img width="120" height="58" alt="GPLv3_Logo svg" src="https://github.com/user-attachments/assets/67d32b0a-2a44-4fa9-a972-202daf28808e" />

---

### 🚨 Disclaimer

The project author is not responsible for how this software is used by others. This plugin is for informational and recreational purposes only.

The plugin provides statistical analysis and predictions based on historical data. These predictions do not guarantee wins and should not be used as financial advice.

Users are solely responsible for determining the legality of their actions in their jurisdiction.

---

⭐️ If you find this plugin useful, please give it a star on GitHub!

Thanks! ❤️ 💞 💖 ❤️‍🔥 💗

---

## 🙏 Credits

- **Developer**: OwnerPlugins
- **Data Sources**: Brightstar Lottery, luigimassa (Superenalotto)
- **Inspiration**: Lottologia, 123lotto.it
- **Community**: LinuxSat-Support, CorvoBoys

---

*Note: This plugin requires an Enigma2-based receiver (OpenPLi, OpenATV, etc.)*
*Internet connection required for archive updates*
*Historical archive may take time to download on first run*
*Predictions are statistical only and do not guarantee wins*
*Play responsibly!*
```