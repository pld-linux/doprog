Summary:	Execute a program (with arguments) on a new tty
Summary(pl):	Uruchamia program (z argumentami) na nowym tty
Name:		doprog
Version:	2.2
Release:	1
License:	GPL
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal
Source0:	ftp://ftp.tpnet.pl/pub/sunsite.unc.edu/utils/console/%{name}-%{version}.tar.gz
URL:		http://www.eleves.ens.fr:8080/home/rideau/Tunes/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simplistic utility to spawn programs on new ttys.

%description -l pl
Proste narzêdzie za pomoc± którego mo¿emy uruchomiæ program na nowym
lub ju¿ istniej±cym tty.

%prep
%setup -q 

%build
%{__make} CFLAGS="%{rpmcflags}" CC="%{__cc}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install doprog 	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/* 
