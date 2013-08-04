%global         with_python3 1

Summary:        A powerful declarative parser/builder for binary data
Name:           python-construct
Version:        2.5.1
Release:        2%{?dist}
License:        MIT
URL:            http://construct.readthedocs.org
Source0:        https://pypi.python.org/packages/source/c/construct/construct-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif
Requires:       python-six

%description
Construct is a powerful declarative parser (and builder) for binary
data.

Instead of writing imperative code to parse a piece of data, you
declaratively define a data structure that describes your data. As
this data structure is not code, you can use it in one direction to
parse data into Pythonic objects, and in the other direction, convert
(build) objects into binary data.

%if 0%{?with_python3}
%package -n     python3-construct
Summary:        A powerful declarative parser/builder for binary data
Requires:       python3-six

%description -n python3-construct
Construct is a powerful declarative parser (and builder) for binary
data.

Instead of writing imperative code to parse a piece of data, you
declaratively define a data structure that describes your data. As
this data structure is not code, you can use it in one direction to
parse data into Pythonic objects, and in the other direction, convert
(build) objects into binary data.

This is the Python 3 version of the package.
%endif

%prep
%setup -q -n construct-%{version}
%if 0%{?with_python3}
%{__rm} -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%{__python} setup.py install --skip-build --root %{buildroot}
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif

%files
%doc README.rst LICENSE
%{python_sitelib}/construct
%{python_sitelib}/construct-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-construct
%doc README.rst LICENSE
%{python3_sitelib}/construct
%{python3_sitelib}/construct-%{version}-py?.?.egg-info
%endif

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 08 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.5.1-1
- initial package
