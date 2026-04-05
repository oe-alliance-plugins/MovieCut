from setuptools import setup
import setup_translate

pkg = 'Extensions.MovieCut'
setup(name='enigma2-plugin-extensions-moviecut',
       version='3.0',
       description='Perform the cuts specified with the Cutlist editor',
       package_dir={pkg: 'MovieCut'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'Readme-MovieCut.txt']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
