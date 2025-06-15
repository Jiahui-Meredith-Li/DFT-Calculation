# -*- coding: utf-8 -*-
setVerbosity(MinimalLog)

# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = Hexagonal(3.70084*Angstrom, 40.0*Angstrom)

# Define elements
elements = [Platinum, Platinum, Selenium, Selenium, Selenium, Selenium]

# Define coordinates
fractional_coordinates = [[ 0.7500001372  ,  0.7500001322  ,  0.416709241835],
                          [ 0.083333111333,  0.416666619267,  0.583311416835],
                          [ 0.083333111333,  0.416666619267,  0.45364094558 ],
                          [ 0.7500001372  ,  0.7500001322  ,  0.62024312058 ],
                          [ 0.416666624267,  0.083333116333,  0.54635905442 ],
                          [ 0.416666624267,  0.083333116333,  0.37975687942 ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
k_point_sampling = MonkhorstPackGrid(
    na=33,
    nb=33,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=120.0*Hartree,
    k_point_sampling=k_point_sampling,
    occupation_method=FermiDirac(300.0*Kelvin*boltzmann_constant),
    )

iteration_control_parameters = IterationControlParameters(
    tolerance=1e-06,
    )

calculator = LCAOCalculator(
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('bulk-PtSe2-band-PDOS', bulk_configuration)

# -------------------------------------------------------------
# Optimize Geometry
# -------------------------------------------------------------

constraints = [FixStrain(x=False, y=False, z=True)]

bulk_configuration = OptimizeGeometry(
    bulk_configuration,
    max_forces=0.005*eV/Ang,
    max_stress=0.01*GPa,
    max_steps=200,
    max_step_length=0.2*Ang,
    constraints=constraints,
    trajectory_filename='bulk-PtSe2-band-PDOS_trajectory.hdf5',
    trajectory_interval=5.0*Minute,
    restart_strategy=RestartFromTrajectory(),
    optimizer_method=LBFGS(),
    enable_optimization_stop_file=True,
)
nlsave('bulk-PtSe2-band-PDOS', bulk_configuration)
nlprint(bulk_configuration)

# -------------------------------------------------------------
# Projected Density Of States
# -------------------------------------------------------------
kpoint_grid = MonkhorstPackGrid(
    na=33,
    nb=33,
    )

projected_density_of_states = ProjectedDensityOfStates(
    configuration=bulk_configuration,
    kpoints=kpoint_grid,
    projections=ProjectOnElements,
    energies=numpy.linspace(-2, 2, 401)*eV,
    energy_zero_parameter=FermiLevel,
    bands_above_fermi_level=All,
    spectrum_method=TetrahedronMethod,
)
nlsave('bulk-PtSe2-band-PDOS', projected_density_of_states)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['G', 'K', 'M', 'G'],
    points_per_segment=201,
    bands_above_fermi_level=All,
    method=Full,
    )
nlsave('bulk-PtSe2-band-PDOS', bandstructure)

# -------------------------------------------------------------
# Fat Bandstructure
# -------------------------------------------------------------
fat_bandstructure = FatBandstructure(
    configuration=bulk_configuration,
    route=['G', 'K', 'M', 'G'],
    points_per_segment=201,
    bands_above_fermi_level=All,
    projections=ProjectOnElements,
)
nlsave('bulk-PtSe2-band-PDOS', fat_bandstructure)
