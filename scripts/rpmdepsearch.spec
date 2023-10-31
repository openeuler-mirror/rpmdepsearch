Name:       rpmdepsearch
Version:    0.1.0
Release:    1
Source0:    %{name}.tar.gz
Summary:    Query rpm package is depended by what packages
License:    MulanPSL-2.0
Requires:   /usr/bin/env
Requires:   python3

%description
Download primary database in XML or Sqlite. Analyze dependency of rpm packages.

%build
#nothing
%install


install -d %{buildroot}%{_sysconfdir}/%{name}
install -d 777 %{buildroot}%{_localstatedir}/cache/%{name}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}/usr/share/man/man1

install -m  755 %{name} %{buildroot}%{_bindir}
install -m  644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}
install -m  644 rpmdepsearch-manpage.1 %{buildroot}/usr/share/man/man1




%files
%{_bindir}/%{name}
%{_sysconfdir}/%{name}/%{name}.conf
%{_localstatedir}/cache/%{name}/
/usr/share/man/man1/rpmdepsearch-manpage.1.gz

%changelog

