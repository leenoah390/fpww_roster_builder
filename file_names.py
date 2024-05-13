'''
Get a list of names for the image files to be included in roster.html
Ignore irrelevant files (htmls, belt graphics, other non-wrestler imgaes, etc.)
'''

# import OS module
import os
# Get the list of all files and directories
path = r"C:\Users\njlee\Documents\FPWW\fpww_website"
all_files = os.listdir(path)

# Irrelevants
irr = ['01iwgp_hw.html', '01_IWGP_HW.png', '02iwgp_ic.html', '02_IWGP_IC.png', 
               '03iwgp_us.html', '03_IWGP_US.png', '04never_open.html', '04_NEVER_OW.png', 
               '05iwgp_jr.html', '05_IWGP_JR.png', '09ghc_hw.html', '09_GHC_HW.png', 
               '10ghc_national.html', '10_GHC_NATIONAL.png', '11ghc_jr.html', '11_GHC_JR.png', 
               '15allasia_hw.html', '15_ALL_ASIA_HW.jpg', '16united_national.html', 
               '16_UNITED_NATIONAL.png', '17nwa_w_jr.html', '17_NWA_W_JR.png', '18tc_hw.html', 
               '18_TC_HW.png', '19pwf_w_jr.html', '19_PWF_J_HW.png', 'index.html', 'roster.html',
               'puro_peace.jpg', 'ajpw.png', 'njpw.png', 'noah.png', 
               'file_names.py', 'roster_creator.py', 'roster_builder', '__pycache__']

# Remove irrelevants from all
final_list = [x for x in all_files if x not in irr]

print("Files and directories in '", path, "' :")
# prints all files
print(final_list)
