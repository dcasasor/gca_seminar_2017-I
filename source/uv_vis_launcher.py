import numpy as np
import uv_vis_functions as functions


# --------------- Import data
raw_uv_data = np.genfromtxt('../data/uv_vis_data.csv', delimiter=',',
                            skip_header=2)

# --------------- Process data

scaling_fc = (1, 1, 1, 1, 1)
Eg_data, tramitance_sc = functions.process_data(raw_uv_data, scaling_fc)

# --------------- Plot data
offset = 0.5
fig_uv, axis_uv = functions.plot_uv_vis(Eg_data, tramitance_sc, offset)

axis_uv.set_title('Example of UV Vis plotting for GCA Seminar')

# Name the curves
names_curves = ['Material %i' % ind for ind in range(1, 6)]
offset_acum = 0
for name in names_curves:
    axis_uv.text(0.8, offset_acum, name)
    offset_acum += offset

# Save figure
fig_uv.savefig('../results/img/uv_plot_gca.png', dpi=400,
               bbox_to_inches='tight')
