%define debug_package %{nil}

Summary:	Nagios plugins to check the status of MS-SQL Servers
Name:		check_mssql_health
Version:	1.5.11
Release:	1%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		http://labs.consol.de/lang/en/nagios/check_mssql_health/
Source0:	http://labs.consol.de/download/shinken-nagios-plugins/check_mssql_health-%{version}.tar.gz
Requires:	perl-Nagios-Plugin
Requires:	perl-DBD-Sybase
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
check_mssql_health is a plugin, which is used to monitor different parameters of a MS SQL server.

%prep
%setup -T -b0 

%build
aclocal
autoconf
automake
./configure --libexecdir=%{_libdir}/nagios/plugins/ --libdir=%{_libdir}
make 


%install
make install DESTDIR="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/nagios/plugins/check_mssql_health

%changelog
* Tue Nov 25 2014 Your Name <you@example.com> 1.5.11-1
- Merge https://github.com/lausser/check_mssql_health (asgeir@ok.is)
- bugfix in database-backup-age (gerhard.lausser@consol.de)
- allow mitigation for failed-jobs if no jobs were run
  (gerhard.lausser@consol.de)
- add --commit which forces auto-commit on (gerhard.lausser@consol.de)
- bugfix in output (gerhard.lausser@consol.de)
- bigfix negate (gerhard.lausser@consol.de)
- implement --negate old_level=new_level, output also ok-messages for my-modes,
  allow floating point numbers in thresholds (gerhard.lausser@consol.de)
- bugfix in transactions. handles databases with auto-close
  (gerhard.lausser@consol.de)
- add jobs-enabled (gerhard.lausser@consol.de)
- update configuee.ac (gerhard.lausser@consol.de)
- drecksrundungsfehler (gerhard.lausser@consol.de)
- protect against non plausible iobusy/cpubusy values
  (gerhard.lausser@consol.de)
- catch wrong io/cpu_busy values (gerhard.lausser@consol.de)
- update gnu autotools (gerhard.lausser@consol.de)
- update asciidoc files (gerhard.lausser@consol.de)
- update config.guess (gerhard.lausser@consol.de)
- fix an uninitialized state_desc (gerhard.lausser@consol.de)
- parameter --notemp is now usable for many modes (gerhard.lausser@consol.de)
- Merge https://github.com/lausser/check_mssql_health (palli@opensource.is)
- fixed a bug in batch-requests, which affected case sensitive colletion
  systems like SAP (Thanks Andreas Seemueller) (gerhard.lausser@consol.de)
- bugfix in doc tables (gerhard.lausser@consol.de)
- updated docs (gerhard.lausser@consol.de)
- rewrote sybase database-free (gerhard.lausser@consol.de)
- bugfix in sybase database-free (gerhard.lausser@consol.de)
- fixed a bug in sybase database-free (gerhard.lausser@consol.de)
- don't compile docs by default (gerhard.lausser@consol.de)
- added asciidoc (gerhard.lausser@consol.de)
- merge conflict (gerhard.lausser@consol.de)
- Merge branch 'master' of github.com:lausser/check_mssql_health
  (gerhard.lausser@consol.de)
- fixed release in download link (gerhard.lausser@consol.de)
- 1.5.18 added asciidoc (gerhard.lausser@consol.de)
- fixed a bug un database-free for sybase (gerhard.lausser@consol.de)
- add deadlock escape (gerhard.lausser@consol.de)
- - fixed a bug in database-free (where the offline state of 1 db was
  propagated t o some others) - implemented all sorts of thresholds - add mode
  sql-runtime (gerhard.lausser@consol.de)
- fixed a bug in database-free (where the offline state of 1 db was propagated
  (gerhard.lausser@consol.de)
- fix a typo (gerhard.lausser@consol.de)
- catch mor eerrors (gerhard.lausser@consol.de)
- catch another error (insufficient privs to access a db)
  (gerhard.lausser@consol.de)
- add more tracedebug (gerhard.lausser@consol.de)
- add paramater mitigation (gerhard.lausser@consol.de)
- fix a bug in logbackup-age (gerhard.lausser@consol.de)
- - database-free can now handle offline databases - add --offlineok - exclude
  dbs with recovery model simple from database-logbackup-age
  (gerhard.lausser@consol.de)
- add database-online (gerhard.lausser@consol.de)
- fix a typo (cancelled is valid and canceled is too)
  (gerhard.lausser@consol.de)
- cancelled and retry are warning, not critical (gerhard.lausser@consol.de)
- add failed-jobs (gerhard.lausser@consol.de)
- update Changelog (gerhard.lausser@consol.de)
- another bug (gerhard.lausser@consol.de)
- another bug.... (gerhard.lausser@consol.de)
- bugfix in dbcc shrink (gerhard.lausser@consol.de)
- add database-file-auto-shrinks (gerhard.lausser@consol.de)
- add database-file-dbcc-shrinks (gerhard.lausser@consol.de)
- rename the term grows to growths (gerhard.lausser@consol.de)
- add database-file-auto-grow (gerhard.lausser@consol.de)
- 1.5.11 (gerhard.lausser@consol.de)
- fedora16 support deprecated for fedora17 (palli@opensource.is)
- feature: if multiline enabled, put summary on top line to prevent clutter
  (palli@opensource.is)
- Merge pull request #1 from opinkerfi/master (gerhard.lausser@consol.de)
- releasers.conf created to point to opensource.is yum repos
  (palli@opensource.is)
- changelog (gerhard.lausser@consol.de)
- add some debugging for cpu_busy (gerhard.lausser@consol.de)

* Thu Aug 16 2012 Pall Sigurdsson <palli@opensource.is> 1.5.10-1
- Initial packaging
