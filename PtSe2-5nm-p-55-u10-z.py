# -*- coding: utf-8 -*-
setVerbosity(MinimalLog)

# -------------------------------------------------------------
# Two-probe Configuration
# -------------------------------------------------------------

# -------------------------------------------------------------
# Left Electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [6.481880572688119, 0.0, 0.0]*Angstrom
vector_b = [0.0, 24.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 3.7423154934959997]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Selenium, Selenium, Platinum, Selenium, Selenium, Platinum]

# Define coordinates
left_electrode_coordinates = [[  2.160589727187,  10.657783575596,   0.935556600656],
                              [  4.321297099466,  13.342226513549,   0.935560670725],
                              [ -0.000006253962,  11.999989910856,   0.935601146092],
                              [  5.401530013531,  10.657783575596,   2.806714347404],
                              [  1.080356813122,  13.342226513549,   2.806718417473],
                              [  3.240934032383,  11.999989910856,   2.80675889284 ]]*Angstrom

# Set up configuration
left_electrode = BulkConfiguration(
    bravais_lattice=left_electrode_lattice,
    elements=left_electrode_elements,
    cartesian_coordinates=left_electrode_coordinates
    )

# -------------------------------------------------------------
# Right Electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [6.481880572688119, 0.0, 0.0]*Angstrom
vector_b = [0.0, 24.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 3.742315493496008]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Selenium, Selenium, Platinum, Selenium, Selenium, Platinum]

# Define coordinates
right_electrode_coordinates = [[  2.160589727187,  10.657783575596,   0.935556600656],
                               [  4.321297099466,  13.342226513549,   0.935560670725],
                               [ -0.000006253962,  11.999989910856,   0.935601146092],
                               [  5.401530013531,  10.657783575596,   2.806714347404],
                               [  1.080356813122,  13.342226513549,   2.806718417473],
                               [  3.240934032383,  11.999989910856,   2.80675889284 ]]*Angstrom

# Set up configuration
right_electrode = BulkConfiguration(
    bravais_lattice=right_electrode_lattice,
    elements=right_electrode_elements,
    cartesian_coordinates=right_electrode_coordinates
    )

# -------------------------------------------------------------
# Central Region
# -------------------------------------------------------------

# Set up lattice
vector_a = [6.481880572688119, 0.0, 0.0]*Angstrom
vector_b = [0.0, 24.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 119.75409579188722]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum,
                           Selenium, Selenium, Platinum, Selenium, Selenium, Platinum]

# Define coordinates
central_region_coordinates = [[   2.160589727187,   10.657783575596,    0.935556600656],
                              [   4.321297099466,   13.342226513549,    0.935560670725],
                              [  -0.000006253962,   11.999989910856,    0.935601146092],
                              [   5.401530013531,   10.657783575596,    2.806714347404],
                              [   1.080356813122,   13.342226513549,    2.806718417473],
                              [   3.240934032383,   11.999989910856,    2.80675889284 ],
                              [   2.160589727187,   10.657783575596,    4.677872094152],
                              [   4.321297099466,   13.342226513549,    4.677876164221],
                              [  -0.000006253962,   11.999989910856,    4.677916639588],
                              [   5.401530013531,   10.657783575596,    6.549029840901],
                              [   1.080356813122,   13.342226513549,    6.54903391097 ],
                              [   3.240934032383,   11.999989910856,    6.549074386337],
                              [   2.160589727187,   10.657783575596,    8.420187587649],
                              [   4.321297099466,   13.342226513549,    8.420191657718],
                              [  -0.000006253962,   11.999989910856,    8.420232133085],
                              [   5.401530013531,   10.657783575596,   10.291345334397],
                              [   1.080356813122,   13.342226513549,   10.291349404466],
                              [   3.240934032383,   11.999989910856,   10.291389879833],
                              [   2.160589727187,   10.657783575596,   12.162503081145],
                              [   4.321297099466,   13.342226513549,   12.162507151214],
                              [  -0.000006253962,   11.999989910856,   12.162547626581],
                              [   5.401530013531,   10.657783575596,   14.033660827894],
                              [   1.080356813122,   13.342226513549,   14.033664897963],
                              [   3.240934032383,   11.999989910856,   14.03370537333 ],
                              [   2.160589727187,   10.657783575596,   15.904818574642],
                              [   4.321297099466,   13.342226513549,   15.904822644711],
                              [  -0.000006253962,   11.999989910856,   15.904863120078],
                              [   5.401530013531,   10.657783575596,   17.77597632139 ],
                              [   1.080356813122,   13.342226513549,   17.775980391459],
                              [   3.240934032383,   11.999989910856,   17.776020866826],
                              [   2.160589727187,   10.657783575596,   19.647134068138],
                              [   4.321297099466,   13.342226513549,   19.647138138207],
                              [  -0.000006253962,   11.999989910856,   19.647178613574],
                              [   5.401530013531,   10.657783575596,   21.518291814887],
                              [   1.080356813122,   13.342226513549,   21.518295884955],
                              [   3.240934032383,   11.999989910856,   21.518336360323],
                              [   2.160589727187,   10.657783575596,   23.389449561635],
                              [   4.321297099466,   13.342226513549,   23.389453631704],
                              [  -0.000006253962,   11.999989910856,   23.389494107071],
                              [   5.401530013531,   10.657783575596,   25.260607308383],
                              [   1.080356813122,   13.342226513549,   25.260611378452],
                              [   3.240934032383,   11.999989910856,   25.260651853819],
                              [   2.160589727187,   10.657783575596,   27.131765055131],
                              [   4.321297099466,   13.342226513549,   27.1317691252  ],
                              [  -0.000006253962,   11.999989910856,   27.131809600567],
                              [   5.401530013531,   10.657783575596,   29.00292280188 ],
                              [   1.080356813122,   13.342226513549,   29.002926871948],
                              [   3.240934032383,   11.999989910856,   29.002967347316],
                              [   2.160589727187,   10.657783575596,   30.874080548628],
                              [   4.321297099466,   13.342226513549,   30.874084618697],
                              [  -0.000006253962,   11.999989910856,   30.874125094064],
                              [   5.401530013531,   10.657783575596,   32.745238295376],
                              [   1.080356813122,   13.342226513549,   32.745242365445],
                              [   3.240934032383,   11.999989910856,   32.745282840812],
                              [   2.160589727187,   10.657783575596,   34.616396042124],
                              [   4.321297099466,   13.342226513549,   34.616400112193],
                              [  -0.000006253962,   11.999989910856,   34.61644058756 ],
                              [   5.401530013531,   10.657783575596,   36.487553788873],
                              [   1.080356813122,   13.342226513549,   36.487557858941],
                              [   3.240934032383,   11.999989910856,   36.487598334309],
                              [   2.160589727187,   10.657783575596,   38.358711535621],
                              [   4.321297099466,   13.342226513549,   38.35871560569 ],
                              [  -0.000006253962,   11.999989910856,   38.358756081057],
                              [   5.401530013531,   10.657783575596,   40.229869282369],
                              [   1.080356813122,   13.342226513549,   40.229873352438],
                              [   3.240934032383,   11.999989910856,   40.229913827805],
                              [   2.160589727187,   10.657783575596,   42.101027029117],
                              [   4.321297099466,   13.342226513549,   42.101031099186],
                              [  -0.000006253962,   11.999989910856,   42.101071574553],
                              [   5.401530013531,   10.657783575596,   43.972184775866],
                              [   1.080356813122,   13.342226513549,   43.972188845934],
                              [   3.240934032383,   11.999989910856,   43.972229321302],
                              [   2.160589727187,   10.657783575596,   45.843342522614],
                              [   4.321297099466,   13.342226513549,   45.843346592683],
                              [  -0.000006253962,   11.999989910856,   45.84338706805 ],
                              [   5.401530013531,   10.657783575596,   47.714500269362],
                              [   1.080356813122,   13.342226513549,   47.714504339431],
                              [   3.240934032383,   11.999989910856,   47.714544814798],
                              [   2.160589727187,   10.657783575596,   49.58565801611 ],
                              [   4.321297099466,   13.342226513549,   49.585662086179],
                              [  -0.000006253962,   11.999989910856,   49.585702561546],
                              [   5.401530013531,   10.657783575596,   51.456815762859],
                              [   1.080356813122,   13.342226513549,   51.456819832927],
                              [   3.240934032383,   11.999989910856,   51.456860308294],
                              [   2.160589727187,   10.657783575596,   53.327973509607],
                              [   4.321297099466,   13.342226513549,   53.327977579676],
                              [  -0.000006253962,   11.999989910856,   53.328018055043],
                              [   5.401530013531,   10.657783575596,   55.199131256355],
                              [   1.080356813122,   13.342226513549,   55.199135326424],
                              [   3.240934032383,   11.999989910856,   55.199175801791],
                              [   2.160589727187,   10.657783575596,   57.070289003103],
                              [   4.321297099466,   13.342226513549,   57.070293073172],
                              [  -0.000006253962,   11.999989910856,   57.070333548539],
                              [   5.401530013531,   10.657783575596,   58.941446749851],
                              [   1.080356813122,   13.342226513549,   58.94145081992 ],
                              [   3.240934032383,   11.999989910856,   58.941491295287],
                              [   2.160589727187,   10.657783575596,   60.8126044966  ],
                              [   4.321297099466,   13.342226513549,   60.812608566669],
                              [  -0.000006253962,   11.999989910856,   60.812649042036],
                              [   5.401530013531,   10.657783575596,   62.683762243348],
                              [   1.080356813122,   13.342226513549,   62.683766313417],
                              [   3.240934032383,   11.999989910856,   62.683806788784],
                              [   2.160589727187,   10.657783575596,   64.554919990096],
                              [   4.321297099466,   13.342226513549,   64.554924060165],
                              [  -0.000006253962,   11.999989910856,   64.554964535532],
                              [   5.401530013531,   10.657783575596,   66.426077736844],
                              [   1.080356813122,   13.342226513549,   66.426081806913],
                              [   3.240934032383,   11.999989910856,   66.42612228228 ],
                              [   2.160589727187,   10.657783575596,   68.297235483593],
                              [   4.321297099466,   13.342226513549,   68.297239553662],
                              [  -0.000006253962,   11.999989910856,   68.297280029029],
                              [   5.401530013531,   10.657783575596,   70.168393230341],
                              [   1.080356813122,   13.342226513549,   70.16839730041 ],
                              [   3.240934032383,   11.999989910856,   70.168437775777],
                              [   2.160589727187,   10.657783575596,   72.039550977089],
                              [   4.321297099466,   13.342226513549,   72.039555047158],
                              [  -0.000006253962,   11.999989910856,   72.039595522525],
                              [   5.401530013531,   10.657783575596,   73.910708723837],
                              [   1.080356813122,   13.342226513549,   73.910712793906],
                              [   3.240934032383,   11.999989910856,   73.910753269273],
                              [   2.160589727187,   10.657783575596,   75.781866470586],
                              [   4.321297099466,   13.342226513549,   75.781870540655],
                              [  -0.000006253962,   11.999989910856,   75.781911016022],
                              [   5.401530013531,   10.657783575596,   77.653024217334],
                              [   1.080356813122,   13.342226513549,   77.653028287403],
                              [   3.240934032383,   11.999989910856,   77.65306876277 ],
                              [   2.160589727187,   10.657783575596,   79.524181964082],
                              [   4.321297099466,   13.342226513549,   79.524186034151],
                              [  -0.000006253962,   11.999989910856,   79.524226509518],
                              [   5.401530013531,   10.657783575596,   81.39533971083 ],
                              [   1.080356813122,   13.342226513549,   81.395343780899],
                              [   3.240934032383,   11.999989910856,   81.395384256266],
                              [   2.160589727187,   10.657783575596,   83.266497457579],
                              [   4.321297099466,   13.342226513549,   83.266501527648],
                              [  -0.000006253962,   11.999989910856,   83.266542003015],
                              [   5.401530013531,   10.657783575596,   85.137655204327],
                              [   1.080356813122,   13.342226513549,   85.137659274396],
                              [   3.240934032383,   11.999989910856,   85.137699749763],
                              [   2.160589727187,   10.657783575596,   87.008812951075],
                              [   4.321297099466,   13.342226513549,   87.008817021144],
                              [  -0.000006253962,   11.999989910856,   87.008857496511],
                              [   5.401530013531,   10.657783575596,   88.879970697823],
                              [   1.080356813122,   13.342226513549,   88.879974767892],
                              [   3.240934032383,   11.999989910856,   88.880015243259],
                              [   2.160589727187,   10.657783575596,   90.751128444572],
                              [   4.321297099466,   13.342226513549,   90.751132514641],
                              [  -0.000006253962,   11.999989910856,   90.751172990008],
                              [   5.401530013531,   10.657783575596,   92.62228619132 ],
                              [   1.080356813122,   13.342226513549,   92.622290261389],
                              [   3.240934032383,   11.999989910856,   92.622330736756],
                              [   2.160589727187,   10.657783575596,   94.493443938068],
                              [   4.321297099466,   13.342226513549,   94.493448008137],
                              [  -0.000006253962,   11.999989910856,   94.493488483504],
                              [   5.401530013531,   10.657783575596,   96.364601684816],
                              [   1.080356813122,   13.342226513549,   96.364605754885],
                              [   3.240934032383,   11.999989910856,   96.364646230252],
                              [   2.160589727187,   10.657783575596,   98.235759431565],
                              [   4.321297099466,   13.342226513549,   98.235763501634],
                              [  -0.000006253962,   11.999989910856,   98.235803977001],
                              [   5.401530013531,   10.657783575596,  100.106917178313],
                              [   1.080356813122,   13.342226513549,  100.106921248382],
                              [   3.240934032383,   11.999989910856,  100.106961723749],
                              [   2.160589727187,   10.657783575596,  101.978074925061],
                              [   4.321297099466,   13.342226513549,  101.97807899513 ],
                              [  -0.000006253962,   11.999989910856,  101.978119470497],
                              [   5.401530013531,   10.657783575596,  103.849232671809],
                              [   1.080356813122,   13.342226513549,  103.849236741878],
                              [   3.240934032383,   11.999989910856,  103.849277217245],
                              [   2.160589727187,   10.657783575596,  105.720390418558],
                              [   4.321297099466,   13.342226513549,  105.720394488627],
                              [  -0.000006253962,   11.999989910856,  105.720434963994],
                              [   5.401530013531,   10.657783575596,  107.591548165306],
                              [   1.080356813122,   13.342226513549,  107.591552235375],
                              [   3.240934032383,   11.999989910856,  107.591592710742],
                              [   2.160589727187,   10.657783575596,  109.462705912054],
                              [   4.321297099466,   13.342226513549,  109.462709982123],
                              [  -0.000006253962,   11.999989910856,  109.46275045749 ],
                              [   5.401530013531,   10.657783575596,  111.333863658802],
                              [   1.080356813122,   13.342226513549,  111.333867728871],
                              [   3.240934032383,   11.999989910856,  111.333908204238],
                              [   2.160589727187,   10.657783575596,  113.205021405551],
                              [   4.321297099466,   13.342226513549,  113.20502547562 ],
                              [  -0.000006253962,   11.999989910856,  113.205065950987],
                              [   5.401530013531,   10.657783575596,  115.076179152299],
                              [   1.080356813122,   13.342226513549,  115.076183222368],
                              [   3.240934032383,   11.999989910856,  115.076223697735],
                              [   2.160589727187,   10.657783575596,  116.947336899047],
                              [   4.321297099466,   13.342226513549,  116.947340969116],
                              [  -0.000006253962,   11.999989910856,  116.947381444483],
                              [   5.401530013531,   10.657783575596,  118.818494645795],
                              [   1.080356813122,   13.342226513549,  118.818498715864],
                              [   3.240934032383,   11.999989910856,  118.818539191231]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

# Add metallic region
metallic_region_0 = BoxRegion(
    0.0*Volt,
    xmin = 0.0*Angstrom, xmax = 6.481880572688119*Angstrom,
    ymin = 1.66*Angstrom, ymax = 4.66*Angstrom,
    zmin = 34.88*Angstrom, zmax = 84.88*Angstrom,
)

metallic_region_1 = BoxRegion(
    0.0*Volt,
    xmin = 0.0*Angstrom, xmax = 6.481880572688119*Angstrom,
    ymin = 19.34*Angstrom, ymax = 22.34*Angstrom,
    zmin = 34.88*Angstrom, zmax = 84.88*Angstrom,
)

metallic_regions = [metallic_region_0, metallic_region_1]
central_region.setMetallicRegions(metallic_regions)

# Add dielectric region
dielectric_region_0 = BoxRegion(
    3.9,
    xmin = 0.0*Angstrom, xmax = 6.481880572688119*Angstrom,
    ymin = 4.66*Angstrom, ymax = 8.66*Angstrom,
    zmin = -3.7423154934959997*Angstrom, zmax = 123.496*Angstrom,
)

dielectric_region_1 = BoxRegion(
    3.9,
    xmin = 0.0*Angstrom, xmax = 6.481880572688119*Angstrom,
    ymin = 15.34*Angstrom, ymax = 19.34*Angstrom,
    zmin = -3.7423154934959997*Angstrom, zmax = 123.496*Angstrom,
)

dielectric_regions = [dielectric_region_0, dielectric_region_1]
central_region.setDielectricRegions(dielectric_regions)

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode],
    equivalent_electrode_lengths=[7.484630986992, 7.484630986992]*Angstrom,
    transverse_electrode_repetitions=[[1, 1], [1, 1]],
    )

# Add tags
device_configuration.addTags('left',  [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
                                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                       26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38])
device_configuration.addTags('right', [153, 154, 155, 156, 157, 158, 159, 160, 161, 162,
                                       163, 164, 165, 166, 167, 168, 169, 170, 171, 172,
                                       173, 174, 175, 176, 177, 178, 179, 180, 181, 182,
                                       183, 184, 185, 186, 187, 188, 189, 190, 191])

doping_density = 5e+13
doping_density1 = 5e+13

# Surface per atom in a bulk Bismuth crystal
atom_surface =0.1667*24.2572691616*Angstrom**2 
# Volume of one Sb atom in units of cm^2
atom_surface_cm = float(atom_surface/(0.01*Meter)**2)

# Calculate charge per atom
doping = doping_density * atom_surface_cm
doping1 = doping_density1 * atom_surface_cm
# Add external potential

external_potential = AtomicCompensationCharge([('left', -1*doping),('right', -1*doping1)])

central_region.setExternalPotential(external_potential) 

left_electrode.setExternalPotential(AtomicCompensationCharge([(Platinum,-1*doping),(Selenium,-1*doping)]))

right_electrode.setExternalPotential(AtomicCompensationCharge([(Platinum, -1*doping1),(Selenium,-1*doping1)]))


# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Numerical Accuracy Settings
#----------------------------------------
left_electrode_k_point_sampling = MonkhorstPackGrid(
    na=50,
    nc=250,
    )
left_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=120.0*Hartree,
    k_point_sampling=left_electrode_k_point_sampling,
    occupation_method=FermiDirac(300.0*Kelvin*boltzmann_constant),
    )

right_electrode_k_point_sampling = MonkhorstPackGrid(
    na=50,
    nc=250,
    )
right_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=120.0*Hartree,
    k_point_sampling=right_electrode_k_point_sampling,
    occupation_method=FermiDirac(300.0*Kelvin*boltzmann_constant),
    )

device_k_point_sampling = MonkhorstPackGrid(
    na=50,
    nc=1,
    )
device_numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=120.0*Hartree,
    k_point_sampling=device_k_point_sampling,
    occupation_method=FermiDirac(300.0*Kelvin*boltzmann_constant),
    )

#----------------------------------------
# Iteration Control Settings
#----------------------------------------
left_electrode_iteration_control_parameters = IterationControlParameters(
    max_steps=200,
    )

right_electrode_iteration_control_parameters = IterationControlParameters(
    max_steps=200,
    )

device_iteration_control_parameters = IterationControlParameters(
    max_steps=200,
    )

#----------------------------------------
# Poisson Solver Settings
#----------------------------------------
left_electrode_poisson_solver = MultigridSolver(
    boundary_conditions=[[PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [NeumannBoundaryCondition(),NeumannBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()]]
    )

right_electrode_poisson_solver = MultigridSolver(
    boundary_conditions=[[PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [NeumannBoundaryCondition(),NeumannBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()]]
    )

device_poisson_solver = MultigridSolver(
    boundary_conditions=[[PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [NeumannBoundaryCondition(),NeumannBoundaryCondition()],
                         [DirichletBoundaryCondition(),DirichletBoundaryCondition()]]
    )

#----------------------------------------
# Contour Integral Settings
#----------------------------------------
equilibrium_contour = SemiCircleContour(
    integral_lower_bound=4.67818892428*Hartree,
    circle_points=30,
    )
contour_parameters = ContourParameters(
    equilibrium_contour=equilibrium_contour,
    )

#----------------------------------------
# Electrode Calculators
#----------------------------------------
left_electrode_calculator = LCAOCalculator(
    numerical_accuracy_parameters=left_electrode_numerical_accuracy_parameters,
    iteration_control_parameters=left_electrode_iteration_control_parameters,
    poisson_solver=left_electrode_poisson_solver,
    )

right_electrode_calculator = LCAOCalculator(
    numerical_accuracy_parameters=right_electrode_numerical_accuracy_parameters,
    iteration_control_parameters=right_electrode_iteration_control_parameters,
    poisson_solver=right_electrode_poisson_solver,
    )

#----------------------------------------
# Device Calculator
#----------------------------------------
calculator = DeviceLCAOCalculator(
    numerical_accuracy_parameters=device_numerical_accuracy_parameters,
    iteration_control_parameters=device_iteration_control_parameters,
    poisson_solver=device_poisson_solver,
    contour_parameters=contour_parameters,
    electrode_calculators=
        [left_electrode_calculator, right_electrode_calculator],
    )

device_configuration.setCalculator(calculator)
nlprint(device_configuration)
device_configuration.update()
nlsave('PtSe2-5nm-p-55-u10-z.hdf5', device_configuration)
