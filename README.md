fedmsg_meta_pld
===============

fedmsg metadata providers for PLD Linux deployment
--------------------------------------------------

[fedmsg](http://fedmsg.com) is a set of tools for knitting together services
and webapps into a realtime messaging net.  This package contains metadata
provider plugins for the primary deployment of that system

If you were to deploy fedmsg at another site, you would like want to write your
own module like this one that could provide textual representations of *your*
messages.

Running the Tests
-----------------

    # Create a virtualenv
    $ sudo yum install python-virtualenv
    $ virtualenv my-env
    $ source my-env/bin/activate

    # Install the dependencies
    $ python setup.py develop

    # Run the tests
    $ pip install nose
    $ $(which nosetests)
