Name:           mysqltuner
Version:        1.7.13
Release:        2%{?dist}.gps
Summary:        MySQL configuration assistant

Group:          Applications/Databases
License:        GPLv3+
URL:            http://mysqltuner.com/
Source0:        https://github.com/major/MySQLTuner-perl/archive/%{version}.tar.gz
Source1:        mysqlmemory.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       mysql
Requires:       which

%description
MySQLTuner is a script written in Perl that will assist you with your
MySQL configuration and make recommendations for increased performance
and stability.  Within seconds, it will display statistics about your
MySQL installation and the areas where it can be improved.


%prep
%setup -q -n MySQLTuner-perl-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 mysqltuner.pl $RPM_BUILD_ROOT%{_bindir}/mysqltuner
install -Dpm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/mysqlmemory
install -d -m 755 -v $RPM_BUILD_ROOT%{_datarootdir}/mysqltuner
install -Dpm 644 basic_passwords.txt $RPM_BUILD_ROOT%{_datarootdir}/mysqltuner/basic_passwords.txt
install -Dpm 644 vulnerabilities.csv $RPM_BUILD_ROOT%{_datarootdir}/mysqltuner/vulnerabilities.csv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/mysqltuner
%{_datarootdir}/mysqltuner/*


%changelog
* Thu Nov 15 2018 Danila Vershinin <info@getpagespeed.com> - 1.7.13-1
- New upstream version

* Sun Feb 18 2018 Danila Vershinin <info@getpagespeed.com> - 1.7.2-1
- New upstream version
- Packed basic passwords and vulnerabilities data files

* Thu Sep 24 2015 Major Hayden <major@mhtx.net> - 1.6.0-1
- New upstream version
- Removed 'v' from source URL

* Thu Aug 20 2015 Major Hayden <major@mhtx.net> - 1.5.1-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 05 2014 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 1.4.0-1
- New upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2.0-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar  8 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.2.0-1
- Update to 1.2.0, patches applied upstream.

* Sun Mar  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.1.1-4.20100125git
- Patch to fix various engine availability related issues (#682477).

* Mon Feb 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.1.1-3.20100125git
- Update to git revision e8495ce for users w/o passwords listing improvements.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 25 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.1.1-1
- Update to 1.1.1.
- Improve summary.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  1 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-1
- Update to 1.0.0.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  4 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-0.1.rc1
- 1.0.0-rc1.

* Thu Sep 11 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.9-1
- 0.9.9.
- Update description.

* Mon Jul 21 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.8-1
- 0.9.8, --checkversion patch applied upstream.

* Sat Jun 21 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-4
- Don't warn if --skipversion is used (#452172).

* Thu Jun 19 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-1
- 0.9.1.
- Patch to not "phone home" by default (--skipversion -> --checkversion).

* Sat Apr 12 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.0-1
- 0.9.0.

* Sun Mar  2 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.8.6-1
- 0.8.6.

* Mon Feb 18 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.8.5-1
- 0.8.5.
