from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup


setup_args = generate_distutils_setup(
    name='speechemotionrecognition',
    version='1.1.0',
    packages=['speechemotionrecognition'],
    url='http://github.com/harry-7/speech-emotion-recognition',
    license='MIT',
    install_requires=[
        'numpy'
        'h5py>=2.7.1'
        'Keras>=2.1.5'
        'scipy>=1.0.1'
        'sklearn'
        'speechpy>=2.2'
        'tensorflow>=1.7.0'
        'pandas>=0.24.0'
    ],
    author='harry7',
    author_email='harry7.opensource@gmail.com',
    description='Package to do speech emotion recognition, packaged for ros'
)

setup(**setup_args)
