import jinja2

xe1_1010_forward = open("xe1_1010_forward.dat").read()
xe2_1010_forward = open("xe2_1010_forward.dat").read()
xe3_1010_forward = open("xe3_1010_forward.dat").read()
xe4_1010_forward = open("xe4_1010_forward.dat").read()
heme_1010_forward = open("heme_1010_forward.dat").read()

xe1_1000_forward = open("xe1_1000_forward.dat").read()
xe2_1000_forward = open("xe2_1000_forward.dat").read()
xe3_1000_forward = open("xe3_1000_forward.dat").read()
xe4_1000_forward = open("xe4_1000_forward.dat").read()
heme_1000_forward = open("heme_1000_forward.dat").read()

xe1_1001_forward = open("xe1_1001_forward.dat").read()
xe2_1001_forward = open("xe2_1001_forward.dat").read()
xe3_1001_forward = open("xe3_1001_forward.dat").read()
xe4_1001_forward = open("xe4_1001_forward.dat").read()
heme_1001_forward = open("heme_1001_forward.dat").read()

xe1_1011_forward = open("xe1_1011_forward.dat").read()
xe2_1011_forward = open("xe2_1011_forward.dat").read()
xe3_1011_forward = open("xe3_1011_forward.dat").read()
xe4_1011_forward = open("xe4_1011_forward.dat").read()
heme_1011_forward = open("heme_1011_forward.dat").read()

xe1_1010_reverse = open("xe1_0110_reverse.dat").read()
xe2_1010_reverse = open("xe2_0110_reverse.dat").read()
xe3_1010_reverse = open("xe3_0110_reverse.dat").read()
xe4_1010_reverse = open("xe4_0110_reverse.dat").read()
heme_1010_reverse = open("heme_0110_reverse.dat").read()

xe1_1000_reverse = open("xe1_0100_reverse.dat").read()
xe2_1000_reverse = open("xe2_0100_reverse.dat").read()
xe3_1000_reverse = open("xe3_0100_reverse.dat").read()
xe4_1000_reverse = open("xe4_0100_reverse.dat").read()
heme_1000_reverse = open("heme_0100_reverse.dat").read()

xe1_1001_reverse = open("xe1_0101_reverse.dat").read()
xe2_1001_reverse = open("xe2_0101_reverse.dat").read()
xe3_1001_reverse = open("xe3_0101_reverse.dat").read()
xe4_1001_reverse = open("xe4_0101_reverse.dat").read()
heme_1001_reverse = open("heme_0101_reverse.dat").read()

xe1_1011_reverse = open("xe1_0111_reverse.dat").read()
xe2_1011_reverse = open("xe2_0111_reverse.dat").read()
xe3_1011_reverse = open("xe3_0111_reverse.dat").read()
xe4_1011_reverse = open("xe4_0111_reverse.dat").read()
heme_1011_reverse = open("heme_0111_reverse.dat").read()

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "TEMPLATE_vol_all_xe42_eq.dat"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(xe1_1010_forward=xe1_1010_forward,#  1010
                             xe2_1010_forward=xe2_1010_forward,
                             xe3_1010_forward=xe3_1010_forward,
                             xe4_1010_forward=xe4_1010_forward,
                             DP_1010_forward=heme_1010_forward, 
                             xe1_1000_forward=xe1_1000_forward,#  1000
                             xe2_1000_forward=xe2_1000_forward,
                             xe3_1000_forward=xe3_1000_forward,
                             xe4_1000_forward=xe4_1000_forward,
                             DP_1000_forward=heme_1000_forward,
                             xe1_1011_forward=xe1_1011_forward,#  1011
                             xe2_1011_forward=xe2_1011_forward,
                             xe3_1011_forward=xe3_1011_forward,
                             xe4_1011_forward=xe4_1011_forward,
                             DP_1011_forward=heme_1011_forward,
                             xe1_1001_forward=xe1_1001_forward,#  1001
                             xe2_1001_forward=xe2_1001_forward,
                             xe3_1001_forward=xe3_1001_forward,
                             xe4_1001_forward=xe4_1001_forward,
                             DP_1001_forward=heme_1001_forward,
                             xe1_1010_reverse=xe1_1010_reverse,#
                             xe2_1010_reverse=xe2_1010_reverse,
                             xe3_1010_reverse=xe3_1010_reverse,
                             xe4_1010_reverse=xe4_1010_reverse,
                             DP_1010_reverse=heme_1010_reverse, 
                             xe1_1000_reverse=xe1_1000_reverse,#
                             xe2_1000_reverse=xe2_1000_reverse,
                             xe3_1000_reverse=xe3_1000_reverse,
                             xe4_1000_reverse=xe4_1000_reverse,
                             DP_1000_reverse=heme_1000_reverse,
                             xe1_1011_reverse=xe1_1011_reverse,#
                             xe2_1011_reverse=xe2_1011_reverse,
                             xe3_1011_reverse=xe3_1011_reverse,
                             xe4_1011_reverse=xe4_1011_reverse,
                             DP_1011_reverse=heme_1011_reverse,
                             xe1_1001_reverse=xe1_1001_reverse,#
                             xe2_1001_reverse=xe2_1001_reverse,
                             xe3_1001_reverse=xe3_1001_reverse,
                             xe4_1001_reverse=xe4_1001_reverse,
                             DP_1001_reverse=heme_1001_reverse)

f = open("vol_xe1xe2.dat", "w").write(outputText)

