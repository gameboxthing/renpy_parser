# Renpy Parser
This is a python script that parses a plain text file into renpy code.

I wrote this program mainly because I didn't want to copy and paste every single
line of the script a friend was writing

## Usage
open up the *main.py* file and change the input file, or just copy and paste
your script into the input file.

Assuming you already have python installed becasue it is required for renpy,
just run the *main.py* and you will get the output and script files. Thats it.

## Formatting
This parser does require some specific syntax to make everything work, but it
should be more human than renpy code.

### Title
```
>> title
```

outputs the line as rpy
```
label title:
```

### Spoken lines
Spoken lines are slightly more complex than the title and look something like
the following
```
[character*:name*] text
```
with the name being an optional argument that changes the name of the character.
This is useful if a mystery character comes into the scene to be named as '???'
or something to that effect later wanting to change to an actual name. An 
example of this is bellow
```
[evil_bob:Man] it was i all along
[exil_bob:evil bob] me Evil Bob
```

there is additionally the special case of the narrator taking the *Narration* 
keyword (i might change this later). This parses into the non-character
format for renpy.

### Commands
I haven't really implemented these in well but i do plan on changing them at
some point when I need to. This might be a point of feedback if people have 
ideas of what could be useful here.

The syntax is as follows
```
[command]
```
this does just get parsed as a comment for the programmer to interpret later

### Comments
any line with a hash (*#*) at the front.
```
# this is a comment
```

## Bugs
I still have a lot of testing to do as well as a lot of features that I would 
like to add to this project, so there is guarenteed to be a few bugs.
These will most likely look like lines that are half between one and another, if 
you find any please let me know I want this to be fairly robust.

## Features and suggestions
Currently I am working on a UI and a file browser so that you can parse multiple
files at one time, but this is still a little bit down the line. In the meantime
I am more than open to suggestions as to what features to include, maybe parsing
music or sfx.