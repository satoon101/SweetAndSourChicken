# SweetAndSourChicken

## Introduction
SweetAndSourChicken is a plugin created for [Source.Python](https://github.com/Source-Python-Dev-Team/Source.Python).  As such, it requires [Source.Python](https://github.com/Source-Python-Dev-Team/Source.Python) to be installed on your Source-engine server.  It only supports CS:GO as it relies on the `chicken` entity in that game.

This plugin grants a reward or dishes out a punishment when killing a chicken.

<br>
## Installation
To install, simply download the current release from its [release thread](https://forums.sourcepython.com/viewtopic.php?t=1442) and install in into the main directory on your server.

Once you have installed SweetAndSourChicken on your server, simply add the following to your autoexec.cfg file:
```
sp plugin load sweet_and_sour_chicken
```

<br>
After having loaded the plugin once, a configuration file will have been created on your server at **../cfg/source-python/most_damage.cfg**

Edit that file to your liking.  The current default configuration file looks like:
```
// Default Value: 50
// The percent (0 - 100) chance that both a reward and a punishment will be
//   granted to the player.
   sasc_percent_for_both 50


// Options:
//     kill,slow,damage
// Default Value: ""
// Punishments to disable on the server.
   sasc_disabled_punishments ""


// Options:
//     armor,health,speed_boost
// Default Value: ""
// Rewards to disable on the server.
   sasc_disabled_rewards ""


// Default Value: 20
// The maximum number of chickens on the map at any given time.
   sasc_chicken_count 20
```
