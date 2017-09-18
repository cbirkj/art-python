.. art-python documentation master file, created by
   sphinx-quickstart on Fri Feb  3 11:15:17 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

art-python documentation
======================================

Fuzzy ART is a ANN architecture that can learn without forgetting. It is similar to human 
memory where people can recognize their parents even if they have not seen them in a while 
and have learned many new faces since. The theory was developed by Grossberg and Carpenter 
and includes various types such as ART 1, ART 2, ART 3, and Fuzzy ART. ART 1 is an architecture 
that can be used for clustering of binary inputs only. ART 2 improved upon the ART 1 
architecture to support continuous inputs. Fuzzy ART, used in the present work, 
incorporates fuzzy set theory into the pattern recognition process.

Code
^^^^
Run training code to learn patterns::

	python train.py

Weights are stored (csv or mysql)

Run testing code to idenfiy anomalies::

	python test.py


.. toctree::
   :maxdepth: 2
   :caption: Source Code:

   train
   test
   installation
   help
   license

Example
^^^^^^^


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
