Name:           ros-hydro-kobuki-bumper2pc
Version:        0.5.7
Release:        0%{?dist}
Summary:        ROS kobuki_bumper2pc package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_bumper2pc
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-kobuki-msgs
Requires:       ros-hydro-nodelet
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-kobuki-msgs
BuildRequires:  ros-hydro-nodelet
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs

%description
Bumper/cliff to pointcloud nodelet: Publish bumpers and cliff sensors events as
points in a pointcloud, so navistack can use them for poor-man navigation.
Implemented as a nodelet intended to run together with kobuki_node.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Aug 18 2014 Jorge Santos Simon <jorge@yujinrobot.com> - 0.5.7-0
- Autogenerated by Bloom

