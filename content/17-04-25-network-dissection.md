Title: Network Dissection
Date: 2017-04-25 16:20
Category: Research Notes

Beware the Chimera
------------------

In Greek mythology, the Chimera was a monster with the body of a
lion, the head of a goat, and the snake of a tail: an beast
made of the parts of many other animals. Today the term is still
used to represent a crazy cross, but it is also used to describe a
highly desired fantasy that is a figment of your imagination.

As we scrutinize internals of deep neural networks hunting for
meaning, we must beware the Chimera. In other words, we need
to make sure that the interpretable phenomena we see are faithful
reflections of the operation of the network, and not illusiory
combinations created by our limited imagination.

## Network Dissection

Discerning chimeras has been one of my concerns as I have worked in
Antonio Torralba's lab, together with Bolei Zhou and Aditya Khosla,
on understanding internal neuron interpretaitons.  My work
is motivated by the amazing emergent structure discovered by
[Bolei and Aditya](https://arxiv.org/abs/1412.6856) in 2014.
They found that when you train a deep network to solve a
whole-image scene classifcation problem (deciding whether an
image is in one of 205 place categories), hidden internal units
emerge that that identify and localize the presence of specific
types of objects such as dogs, cars, houses, and boats,
that were not labeled in the training set.  Since object
segmentation is a difficult problem, it is amazing to see the
problem being solved without any specific training for that problem.

Examples of emergent detectors can be seen below.  Each block
of images represents the areas of highest activation of
single convolutional units inside a deep network.

[![Network Dissection samples](/davidbau/home/img/netdissect-grid.png)](http://netdissect.csail.mit.edu)

The emergence of these common-sense concepts is striking. When
you look inside smaller networks (such as the MNIST networks I
examined last summer) you do not find this effect.

Nevertheless, I am still left with the questions, "are our
interpretations of these units a chimera"?
Is the network truly discovering the visual concept of a
"dog" or an "airplane", or is the network discovering
a more general way of organizing the images, and when
we peer into an aspect of that organization, we impose
our own concept of object classes on it.

## Isotropic Phenomena

How can we tell the difference between a chimera and a true
interpretatation?  One way was proposed by
[Szegedy in 2013](https://arxiv.org/abs/1312.6199):
if random combinations of units are just as interpretable
as individual units, then

