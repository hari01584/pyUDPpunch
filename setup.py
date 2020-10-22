from distutils.core import setup
setup(
  name = 'pyUDPpunch',         # How you named your package folder (MyLib)
  packages = ['pyUDPpunch'],   # Chose the same as "name"
  version = '0.62',      # Start with a small number and increase it with every change you make
  license='GPLv3+',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Punching Holes Through UDP Sockets!!',   # Give a short description about your library
  author = 'Harishankar Kumar',                   # Type in your name
  author_email = 'hari01584@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/hari01584/pyUDPpunch',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/hari01584/pyUDPpunch/archive/v_062.tar.gz',    # I explain this later on
  keywords = ['Hole Punching', 'Python', 'NAT Traversal'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pystun3',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
