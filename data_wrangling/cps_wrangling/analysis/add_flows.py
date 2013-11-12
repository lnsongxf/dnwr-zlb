"""
Run during or after panel_constructoin.

Modifies the panels on disk... so be careful.
"""
import json
import pandas as pd

from helpers import add_flows_panel, get_useful

with open('../panel_construction/settings.txt') as f:
    settings = json.load(f)

panel_store = pd.HDFStore(settings['panel_store_path'])

for k, _ in panel_store.iteritems():
    _wp = panel_store.select(k)
    wp = get_useful(_wp.copy())
    try:
        add_flows_panel(wp, inplace=True)
        _wp['flow'] = wp['flow']
        _wp.to_hdf(panel_store, k, append=False)
    except:
        print("Skipping {}".format(k))
