Title: Choosing a Research Path
Date: 2016-03-25 13:29
Category: Blog

I am approaching the end of my first year of my EECS graduate program at
MIT, and although a PhD typically stretches for years, I feel how acutely
limited and precious this time is. It is a unique moment of academic
freedom.  What really interests me?

### Creating a Programmable World

The problem that motivates me most is the problem of
programmability. How can we put people in charge of our
computational systems, instead of the other way around?  I am very
proud of my work in helping to implement programmable web
standards, democratizing the internet by making web browsers radically
easy to program. I am also proud of my work helping to teach young
people to program. When I came to MIT, I had planned to continue
work on programming tools geared toward making programming
understandable to everyday users and beginners.

But in doing my required coursework, I was
struck by a seductive new problem.

We all know that deep neural networks are making remarkable strides.
For the first time, simple optimization techniques are automatically
creating complexity that is worthy of being called artificial
intelligence. We are training neural networks with dozens of layers and
hundreds of millions of learned parameters, the equivalent of
thousands of lines of automatically-generated code.  And yet
we do not know, really, how they work, why they fail when they do,
or how to intentionally create beavhior within them.

Meanwhile, within the deep network community, understandable
AI is generally perceived as an ineffective approach: people can only
comprehend a few things at once, but neural networks are capable
balancing thousands of signals at every neuron - and this capability
seems essential to their function.  For example, biasing a network
towards sparse connections to aid understandability appears to
penalize performance. So practitioners generally believe it is
best to set aside human comprehension and let the
algorithms optimize freely.

For my whole career, I have built tools to make it easier to for
people to program, debug, and control increasingly complex software
systems. So this is a disquieting moment.  Whereas previously
all my work has made human programmers progressively more capable,
more aware, and more expressive, for the first time, the best way
to program a computer is to take the human out of the loop. For
the first time, it is best to let the computers devise
their own algorithms.

### Can Deep Neural Networks be Designed?

But does stocastic gradient descent really mean the end of
human software engineering?

I think there are reasons to believe that opening the black box
of deep neural networks is still worthwhile, even just measured with the
metric of pursuing performance.  Here are a few reasons.

   1. There has been significant success with transfer learning, where models
      trained on large data sets have been retrained on different problems
      with good success.  [Oquab et al found that hidden layers of a
      network pretrained on object recogntition were able to be reused and
      achieve state-of-the-art performance in other contexts](https://scholar.google.com/scholar?q=oquab+learning+transferring+mid-level+representations).
   2. When examining the activations of individual hidden units,
      some interpretable meaning seems to emerge.  [Zhou and Khosla
      et al observe that object detectors emerge on a network trained
      only to classify places](https://scholar.google.com/scholar?hl=en&q=zhou+object+detectors+emerge+in+deep+scene+cnns).
   3. There are relatively simple problems that are not amenable to
      direct learning by a deep network via stochastic gradient descent,
      but that are easy to learn when an intermediate goal is learned first.
      [Gulcehre and Bengio demonstrate this on a problem of identifying
      images of pentominos in which all the pentominos in are of the same
      type.](http://arxiv.org/abs/1301.4083)
   4. Biological brains seem to do a good job at creating single neurons
      that represent well-factored single concepts.
      [Quiroga found individual neurons in the hippocampus of epilsepy
      patients that cleanly encoded concepts such as "Halle Berry."](https://scholar.google.com/scholar?q=quiroga+Invariant+visual+representation+by+single+neurons+in+the+human+brain)

These are all reasons to believe that even better neural networks
could be created by combining the power of gradient descent with
the power of human-driven software engineering.

But it might be a different flavor of software engineering, one
more driven by measurement, experience, and learning rather
than by types, axioms, and proofs.  Programming might be
more akin to biologists investigating gene expression and
less like mathematicians preserving hard invariants in an
argument. Is there structure nevertheless?  Can neural networks
have the equivalent of recombinant DNA?

What a neat problem!

