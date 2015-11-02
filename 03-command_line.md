# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pushd - takes your current directory and "pushes" it into a list for later, then it changes to another directory. If no arguements are given it will revert to the last pushd directory from your current.  It makes it easy to 'toggle' between them.  This seems incredibly useful and time-saving.

popd - takes the last directory you pushed and "pops" it off, taking you back there.

cp - copies a file or directory

mv - moves a file or directory (really it just renames it, but saves you time over a GUI)

ls - list files/directories in working directory

chmod - changes permission modifiers (way easier and saves way more time compared to alternative options)

env - easy way to check your environment

pwd - see where you are at by printing the working directory

cd - easily change directories

man - helps with understanding command line tools fully in-depth

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

'ls' lists the files and directories in the current directory.  'ls -a' lists all files and directories also, however, it includes files that start with '.' which are otherwise hidden.  'ls -l' provides a more in-depth 'long list' of the files and directories.  'ls -lh' does the same but in human-readable format (this is preferred - as the size of files is labelled).

The most powerful combination of these flags is really 'ls -a' and 'ls -lh' because you'll see all the files in human-readable format with the most information possible.
---


---

What does `xargs` do? Give an example of how to use it.

'xargs' provides arguments which are needed for some command line commands like 'cp' and 'echo'.  Also, some programs need arguments instead of STDIN.  Unfortunately, standard input streams do not work with every argument so 'xargs' are needed.  Furthermore, an increasingly important and common reason for 'xargs' is that it can parallel process jobs.  An example of how to us it is as follows:

touch file1.txt
echo file1.txt | xargs touch

These two command line inputs do exactly the same thing.  Touch creates a new empty file named file1.txt.  Echo prints file1.txt as it is taken as an input to the arguement 'touch'.  Essentially, these are two ways of doing the same thing and it shows how 'xargs' is used.
---

