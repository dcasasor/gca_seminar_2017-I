import numpy as np
import uv_vis_functions as uvfuncs


# --------------- Import data
raw_uv_data = np.genfromtxt('../data/uv_vis_data.csv', delimiter=',',
                            skip_header=2)

# --------------- Process data

scaling_fc = (1, 1, 1, 1, 1)
Eg_data, tramitance_sc = uvfuncs.process_data(raw_uv_data, scaling_fc)

# Export processed data
np.savetxt('../results/tables/Eg_data.csv', Eg_data, delimiter=',')
np.savetxt('../results/tables/tramitance_sc.csv', tramitance_sc, delimiter=',')

# --------------- Plot data
offset = 20
fig_uv, axis_uv = uvfuncs.plot_uv_vis(Eg_data, tramitance_sc, offset)

# Edit axes
axis_uv.set_title('Example of UV Vis plotting for GCA Seminar')
axis_uv.set_xlim(3, 6.2)
axis_uv.set_ylim(ymax=110)
axis_uv.yaxis.set_ticks([])  # Remove yticks

# Name the curves
names_curves = ['Material %i' % ind for ind in range(1, 6)]
offset_acum = 1
for name in names_curves:
    axis_uv.text(3.2, offset_acum, name)
    offset_acum += offset

# Save figure
fig_uv.savefig('../results/img/uv_plot_gca.png', dpi=400,
               bbox_to_inches='tight')
