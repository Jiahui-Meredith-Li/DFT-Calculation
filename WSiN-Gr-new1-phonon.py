# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = Hexagonal(5.06585*Angstrom, 40.0*Angstrom)

# Define elements
elements = [Nitrogen, Nitrogen, Nitrogen, Silicon, Silicon, Silicon, Nitrogen,
            Nitrogen, Nitrogen, Tungsten, Tungsten, Tungsten, Nitrogen,
            Nitrogen, Nitrogen, Silicon, Silicon, Silicon, Nitrogen, Nitrogen,
            Nitrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon]

# Define coordinates
fractional_coordinates = [[ 0.441010846625,  0.107858188424,  0.373032883896],
                          [ 0.107678315202,  0.441189833523,  0.373032546368],
                          [ 0.774343501027,  0.774523339329,  0.373035944961],
                          [ 0.77434375302 ,  0.107865778223,  0.385929050659],
                          [ 0.441003952804,  0.441183370646,  0.385929348034],
                          [ 0.107685909038,  0.774521974474,  0.385928355305],
                          [ 0.774358924544,  0.107868960398,  0.429882635037],
                          [ 0.441012901929,  0.441184447875,  0.429882749236],
                          [ 0.107703932885,  0.774525417875,  0.429882262817],
                          [ 0.107694032981,  0.107849839329,  0.461168102713],
                          [ 0.774361925148,  0.441211981444,  0.461166521117],
                          [ 0.441033648486,  0.774523835671,  0.461168261941],
                          [ 0.774378754589,  0.107924615168,  0.492436230835],
                          [ 0.441031680141,  0.441174660701,  0.492436980163],
                          [ 0.107693994511,  0.774494712311,  0.492436967887],
                          [ 0.774402957019,  0.10789975953 ,  0.536356733144],
                          [ 0.441016649199,  0.441193152036,  0.536368417087],
                          [ 0.107769949977,  0.774550183953,  0.536367575751],
                          [ 0.440970422104,  0.107818239438,  0.549245823715],
                          [ 0.107827061561,  0.441246818945,  0.549256328395],
                          [ 0.774394609535,  0.774582824973,  0.549222793993],
                          [ 0.595009987888,  0.177823433518,  0.630208372712],
                          [ 0.094856480904,  0.177725081728,  0.630174830357],
                          [ 0.928098142428,  0.34436929197 ,  0.630200150549],
                          [ 0.428238342056,  0.344513550205,  0.630167507768],
                          [ 0.594823490025,  0.677759802101,  0.630199205341],
                          [ 0.094875959481,  0.677840427567,  0.630167644496],
                          [ 0.928298189733,  0.844499874209,  0.630207750376],
                          [ 0.428257447775,  0.84443780807 ,  0.630174648376]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add tags
bulk_configuration.addTags('Left Interface 0',  [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
                                                 13, 14, 15, 16, 17, 18, 19, 20])
bulk_configuration.addTags('Right Interface 0', [21, 22, 23, 24, 25, 26, 27, 28])

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
k_point_sampling = MonkhorstPackGrid(
    na=11,
    nb=11,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=100.0*Hartree,
    k_point_sampling=k_point_sampling,
    occupation_method=FermiDirac(300.0*Kelvin*boltzmann_constant),
    )

iteration_control_parameters = IterationControlParameters(
    tolerance=1e-08,
    )

#----------------------------------------
# Grimme DFTD3
#----------------------------------------
correction_extension = GrimmeDFTD3(
    exchange_correlation=GGA.PBE,
    maximum_neighbour_distance=30.0*Ang,
    include_three_body_term=False,
    )

calculator = LCAOCalculator(
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    correction_extension=correction_extension,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('WSiN-Gr-new1-phonon', bulk_configuration)

# -------------------------------------------------------------
# Dynamical Matrix
# -------------------------------------------------------------
dynamical_matrix = DynamicalMatrix(
    bulk_configuration,
    filename='WSiN-Gr-new1-phonon',
    object_id='dynamical_matrix',
    repetitions=(3, 3, 1),
    atomic_displacement=0.01*Angstrom,
    acoustic_sum_rule=True,
    finite_difference_method=Central,
    force_tolerance=1e-08*Hartree/Bohr**2,
    processes_per_displacement=None,
    log_filename_prefix='forces_displacement_',
    use_wigner_seitz_scheme=True,
    )
dynamical_matrix.update()

# -------------------------------------------------------------
# Phonon Bandstructure
# -------------------------------------------------------------
phonon_bandstructure = PhononBandstructure(
    configuration=bulk_configuration,
    dynamical_matrix=dynamical_matrix,
    route=['G', 'M', 'K', 'G'],
    points_per_segment=200,
    number_of_bands=All
    )
nlsave('WSiN-Gr-new1-phonon', phonon_bandstructure)
