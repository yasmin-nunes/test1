from setuptools import setup

package_name = 'test1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
    ('share/ament_index/resource_index/packages', ['resource/test1']),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/test1.launch.py']),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yasmin',
    maintainer_email='yasmin.nunes@amperaracing.com',
    description='Um exemplo de nó ROS 2',
    license='MIT',
    entry_points={
        'console_scripts': [
            'test1_node = test1.test1_node:main'
        ],
    },
)
