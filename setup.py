import sys
from setuptools import setup, find_packages
import sdist_upip

setup(name='micropython-the-pad',
      #use_scm_version=True,
      #setup_requires=['setuptools_scm'],
      description='Modules and demos for the pad',
      long_description="Modules and demos for the pad",
      url='https://github.com/bytebarista/the_pad',
      author='ByteBarista',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      version="1.2.9",
      py_modules=['ak8963', 'boot', 'glcdfont', 'ili934xhaxx', 'led_show', 'pu6500', 'pins', 'bme28', 'ili934xhax', 'bme280', 'bme280_int', 'ili934xnew', 'mcp', 'mcpnew', 'mpu9250', 'mpu6500', 'sdcard'],
      #packages=find_packages('the_pad'),
      packages=['the_pad.demos'],
      #py_modules=['the_pad/boot.py'])
      )