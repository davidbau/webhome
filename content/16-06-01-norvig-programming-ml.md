Title: Norvig on Debugging with Machine Learining
Date: 2016-06-01 14:29
Category: Research Notes

At an EmTech digital talk last week, [Peter Norvig spoke](http://events.technologyreview.com/emtech/digital/16/video/watch/peter-norvig-state-of-the-art-ai/)
about the challenges presented by using machine learning.  He talked
about understandability, testability, and debugging of machine learned
systems. The points he makes are the same that drive my research.
For example:

* Traditional software is *modular*, which means that you can
  decompose it and understand it.  Each module has inputs and
  outputs that can be defined and isolated.
* Machine-learned systems appear to be *monolitic*, which means that
  it seems like everything depends on everything else, and changing
  any one thing changes everything else.

In the machine learning world, we can identify mistakes. We can
also retrain a network from scratch to try to fix a mistake.
However, we do not know how to make small local changes, fixing
a small bug without changing everything at once, which is the
everyday practice that defines bugfixing in traditional programming.
In machine learning, fixing a bug means restarting and rebuilding
the whole system.

Norvig points out that this "rebuild the whole thing" approach
impedes understanding, quality assurance, and stability of behavior,
and he concludes by saying that we need and entirely new toolset
for dealing with programming with machine learning.
The talk is worth a watch.

### Starting in on a New Toolset

My goal is to develop tools that attack these problem.  For example:

* I am developing a way to *localize* and *explain* knowledge
  within a deep neural network. In particular, I am trying to
  get to the bottom of "why" a specific neuron appears in a
  neural network: not only what it does, but what it is for.

* I am developing a way of *altering* neural networks in small ways,
  without destroying all the other behavior.  In particular, I am looking
  for ways of transplanting portions of networks from one instance
  to another. I am also interested in targeted ablations.

There are plenty of things to try here - it is a very interesting area.
One theme of my current work is to see if we can break through the feeling
that neural networks are monolithic. If you make small changes in the wrong
way, then it does feel like everything can be destroyed very easily;
but it is also possible to make small changes in the right way, which
does not perturb behavior too much.  Similarly, individual neurons do
seem to have semantic roles, and I am working on getting a clearer picture
of these roles in a robust way.

Modularity does not need to be in oppositition to neural networks;
there are hints that neural networks already have some emergent modularity.
We just need to find ways to measure it, maximize it, and exploit it.
