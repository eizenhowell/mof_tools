import os
import shutil 

def move_extracted_ravioli (src_folder, trg_folder, filename="/File0001.png", replace_hypens=True):
	for fldr_name in os.listdir(src_folder):
		current_file = src_folder + fldr_name
		for ext_file in os.listdir(current_file):
			filename = ext_file
		current_file = src_folder+fldr_name+"/"+filename

		target_filename = fldr_name.replace('.gi', '') + ".png"
		# Check if filetype is included in filename
		if not ".png" in target_filename:
			target_filename += ".png"
		if replace_hypens:
			target_filename = fldr_name.replace("-", "_")
			
		current_file = src_folder+fldr_name+"/"+filename
		target_file = trg_folder+target_filename
		
		shutil.copy2(current_file, target_file)

def isExit(user_in):
	if user_in == "exit":
		return True
	return False
		
def main():
	currently_running = True
	while currently_running:
		print("""
==============================================================================
##     ##  #######  ########    ########  #######   #######  ##        ######  
###   ### ##     ## ##             ##    ##     ## ##     ## ##       ##    ## 
#### #### ##     ## ##             ##    ##     ## ##     ## ##       ##       
## ### ## ##     ## ######         ##    ##     ## ##     ## ##        ######  
##     ## ##     ## ##             ##    ##     ## ##     ## ##             ## 
##     ## ##     ## ##             ##    ##     ## ##     ## ##       ##    ## 
##     ##  #######  ##             ##     #######   #######  ########  ######  
==============================================================================
		""")
		print("Source Folder Address: ", end="")
		src_folder = input()
		if isExit(src_folder): break
		print("Target Folder Address: ", end="")
		trg_folder = input()
		if isExit(trg_folder): break
		move_extracted_ravioli(src_folder, trg_folder, True)
	
if __name__ == "__main__": main()