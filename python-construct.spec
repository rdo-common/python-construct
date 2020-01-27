%{?python_enable_dependency_generator}
%if 0%{?fedora} && 0%{?fedora} < 32
%global         with_python2 1
%endif

Summary:        A powerful declarative parser/builder for binary data
Name:           python-construct
Version:        2.8.22
Release:        1%{?dist}
License:        MIT
URL:            http://construct.readthedocs.org
Source0:        https://pypi.python.org/packages/source/c/construct/construct-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?with_python2}
BuildRequires:  python2-devel
#BuildRequires:  python2-pytest
%endif
BuildRequires:  python3-devel
#BuildRequires:  python3-pytest

%global _description\
Construct is a powerful declarative parser (and builder) for binary\
data.\
\
Instead of writing imperative code to parse a piece of data, you\
declaratively define a data structure that describes your data. As\
this data structure is not code, you can use it in one direction to\
parse data into Pythonic objects, and in the other direction, convert\
(build) objects into binary data.

%description %_description

%if 0%{?with_python2}
%package     -n python2-construct
Summary:        %summary
Requires:       python2-six
%{?python_provide:%python_provide python2-construct}
%description -n python2-construct %_description
%endif

%package     -n python3-construct
Summary:        %summary
Requires:       python3-six
%description -n python3-construct %_description

%prep
%setup -q -n construct-%{version}

%build
%if 0%{?with_python2}
%{py2_build}
%endif
%{py3_build}

%install
%if 0%{?with_python2}
%{py2_install}
%endif
%{py3_install}

%check
# tests are not part of release tarball
#{__python2} -m pytest --benchmark-disable --showlocals
#{__python3} -m pytest --benchmark-disable --showlocals

%if 0%{?with_python2}
%files -n python2-construct
%license LICENSE
%doc README.rst
%{python2_sitelib}/construct
%{python2_sitelib}/construct-%{version}-py?.?.egg-info
%endif

%files -n python3-construct
%license LICENSE
%doc README.rst
%{python3_sitelib}/construct
%{python3_sitelib}/construct-%{version}-py?.?.egg-info

%changelog
* Tue Dec 10 2019 Yatin Karel <ykarel@redhat.com> - 2.8.22-1
- Built u-c version 2.8.22

* Sat Feb 04 2017 Alan Pevec <alan.pevec@redhat.com> 2.8.10-1
- Update to 2.8.10

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 08 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.5.1-1
- initial package
