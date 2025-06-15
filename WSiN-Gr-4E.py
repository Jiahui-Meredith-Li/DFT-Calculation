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
fractional_coordinates = [[ 0.437565297644,  0.1042451372  ,  0.373035920234],
                          [ 0.104229207936,  0.437578943114,  0.373035890549],
                          [ 0.770895865674,  0.770910636926,  0.373037452681],
                          [ 0.770901459693,  0.104252465569,  0.385929283793],
                          [ 0.437556952624,  0.43757255864 ,  0.385927685963],
                          [ 0.104237387105,  0.770916339943,  0.385928314396],
                          [ 0.770906721718,  0.104270105768,  0.429881137015],
                          [ 0.437572947654,  0.437617036556,  0.429880881031],
                          [ 0.104235278104,  0.770948721024,  0.429880941124],
                          [ 0.104251910594,  0.104287731203,  0.461163785758],
                          [ 0.770902348344,  0.437621102751,  0.461161988308],
                          [ 0.43755625694 ,  0.770940279214,  0.461163557726],
                          [ 0.770902926004,  0.104262510233,  0.492431366396],
                          [ 0.437641713336,  0.437673088728,  0.492432072803],
                          [ 0.104156214843,  0.770923544484,  0.492432080503],
                          [ 0.770883983877,  0.104266959907,  0.536349824365],
                          [ 0.437546843469,  0.437650731054,  0.5363626597  ],
                          [ 0.104209133679,  0.77098081459 ,  0.53636242883 ],
                          [ 0.437451653825,  0.104235999885,  0.549228866771],
                          [ 0.104310258361,  0.4376669743  ,  0.549230746276],
                          [ 0.770880332062,  0.771000879077,  0.549244298629],
                          [ 0.604151171385,  0.187261327922,  0.630210210822],
                          [ 0.103981598478,  0.187149194496,  0.630184181637],
                          [ 0.937194092293,  0.353784512091,  0.630210435706],
                          [ 0.437343420537,  0.353932702998,  0.630176231687],
                          [ 0.603947199371,  0.687190627579,  0.630212028882],
                          [ 0.104001827079,  0.687260587266,  0.630176309545],
                          [ 0.937398101772,  0.853917774898,  0.630211936978],
                          [ 0.437363658216,  0.853841916218,  0.63018410492 ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add metallic region
metallic_region_0 = BoxRegion(
    0.0*Volt,
    xmin = 0.0*Angstrom, xmax = 5.1*Angstrom,
    ymin = -5.1*Angstrom, ymax = 5.1*Angstrom,
    zmin = 0.0*Angstrom, zmax = 1.0*Angstrom,
)

metallic_region_1 = BoxRegion(
    16.0*Volt,
    xmin = 0.0*Angstrom, xmax = 5.1*Angstrom,
    ymin = -5.1*Angstrom, ymax = 5.1*Angstrom,
    zmin = 39.0*Angstrom, zmax = 40.0*Angstrom,
)

metallic_regions = [metallic_region_0, metallic_region_1]
bulk_configuration.setMetallicRegions(metallic_regions)

# Add tags
bulk_configuration.addTags('Left Interface 0',  [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
                                                 13, 14, 15, 16, 17, 18, 19, 20])
bulk_configuration.addTags('Right Interface 0', [21, 22, 23, 24, 25, 26, 27, 28])

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = HybridGGA.HSE06

k_point_sampling = MonkhorstPackGrid(
    na=15,
    nb=15,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=100.0*Hartree,
    k_point_sampling=k_point_sampling,
    occupation_method=FermiDirac(300.0*Kelvin*boltzmann_constant),
    )

iteration_control_parameters = IterationControlParameters(
    tolerance=1e-05,
    )

poisson_solver = MultigridSolver(
    boundary_conditions=[[PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [DirichletBoundaryCondition(),DirichletBoundaryCondition()]]
    )

#----------------------------------------
# Grimme DFTD3
#----------------------------------------
correction_extension = GrimmeDFTD3(
    exchange_correlation=HybridGGA.HSE06,
    maximum_neighbour_distance=30.0*Ang,
    include_three_body_term=False,
    )

calculator = LCAOCalculator(
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    poisson_solver=poisson_solver,
    correction_extension=correction_extension,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('WSiN-Gr-4E.hdf5', bulk_configuration)

# -------------------------------------------------------------
# Fat Bandstructure
# -------------------------------------------------------------
fat_bandstructure = FatBandstructure(
    configuration=bulk_configuration,
    route=['G', 'M', 'K', 'G'],
    points_per_segment=60,
    bands_above_fermi_level=All,
    projections=ProjectOnTags,
)
nlsave('WSiN-Gr-4E.hdf5', fat_bandstructure)
