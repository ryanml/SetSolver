# SetSolver
Generates the valid sets of cards in a game of Set

# Running the code
First, clone the repository by running:

`git clone https://github.com/ryanml/SetSolver.git`

The SetSolver is created as a Python package. It will need setuptools to be built. You can get it by running:

`pip install setuptools`

To set up SetSolver, navigate to the cloned directory and run:

`python setup.py install`

The program can then be started by running:

`python -m setsolver`

### OR
If you would not like to set it up as a package, once you are inside the cloned directory navigate to the setsolver folder:

`cd setsolver`

And run:

`python main.py`

This will start the program. Tests can be run from the same directory by running:

`python tests.py`

## Use
The SetSolver is meant to be interactive so that you may use it to *help* you solve a game of set, such as the one posted daily at: [http://www.setgame.com/](http://www.setgame.com/)

When the program is run, we are prompted for the dimensions that are in play for the game. Enter as many as you'd like, and type in 'exit' when you wish to stop. You will then see an options menu:
![options](https://github.com/ryanml/SetSolver/blob/master/assets/set_dim_options.png "options")

You can add a card to the collection by enter a '1'. For an example, we will enter this card:

![example](https://github.com/ryanml/SetSolver/blob/master/assets/two_ovals.png "example")

For every dimension that we defined, we will be prompted for a state. There is no need to define the different kinds of states, there can be as many as you'd like:

![enter-shape](https://github.com/ryanml/SetSolver/blob/master/assets/enter_shape.png "enter-shape")

If you enter something incorrectly for the card, you may enter a '3' at the options menu when you're done to delete it. Once all of the desired cards in the collection have been added, enter a '2' to generate all of the possible sets:
![all-sets](https://github.com/ryanml/SetSolver/blob/master/assets/all_sets.png "all-sets")

And there you have it! You have just *solved* a game of set. You can exit and repeat using as many, cards, dimensions, and states as you'd like!
