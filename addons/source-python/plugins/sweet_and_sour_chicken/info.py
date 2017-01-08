# ../sweet_and_sour_chicken/info.py

"""Provides/stores information about the plugin."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from cvars.public import PublicConVar
from plugins.info import PluginInfo


# =============================================================================
# >> PLUGIN INFO
# =============================================================================
info = PluginInfo()
info.name = 'Sweet And Sour Chicken'
info.author = 'satoon101'
info.version = '1.0'
info.basename = 'sweet_and_sour_chicken'
info.variable = info.basename + '_version'
info.url = ''
info.convar = PublicConVar(info.variable, info.version, info.name + ' Version')
