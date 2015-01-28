# pythian
A Vagrantfile and supporting cookbooks for my "homework" for a Pythian interview

Notes:

	To access: http://10.0.0.33:8080/river as soon as the Vagrant installation finishes

	The "stack" is minimal: web.py serving content on port 8080 after
        grabbing current river data from the USGS for a river crossing 20
        miles from my house in Washington State.

        The format is a readable tab-delimited format that looks OK either in
        a browser or a direct web connection via wget or whatever you prefer.

	I was thinking I'd have to do something more complex like unpacking
        the data into a database then reading it back, but then I saw that it
        looked OK as is.

        I was inspired along this track and away from my first thought of a minimal Django app by a podcast I heard: Software Engineering Radio #216: Adrian Cockroft on "The Modern Cloud-based Platform." He described Netflix's move from a monolithic and inherently conflict-ridden Java class setup to a bunch of immutable REST-based APIs ... well worth a listen for anybody working on cloud installations.