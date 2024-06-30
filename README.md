# AMP16DX-Plugin
GoldHEN Plugin used for loading AMP16DX files, heavily based on the RB4DX-Plugin (1.0 debug fork)

## Usage

* Put this code under [default] of `plugins.ini`
```ini
/data/GoldHEN/plugins/Discord-Plugin.prx=true
```


## Building

Install the [OpenOrbis PS4 Toolchain](https://github.com/OpenOrbis/OpenOrbis-PS4-Toolchain) and [GoldHEN Plugin SDK](https://github.com/GoldHEN/GoldHEN_Plugins_SDK), make sure the `OO_PS4_TOOLCHAIN` and `GOLDHEN_SDK` environment variables are set to their respective directories, then just type `make` in the Discord-Plugin project directory.

