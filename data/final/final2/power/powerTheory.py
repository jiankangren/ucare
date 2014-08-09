#!/usr/bin/python26 -B
"""
_simulator_

Created by Bjorn Barrefors on 26/9/2013

University of Nebraska-Lincoln
"""
###############################################################################
#                                                                             #
#                             S I M U L A T O R                               #
#                                                                             #
###############################################################################

import sys
import math

cluster = [{'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.0, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.01, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.02, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.029999999999999999, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.040000000000000001, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.050000000000000003, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.060000000000000005, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.070000000000000007, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.080000000000000002, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.089999999999999997, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.099999999999999992, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.10999999999999999, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.11999999999999998, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.12999999999999998, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.13999999999999999, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.14999999999999999, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.16, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.17000000000000001, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.18000000000000002, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}, {'a1': -0.0040000000000000001, 'u1': 276.60000000000002, 'u0': 402.89999999999998, 'u2': 114.0, 'util': 4, 'a3': 0.29770000000000002, 'a2': 5.5271999999999997, 'a5': -13.2765, 'a4': 0.19000000000000003, 'a6': 56.424199999999999, 't_amb': -10.0, 'r': 0.73099999999999998}]

freqs = [[1.1455174685412723, 1.3955013979390143, 1.5072420769872896, 1.5166723046054347, 1.8131716345762372, 1.9282384661683278, 2.0114396851774212, 2.1668387931009789, 2.3287084374004956, 2.3907374865141269], [1.1636631847707608, 1.3644676524293884, 1.4254966438619607, 1.6025155717253901, 1.7190288548138477, 1.7778906103152423, 1.9594342368779418, 2.1579795041824892, 2.2262206160626872, 2.3683836356552379], [1.1584889807435466, 1.3276929674839932, 1.4200437227630214, 1.6088333508835204, 1.7262984408648441, 1.9156836348129769, 1.99026881733761, 2.108613587700332, 2.2586729164987198, 2.3791298861142316], [1.1817135121807658, 1.2679279384353686, 1.5309113677835609, 1.5629893234904098, 1.655879651027707, 1.9286478751152547, 2.0393278896135048, 2.2178369777504972, 2.2321852752356204, 2.4779647766795549], [1.1911821085493088, 1.2872687116457628, 1.455490657914861, 1.5990331596639162, 1.6847709457404187, 1.8849154722564385, 2.0929960889624244, 2.2002784308022094, 2.2208617074052368, 2.4870887809963085], [1.2270097529544528, 1.2998911905308648, 1.3930189480193556, 1.5219855323859162, 1.7007887846113077, 1.9066559840571871, 1.9398271633647666, 2.08195745218192, 2.1615201197484684, 2.3390325061340702], [1.1871135719964823, 1.3222493387135164, 1.4515412549709126, 1.5413497258904798, 1.759147453028967, 1.9394946618166298, 2.0317871567293588, 2.0557210712422904, 2.1627403269638386, 2.3503764351574241], [1.1735132198054812, 1.3773385008155421, 1.5201198060296339, 1.5288082981188456, 1.7523069737622563, 1.8087220756602944, 1.9558063897630651, 2.0747862231630432, 2.2651577640229394, 2.4188486793091677], [1.1432406964596398, 1.371236212433985, 1.4773022289623603, 1.617017872392817, 1.7766618551008035, 1.9402231938490877, 2.0064038609803361, 2.1473682203967717, 2.3205980303927816, 2.3516772603935516], [1.1648794262170785, 1.344794567985595, 1.5190321112660305, 1.6258523600704089, 1.7576742137447654, 1.8935941336670115, 2.0131812282522299, 2.1594474245260433, 2.3384141638386735, 2.3843708273072108], [1.1461669363451248, 1.2776346530552263, 1.4774865685981697, 1.6417141457444708, 1.6458752899550559, 1.9152279995203423, 1.9365842984133361, 2.1701216079023156, 2.2177256129626537, 2.3089737993433381], [1.23080313321501, 1.3164365422845306, 1.5111072521005711, 1.660329760268358, 1.7196165288252625, 1.8634942665312473, 2.0898308234887688, 2.097993052773818, 2.3332320995449805, 2.34760777016883], [1.1984955010547511, 1.3140991767649515, 1.5032822218235284, 1.6643643766827168, 1.7997163420884683, 1.8021540348009768, 1.985012844646056, 2.1096993489508296, 2.2846986470355626, 2.3951269338611203], [1.1447422597281627, 1.3583248390335614, 1.5255552683355014, 1.5905639863696441, 1.7265432630046085, 1.8881987955257133, 2.0301794122216372, 2.0879174353045191, 2.2860941082448476, 2.3639090959669953], [1.2436479855397071, 1.3219257079416438, 1.4052081830270466, 1.5633018200091333, 1.6479275488087384, 1.836715793550513, 1.90869754210954, 2.1920253209588978, 2.2920993648728314, 2.3773809285034599], [1.1452026800129886, 1.3514137377085824, 1.397953520433749, 1.586783850126197, 1.6845818600141034, 1.9105503973357525, 2.0476721402779301, 2.0489345402594843, 2.1877297974047232, 2.2791900289569953], [1.1514773931348787, 1.3299052935776552, 1.4630278763586664, 1.6076235365822436, 1.7648272483912901, 1.813354837700923, 2.0767417409360882, 2.1520571688737, 2.1777566765413954, 2.2963846462415134], [1.2468001278364726, 1.3243311047062662, 1.4691206267471923, 1.6453963569079559, 1.7565575051214097, 1.8718875701509754, 1.8970144951124062, 2.1923914401382771, 2.2800271469341671, 2.3771675404574681], [1.1563279056338693, 1.3297327224404945, 1.394144811962396, 1.5859928984511844, 1.797854224824418, 1.8908727715079796, 2.0451456859002697, 2.0643730813533967, 2.1505052370106816, 2.4521305231079844], [1.2320807879209827, 1.2686267354162502, 1.4486804803816744, 1.5803685488260644, 1.7761011843814458, 1.8017272063881613, 2.0673340355337166, 2.1862458071773316, 2.2717012832821721, 2.3355247743911018]]

def maxTemp(core, freq):
    # Based on cpu properties and frequency, return the maximum possible temperature for core
    f = freq
    a1 = cluster[core]['a1']
    a2 = cluster[core]['a2']
    a3 = cluster[core]['a3']
    a4 = cluster[core]['a4']
    a5 = cluster[core]['a5']
    a6 = cluster[core]['a6']
    r = cluster[core]['r']
    t_amb = cluster[core]['t_amb']
    A = a1*r
    B = a3*r*f + a4*r - 1
    C = a2*r*math.pow(f,2) + a5*f*r + a6*r + t_amb
    max_temp = -B/(2*A) - math.sqrt(math.pow(B,2) - 4*A*C)/(2*A)
    return max_temp

def power(core, freq, util):
    # Based on cpu properties and a frequency, return the power consumption at maximum temperature
    f = freq
    if f == 1.197000:
        u1 = cluster[core]['u1']
        u2 = cluster[core]['u2']
        u0 = cluster[core]['u0']
        power1 = 0.1*(u1*util - u2*math.pow(util,2) + u0)
        return power1
    a1 = cluster[core]['a1']
    a2 = cluster[core]['a2']
    a3 = cluster[core]['a3']
    a4 = cluster[core]['a4']
    a5 = cluster[core]['a5']
    a6 = cluster[core]['a6']
    r = cluster[core]['r']
    t_amb = cluster[core]['t_amb']
    t = maxTemp(core, freq)
    power1 = a1*math.pow(t,2) + a2*math.pow(f,2) + a3*f*t + a4*t + a5*f + a6
    return power1

################################################################################
#                                                                              #
#                                 M A I N                                      #
#                                                                              #
################################################################################

def main():
    """
    __main__


    """
    numTasks = [250, 350, 450]
    totUtils = [25, 35, 45]
    algs = ['HyMWGA', 'BaB']

    files = []

    for u in totUtils:
        for t in numTasks:
            for a in algs:
                files.append('u%dt%da%s' % (u, t, a))

    fd = open('Schedule', 'r')
    lines = fd.readlines()
    j = 0
    i = 1
    for line in lines:
        line = line.strip()
        l = line.partition("\t")
        cpu = l[0]
        if (i == 21):
            i = 1
            j += 1
        if (cpu == str(i)):
            if l[2] == str(0):
                p = 0
            else:
                u = float(l[2])
                u = u/4
                for f in freqs[i-1]:
                    if (f/freqs[i-1][9]) >= (u):
                        p = power(i - 1, f, u)
                        break
            fw = open(files[j], 'a')
            fw.write(str(p) + '\n')
            fw.close()
            i += 1
    fd.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())