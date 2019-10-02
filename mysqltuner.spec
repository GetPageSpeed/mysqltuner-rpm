Name:           mysqltuner
Version:        1.7.17
Release: 1%{?dist}
Summary:        MySQL configuration assistant

Group:          Applications/Databases
License:        GPLv3+
URL:            http://mysqltuner.com/
Source0:        https://github.com/major/MySQLTuner-perl/archive/%{version}.tar.gz
Source1:        mysqlmemory.sh
Source2:        mysqltuner.cron
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl-generators
# perl-generators won't find modules  defined at 'eval'
# and mysqltuner has some:
Requires:       perl(JSON)
Requires:       perl(Text::Template)
# generates man page in build step
BuildRequires:  pandoc

# this is dependency for client program only
Requires:       mysql
Requires:       which

%description
MySQLTuner is a script written in Perl that will assist you with your
MySQL configuration and make recommendations for increased performance
and stability.  Within seconds, it will display statistics about your
MySQL installation and the areas where it can be improved.

%package cron
Summary:        Cron job to do weekly reports with MySQLTuner
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       crontabs
Requires:       jq

%description cron
Cron job for weekly suggestions of MySQL tuning.

%prep
%setup -q -n MySQLTuner-perl-%{version}
# fix line encodings in README
sed -i 's/\r$//' README.md
# add info section to USAGE.md so it can be nicely converted to man page
sed -i '1i% mysqltuner(1)\n% Major Hayden - major@mhtx.net\n% July 2019\n\n' \
  USAGE.md
# fix-up E: wrong-script-interpreter in EL8
sed -i 's@/usr/bin/env perl@%{_bindir}/perl@' %{name}.pl



%build
# generates man page
pandoc -s -t man USAGE.md -o %{name}.1
# nothins else to do

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 mysqltuner.pl $RPM_BUILD_ROOT%{_bindir}/mysqltuner
install -Dpm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/mysqlmemory
install -d -m 755 -v $RPM_BUILD_ROOT%{_datarootdir}/mysqltuner
install -Dpm 644 basic_passwords.txt $RPM_BUILD_ROOT%{_datarootdir}/mysqltuner/basic_passwords.txt
install -Dpm 644 vulnerabilities.csv $RPM_BUILD_ROOT%{_datarootdir}/mysqltuner/vulnerabilities.csv

install -D -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/cron.weekly/%{name}

%{__install} -Dpm0644 %{name}.1 \
    $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
# Virtually add license macro for EL6:
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%{_bindir}/mysqltuner
%{_bindir}/mysqlmemory
%{_datarootdir}/mysqltuner/*
%{_mandir}/man1/*.1*


%files cron
%{_sysconfdir}/cron.weekly/%{name}


%changelog
* Wed Oct 02 2019 Danila Vershinin <info@getpagespeed.com> 1.7.17-1
- upstream version auto-updated to 1.7.17

* Mon Jul 22 2019 Danila Vershinin <info@getpagespeed.com> 1.7.15-3
- added dependency on couple of perl modules not detected by perl-generators
- generate man page from USAGE.md

* Wed Jun 12 2019 Danila Vershinin <info@getpagespeed.com> 1.7.15-2
- upstream version auto-updated to 1.7.15
- fix README.md

* Tue Apr 2 2019 Danila Vershinin <info@getpagespeed.com> - 1.7.13-4
- added cron subpackage for weekly reports

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
