%undefine _missing_build_ids_terminate_build
%define debug_package   %{nil}

Name:
Version:
Release:        1%{?dist}
Summary:

Group:
License:
URL:
Source0:

BuildRequires:
Requires:

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog