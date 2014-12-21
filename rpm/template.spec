Name:           ros-indigo-kobuki-random-walker
Version:        0.6.5
Release:        0%{?dist}
Summary:        ROS kobuki_random_walker package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_random_walker
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-threads
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-kobuki-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-yocs-cmd-vel-mux
Requires:       ros-indigo-yocs-controllers
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-threads
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-kobuki-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-yocs-controllers

%description
Random walker app for Kobuki

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.6.5-0
- Autogenerated by Bloom

