import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'angel_db_manager'
setup(
    name=package_name,
    version='0.1.0',
    # packages=find_packages(exclude=['test']),
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Minsoo Song',
    author_email='sms0432@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=('Package containing examples of how to use the rclpy API.'
    ),
    license='Apache License, Version 2.0',
    test_suite='pytest',
    entry_points={
        'console_scripts': [
            'angel_db_reader = angel_db_manager.angel_db_reader:main',
            'angel_db_writer = angel_db_manager.angel_db_writer:main',
            'angel_db_version= angel_db_manager.angel_db_version:main'
        ],
    },
)


