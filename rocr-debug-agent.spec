# ROCr debug agent. TheRock 10.0.

Name:		rocr-debug-agent
Version:	10.0.0
Release:	1
Summary:	ROCr GPU debug agent
License:	MIT
Group:		Development/Debuggers
URL:		https://github.com/ROCm/rocm-systems
Source0:	https://github.com/ROCm/rocm-systems/releases/download/therock-10.0/rocr-debug-agent.tar.gz#/rocr-debug-agent-%{version}.tar.gz

BuildRequires:	rocm-rpm-macros
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	rocm-runtime-devel
BuildRequires:	rocdbgapi-devel
BuildRequires:	pkgconfig(libdw)
BuildRequires:	pkgconfig(libelf)

%description
librocm-debug-agent is loaded into GPU processes to support
ROCgdb and post-mortem GPU debugging.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Unversioned library symlink for the ROCr debug agent.

%prep
%autosetup -n rocr-debug-agent -p1

%build
%cmake %{rocm_cmake_fhs} \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DENABLE_TESTS=OFF \
	-DROCM_PATH=%{_prefix} \
	-DCMAKE_PREFIX_PATH=%{_prefix} \
	-G Ninja

%ninja_build -C build

%install
%ninja_install -C build

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{_libdir}/librocm-debug-agent.so.*

%files devel
%{_libdir}/librocm-debug-agent.so
