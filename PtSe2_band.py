# -*- coding: utf-8 -*-
setVerbosity(MinimalLog)

# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = Hexagonal(3.742315493496491*Angstrom, 24.0*Angstrom)

# Define elements
elements = [Platinum, Selenium, Selenium]

# Define coordinates
fractional_coordinates = [[ 0.249874871094,  0.249872941419,  0.499999579619],
                          [ 0.583189730823,  0.9165364505  ,  0.555926104731],
                          [ 0.916534398082,  0.583189608081,  0.44407431565 ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Basis Set
#----------------------------------------
basis_set = [
    BasisGGAPseudoDojo.Selenium_High,
    BasisGGAPseudoDojo.Platinum_High,
    ]

#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = GGA.BLYP

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
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('PtSe2_band.hdf5', bulk_configuration)

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
nlsave('PtSe2_band.hdf5', bandstructure)

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
nlsave('PtSe2_band.hdf5', fat_bandstructure)

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
nlsave('PtSe2_band.hdf5', projected_density_of_states)
