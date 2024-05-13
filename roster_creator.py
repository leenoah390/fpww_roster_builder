'''
FPWW Gallery creator
'''

# Import file_names to get a list of all wrestler profile images
import file_names

# Profile pics (pfps)
pfps = file_names.final_list

# Loop through images to create sets of 10s 
## Modified code from: https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
# Yield successive n-sized
def divide_chunks(pfps, n): 
	# looping till length l 
	for i in range(0, len(pfps), n): 
		yield pfps[i:i + n] 
# List split into portions of n
n = 10 # CHANGE ME IF YOU WANT MORE WRESTLERS PER ROW!!
# DON"T FORGET TO MAKE PERCENTAGES EVEN LATER ON!!
div10 = list(divide_chunks(pfps, n))


# Format html code:
gcode = '<table style="margin-left:auto;margin-right:auto;" border="1" WIDTH=1440>\n'
for row in div10:
    
    #if len(row) == 10:
        newline = '<tr>\n' # Start the row
        for index in range(len(row)):
            # Get image
            newline += '<td width="10%"style="text-align: center; vertical-align: middle;"><br />\n'
            newline += '<img src="{}" width="128" height="128">\n'.format(row[index])
            # Get name
            name = row[index]
            name = name.replace("_", " ")
            name = name.replace(".jpg", "")            
            newline += '{}</td>\n'.format(name)

        newline += '</tr>\n'
    #else:
        
    
        gcode += newline

print(gcode)


# Open the html file
f = open('roster.html', 'w')

# html code to be run
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">  
  <title>Roster</title>
</head>
<body style="background-color:LightGray">
<h1>DoofNookie's FPWW Roster</h1> 
</head> 
<body> 
<h2>Roster (partial)</h2> 
  
<p>All wrestlers, listed alphabetically<br />
    <a href="index.html">Go back to home</a>
</p>

{}

</body> 
</html> 
""".format(gcode)
  
# writing the code into the file 
f.write(html_template) 
  
# close the file 
f.close() 