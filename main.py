from openai import OpenAI
import subprocess
import sys
import os

input_website = sys.argv[1] # get input from arg
surfraw_destination = "/home/mat/Documents/ProgramExperiments/searchPanel/elvi/"
escaped_args = "{escaped_args}" ## big brain

with open(surfraw_destination + "dictionary", "r") as file:
    example_sr = file.read()

prompt = f"""<example>{example_sr}</example> 
I would like to use this example as a template to create another file like this used for this website: {input_website}
- MOST IMPORTANT, please update the two `w3_browse_url` lines to reflect the format for this website: {input_website}
    - Note: "{input_website}" has a search term at the end which is an example, that's where {escaped_args} should go, not the example search term.
    - example: if the target website used this format, "http://www.etymonline.com/?search=${escaped_args}" then the result should be: w3_browse_url "http://www.etymonline.com/?search=${escaped_args}"
    - example: (note the removal of "google.com" from the source) source: "https://web.archive.org/web/20240000000000*/google.com" target: "w3_browse_url https://web.archive.org/web/20240000000000*/${escaped_args}"
- replace the "#elvis: " line with a similar line based on the website provided {input_website}.
- update the Description: and Example: lines to act similarly
Please take the following website and convert it into a full file and only the file. Do not include any backticks like "```bash" in the script.
    """

client = OpenAI()
def textFromAI():
    res = client.chat.completions.create(model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": input_website}
    ])
    story = res.choices[0].message.content
    return str(story)

new_surfraw = textFromAI()
surfraw_file_path = surfraw_destination + new_surfraw

elvi_name = input("what would you like the elvi to be named?\n")

with open(elvi_name, "w+") as file:
    file.write(new_surfraw)

subprocess.run(["chmod", "+x", elvi_name], check=True)
os.rename(elvi_name, surfraw_destination + elvi_name)




# master plan:
# DONE get a seed file / import, 
# DONE make prompt to explain what to do, 
# DONE have file accept an arg that's the target website having searched for an address, 
# DONE strip website from 
# DONE write to a file
# DONE chmod +x $file, 
# DONE mv to the local options (I've got my vcs file, just set a var for it), 
# !!! figure out how to give a good example in the prompt
# and then run it to test out.

# starting coding at (09:20:38) --- (09:54:20) haven't run it, but hvae the skeleton done.
# (10:13:41) call it. It works on both maps and archive.org. I could use some porpmt tuning.
# I want to do some cleaning, but that should take a couple minutes.
# also the name generation should be better.
