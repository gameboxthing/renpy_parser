# Renpy Parser
This is a python script that parses a plain text file into renpy code.

I wrote this program mainly because I didn't want to copy and paste every single
line of the script a friend was writing.

## Usage
Open up the `main.py` file and change the input file, or just copy and paste
your script into the input file.

Assuming you already have python installed becasue it is required for renpy,
just run the `main.py` and you will get the output and script files. Thats it!

## Formatting
This parser does require some specific syntax to make everything work, but it
should be more human than renpy code.

### Title
```
>> title
```

Outputs the line as rpy label
```
label title:
```

### Spoken lines
Spoken lines are slightly more complex than the title and look something like
the following
```
[character:name] text
```
The `name` here is optional.
This is useful if a mystery character comes into the scene to be named as '???'
or something to that effect later wanting to change to an actual name. An 
example of this is bellow
```
[character] text
```
Some examples of useage
```
[evil_bob:Man] It was I all along
[exil_bob:Evil Bob] Me Evil Bob
[evil_bob] mwahaha
```
The output from the parsed rpy script will look something like the following

> Man: It was I all along<br>
> Evil Bob: Me Evil Bob<br>
> Evil Bob: mwahaha

The final line here, maintains the name set by the one before.

There is additionally the special case of the narrator taking the `Narration` 
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
This does just get parsed as a comment for the programmer to interpret later.
It is intended to be used for things like the `scene` keyword or `show` or other
things to that effect.

### Comments
Any line with a hash (*#*) at the front
```
# this is a comment
```

## Bugs
I still have a lot of testing to do as well as a lot of features that I would 
like to add to this project, so there is guarenteed to be a few bugs.
These will most likely look like lines that are half between one and another, if 
you find any please let me know, I want this to be fairly robust.

## Features and suggestions
Currently I am working on a UI and a file browser so that you can parse multiple
files at one time, but this is still a little bit down the line. In the meantime
I am more than open to suggestions as to what features to include, maybe parsing
music or sfx?