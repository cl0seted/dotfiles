#!/usr/bin/python3
from subprocess import run, check_output
import re

# run command and keep in a variable
output = str(check_output(["wpctl","status"], encoding="UTF-8"))

# clean up ascii tree characters, split into array by newlines
output = output.replace("├","").replace("─","").replace("│","").replace("└","").splitlines()


# for i in range(0,len(output)):
#     print(output[i])

for i in range(0,len(output)):
    if "Sinks:" in output[i]:
        # print(i, "yes", output[i])
        sinks_index = i
        break
    
for i in range(sinks_index,len(output)):
    # print(output[i])
    # break upon the first "blank" observed
    if output[i] == "" or output[i].isspace():
        # print(f'{i}"blank"')
        sink_break = i
        break

sinks = []

for i in range(sink_break-sinks_index):
    # print(output[sinks_index+i+1])
    # print(re.sub('(\\s{2,})|(\\[.*?\\])', '', output[sinks_index+i+1]))
    sinks.append(re.sub('(\\s{2,})|(\\[.*?\\])', '', output[sinks_index+i+1]))


for i in range(0, len(sinks)):
    sinks[i] = sinks[i].replace(". ", ":")
    # print(f'{i}{sinks[i]}')

print(sinks)

## -- At this juncture, we have an array containing all current sinks in the system





## >> Next step, identify the ID attached to Rubix22 and Starship and store in a variable
## >> Once ID for each sink is able to be obtained dynamically, need to detect current "default sink"
## >> Once able to detect default sink, write code to toggle between two sinks

# print(output[sinks_index:sink_break])

# print(output)


# https://www.reddit.com/r/hyprland/comments/10rmv6r/i_made_a_script_to_change_audio_sinks_using_wpctl/
# https://github.com/Sebastiaan76/waybar_wireplumber_audio_changer/blob/main/audio_changer.py