# Figure scripts

Scripts for the schematic figures. Each script writes its figure (pdf, svg, png) next to itself.

- `R119/make_fig_pipeline_R119.py` and `R119/make_fig_overview_R119.py` (shared style `style_R119.py`).
- `R130/make_fig2_R130.py A|B` (two variants of the pipeline figure; style `style_R119.py`).

The data figures of the UR5e experiment are produced by the `make_figure*.py` scripts in `../ur5e_kinematic_verification/`. Figure 8 is produced by `../evidence_matrix/matrix_summary.py`.
Requires Python 3 with matplotlib (tested with 3.11.2).
