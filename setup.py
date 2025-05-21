from setuptools import setup

package_name = 'test'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/test1.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yasmin Avila Nunes',
    maintainer_email='yasmin.nunes@amperaracing.com',
    description='Meu pacote de exemplo ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test1_node = test1.test1_node:main',
        ],
    },
)
