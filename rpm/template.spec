Name:           ros-hydro-kobuki-description
Version:        0.5.7
Release:        0%{?dist}
Summary:        ROS kobuki_description package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-urdf
Requires:       ros-hydro-xacro
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-urdf
BuildRequires:  ros-hydro-xacro

%description
Description of the Kobuki model. Provides the model description of Kobuki for
simulation and visualisation. The files in this package are parsed and used by a
variety of other components. Most users will not interact directly with this
package. WARNING: This package is disabled because it cannot be catkinized by
now, as xacro dependency is not catkin still. In the interim we use a unary pre-
catkin stack named kobuki_description.

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
* Mon Aug 18 2014 Younghun Ju <yhju@yujinrobot.com> - 0.5.7-0
- Autogenerated by Bloom

