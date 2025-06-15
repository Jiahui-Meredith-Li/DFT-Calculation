# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Analysis from File
# -------------------------------------------------------------
path = 'PtSe2-5nm-n-55-u10-z-g.hdf5'
configuration = nlread(path, object_id='confs-0.1 V')[0]

# -------------------------------------------------------------
# Projected Local Density Of States
# -------------------------------------------------------------
kpoint_grid = MonkhorstPackGrid(
    na=61,
    )

projected_local_density_of_states = ProjectedLocalDensityOfStates(
    configuration=configuration,
    method=DeviceDensityOfStates,
    energies=numpy.linspace(-2, 2, 401)*eV,
    kpoints=kpoint_grid,
    contributions=All,
    self_energy_calculator=RecursionSelfEnergy(),
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    density_mesh_cutoff=120.0*Hartree,
    processes_per_energy=All,
    )
nlsave('PtSe2-5nm-n-55-u10-LDDOS-off-HP.hdf5', projected_local_density_of_states)
