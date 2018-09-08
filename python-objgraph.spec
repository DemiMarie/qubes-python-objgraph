# Created by pyp2rpm-3.3.2
%global pypi_name objgraph

Name:           python-%{pypi_name}
Version:        3.4.0
Release:        1%{?dist}
Summary:        Draws Python object reference graphs with graphviz

License:        MIT
URL:            https://mg.pov.lt/objgraph/
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python%{python3_pkgversion}-devel
#BuildRequires:  python3dist(graphviz)
BuildRequires:  graphviz
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx

%description
Python Object Graphs :target:

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
 
#Requires:       python3dist(graphviz)
Requires:       graphviz
%description -n python%{python3_pkgversion}-%{pypi_name}
Python Object Graphs :target:

%package -n python-%{pypi_name}-doc
Summary:        objgraph documentation
%description -n python-%{pypi_name}-doc
Documentation for objgraph

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sat Sep 08 2018 Marek Marczykowski-Górecki <marmarek@invisiblethingslab.com> - 3.4.0-1
- Initial package.
