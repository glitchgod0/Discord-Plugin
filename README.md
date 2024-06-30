# Discord-Plugin
GoldHEN Plugin and python script used for rich presence on jailbroken PS4 systems.

## Usage

* Put this code under [default] of `/data/GoldHEN/plugins.ini`
```ini
/data/GoldHEN/plugins/Discord-Plugin.prx=true
```

## Current Flaws
* Requires a plugin, could probably be done through other things in the Klog.
* Uses the Klog, Due to a limitation, only 1 client can access the Klog at once.


## Building

Install the [OpenOrbis PS4 Toolchain](https://github.com/OpenOrbis/OpenOrbis-PS4-Toolchain) and [GoldHEN Plugin SDK](https://github.com/GoldHEN/GoldHEN_Plugins_SDK), make sure the `OO_PS4_TOOLCHAIN` and `GOLDHEN_SDK` environment variables are set to their respective directories, then just type `make` in the Discord-Plugin project directory.

