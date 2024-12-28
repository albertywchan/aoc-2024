from parse import search

NUM_Z_WIRES = 45
SWAPS = {
    "z05": "gdd",
    "gdd": "z05",
    "z09": "cwt",
    "cwt": "z09",
    "css": "jmv",
    "jmv": "css",
    "pqt": "z37",
    "z37": "pqt",
}


def part_one():
    with open("input.txt") as file:
        wireInputs, gateInputs = file.read().split("\n\n")
        wires = dict()
        for input in wireInputs.splitlines():
            wire, value = input.split(":")
            wires[wire] = int(value.strip())
        gateInputs = gateInputs.splitlines()
        numGates = len(gateInputs)
        bits = [None] * (NUM_Z_WIRES + 1)
        completed = set()
        while len(completed) < numGates:
            for i in range(numGates):
                input1, gate, input2, output = search(
                    "{:w} {:w} {:w} -> {:w}", gateInputs[i]
                )
                if input1 in wires and input2 in wires and output not in completed:
                    wire1, wire2 = wires[input1], wires[input2]
                    if gate == "AND":
                        wires[output] = wire1 & wire2
                    elif gate == "OR":
                        wires[output] = wire1 | wire2
                    else:
                        wires[output] = wire1 ^ wire2
                    if output.startswith("z") and not bits[int(output[1:])]:
                        bits[int(output[1:])] = wires[output]
                    completed.add(output)
        bits.reverse()
        binaryNumber = "".join(map(str, bits))
        decimalNumber = int(binaryNumber, 2)
        print(decimalNumber)


def part_two():
    with open("input.txt") as file:
        _, gateInputs = file.read().split("\n\n")
        assert (
            gateInputs
            == """kgv OR rdq -> stt
y00 AND x00 -> pjf
y13 XOR x13 -> wqh
y21 AND x21 -> ccs
wws AND cds -> kgv
x09 AND y09 -> sgj
x14 XOR y14 -> tnm
msn OR ssj -> vfb
cwt AND wfd -> wjk
y41 XOR x41 -> fsh
jhn AND hjd -> nfk
kvg OR sgj -> z09
trk OR trs -> nvk
jnf XOR wgh -> cwt
bkg AND tgw -> vrw
dvr OR wtv -> dwg
vch AND css -> cjn
wmf AND mdn -> qnn
gbv AND pth -> hns
jgb AND qbm -> jdb
x05 XOR y05 -> wcq
gtv OR pjr -> crc
y23 XOR x23 -> vph
jwq AND fqf -> tgv
y38 XOR x38 -> ghm
dgc OR ntm -> hrs
y22 XOR x22 -> tgw
stt AND wcr -> krw
gvt AND kns -> nmv
y03 AND x03 -> scc
x42 XOR y42 -> vcf
jbj OR rrc -> cvn
pth XOR gbv -> z17
hpb OR scc -> ngk
mvf XOR hrs -> z29
x17 XOR y17 -> gbv
y22 AND x22 -> kkq
y37 XOR x37 -> vcr
sqq XOR fgt -> z36
wcq AND knc -> gnw
krw OR hbj -> nkt
hpm OR mrw -> knc
vts OR hsk -> vfw
y19 AND x19 -> sjt
qbm XOR jgb -> z21
x28 AND y28 -> ntm
bwv XOR wsh -> z12
y43 XOR x43 -> cch
vfb XOR fpt -> z03
qkc OR sqw -> hjd
vqr OR ndj -> fqf
mcf AND cch -> kcq
qjb XOR kjr -> z35
y44 AND x44 -> mgv
vfw AND mqt -> ndj
x34 XOR y34 -> jwk
jnf AND wgh -> kvg
x41 AND y41 -> dqw
x02 AND y02 -> msn
vfb AND fpt -> hpb
swb AND qvq -> gtv
vnq XOR wqh -> z13
trn XOR pgk -> z06
cvn XOR gmp -> z30
vfw XOR mqt -> z07
ctf XOR tnm -> z14
hwb OR wmb -> ctf
ghm XOR hjg -> z38
wkt OR qjj -> tgj
kcq OR dcc -> cpw
x06 XOR y06 -> pgk
cjn OR jmv -> jgb
y00 XOR x00 -> z00
mdn XOR wmf -> z39
y36 AND x36 -> gst
tgw XOR bkg -> z22
tgv OR cfk -> wgh
y25 XOR x25 -> ktd
wdj AND fvw -> dvr
kbk OR wpm -> sgn
x44 XOR y44 -> dph
wsh AND bwv -> tnr
y24 XOR x24 -> skp
y30 XOR x30 -> gmp
y05 AND x05 -> z05
x11 AND y11 -> rsw
qnn OR rrn -> fvw
x34 AND y34 -> hgg
wcs OR rpr -> fgt
x07 AND y07 -> vqr
fvw XOR wdj -> z40
y29 AND x29 -> rrc
fsh XOR dwg -> z41
cpw XOR dph -> z44
y32 XOR x32 -> hbg
pjf AND fcg -> vms
cwt XOR wfd -> z10
x27 AND y27 -> hbj
y04 AND x04 -> mrw
vcf XOR btn -> z42
vnq AND wqh -> wmb
x43 AND y43 -> dcc
vrw OR kkq -> jjr
cds XOR wws -> z26
x39 XOR y39 -> wmf
y29 XOR x29 -> mvf
rfn OR pmm -> mhh
y35 XOR x35 -> qjb
ngk XOR vvf -> z04
kht OR gfk -> cds
bgb OR tnr -> vnq
kns XOR gvt -> z33
sjt OR pbd -> vch
hvp OR nfk -> pth
x38 AND y38 -> dtt
y18 AND x18 -> pjr
x07 XOR y07 -> mqt
gst OR bmm -> nwb
y21 XOR x21 -> qbm
jwk AND gfr -> cph
nvk XOR brp -> z31
x17 AND y17 -> nkr
sqt OR nqs -> kns
qbs OR vht -> sfw
brp AND nvk -> rfn
hrs AND mvf -> jbj
x12 AND y12 -> bgb
y36 XOR x36 -> sqq
jdb OR ccs -> bkg
x04 XOR y04 -> vvf
y19 XOR x19 -> vmj
vms OR vpb -> kmq
y35 AND x35 -> wcs
vph AND jjr -> qbs
fgt AND sqq -> bmm
vcf AND btn -> fbb
wjk OR ktk -> kmn
x08 AND y08 -> cfk
y01 XOR x01 -> fcg
y23 AND x23 -> vht
kgm AND nkt -> dgc
swb XOR qvq -> z18
x09 XOR y09 -> jnf
cch XOR mcf -> z43
sgn XOR smv -> z15
y40 XOR x40 -> wdj
gnw OR gdd -> trn
dgn OR pqt -> hjg
y30 AND x30 -> trs
ngk AND vvf -> hpm
y12 XOR x12 -> bwv
kmn XOR dmk -> z11
y20 AND x20 -> css
stt XOR wcr -> z27
vph XOR jjr -> z23
nmv OR wjj -> gfr
x02 XOR y02 -> jdc
y28 XOR x28 -> kgm
gfr XOR jwk -> z34
x16 AND y16 -> hvp
gkb OR mgv -> z45
mhh AND hbg -> sqt
fqf XOR jwq -> z08
x13 AND y13 -> hwb
vmj AND crc -> pbd
dwg AND fsh -> brb
sfw AND skp -> qjj
knc XOR wcq -> gdd
x31 XOR y31 -> brp
fcg XOR pjf -> z01
dqw OR brb -> btn
cvn AND gmp -> trk
y16 XOR x16 -> jhn
y27 XOR x27 -> wcr
x33 XOR y33 -> gvt
y08 XOR x08 -> jwq
trn AND pgk -> hsk
nkt XOR kgm -> z28
y15 AND x15 -> sqw
crc XOR vmj -> z19
hbg XOR mhh -> z32
smv AND sgn -> qkc
vcr XOR nwb -> pqt
x14 AND y14 -> kbk
jhn XOR hjd -> z16
x10 AND y10 -> ktk
kmq AND jdc -> ssj
y15 XOR x15 -> smv
sqd OR dtt -> mdn
x24 AND y24 -> wkt
hgg OR cph -> kjr
ktd XOR tgj -> z25
ctf AND tnm -> wpm
x40 AND y40 -> wtv
x10 XOR y10 -> wfd
y33 AND x33 -> wjj
x39 AND y39 -> rrn
y03 XOR x03 -> fpt
x31 AND y31 -> pmm
y32 AND x32 -> nqs
x11 XOR y11 -> dmk
y18 XOR x18 -> qvq
x37 AND y37 -> dgn
skq OR rsw -> wsh
vch XOR css -> z20
kmn AND dmk -> skq
ghm AND hjg -> sqd
kjr AND qjb -> rpr
y01 AND x01 -> vpb
cpw AND dph -> gkb
y26 AND x26 -> rdq
tgj AND ktd -> kht
x26 XOR y26 -> wws
sfw XOR skp -> z24
y42 AND x42 -> thc
nkr OR hns -> swb
y20 XOR x20 -> jmv
vcr AND nwb -> z37
fbb OR thc -> mcf
x06 AND y06 -> vts
jdc XOR kmq -> z02
y25 AND x25 -> gfk
"""
        ), "Wrong input file"
        gateInputs = gateInputs.splitlines()
        gates = dict()
        numGates = len(gateInputs)
        for i in range(numGates):
            input1, wire, input2, output = search(
                "{:w} {:w} {:w} -> {:w}", gateInputs[i]
            )
            if output in SWAPS:
                output = SWAPS[output]
            gates[output] = (wire, input1, input2)

        def verifyIntermediate(wire, index):
            operator, wire1, wire2 = gates[wire]
            # print(f"Verifying intermediate {wire1} {operator} {wire2} -> {wire}")
            if operator != "XOR":
                return False
            return {wire1, wire2} == {f"x{index}", f"y{index}"}

        def verifyDirectCarry(wire, index):
            operator, wire1, wire2 = gates[wire]
            # print(f"Verifying direct carry {wire1} {operator} {wire2} -> {wire}")
            if operator != "AND":
                return False
            return {wire1, wire2} == {f"x{index}", f"y{index}"}

        def verifyIndirectCarry(wire, index):
            operator, wire1, wire2 = gates[wire]
            # print(f"Verifying indirect carry {wire1} {operator} {wire2} -> {wire}")
            if operator != "AND":
                return False
            return (verifyIntermediate(wire1, index) and verifyCarry(wire2, index)) or (
                verifyIntermediate(wire2, index) and verifyCarry(wire1, index)
            )

        def verifyCarry(wire, index):
            operator, wire1, wire2 = gates[wire]
            # print(f"Verifying carry {wire1} {operator} {wire2} -> {wire}")
            if index == "01":
                return {wire1, wire2} == {"x00", "y00"}
            if operator != "OR":
                return False
            checkIndex = str(int(index) - 1).rjust(2, "0")
            return (
                verifyDirectCarry(wire1, checkIndex)
                and verifyIndirectCarry(wire2, checkIndex)
            ) or (
                verifyDirectCarry(wire2, checkIndex)
                and verifyIndirectCarry(wire1, checkIndex)
            )

        # Credit to HyperNeutrino (https://www.youtube.com/watch?v=SU6lp6wyd3I)
        def verify(wire):
            operator, wire1, wire2 = gates[wire]
            # print(f"Verifying {wire1} {operator} {wire2} -> {wire}")
            if operator != "XOR":
                return False
            index = wire[1:]
            if index == "00":
                return {wire1, wire2} == {"x00", "y00"}
            return (verifyIntermediate(wire1, index) and verifyCarry(wire2, index)) or (
                verifyIntermediate(wire2, index) and verifyCarry(wire1, index)
            )

        i = 0
        while i < NUM_Z_WIRES:
            wire = "z" + str(i).rjust(2, "0")
            if not verify(wire):
                # print(f"Incorrect wires found at {wire}")
                break
            i += 1
        if i == NUM_Z_WIRES:
            # print("System working as intended")
            swappedWires = ",".join(sorted(SWAPS.keys()))
            print(swappedWires)


if __name__ == "__main__":
    part_one()
    part_two()
