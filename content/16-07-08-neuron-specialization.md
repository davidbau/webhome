Title: Neuron Specialization
Date: 2016-06-17 15:29
Category: Research Notes

<video width="960" height="540" controls>
<source src="/davidbau/movies/syn/lenet_gradient_and_activation.mov" type="video/mp4">
</video>
*Video by David Bau; music by David Szesztay used under creative commons license.*

Why does a deep network need to have so many neurons to work?

Intuitively, the hidden units must be needed to represent different
subfeatures that are necessary for recognizing the target classes.
For example, there are two major ways of writing a handwritten 7:
most people write just a single horizontal stroke attached to a single
diagonal stroke.  However, some people add a cross, striking a second
horizontal stroke through the diagonal.

A good reader of handwritten digits must recognize both forms, but
since they look somewhat different, it would make sense to recognize
them separately.  The same situation is true for the digit "2" written
with or without an open loop in the bottom-left corner, or other
variations.

In LeNet-5, is there a neuron devoted to recognizing the seven-with-stroke?

To determine this, I think it is necessary to:

 1. Use visualizations to determine which neurons might have that role.
 2. Show that by removing that neuron, the network loses the knowledge.

My previous attempts to ablate all knowledge of entire classes by
ablating sets of hidden units (driven by the visualizations) have not
been very successful.  However, I am still trying to make things work
In the movie above, I show both the gradient examples (as also shown
in the last blog entry) adjacent to neuron activations (shown in the row
underneath each gradient visualization).

In most cases, strong gradients for a class correspond to average strong
activations for a class.

However, there are a few anomolies.

For example, notice neuron #58 in the linear-0 layer: during training it
is very clear that this neuron is getting positive gradients for "7" digits
(as well as "4" digits, and negative on 9).  However, the average activation
for 7 is negative.

The image of the strong positive gradients during training shows many 7
digits with strokes through the middle.  So neuron 58 is a natural one
to look at to see if it is actually a stroked-7 detector.  Is it?

Currently my visualizations are not interactive, and it requires programming
to ask any question.  I should build a tool that allows questions to be
asked and answered interactively.

But here is a visualization of neuron #58 where we have rectified the
activation, i.e., rather than applying a negative weight when the neuron
does not fire, we zero non-firing contributions.  As you can see, the
average "7" which activates this neuron does indeed have a crossbar.
This differs from most other neurons that fire on 7.

![unit linear-0-58 showing a crossed 7](/davidbau/home/img/linear_0-58-crossed-7.png)

The phenomenon of a neuron on which the gradient is strong but the activation
is not strong seem to be interesting.  Here is another such neuron, unit 28
of the linear_0 layer.  This one shows yet another way to draw a 7, which
is with a vertical hook overhanging the left end of the horizontal bar.

![unit linear-0-28 showing a crossed 7](/davidbau/home/img/linear_0-28-hooked-7.png)

cannot discern any particular kind of specialization.  For example,
unit 8 in linear-0 learns with very strong gradient for 8, but it
activates only weakly for 8, activating much more strongly for 1.
However, I cannot see anything special about the set of 8 instances
that activate it: perhaps this neuron specializes in something negative,
for example, its ability to fire on 8 while not firing on any other
digit other than 1.

![unit linear-0-8 showing a low-activation 8](/davidbau/home/img/linear_0-8-unknown-8.png)

