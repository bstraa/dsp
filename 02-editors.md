# Choose and learn your editor(s)


Computing's interface is text. To work effectively, you need to be fluent with this interface.


### Typing

It may sound silly, but [make sure](http://www.typingtest.com/) you know how to type. You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, practice until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.


### Terminal Editor

Sometimes you will need to use a non-graphical text editor. This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

Make sure that you know at least one of these well enough to do basic editing in a terminal:

 * Emacs
 * vim
 * nano

You should know at least enough vim to be able to get out of it, because it is the default on many systems and you might find yourself in it even if you didn't mean to be.

If you intend to use a graphical editor that doesn't run in a terminal, nano might be a good choice for you because it is very simple.

Both Emacs and vim have built-in interactive tutorials that you can try.

---

What terminal editor will you use? How did you make your decision?

I will use the emacs terminal editor.  I made my decision by deciding that it was best to choose between emacs and vim.  I really like their speed and universality.  Specifically, it is complementary to use them with their appropriate graphical editor.

I chose emacs over vim ultimately because I disliked the different modes in vim.  


---


### Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * Emacs
 * vim
 * Sublime
 * Atom
 * Spyder
 * PyCharm

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter (IPython) notebooks, but this does not remove the need for proficiency in an editor or IDE.

---

What graphical editor will you use? How did you make your decision? What are some interesting features of your editor? What are some useful keyboard shortcuts for your editor? How do you customize your editor?

I chose Emacs because it made the most sense after choosing it for my terminal editor.  I think the most interesting features are those of which are generally implemented combinatorically.

For example, deleting one character, regardless if its the next or previous character relative to the cursor, is quite simple, easy, expected, and relatively uninteresting.  However, the truly interesting features seem to combine an action (such as deleting) with specific quantative and directional specifications such as killing the next 12 lines after the cursor.  This would be implemented by pressing 'C-u 12 C-k'.

Customization can be done by creating a customization buffer where you can alter your settings.  To do this, press 'M-x' then type 'customize'.

---
