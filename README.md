# Examples of wrapping C headers (only headers with defines and structs) for use in python.
I needed to look at various tech for this purpose. Results are here. Each
subfolder that names a tech (and has been implemented) produces an extension
module.

As of now, all of this was tested on Python 3.4 (via anaconda environments)
*except* for ctypesgen (which didn't work with python 3, and I used python
2.7). I may not have the dependencies quite up to date for each.
