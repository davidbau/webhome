Title: The Purpose of a Neuron
Date: 2016-06-17 15:29
Category: Research Notes

<video width="960" height="540" controls>
<source src="/davidbau/movies/syn/composite.mov" type="video/mp4">
</video>
*Video by David Bau; music by David Szesztay used under creative commons license.*

One of the great scientific debates of the 19th century was whether
the structure of the brain could be decomposed.
[Reticulists](https://en.wikipedia.org/wiki/Reticular_theory) such as
[Golgi](https://en.wikipedia.org/wiki/Camillo_Golgi)
believed the brain was monolithic, a single complex body of protoplasm,
crisscrossed by dendrites and axons, but fundamentally indivisible.
[Neuronists](https://en.wikipedia.org/wiki/Neuron_doctrine), led by
[Santiago Ramón y Cajal](https://en.wikipedia.org/wiki/Santiago_Ram%C3%B3n_y_Cajal),
believed the brain to be composed of a collection of
separate individual cells that communicated with each other.

Of course, Cajal was proven correct: brains are made up of separate
neurons, and his *neuron doctrine* became the driving model for
neuroscientists.  However, the conceptual debate at the heart of the
matter is still not completely settled, even today.  Although there
is no question that a brain, or an artificial neural network,
is physically decomposable into separate neurons, there is still
a question of whether this physical decomposition corresponds to a
decomposition of high-level thoughts, concepts, and knowledge.

## Grandmother Cells

Teaching at MIT in 1969, pioneering cognitive scientist
[Jerry Lettvin](https://en.wikipedia.org/wiki/Jerome_Lettvin)
would tell a
[humorous story](http://www.as.wvu.edu/daly/439/readings/Gross%202002%20Grandmother%20Cell.pdf)
imagining removing a specific
high-level concept from a brain by removing a selection of
neurons.  He imagined how remarkable it might be that there could
be cells representing high-level concepts such as "mother"
and "grandmother".
Surprisingly,
[some evidence](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3662881/)
has emerged that grandmother cells might exist. For example,
[in 2005, Quian Quiroga](http://www.nature.com/nature/journal/v435/n7045/full/nature03687.html)
discovered individual cells in the medial temporal lobe of an individual
that respond to a specific concept such as "Halle Berry", firing for
different views of the same person, even when dressed up as Catwoman,
and even firing in response to the written text "HALLE BERRY". This seemed
like compelling evidence for the presence of "Grandmother neurons:"
individual neurons that strongly localize a high-level concept.

However, Quiroga and others have vociferously argued that the simplistic
model of a localized representation need not be implied by these
experimental results: he argues that a distributed code is potentially
much more efficient (for example, 10 bits in a localized code can
represent 10 concepts, while 10 bits in a distributed code could represent
2^10 = 1024 concepts), and given the large numbers of untested
neurons and concepts, it would be difficult to distinguish a
localized code from a distributed code on the basis of his experiments.

So the debate today is whether individual neurons localize meaning, or
whether meaning is an emergent property of many neurons working together
in a distributed code.

## Localizing Meaning Intentionally

Regardless of whether neurons in biological brains *do* localize meaning,
any engineer would agree that it would be *useful* for neurons to
localize meaning. A well-engineered system is modular, which means that
it can be split on meaningful boundaries. A monolithic system is
"spaghetti code," hard to understand and hard to debug.
So when we create neural networks, we should strive for localized meaning
and clean boundaries.  Whether this is possible is an open question.

I think the science of modular neural networks comes down to three steps:

   1. Find a way to measure the purpose of a neuron, localized or not.
   2. Prove that we can identify and use localized knowledge by using ablation or transplant.
   3. Create ways of intentionally localizing important knowledge, so it can be modularized.

On step 1, I have been helping Aditya Khosla on work that localizes
interpretable concepts that emerge within neural networks.  The work
follows in the tradition of the neuroscientists: to discern the meaning
of a neuron, Khosla exposes the network to various input, and then identifies
which stimulus causes the neuron to fire the strongest. We are finding
some interesting properties of networks using this approach, which
we will write up as a paper soon.

This last spring I did some informal experiments attempting to jump
straight to #2. I did this after a short conversation with
[D. Sculley](http://research.google.com/pubs/author38217.html)
where he asked the question, "after you psychoanalyze a neural
network to understand its neurons, what do you do with it?"
But my experiments were a muddle: removing random neurons from networks
would gradually degrade the ability of network to think (if the
ablation were done correctly), and there were hints that it might
be possible to glue together parts of two networks to get something
new. However, without a good map what individual neurons were really
*for*, it was difficult to test ablations and transplants in any
compelling way.

So I am back to measurements, looking for an approach that will go
beyond providing hints of meaning, and provide a more complete and
detailed map of neuronal purpose even for neurons that are participating
in some sort of distributed code.

## Imagining a Distributed Code

Suppose a neural network has the job of distinguishing 1000 different types
of inputs, and we find a hidden unit that fires strongest when provided
input type #421.  Is this a "421" neuron?  If the neuron is part of a
distributed code, then perhaps it is actually the "odd number" neuron.
To understand the neuron, rather than looking at just the one category
it fires strongest on, we might be better served by contrasting the set
it fires on versus the set it does not fire on.

This contrast might best be seen not on the set of cases where the neuron
fires strongest, but on the set of cases which are on some sort of boundary
between the neuron firing and the neuron not-firing.  Or, with a
more complicated code, maybe around a boundary between the neuron firing
stronger than some threshold x versus firing weaker than that threshold.

There is more subtlety to this as well: even if there is a distributed
code, there is no reason to believe that it is perfectly efficient.
A neuron firing might be important to the code in some cases and
unimportant in some other cases.  To understand the purpose of a neuron,
we might best want to examine situations for which the neuron firing
(or not firing) makes a difference.

I have been developing a rough idea for a way of visualizing the purpose
of a neuron as a decision-making unit that captures these intuitions
above. I have some things, but I am not yet confident that they
work well and reflect reality.  My goal is to develop a fine-grained
enough tool that we can use it as a map for ablations and transplants.

## Visualizing the Purpose of Neurons

But here is what I have so far: I have posted above a little video of my
idea in action.
Here I am probing the classic network LeNet-5, which is a small convolutional
neural network that classifies 10 handwritten digits from the MNIST data set.
I am using the original network design by Yann LeCun with some L2
regularization, tuned so that it can reach testing accuracy of about 99.2%
after about 3000 training batches (with 500 instances in each batch).

In the video above, each neuron is represented by a row, which attempts
to show its "purpose" in distinguishing the 10 different classes of
handwritten digits.  Where a neuron is responsible for positively firing
on a digit, the digit is shown as black ink on a white field; where the
neuron is responsible for not firing on a digit, it is shown as
white ink on a black field.  Gray boxes are shown where I think the
neuron firing (which it might do) is not important to that case.

There are 6 layers of neurons, and within each layer, each neuron is
numbered.  The topmost layer, shown first, is the output layer, and
it is responsible for making the final judgment of which numeral
is being written: that is why positive responsibilities fall clearly
on the diagonal in that layer.  LeNet-5 has two convolutional layers
here called conv_0 and conv_1, and it has three fully-connected layers,
here called linear_0, linear_1, and linear_2.

The specialization of neurons is more specific than just classes of
digits, so I have tried to render the average shape of digits that a
neuron is most responsible for distinguishing.

For example, I think neuron 94 in linear_0 is probably
responsible for distinguishing handwritten "4" digits
that have a nearly closed top (so they almost look like a 9)
from "9" digits that have a gap at the top (so they almost
look like a 4) as well as "8" digits that have an extremely
small bottom loop and a left-skewing top-loop (so they also almost
look like a 4 with a nearly-closed top).  Another example:
Neuron 25 in linear_0 seems to be responsible for distinguishing
"7" from other digits when they are drawn in a strongly
diagonal orientation.

I need to do some more work on this tool; if I can convince myself
that it actually works, I will write it up.
