# Toledo Blade NewsDiffs Parser

This is a parser for http://www.toledoblade.com *written for [NewsDiffs](https://github.com/ecprice/newsdiffs)*. To clarify: that means this doesn't work on its own!

# Usage

Drop in your `newsdiffs/parsers` directory. Then follow the directions on NewsDiffs's readme to get the rest of the program to use it.

# Testing

Remember that the Blade could choose to change its structure at any time. Make sure this works by doing this: 

`$ python test_parser.py blade.BladeParser`

Choose a URL from the list and enter something like this:

`$ python test_parser.py blade.BladeParser http://www.toledoblade.com/Pro/2015/07/11/Mud-Hens-take-Game-1-of-doubleheader.html`

If the output looks good, you're all set.

#License

Under MIT license.
